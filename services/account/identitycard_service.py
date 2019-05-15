import os, sys
import inspect, types

ROOT_DIR = os.getcwd()  # Get root directory
sys.path.append(os.path.dirname(ROOT_DIR + r'/'))# Add absolute path to current sys.path

from services.base_service import BaseService
from services.account.account_service import AccountService

"""
doc: Service class to process logic
"""
class IdentityCardService():


    def __init__(self):
        self.base_service = BaseService()
        self.db = BaseService.DbFilePath
        self.ec = self.base_service.Entity()
        self.util_common = self.base_service.UtilCommon()
        self.IdentityCard = self.ec.InitEntityClass('IdentityCard')
        self.service_account = AccountService()   


    def get_idcard_all(self):
        with self.base_service.DbContext() as __context:
            result = __context.table(self.IdentityCard).select_all()
            return result
        
        return None

    def get_idcard_byId(self, idValue):
        with self.base_service.DbContext() as __context:
            result = __context.table(self.IdentityCard).select_by_id(idValue)
            return result
        
        return None
    
    def get_idcard_byName(self, searchText):
        with self.base_service.DbContext() as __context:
            conditions = ''' FullName like '%{0}%' '''.format(searchText)
            result = __context.table(self.IdentityCard).select_by(conditions) 
            return result
        
        return None
   
    def add_idcard(self, paramModel):
        if( paramModel is not None and inspect.isclass(type(paramModel)) and type(paramModel) == self.IdentityCard):
            with self.base_service.DbContext() as __context:
                
                modelAdmin = self.service_account.get_accountAdmin()# get limit 1 result 

                modelLastIdentityCard = __context.table(self.IdentityCard).select_lastrecord()# get last record of IdentityCard table to increment IndexNo
                
                # create new object of IdentityCard
                modelIdentityCard = self.IdentityCard()
                modelIdentityCard.IdentityCardId = str(self.util_common.generateUUID())
                modelIdentityCard.IndexNo = hasattr(paramModel, 'IndexNo') and paramModel.IndexNo or (modelLastIdentityCard.IndexNo + 1)
                modelIdentityCard.IdentityCardType = hasattr(paramModel, 'IdentityCardType') and paramModel.IdentityCardType or None
                modelIdentityCard.IdentityNo = hasattr(paramModel, 'IdentityNo') and paramModel.IdentityNo or None
                modelIdentityCard.FullName = hasattr(paramModel, 'FullName') and paramModel.FullName.upper() or None
                modelIdentityCard.DOB = hasattr(paramModel, 'DOB') and paramModel.DOB or None
                modelIdentityCard.Gender = hasattr(paramModel, 'Gender') and paramModel.Gender or None
                modelIdentityCard.HomeTownAddress = hasattr(paramModel, 'HomeTownAddress') and paramModel.HomeTownAddress or None
                modelIdentityCard.PermanentAddress = hasattr(paramModel, 'PermanentAddress') and paramModel.PermanentAddress or None
                modelIdentityCard.CountryId = hasattr(paramModel, 'CountryId') and paramModel.CountryId or None
                modelIdentityCard.DateIssued = hasattr(paramModel, 'DateIssued') and paramModel.DateIssued or None
                modelIdentityCard.DateExpired = hasattr(paramModel, 'DateExpired') and paramModel.DateExpired or None
                modelIdentityCard.ScanFile = hasattr(paramModel, 'ScanFile') and paramModel.ScanFile or None
                
                modelIdentityCard.CreatedBy = modelAdmin.IndexNo
                modelIdentityCard.LastModifiedBy = modelAdmin.IndexNo
                modelIdentityCard.DateCreated = str(self.util_common.currentDateTime())
                modelIdentityCard.DateLastModified = str(self.util_common.currentDateTime())

                # insert to db
                result = __context.table(self.IdentityCard).insert_by_model(modelIdentityCard)
                if result:
                    return modelIdentityCard
        
        return None

    def update_idcard(self, paramModel):
        if(paramModel is not None and inspect.isclass(type(paramModel)) and type(paramModel) == self.IdentityCard):
            
            modelIdentityCardFromDb = self.get_idcard_byId(paramModel.IdentityCardId)
            
            if(modelIdentityCardFromDb is not None):

                modelAdmin = self.service_account.get_accountAdmin()# get limit 1 result 
           
                modelIdentityCardFromDb.IndexNo = hasattr(paramModel, 'IndexNo') and paramModel.IndexNo or modelIdentityCardFromDb.IndexNo
                modelIdentityCardFromDb.IdentityCardType = hasattr(paramModel, 'IdentityCardType') and paramModel.IdentityCardType or modelIdentityCardFromDb.IdentityCardType
                modelIdentityCardFromDb.IdentityNo = hasattr(paramModel, 'IdentityNo') and paramModel.IdentityNo or modelIdentityCardFromDb.IdentityNo
                modelIdentityCardFromDb.FullName = hasattr(paramModel, 'FullName') and paramModel.FullName.upper() or modelIdentityCardFromDb.FullName
                modelIdentityCardFromDb.DOB = hasattr(paramModel, 'DOB') and paramModel.DOB or modelIdentityCardFromDb.DOB
                modelIdentityCardFromDb.Gender = hasattr(paramModel, 'Gender') and paramModel.Gender or modelIdentityCardFromDb.Gender
                modelIdentityCardFromDb.HomeTownAddress = hasattr(paramModel, 'HomeTownAddress') and paramModel.HomeTownAddress or modelIdentityCardFromDb.HomeTownAddress
                modelIdentityCardFromDb.PermanentAddress = hasattr(paramModel, 'PermanentAddress') and paramModel.PermanentAddress or modelIdentityCardFromDb.PermanentAddress
                modelIdentityCardFromDb.CountryId = hasattr(paramModel, 'CountryId') and paramModel.CountryId or modelIdentityCardFromDb.CountryId
                modelIdentityCardFromDb.DateIssued = hasattr(paramModel, 'DateIssued') and paramModel.DateIssued or modelIdentityCardFromDb.DateIssued
                modelIdentityCardFromDb.DateExpired = hasattr(paramModel, 'DateExpired') and paramModel.DateExpired or modelIdentityCardFromDb.DateExpired
                modelIdentityCardFromDb.ScanFile = hasattr(paramModel, 'ScanFile') and paramModel.ScanFile or modelIdentityCardFromDb.ScanFile
                
                modelIdentityCardFromDb.LastModifiedBy = modelAdmin.IndexNo
                modelIdentityCardFromDb.DateLastModified = str(self.util_common.currentDateTime())

                with self.base_service.DbContext() as __context:
                    # update to db
                    result = __context.table(self.IdentityCard).update_by_model(modelIdentityCardFromDb)
                    if result:
                        return modelIdentityCardFromDb
        return None

        


