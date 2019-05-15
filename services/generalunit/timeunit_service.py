import os, sys
import inspect, types

ROOT_DIR = os.getcwd()  # Get root directory
sys.path.append(os.path.dirname(ROOT_DIR + r'/'))# Add absolute path to current sys.path


from services.base_service import BaseService

from services.account.account_service import AccountService

"""
doc: Service class to process logic
"""
class TimeUnitService():

    def __init__(self):
        self.base_service = BaseService()
        self.db = BaseService.DbFilePath
        self.ec = self.base_service.Entity()
        self.util_common = self.base_service.UtilCommon()
        self.TimeUnit = self.ec.InitEntityClass('TimeUnit')
        self.service_account = AccountService()


    def get_timeunit_all(self):
        with self.base_service.DbContext() as __context:
            result = __context.table(self.TimeUnit).select_all()
            return result
        
        return None

    def get_timeunit_byId(self, idValue):
        with self.base_service.DbContext() as __context:
            result = __context.table(self.TimeUnit).select_by_id(idValue)
            return result
        
        return None

    def get_timeunit_byName(self, searchText):
        with self.base_service.DbContext() as __context:
            conditions = ''' Name like '%{0}%' '''.format(searchText)
            result = __context.table(self.TimeUnit).select_by(conditions) 
            return result
        
        return None
   
    def add_timeunit(self, paramModel):
        if( paramModel is not None and inspect.isclass(type(paramModel)) and type(paramModel) == self.TimeUnit):
            with self.base_service.DbContext() as __context:
                
                modelLastTimeUnit = __context.table(self.TimeUnit).select_lastrecord()# get last record of TimeUnit table to increment IndexNo
                
                # create new object of TimeUnit
                modelTimeUnit = self.TimeUnit()
                modelTimeUnit.TimeUnitId = modelLastTimeUnit.TimeUnitId + 1
                modelTimeUnit.Name = hasattr(paramModel, 'Name') and paramModel.Name or None
                modelTimeUnit.Description = hasattr(paramModel, 'Description') and paramModel.Description or None
                modelTimeUnit.ToHours = hasattr(paramModel, 'ToHours') and paramModel.ToHours or None
                modelTimeUnit.ToHoursLeapYear = hasattr(paramModel, 'ToHoursLeapYear') and paramModel.ToHoursLeapYear or None
                modelTimeUnit.SortOrder = hasattr(paramModel, 'SortOrder') and paramModel.SortOrder or None
                modelTimeUnit.IsAvailable = hasattr(paramModel, 'IsAvailable') and paramModel.IsAvailable or 1

                # insert to db
                result = __context.table(self.TimeUnit).insert_by_model(modelTimeUnit)
                if result:
                    return modelTimeUnit
        
        return None

    def update_timeunit(self, paramModel):
        if(paramModel is not None and inspect.isclass(type(paramModel)) and type(paramModel) == self.TimeUnit):
            
            modelTimeUnitFromDb = self.get_timeunit_byId(paramModel.TimeUnitId)
            
            if(modelTimeUnitFromDb is not None):
           
                modelTimeUnitFromDb.Name = hasattr(paramModel, 'Name') and paramModel.Name or modelTimeUnitFromDb.Name
                modelTimeUnitFromDb.Description = hasattr(paramModel, 'Description') and paramModel.Description or modelTimeUnitFromDb.Description
                modelTimeUnitFromDb.ToHours = hasattr(paramModel, 'ToHours') and paramModel.ToHours or modelTimeUnitFromDb.ToHours
                modelTimeUnitFromDb.ToHoursLeapYear = hasattr(paramModel, 'ToHoursLeapYear') and paramModel.ToHoursLeapYear or modelTimeUnitFromDb.ToHoursLeapYear
                modelTimeUnitFromDb.SortOrder = hasattr(paramModel, 'SortOrder') and paramModel.SortOrder or modelTimeUnitFromDb.SortOrder
                modelTimeUnitFromDb.IsAvailable = hasattr(paramModel, 'IsAvailable') and paramModel.IsAvailable or modelTimeUnitFromDb.IsAvailable

                with self.base_service.DbContext() as __context:
                    # update to db
                    result = __context.table(self.TimeUnit).update_by_model(modelTimeUnitFromDb)
                    if result:
                        return modelTimeUnitFromDb
        return None

        


