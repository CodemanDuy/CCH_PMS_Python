import os, sys
import inspect, types

ROOT_DIR = os.getcwd()  # Get root directory
sys.path.append(os.path.dirname(ROOT_DIR + r'/'))# Add absolute path to current sys.path


from services.base_service import BaseService

from services.account.account_service import AccountService

"""
doc: Service class to process logic
"""
class PropertyStatusService():

    def __init__(self):
        self.base_service = BaseService()
        self.db = BaseService.DbFilePath
        self.ec = self.base_service.Entity()
        self.util_common = self.base_service.UtilCommon()
        self.PropertyStatus = self.ec.InitEntityClass('PropertyStatus')
        self.service_account = AccountService()


    def get_propstatus_all(self):
        with self.base_service.DbContext() as __context:
            result = __context.table(self.PropertyStatus).select_all()
            return result
        
        return None

    def get_propstatus_byId(self, idValue):
        with self.base_service.DbContext() as __context:
            result = __context.table(self.PropertyStatus).select_by_id(idValue)
            return result
        
        return None

    def get_propstatus_byName(self, searchText):
        with self.base_service.DbContext() as __context:
            conditions = ''' Name like '%{0}%' '''.format(searchText)
            result = __context.table(self.PropertyStatus).select_by(conditions) 
            return result
        
        return None
   
    def add_propstatus(self, paramModel):
        if( paramModel is not None and inspect.isclass(type(paramModel)) and type(paramModel) == self.PropertyStatus):
            with self.base_service.DbContext() as __context:
                
                modelLastPropertyStatus = __context.table(self.PropertyStatus).select_lastrecord()# get last record of PropertyStatus table to increment IndexNo
                
                # create new object of PropertyStatus
                modelPropertyStatus = self.PropertyStatus()
                modelPropertyStatus.PropertyStatusId = modelLastPropertyStatus.PropertyStatusId + 1
                modelPropertyStatus.Name = hasattr(paramModel, 'Name') and paramModel.Name or None
                modelPropertyStatus.Description = hasattr(paramModel, 'Description') and paramModel.Description or None
                modelPropertyStatus.SortOrder = hasattr(paramModel, 'SortOrder') and paramModel.SortOrder or None
                modelPropertyStatus.IsAvailable = hasattr(paramModel, 'IsAvailable') and paramModel.IsAvailable or 1

                # insert to db
                result = __context.table(self.PropertyStatus).insert_by_model(modelPropertyStatus)
                if result:
                    return modelPropertyStatus
        
        return None

    def update_propstatus(self, paramModel):
        if(paramModel is not None and inspect.isclass(type(paramModel)) and type(paramModel) == self.PropertyStatus):
            
            modelPropertyStatusFromDb = self.get_propstatus_byId(paramModel.PropertyStatusId)
            
            if(modelPropertyStatusFromDb is not None):
           
                modelPropertyStatusFromDb.Name = hasattr(paramModel, 'Name') and paramModel.Name or modelPropertyStatusFromDb.Name
                modelPropertyStatusFromDb.Description = hasattr(paramModel, 'Description') and paramModel.Description or modelPropertyStatusFromDb.Description
                modelPropertyStatusFromDb.SortOrder = hasattr(paramModel, 'SortOrder') and paramModel.SortOrder or modelPropertyStatusFromDb.SortOrder
                modelPropertyStatusFromDb.IsAvailable = hasattr(paramModel, 'IsAvailable') and paramModel.IsAvailable or modelPropertyStatusFromDb.IsAvailable

                with self.base_service.DbContext() as __context:
                    # update to db
                    result = __context.table(self.PropertyStatus).update_by_model(modelPropertyStatusFromDb)
                    if result:
                        return modelPropertyStatusFromDb
        return None

        


