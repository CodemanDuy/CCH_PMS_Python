import os, sys
import inspect, types

ROOT_DIR = os.getcwd()  # Get root directory
sys.path.append(os.path.dirname(ROOT_DIR + r'/'))# Add absolute path to current sys.path


from services.base_service import BaseService

from services.account.account_service import AccountService

"""
doc: Service class to process logic
"""
class PropertyAvailibiltyTypeService():

    def __init__(self):
        self.base_service = BaseService()
        self.db = BaseService.DbFilePath
        self.ec = self.base_service.Entity()
        self.util_common = self.base_service.UtilCommon()
        self.PropertyAvailibiltyType = self.ec.InitEntityClass('PropertyAvailibiltyType')
        self.service_account = AccountService()


    def get_propavailtype_all(self):
        with self.base_service.DbContext() as __context:
            result = __context.table(self.PropertyAvailibiltyType).select_all()
            return result
        
        return None

    def get_propavailtype_byId(self, idValue):
        with self.base_service.DbContext() as __context:
            result = __context.table(self.PropertyAvailibiltyType).select_by_id(idValue)
            return result
        
        return None

    def get_propavailtype_byName(self, searchText):
        with self.base_service.DbContext() as __context:
            conditions = ''' Name like '%{0}%' '''.format(searchText)
            result = __context.table(self.PropertyAvailibiltyType).select_by(conditions) 
            return result
        
        return None
   
    def add_propavailtype(self, paramModel):
        if( paramModel is not None and inspect.isclass(type(paramModel)) and type(paramModel) == self.PropertyAvailibiltyType):
            with self.base_service.DbContext() as __context:
                
                modelLastPropertyAvailibiltyType = __context.table(self.PropertyAvailibiltyType).select_lastrecord()# get last record of PropertyAvailibiltyType table to increment IndexNo
                
                # create new object of PropertyAvailibiltyType
                modelPropertyAvailibiltyType = self.PropertyAvailibiltyType()
                modelPropertyAvailibiltyType.PropAvailTypeId = modelLastPropertyAvailibiltyType.PropAvailTypeId + 1
                modelPropertyAvailibiltyType.Name = hasattr(paramModel, 'Name') and paramModel.Name or None
                modelPropertyAvailibiltyType.Description = hasattr(paramModel, 'Description') and paramModel.Description or None
                modelPropertyAvailibiltyType.SortOrder = hasattr(paramModel, 'SortOrder') and paramModel.SortOrder or None
                modelPropertyAvailibiltyType.IsAvailable = hasattr(paramModel, 'IsAvailable') and paramModel.IsAvailable or 1

                # insert to db
                result = __context.table(self.PropertyAvailibiltyType).insert_by_model(modelPropertyAvailibiltyType)
                if result:
                    return modelPropertyAvailibiltyType
        
        return None

    def update_propavailtype(self, paramModel):
        if(paramModel is not None and inspect.isclass(type(paramModel)) and type(paramModel) == self.PropertyAvailibiltyType):
            
            modelPropertyAvailibiltyTypeFromDb = self.get_propavailtype_byId(paramModel.PropAvailTypeId)
            
            if(modelPropertyAvailibiltyTypeFromDb is not None):
           
                modelPropertyAvailibiltyTypeFromDb.Name = hasattr(paramModel, 'Name') and paramModel.Name or modelPropertyAvailibiltyTypeFromDb.Name
                modelPropertyAvailibiltyTypeFromDb.Description = hasattr(paramModel, 'Description') and paramModel.Description or modelPropertyAvailibiltyTypeFromDb.Description
                modelPropertyAvailibiltyTypeFromDb.SortOrder = hasattr(paramModel, 'SortOrder') and paramModel.SortOrder or modelPropertyAvailibiltyTypeFromDb.SortOrder
                modelPropertyAvailibiltyTypeFromDb.IsAvailable = hasattr(paramModel, 'IsAvailable') and paramModel.IsAvailable or modelPropertyAvailibiltyTypeFromDb.IsAvailable

                with self.base_service.DbContext() as __context:
                    # update to db
                    result = __context.table(self.PropertyAvailibiltyType).update_by_model(modelPropertyAvailibiltyTypeFromDb)
                    if result:
                        return modelPropertyAvailibiltyTypeFromDb
        return None

        


