import os, sys
import inspect, types

ROOT_DIR = os.getcwd()  # Get root directory
sys.path.append(os.path.dirname(ROOT_DIR + r'/'))# Add absolute path to current sys.path


from services.base_service import BaseService

from services.account.account_service import AccountService

"""
doc: Service class to process logic
"""
class PropertyTypeService():

    def __init__(self):
        self.base_service = BaseService()
        self.db = BaseService.DbFilePath
        self.ec = self.base_service.Entity()
        self.util_common = self.base_service.UtilCommon()
        self.PropertyType = self.ec.InitEntityClass('PropertyType')
        self.service_account = AccountService()


    def get_proptype_all(self):
        with self.base_service.DbContext() as __context:
            result = __context.table(self.PropertyType).select_all()
            return result
        
        return None

    def get_proptype_byId(self, idValue):
        with self.base_service.DbContext() as __context:
            result = __context.table(self.PropertyType).select_by_id(idValue)
            return result
        
        return None

    def get_proptype_byName(self, searchText):
        with self.base_service.DbContext() as __context:
            conditions = ''' Name like '%{0}%' '''.format(searchText)
            result = __context.table(self.PropertyType).select_by(conditions) 
            return result
        
        return None
   
    def add_proptype(self, paramModel):
        if( paramModel is not None and inspect.isclass(type(paramModel)) and type(paramModel) == self.PropertyType):
            with self.base_service.DbContext() as __context:
                
                modelLastPropertyType = __context.table(self.PropertyType).select_lastrecord()# get last record of PropertyType table to increment IndexNo
                
                # create new object of PropertyType
                modelPropertyType = self.PropertyType()
                modelPropertyType.PropertyTypeId = modelLastPropertyType.PropertyTypeId + 1
                modelPropertyType.Name = hasattr(paramModel, 'Name') and paramModel.Name or None
                modelPropertyType.Description = hasattr(paramModel, 'Description') and paramModel.Description or None
                modelPropertyType.SortOrder = hasattr(paramModel, 'SortOrder') and paramModel.SortOrder or None
                modelPropertyType.IsAvailable = hasattr(paramModel, 'IsAvailable') and paramModel.IsAvailable or 1

                # insert to db
                result = __context.table(self.PropertyType).insert_by_model(modelPropertyType)
                if result:
                    return modelPropertyType
        
        return None

    def update_proptype(self, paramModel):
        if(paramModel is not None and inspect.isclass(type(paramModel)) and type(paramModel) == self.PropertyType):
            
            modelPropertyTypeFromDb = self.get_proptype_byId(paramModel.PropertyTypeId)
            
            if(modelPropertyTypeFromDb is not None):
           
                modelPropertyTypeFromDb.Name = hasattr(paramModel, 'Name') and paramModel.Name or modelPropertyTypeFromDb.Name
                modelPropertyTypeFromDb.Description = hasattr(paramModel, 'Description') and paramModel.Description or modelPropertyTypeFromDb.Description
                modelPropertyTypeFromDb.SortOrder = hasattr(paramModel, 'SortOrder') and paramModel.SortOrder or modelPropertyTypeFromDb.SortOrder
                modelPropertyTypeFromDb.IsAvailable = hasattr(paramModel, 'IsAvailable') and paramModel.IsAvailable or modelPropertyTypeFromDb.IsAvailable

                with self.base_service.DbContext() as __context:
                    # update to db
                    result = __context.table(self.PropertyType).update_by_model(modelPropertyTypeFromDb)
                    if result:
                        return modelPropertyTypeFromDb
        return None

        


