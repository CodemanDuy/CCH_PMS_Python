import os, sys
import inspect, types

ROOT_DIR = os.getcwd()  # Get root directory
sys.path.append(os.path.dirname(ROOT_DIR + r'/'))# Add absolute path to current sys.path


from services.base_service import BaseService

from services.account.account_service import AccountService

"""
doc: Service class to process logic
"""
class BookingStatusService():

    def __init__(self):
        self.base_service = BaseService()
        self.db = BaseService.DbFilePath
        self.ec = self.base_service.Entity()
        self.util_common = self.base_service.UtilCommon()
        self.BookingStatus = self.ec.InitEntityClass('BookingStatus')
        self.service_account = AccountService()


    def get_bookingstatus_all(self):
        with self.base_service.DbContext() as __context:
            result = __context.table(self.BookingStatus).select_all()
            return result
        
        return None

    def get_bookingstatus_byId(self, idValue):
        with self.base_service.DbContext() as __context:
            result = __context.table(self.BookingStatus).select_by_id(idValue)
            return result
        
        return None

    def get_bookingstatus_byName(self, searchText):
        with self.base_service.DbContext() as __context:
            conditions = ''' Name like '%{0}%' '''.format(searchText)
            result = __context.table(self.BookingStatus).select_by(conditions) 
            return result
        
        return None
   
    def add_bookingstatus(self, paramModel):
        if( paramModel is not None and inspect.isclass(type(paramModel)) and type(paramModel) == self.BookingStatus):
            with self.base_service.DbContext() as __context:
                
                modelLastBookingStatus = __context.table(self.BookingStatus).select_lastrecord()# get last record of BookingStatus table to increment IndexNo
                
                # create new object of BookingStatus
                modelBookingStatus = self.BookingStatus()
                modelBookingStatus.BookingStatusId = modelLastBookingStatus.BookingStatusId + 1
                modelBookingStatus.Name = hasattr(paramModel, 'Name') and paramModel.Name or None
                modelBookingStatus.Description = hasattr(paramModel, 'Description') and paramModel.Description or None
                modelBookingStatus.SortOrder = hasattr(paramModel, 'SortOrder') and paramModel.SortOrder or None
                modelBookingStatus.IsAvailable = hasattr(paramModel, 'IsAvailable') and paramModel.IsAvailable or 1

                # insert to db
                result = __context.table(self.BookingStatus).insert_by_model(modelBookingStatus)
                if result:
                    return modelBookingStatus
        
        return None

    def update_bookingstatus(self, paramModel):
        if(paramModel is not None and inspect.isclass(type(paramModel)) and type(paramModel) == self.BookingStatus):
            
            modelBookingStatusFromDb = self.get_bookingstatus_byId(paramModel.BookingStatusId)
            
            if(modelBookingStatusFromDb is not None):
           
                modelBookingStatusFromDb.Name = hasattr(paramModel, 'Name') and paramModel.Name or modelBookingStatusFromDb.Name
                modelBookingStatusFromDb.Description = hasattr(paramModel, 'Description') and paramModel.Description or modelBookingStatusFromDb.Description
                modelBookingStatusFromDb.SortOrder = hasattr(paramModel, 'SortOrder') and paramModel.SortOrder or modelBookingStatusFromDb.SortOrder
                modelBookingStatusFromDb.IsAvailable = hasattr(paramModel, 'IsAvailable') and paramModel.IsAvailable or modelBookingStatusFromDb.IsAvailable

                with self.base_service.DbContext() as __context:
                    # update to db
                    result = __context.table(self.BookingStatus).update_by_model(modelBookingStatusFromDb)
                    if result:
                        return modelBookingStatusFromDb
        return None

        


