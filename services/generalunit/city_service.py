import os, sys
import inspect, types

ROOT_DIR = os.getcwd()  # Get root directory
sys.path.append(os.path.dirname(ROOT_DIR + r'/'))# Add absolute path to current sys.path


from services.base_service import BaseService

from services.account.account_service import AccountService

"""
doc: Service class to process logic
"""
class CityService():

    def __init__(self):
        self.base_service = BaseService()
        self.db = BaseService.DbFilePath
        self.ec = self.base_service.Entity()
        self.util_common = self.base_service.UtilCommon()
        self.City = self.ec.InitEntityClass('City')
        self.service_account = AccountService()


    def get_city_all(self):
        with self.base_service.DbContext() as __context:
            result = __context.table(self.City).select_all()
            return result
        
        return None

    def get_city_byId(self, idValue):
        with self.base_service.DbContext() as __context:
            result = __context.table(self.City).select_by_id(idValue)
            return result
        
        return None

    def get_city_byName(self, searchText):
        with self.base_service.DbContext() as __context:
            conditions = ''' Name like '%{0}%' '''.format(searchText)
            result = __context.table(self.City).select_by(conditions) 
            return result
        
        return None
    
    def get_city_byCode(self, searchText):
        with self.base_service.DbContext() as __context:
            conditions = ''' CityCode like '%{0}%' '''.format(searchText)
            result = __context.table(self.City).select_by(conditions) 
            return result
        
        return None
   
    def add_city(self, paramModel):
        if( paramModel is not None and inspect.isclass(type(paramModel)) and type(paramModel) == self.City):
            with self.base_service.DbContext() as __context:
                
                modelLastCity = __context.table(self.City).select_lastrecord()# get last record of City table to increment IndexNo
                
                # create new object of City
                modelCity = self.City()
                modelCity.CityId = modelLastCity.CityId + 1
                modelCity.CountryId = hasattr(paramModel, 'CountryId') and paramModel.CountryId or None
                modelCity.ParentId = hasattr(paramModel, 'ParentId') and paramModel.ParentId or None
                modelCity.Name = hasattr(paramModel, 'Name') and paramModel.Name or None
                modelCity.CityCode = hasattr(paramModel, 'CityCode') and paramModel.CityCode or None
                modelCity.SortOrder = hasattr(paramModel, 'SortOrder') and paramModel.SortOrder or None
                modelCity.IsAvailable = hasattr(paramModel, 'IsAvailable') and paramModel.IsAvailable or 1

                # insert to db
                result = __context.table(self.City).insert_by_model(modelCity)
                if result:
                    return modelCity
        
        return None

    def update_city(self, paramModel):
        if(paramModel is not None and inspect.isclass(type(paramModel)) and type(paramModel) == self.City):
            
            modelCityFromDb = self.get_city_byId(paramModel.CityId)
            
            if(modelCityFromDb is not None):
                
                modelCityFromDb.CountryId = hasattr(paramModel, 'CountryId') and paramModel.CountryId or modelCityFromDb.CountryId
                modelCityFromDb.ParentId = hasattr(paramModel, 'ParentId') and paramModel.ParentId or modelCityFromDb.ParentId
                modelCityFromDb.Name = hasattr(paramModel, 'Name') and paramModel.Name or modelCityFromDb.Name
                modelCityFromDb.CityCode = hasattr(paramModel, 'CityCode') and paramModel.CityCode or modelCityFromDb.CityCode
                modelCityFromDb.SortOrder = hasattr(paramModel, 'SortOrder') and paramModel.SortOrder or modelCityFromDb.SortOrder
                modelCityFromDb.IsAvailable = hasattr(paramModel, 'IsAvailable') and paramModel.IsAvailable or modelCityFromDb.IsAvailable

                with self.base_service.DbContext() as __context:
                    # update to db
                    result = __context.table(self.City).update_by_model(modelCityFromDb)
                    if result:
                        return modelCityFromDb
        return None

        


