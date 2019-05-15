import os, sys
import inspect, types

ROOT_DIR = os.getcwd()  # Get root directory
sys.path.append(os.path.dirname(ROOT_DIR + r'/'))# Add abase_serviceolute path to current sys.path


from services.base_service import BaseService

"""
doc: Service class to process logic
"""
class AccountService():
    
    def __init__(self):
        self.base_service = BaseService()
        self.db = BaseService.DbFilePath
        self.ec = self.base_service.Entity()
        self.util_common = self.base_service.UtilCommon()
        self.util_security = self.base_service.UtilSecurity()
        self.Account = self.ec.InitEntityClass('Account')
        

    def get_account_all(self):
        with self.base_service.DbContext() as __context:
            result = __context.table(self.Account).select_all()
            return result
        
        return None

    def get_account_byId(self, idValue):
        with self.base_service.DbContext() as __context:
            result = __context.table(self.Account).select_by_id(idValue)
            return result
        
        return None
    
    def get_account_byUname(self, searchText):
        with self.base_service.DbContext() as __context:
            conditions = ''' Username like '%{0}%' '''.format(searchText)
            result = __context.table(self.Account).select_by(conditions) 
            return result
        
        return None
    
    def get_accountAdmin(self):
        with self.base_service.DbContext() as __context:
            conditions = ''' IsMasterAdmin = 1 '''
            result = __context.table(self.Account).select_by(conditions)
            return result[0]
        
        return None
   
    def add_account(self, paramModel):
        if( paramModel is not None and inspect.isclass(type(paramModel)) and type(paramModel) == self.Account):
            with self.base_service.DbContext() as __context:
                
                modelAdmin = self.get_accountAdmin()# get limit 1 result 

                modelLastAccount = __context.table(self.Account).select_lastrecord()# get last record of Account table to increment IndexNo

                password = hasattr(paramModel, 'Pw') and paramModel.Pw or self.util_common.randomString(8)
                hashedpassword = self.util_security.generatePasswordByBcrypt(password, 6)# generate hashed password using bcrypt

                # create new object of Account
                modelAcc = self.Account()
                modelAcc.AccountId = str(self.util_common.generateUUID())
                modelAcc.IndexNo = hasattr(paramModel, 'IndexNo') and paramModel.IndexNo or (modelLastAccount.IndexNo + 1)
                modelAcc.Username = hasattr(paramModel, 'Username') and paramModel.Username or None
                modelAcc.IsBooker = hasattr(paramModel, 'IsBooker') and paramModel.IsBooker or 1
                modelAcc.IpAddress = hasattr(paramModel, 'IpAddress') and paramModel.IpAddress or None
                modelAcc.Pw = hashedpassword
                modelAcc.SaltKey = hasattr(paramModel, 'SaltKey') and paramModel.SaltKey or None
                modelAcc.IsAvailable = hasattr(paramModel, 'IsAvailable') and paramModel.IsAvailable or 1

                modelAcc.CreatedBy = modelAdmin.IndexNo
                modelAcc.LastModifiedBy = modelAdmin.IndexNo
                modelAcc.DateCreated = str(self.util_common.currentDateTime())
                modelAcc.DateLastModified = str(self.util_common.currentDateTime())
                # insert to db
                result = __context.table(self.Account).insert_by_model(modelAcc)
                if result:
                    return modelAcc
        
        return None

    def update_account(self, paramModel):
        if(paramModel is not None and inspect.isclass(type(paramModel)) and type(paramModel) == self.Account):
            
            modelAccFromDb = self.get_account_byId(paramModel.AccountId)
            
            if(modelAccFromDb is not None):

                modelAdmin = self.get_accountAdmin()# get limit 1 result 
                modelAccFromDb.Pw = (
                    # if paramModel.Pw (new password) has value and it not matched exist password
                    (hasattr(paramModel, 'Pw') and not self.util_security.verifyHashed(self.util_security, paramModel.Pw, modelAccFromDb.Pw)) 
                    # then generate new hashed password for new password
                    and self.util_security.generatePasswordByBcrypt(paramModel.Pw , 6) 
                    # else if they matched together, get exist password
                    or modelAccFromDb.Pw
                )
                modelAccFromDb.IndexNo = hasattr(paramModel, 'IndexNo') and paramModel.IndexNo or modelAccFromDb.IndexNo
                modelAccFromDb.Username = hasattr(paramModel, 'Username') and paramModel.Username or  modelAccFromDb.Username
                modelAccFromDb.IsBooker = hasattr(paramModel, 'IsBooker') and paramModel.IsBooker or modelAccFromDb.IsBooker
                modelAccFromDb.IsMasterAdmin = hasattr(paramModel, 'IsMasterAdmin') and paramModel.IsMasterAdmin or modelAccFromDb.IsMasterAdmin
                modelAccFromDb.IpAddress = hasattr(paramModel, 'IpAddress') and paramModel.IpAddress or modelAccFromDb.IpAddress
                modelAccFromDb.DateLastLogin = hasattr(paramModel, 'DateLastLogin') and paramModel.DateLastLogin or modelAccFromDb.DateLastLogin
                modelAccFromDb.IsAvailable = hasattr(paramModel, 'IsAvailable') and paramModel.IsAvailable or  modelAccFromDb.IsAvailable
                
                modelAccFromDb.LastModifiedBy = modelAdmin.IndexNo
                modelAccFromDb.DateLastModified = str(self.util_common.currentDateTime())

                with self.base_service.DbContext() as __context:
                    # update to db
                    result = __context.table(self.Account).update_by_model(modelAccFromDb)
                    if result:
                        return modelAccFromDb
        return None

        



