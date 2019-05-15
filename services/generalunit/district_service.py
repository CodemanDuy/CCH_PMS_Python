import os, sys
import inspect, types

ROOT_DIR = os.getcwd()  # Get root directory
sys.path.append(os.path.dirname(ROOT_DIR + r'/'))# Add absolute path to current sys.path


from services.base_service import BaseService

from services.account.account_service import AccountService

"""
doc: Service class to process logic
"""
class DistrictService():

    def __init__(self):
        self.base_service = BaseService()
        self.db = BaseService.DbFilePath
        self.ec = self.base_service.Entity()
        self.util_common = self.base_service.UtilCommon()
        self.District = self.ec.InitEntityClass('District')
        self.service_account = AccountService()


    def get_district_all(self):
        with self.base_service.DbContext() as __context:
            result = __context.table(self.District).select_all()
            return result
        
        return None

    def get_district_byId(self, idValue):
        with self.base_service.DbContext() as __context:
            result = __context.table(self.District).select_by_id(idValue)
            return result
        
        return None

    def get_district_byName(self, searchText):
        with self.base_service.DbContext() as __context:
            conditions = ''' Name like '%{0}%' '''.format(searchText)
            result = __context.table(self.District).select_by(conditions) 
            return result
        
        return None
    
    def get_district_byCode(self, searchText):
        with self.base_service.DbContext() as __context:
            conditions = ''' DistrictCode like '%{0}%' '''.format(searchText)
            result = __context.table(self.District).select_by(conditions) 
            return result
        
        return None
   
    def add_district(self, paramModel):
        if( paramModel is not None and inspect.isclass(type(paramModel)) and type(paramModel) == self.District):
            with self.base_service.DbContext() as __context:
                
                modelLastDistrict = __context.table(self.District).select_lastrecord()# get last record of District table to increment IndexNo
                
                # create new object of District
                modelDistrict = self.District()
                modelDistrict.DistrictId = modelLastDistrict.DistrictId + 1
                modelDistrict.CityId = hasattr(paramModel, 'CityId') and paramModel.CityId or None
                modelDistrict.Name = hasattr(paramModel, 'Name') and paramModel.Name or None
                modelDistrict.DistrictCode = hasattr(paramModel, 'DistrictCode') and paramModel.DistrictCode or None
                modelDistrict.SortOrder = hasattr(paramModel, 'SortOrder') and paramModel.SortOrder or None
                modelDistrict.IsAvailable = hasattr(paramModel, 'IsAvailable') and paramModel.IsAvailable or 1

                # insert to db
                result = __context.table(self.District).insert_by_model(modelDistrict)
                if result:
                    return modelDistrict
        
        return None

    def update_district(self, paramModel):
        if(paramModel is not None and inspect.isclass(type(paramModel)) and type(paramModel) == self.District):
            
            modelDistrictFromDb = self.get_district_byId(paramModel.DistrictId)
            
            if(modelDistrictFromDb is not None):
                
                modelDistrictFromDb.CityId = hasattr(paramModel, 'CityId') and paramModel.CityId or modelDistrictFromDb.CityId
                modelDistrictFromDb.Name = hasattr(paramModel, 'Name') and paramModel.Name or modelDistrictFromDb.Name
                modelDistrictFromDb.DistrictCode = hasattr(paramModel, 'DistrictCode') and paramModel.DistrictCode or modelDistrictFromDb.DistrictCode
                modelDistrictFromDb.SortOrder = hasattr(paramModel, 'SortOrder') and paramModel.SortOrder or modelDistrictFromDb.SortOrder
                modelDistrictFromDb.IsAvailable = hasattr(paramModel, 'IsAvailable') and paramModel.IsAvailable or modelDistrictFromDb.IsAvailable

                with self.base_service.DbContext() as __context:
                    # update to db
                    result = __context.table(self.District).update_by_model(modelDistrictFromDb)
                    if result:
                        return modelDistrictFromDb
        return None

        


