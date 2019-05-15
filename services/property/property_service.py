import os, sys
import inspect, types

ROOT_DIR = os.getcwd()  # Get root directory
sys.path.append(os.path.dirname(ROOT_DIR + r'/'))# Add absolute path to current sys.path


from services.base_service import BaseService

from services.account.account_service import AccountService

"""
doc: Service class to process logic
"""
class PropertyService():

    def __init__(self):
        self.base_service = BaseService()
        self.db = BaseService.DbFilePath
        self.ec = self.base_service.Entity()
        self.util_common = self.base_service.UtilCommon()
        self.Property = self.ec.InitEntityClass('Property')
        self.service_account = AccountService()


    def get_property_all(self):
        with self.base_service.DbContext() as __context:
            result = __context.table(self.Property).select_all()
            return result
        
        return None

    def get_property_byId(self, idValue):
        with self.base_service.DbContext() as __context:
            result = __context.table(self.Property).select_by_id(idValue)
            return result
        
        return None
    
    def get_property_byName(self, searchText):
        with self.base_service.DbContext() as __context:
            conditions = ''' Name like '%{0}%' '''.format(searchText)
            result = __context.table(self.Property).select_by(conditions) 
            return result
        
        return None
   
    def add_property(self, paramModel):
        if( paramModel is not None and inspect.isclass(type(paramModel)) and type(paramModel) == self.Property):
            with self.base_service.DbContext() as __context:
                
                modelAdmin = self.service_account.get_accountAdmin()# get limit 1 result 

                modelLastProperty = __context.table(self.Property).select_lastrecord()# get last record of Property table to increment IndexNo
                
                # create new object of Property
                modelProperty = self.Property()
                modelProperty.PropertyId = modelLastProperty.PropertyId + 1
                modelProperty.Name = hasattr(paramModel, 'Name') and paramModel.Name or None
                modelProperty.Description = hasattr(paramModel, 'Description') and paramModel.Description or None
                modelProperty.CountryId = hasattr(paramModel, 'CountryId') and paramModel.CountryId or None
                modelProperty.AreaId = hasattr(paramModel, 'AreaId') and paramModel.AreaId or None
                modelProperty.CityId = hasattr(paramModel, 'CityId') and paramModel.CityId or None
                modelProperty.DistrictId = hasattr(paramModel, 'DistrictId') and paramModel.DistrictId or None
                modelProperty.SubDistrictId = hasattr(paramModel, 'SubDistrictId') and paramModel.SubDistrictId or None
                modelProperty.Address = hasattr(paramModel, 'Address') and paramModel.Address or None
                modelProperty.IsAvailable = hasattr(paramModel, 'IsAvailable') and paramModel.IsAvailable or 1
                modelProperty.IsRemoved = hasattr(paramModel, 'IsRemoved') and paramModel.IsRemoved or 0
                
                modelProperty.CreatedBy = modelAdmin.IndexNo
                modelProperty.LastModifiedBy = modelAdmin.IndexNo
                modelProperty.DateCreated = str(self.util_common.currentDateTime())
                modelProperty.DateLastModified = str(self.util_common.currentDateTime())

                # insert to db
                result = __context.table(self.Property).insert_by_model(modelProperty)
                if result:
                    return modelProperty
        
        return None

    def update_property(self, paramModel):
        if(paramModel is not None and inspect.isclass(type(paramModel)) and type(paramModel) == self.Property):
            
            modelPropertyFromDb = self.get_property_byId(paramModel.PropertyId)
            
            if(modelPropertyFromDb is not None):

                modelAdmin = self.service_account.get_accountAdmin()# get limit 1 result 
                
                modelPropertyFromDb.Name = hasattr(paramModel, 'Name') and paramModel.Name or modelPropertyFromDb.Name
                modelPropertyFromDb.Description = hasattr(paramModel, 'Description') and paramModel.Description or modelPropertyFromDb.Description
                modelPropertyFromDb.CountryId = hasattr(paramModel, 'CountryId') and paramModel.CountryId or modelPropertyFromDb.CountryId
                modelPropertyFromDb.AreaId = hasattr(paramModel, 'AreaId') and paramModel.AreaId or modelPropertyFromDb.AreaId
                modelPropertyFromDb.CityId = hasattr(paramModel, 'CityId') and paramModel.CityId or modelPropertyFromDb.CityId
                modelPropertyFromDb.DistrictId = hasattr(paramModel, 'DistrictId') and paramModel.DistrictId or modelPropertyFromDb.DistrictId
                modelPropertyFromDb.SubDistrictId = hasattr(paramModel, 'SubDistrictId') and paramModel.SubDistrictId or modelPropertyFromDb.SubDistrictId
                modelPropertyFromDb.Address = hasattr(paramModel, 'Address') and paramModel.Address or modelPropertyFromDb.Address
                modelPropertyFromDb.IsAvailable = hasattr(paramModel, 'IsAvailable') and paramModel.IsAvailable or 1
                modelPropertyFromDb.IsRemoved = hasattr(paramModel, 'IsRemoved') and paramModel.IsRemoved or 0
                
                modelPropertyFromDb.LastModifiedBy = modelAdmin.IndexNo
                modelPropertyFromDb.DateLastModified = str(self.util_common.currentDateTime())

                with self.base_service.DbContext() as __context:
                    # update to db
                    result = __context.table(self.Property).update_by_model(modelPropertyFromDb)
                    if result:
                        return modelPropertyFromDb
        return None

        


