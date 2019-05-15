import os, sys
import inspect, types

ROOT_DIR = os.getcwd()  # Get root directory
sys.path.append(os.path.dirname(ROOT_DIR + r'/'))# Add absolute path to current sys.path


from services.base_service import BaseService
from services.account.account_service import AccountService

"""
doc: Service class to process logic
"""
class ClientService():

    def __init__(self):
        self.base_service = BaseService()
        self.db = BaseService.DbFilePath
        self.ec = self.base_service.Entity()
        self.util_common = self.base_service.UtilCommon()
        self.Client = self.ec.InitEntityClass('Client')
        self.service_account = AccountService()


    def get_client_all(self):
        with self.base_service.DbContext() as __context:
            result = __context.table(self.Client).select_all()
            return result
        
        return None

    def get_client_byId(self, idValue):
        with self.base_service.DbContext() as __context:
            result = __context.table(self.Client).select_by_id(idValue)
            return result
        
        return None
    
    def get_client_byName(self, searchText):
        with self.base_service.DbContext() as __context:
            conditions = ''' FullName like '%{0}%' '''.format(searchText)
            result = __context.table(self.Client).select_by(conditions) 
            return result
        
        return None
   
    def add_client(self, paramModel):
        if( paramModel is not None and inspect.isclass(type(paramModel)) and type(paramModel) == self.Client):
            with self.base_service.DbContext() as __context:
                
                modelAdmin = self.service_account.get_accountAdmin()# get limit 1 result 

                modelLastClient = __context.table(self.Client).select_lastrecord()# get last record of Client table to increment IndexNo
                
                # create new object of Client
                modelClient = self.Client()
                modelClient.ClientId = str(self.util_common.generateUUID())
                modelClient.IndexNo = hasattr(paramModel, 'IndexNo') and paramModel.IndexNo or (modelLastClient.IndexNo + 1)
                modelClient.BookerFgCode = hasattr(paramModel, 'BookerFgCode') and paramModel.BookerFgCode or '00000000'
                modelClient.IdentityPicture = hasattr(paramModel, 'IdentityPicture') and paramModel.IdentityPicture or None
                modelClient.IdentityCardId = hasattr(paramModel, 'IdentityCardId') and paramModel.IdentityCardId or None
                modelClient.FullName = hasattr(paramModel, 'FullName') and paramModel.FullName.upper() or None
                modelClient.FourgramCode = hasattr(paramModel, 'FullName') and self.__generateFourgramCode(paramModel.FullName) or None
                modelClient.Phone1 = hasattr(paramModel, 'Phone1') and paramModel.Phone1 or None
                modelClient.Phone2 = hasattr(paramModel, 'Phone2') and paramModel.Phone2 or None
                modelClient.Email = hasattr(paramModel, 'Email') and paramModel.Email or None
                modelClient.TemporaryAddress = hasattr(paramModel, 'TemporaryAddress') and paramModel.TemporaryAddress or None
                modelClient.CurrentJob = hasattr(paramModel, 'CurrentJob') and paramModel.CurrentJob or None
                modelClient.SignatureScan = hasattr(paramModel, 'SignatureScan') and paramModel.SignatureScan or None
                modelClient.IsAvailable = hasattr(paramModel, 'IsAvailable') and paramModel.IsAvailable or 1
                
                modelClient.CreatedBy = modelAdmin.IndexNo
                modelClient.LastModifiedBy = modelAdmin.IndexNo
                modelClient.DateCreated = str(self.util_common.currentDateTime())
                modelClient.DateLastModified = str(self.util_common.currentDateTime())

                # insert to db
                result = __context.table(self.Client).insert_by_model(modelClient)
                if result:
                    return modelClient
        
        return None

    def update_client(self, paramModel):
        if(paramModel is not None and inspect.isclass(type(paramModel)) and type(paramModel) == self.Client):
            
            modelClientFromDb = self.get_client_byId(paramModel.ClientId)
            
            if(modelClientFromDb is not None):

                modelAdmin = self.service_account.get_accountAdmin()# get limit 1 result 

                modelClientFromDb.IndexNo = hasattr(paramModel, 'IndexNo') and paramModel.IndexNo or modelClientFromDb.IndexNo
                modelClientFromDb.BookerFgCode = hasattr(paramModel, 'BookerFgCode') and paramModel.BookerFgCode or modelClientFromDb.BookerFgCode
                modelClientFromDb.IdentityPicture = hasattr(paramModel, 'IdentityPicture') and paramModel.IdentityPicture or modelClientFromDb.IdentityPicture
                modelClientFromDb.FullName = hasattr(paramModel, 'FullName') and paramModel.FullName.upper() or modelClientFromDb.FullName
                modelClientFromDb.Phone1 = hasattr(paramModel, 'Phone1') and paramModel.Phone1 or modelClientFromDb.Phone1
                modelClientFromDb.Phone2 = hasattr(paramModel, 'Phone2') and paramModel.Phone2 or modelClientFromDb.Phone2
                modelClientFromDb.Email = hasattr(paramModel, 'Email') and paramModel.Email or modelClientFromDb.Email
                modelClientFromDb.TemporaryAddress = hasattr(paramModel, 'TemporaryAddress') and paramModel.TemporaryAddress or modelClientFromDb.TemporaryAddress
                modelClientFromDb.CurrentJob = hasattr(paramModel, 'CurrentJob') and paramModel.CurrentJob or modelClientFromDb.CurrentJob
                modelClientFromDb.SignatureScan = hasattr(paramModel, 'SignatureScan') and paramModel.SignatureScan or modelClientFromDb.SignatureScan
                modelClientFromDb.IsAvailable = hasattr(paramModel, 'IsAvailable') and paramModel.IsAvailable or modelClientFromDb.IsAvailable
               
                modelClientFromDb.LastModifiedBy = modelAdmin.IndexNo
                modelClientFromDb.DateLastModified = str(self.util_common.currentDateTime())

                with self.base_service.DbContext() as __context:
                    # update to db
                    result = __context.table(self.Client).update_by_model(modelClientFromDb)
                    if result:
                        return modelClientFromDb
        return None

        
    def __generateFourgramCode(self, fullname):
        if fullname:
            fourgramcode = ''

            lstWord = fullname.strip().split(' ')
            firstWord = lstWord[0]
            lastWord = lstWord[len(lstWord) - 1]
            finalChars = str(lastWord[:2]).upper() + str(firstWord[:2]).upper()# get first 2 character of string

            with self.base_service.DbContext() as __context:
                conditions = ''' FourgramCode like '%{0}%' ORDER BY FourgramCode DESC LIMIT 1'''.format(finalChars)
                result = __context.table(self.Client).select_by(conditions) 
                
                if result:
                    
                    # lastDigitFCode = result[0].FourgramCode[-4:]
                    lastDigitFCode = ''.join([n for n in list(result[0].FourgramCode) if n.isdigit()])
                    fourgramcode = finalChars + str("{:04d}".format(int(lastDigitFCode) + 1))
                else:
                    fourgramcode = finalChars + "{:04d}".format(1)# display number leading zeros with format 4 digits
            
            return fourgramcode

        return None



