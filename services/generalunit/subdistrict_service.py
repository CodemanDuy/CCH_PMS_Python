import os, sys
import inspect, types

ROOT_DIR = os.getcwd()  # Get root directory
sys.path.append(os.path.dirname(ROOT_DIR + r'/'))# Add absolute path to current sys.path


from services.base_service import BaseService

from services.account.account_service import AccountService

"""
doc: Service class to process logic
"""
class SubdistrictService():

    def __init__(self):
        self.base_service = BaseService()
        self.db = BaseService.DbFilePath
        self.ec = self.base_service.Entity()
        self.util_common = self.base_service.UtilCommon()
        self.Subdistrict = self.ec.InitEntityClass('Subdistrict')
        self.service_account = AccountService()


    def get_subdistrict_all(self):
        with self.base_service.DbContext() as __context:
            result = __context.table(self.Subdistrict).select_all()
            return result
        
        return None

    def get_subdistrict_byId(self, idValue):
        with self.base_service.DbContext() as __context:
            result = __context.table(self.Subdistrict).select_by_id(idValue)
            return result
        
        return None

    def get_subdistrict_byName(self, searchText):
        with self.base_service.DbContext() as __context:
            conditions = ''' Name like '%{0}%' '''.format(searchText)
            result = __context.table(self.Subdistrict).select_by(conditions) 
            return result
        
        return None
    
    def get_subdistrict_byCode(self, searchText):
        with self.base_service.DbContext() as __context:
            conditions = ''' SubdistrictCode like '%{0}%' '''.format(searchText)
            result = __context.table(self.Subdistrict).select_by(conditions) 
            return result
        
        return None
   
    def add_district(self, paramModel):
        if( paramModel is not None and inspect.isclass(type(paramModel)) and type(paramModel) == self.Subdistrict):
            with self.base_service.DbContext() as __context:
                
                modelLastSubdistrict = __context.table(self.Subdistrict).select_lastrecord()# get last record of Subdistrict table to increment IndexNo
                
                # create new object of Subdistrict
                modelSubdistrict = self.Subdistrict()
                modelSubdistrict.SubdistrictId = modelLastSubdistrict.SubdistrictId + 1
                modelSubdistrict.CityId = hasattr(paramModel, 'CityId') and paramModel.CityId or None
                modelSubdistrict.Name = hasattr(paramModel, 'Name') and paramModel.Name or None
                modelSubdistrict.SubdistrictCode = hasattr(paramModel, 'SubdistrictCode') and paramModel.SubdistrictCode or None
                modelSubdistrict.SortOrder = hasattr(paramModel, 'SortOrder') and paramModel.SortOrder or None
                modelSubdistrict.IsAvailable = hasattr(paramModel, 'IsAvailable') and paramModel.IsAvailable or 1

                # insert to db
                result = __context.table(self.Subdistrict).insert_by_model(modelSubdistrict)
                if result:
                    return modelSubdistrict
        
        return None

    def update_district(self, paramModel):
        if(paramModel is not None and inspect.isclass(type(paramModel)) and type(paramModel) == self.Subdistrict):
            
            modelSubdistrictFromDb = self.get_subdistrict_byId(paramModel.SubdistrictId)
            
            if(modelSubdistrictFromDb is not None):
                
                modelSubdistrictFromDb.CityId = hasattr(paramModel, 'CityId') and paramModel.CityId or modelSubdistrictFromDb.CityId
                modelSubdistrictFromDb.Name = hasattr(paramModel, 'Name') and paramModel.Name or modelSubdistrictFromDb.Name
                modelSubdistrictFromDb.SubdistrictCode = hasattr(paramModel, 'SubdistrictCode') and paramModel.SubdistrictCode or modelSubdistrictFromDb.SubdistrictCode
                modelSubdistrictFromDb.SortOrder = hasattr(paramModel, 'SortOrder') and paramModel.SortOrder or modelSubdistrictFromDb.SortOrder
                modelSubdistrictFromDb.IsAvailable = hasattr(paramModel, 'IsAvailable') and paramModel.IsAvailable or modelSubdistrictFromDb.IsAvailable

                with self.base_service.DbContext() as __context:
                    # update to db
                    result = __context.table(self.Subdistrict).update_by_model(modelSubdistrictFromDb)
                    if result:
                        return modelSubdistrictFromDb
        return None

        


