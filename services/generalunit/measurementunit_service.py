import os, sys
import inspect, types

ROOT_DIR = os.getcwd()  # Get root directory
sys.path.append(os.path.dirname(ROOT_DIR + r'/'))# Add absolute path to current sys.path


from services.base_service import BaseService

from services.account.account_service import AccountService

"""
doc: Service class to process logic
"""
class MeasurementUnitService():

    def __init__(self):
        self.base_service = BaseService()
        self.db = BaseService.DbFilePath
        self.ec = self.base_service.Entity()
        self.util_common = self.base_service.UtilCommon()
        self.MeasurementUnit = self.ec.InitEntityClass('MeasurementUnit')
        self.service_account = AccountService()


    def get_measurementunit_all(self):
        with self.base_service.DbContext() as __context:
            result = __context.table(self.MeasurementUnit).select_all()
            return result
        
        return None

    def get_measurementunit_byId(self, idValue):
        with self.base_service.DbContext() as __context:
            result = __context.table(self.MeasurementUnit).select_by_id(idValue)
            return result
        
        return None

    def get_measurementunit_byName(self, searchText):
        with self.base_service.DbContext() as __context:
            conditions = ''' Name like '%{0}%' '''.format(searchText)
            result = __context.table(self.MeasurementUnit).select_by(conditions) 
            return result
        
        return None
   
    def add_measurementunit(self, paramModel):
        if( paramModel is not None and inspect.isclass(type(paramModel)) and type(paramModel) == self.MeasurementUnit):
            with self.base_service.DbContext() as __context:
                
                modelLastMeasurementUnit = __context.table(self.MeasurementUnit).select_lastrecord()# get last record of MeasurementUnit table to increment IndexNo
                
                # create new object of MeasurementUnit
                modelMeasurementUnit = self.MeasurementUnit()
                modelMeasurementUnit.MeasurementUnitId = modelLastMeasurementUnit.MeasurementUnitId + 1
                modelMeasurementUnit.Name = hasattr(paramModel, 'Name') and paramModel.Name or None
                modelMeasurementUnit.Description = hasattr(paramModel, 'Description') and paramModel.Description or None
                modelMeasurementUnit.SortOrder = hasattr(paramModel, 'SortOrder') and paramModel.SortOrder or None
                modelMeasurementUnit.IsAvailable = hasattr(paramModel, 'IsAvailable') and paramModel.IsAvailable or 1

                # insert to db
                result = __context.table(self.MeasurementUnit).insert_by_model(modelMeasurementUnit)
                if result:
                    return modelMeasurementUnit
        
        return None

    def update_measurementunit(self, paramModel):
        if(paramModel is not None and inspect.isclass(type(paramModel)) and type(paramModel) == self.MeasurementUnit):
            
            modelMeasurementUnitFromDb = self.get_measurementunit_byId(paramModel.MeasurementUnitId)
            
            if(modelMeasurementUnitFromDb is not None):
           
                modelMeasurementUnitFromDb.Name = hasattr(paramModel, 'Name') and paramModel.Name or modelMeasurementUnitFromDb.Name
                modelMeasurementUnitFromDb.Description = hasattr(paramModel, 'Description') and paramModel.Description or modelMeasurementUnitFromDb.Description
                modelMeasurementUnitFromDb.SortOrder = hasattr(paramModel, 'SortOrder') and paramModel.SortOrder or modelMeasurementUnitFromDb.SortOrder
                modelMeasurementUnitFromDb.IsAvailable = hasattr(paramModel, 'IsAvailable') and paramModel.IsAvailable or modelMeasurementUnitFromDb.IsAvailable

                with self.base_service.DbContext() as __context:
                    # update to db
                    result = __context.table(self.MeasurementUnit).update_by_model(modelMeasurementUnitFromDb)
                    if result:
                        return modelMeasurementUnitFromDb
        return None

        


