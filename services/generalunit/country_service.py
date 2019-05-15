import os, sys
import inspect, types

ROOT_DIR = os.getcwd()  # Get root directory
sys.path.append(os.path.dirname(ROOT_DIR + r'/'))# Add absolute path to current sys.path


from services.base_service import BaseService

from services.account.account_service import AccountService

"""
doc: Service class to process logic
"""
class CountryService():

    def __init__(self):
        self.base_service = BaseService()
        self.db = BaseService.DbFilePath
        self.ec = self.base_service.Entity()
        self.util_common = self.base_service.UtilCommon()
        self.Country = self.ec.InitEntityClass('Country')
        self.service_account = AccountService()


    def get_country_all(self):
        with self.base_service.DbContext() as __context:
            result = __context.table(self.Country).select_all()
            return result
        
        return None

    def get_country_byId(self, idValue):
        with self.base_service.DbContext() as __context:
            result = __context.table(self.Country).select_by_id(idValue)
            return result
        
        return None

    def get_country_byName(self, searchText):
        with self.base_service.DbContext() as __context:
            conditions = ''' Name like '%{0}%' '''.format(searchText)
            result = __context.table(self.Country).select_by(conditions) 
            return result
        
        return None
    
    def get_country_byCode(self, searchText):
        with self.base_service.DbContext() as __context:
            conditions = ''' CountryCode like '%{0}%' '''.format(searchText)
            result = __context.table(self.Country).select_by(conditions) 
            return result
        
        return None
   
    def add_country(self, paramModel):
        if( paramModel is not None and inspect.isclass(type(paramModel)) and type(paramModel) == self.Country):
            with self.base_service.DbContext() as __context:
                
                modelLastCountry = __context.table(self.Country).select_lastrecord()# get last record of Country table to increment IndexNo
                
                # create new object of Country
                modelCountry = self.Country()
                modelCountry.CountryId = modelLastCountry.CountryId + 1
                modelCountry.Name = hasattr(paramModel, 'Name') and paramModel.Name or None
                modelCountry.CountryCode = hasattr(paramModel, 'CountryCode') and paramModel.CountryCode or None
                modelCountry.SortOrder = hasattr(paramModel, 'SortOrder') and paramModel.SortOrder or None
                modelCountry.IsAvailable = hasattr(paramModel, 'IsAvailable') and paramModel.IsAvailable or 1

                # insert to db
                result = __context.table(self.Country).insert_by_model(modelCountry)
                if result:
                    return modelCountry
        
        return None

    def update_country(self, paramModel):
        if(paramModel is not None and inspect.isclass(type(paramModel)) and type(paramModel) == self.Country):
            
            modelCountryFromDb = self.get_country_byId(paramModel.CountryId)
            
            if(modelCountryFromDb is not None):
           
                modelCountryFromDb.Name = hasattr(paramModel, 'Name') and paramModel.Name or modelCountryFromDb.Name
                modelCountryFromDb.CountryCode = hasattr(paramModel, 'CountryCode') and paramModel.CountryCode or modelCountryFromDb.CountryCode
                modelCountryFromDb.SortOrder = hasattr(paramModel, 'SortOrder') and paramModel.SortOrder or modelCountryFromDb.SortOrder
                modelCountryFromDb.IsAvailable = hasattr(paramModel, 'IsAvailable') and paramModel.IsAvailable or modelCountryFromDb.IsAvailable

                with self.base_service.DbContext() as __context:
                    # update to db
                    result = __context.table(self.Country).update_by_model(modelCountryFromDb)
                    if result:
                        return modelCountryFromDb
        return None

        


