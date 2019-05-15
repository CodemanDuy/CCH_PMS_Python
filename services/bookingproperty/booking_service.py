import os, sys
import inspect, types

ROOT_DIR = os.getcwd()  # Get root directory
sys.path.append(os.path.dirname(ROOT_DIR + r'/'))# Add absolute path to current sys.path


from services.base_service import BaseService
from services.account.account_service import AccountService

"""
doc: Service class to process logic
"""
class BookingService():

    def __init__(self):
        self.base_service = BaseService()
        self.db = BaseService.DbFilePath
        self.ec = self.base_service.Entity()
        self.util_common = self.base_service.UtilCommon()
        self.Booking = self.ec.InitEntityClass('Booking')
        self.service_account = AccountService()

    def get_booking_all(self):
        with self.base_service.DbContext() as __context:
            result = __context.table(self.Booking).select_all()
            return result
        
        return None

    def get_booking_byId(self, idValue):
        with self.base_service.DbContext() as __context:
            result = __context.table(self.Booking).select_by_id(idValue)
            return result
        
        return None
   
    def add_booking(self, paramModel):
        if( paramModel is not None and inspect.isclass(type(paramModel)) and type(paramModel) == self.Booking):
            with self.base_service.DbContext() as __context:
                
                modelAdmin = self.service_account.get_accountAdmin()# get limit 1 result 
                
                # create new object of Booking
                modelBooking = self.Booking()
                modelBooking.BookingId = str(self.util_common.generateUUID())
                modelBooking.AccountBookerId = hasattr(paramModel, 'AccountBookerId') and paramModel.AccountBookerId or None
                modelBooking.PropPriceId = hasattr(paramModel, 'PropPriceId') and paramModel.PropPriceId or None
                modelBooking.DateArrival = hasattr(paramModel, 'DateArrival') and paramModel.DateArrival or None
                modelBooking.DateCheckout = hasattr(paramModel, 'DateCheckout') and paramModel.DateCheckout or None
                modelBooking.DateActualArrival = hasattr(paramModel, 'DateActualArrival') and paramModel.DateActualArrival or None
                modelBooking.DateActualCheckout = hasattr(paramModel, 'DateActualCheckout') and paramModel.DateActualCheckout or None
                modelBooking.TotalPeople = hasattr(paramModel, 'TotalPeople') and paramModel.TotalPeople or None
                modelBooking.PriceDealed = hasattr(paramModel, 'PriceDealed') and paramModel.PriceDealed or None
                modelBooking.DepositDealed = hasattr(paramModel, 'DepositDealed') and paramModel.DepositDealed or None
                modelBooking.PaymentDateInMonth = hasattr(paramModel, 'PaymentDateInMonth') and paramModel.PaymentDateInMonth or None
                
                modelBooking.CreatedBy = modelAdmin.IndexNo
                modelBooking.LastModifiedBy = modelAdmin.IndexNo
                modelBooking.DateCreated = str(self.util_common.currentDateTime())
                modelBooking.DateLastModified = str(self.util_common.currentDateTime())

                # insert to db
                result = __context.table(self.Booking).insert_by_model(modelBooking)
                if result:
                    return modelBooking
        
        return None

    def update_booking(self, paramModel):
        if(paramModel is not None and inspect.isclass(type(paramModel)) and type(paramModel) == self.Booking):
            
            modelBookingFromDb = self.get_booking_byId(paramModel.BookingId)
            
            if(modelBookingFromDb is not None):

                modelAdmin = self.service_account.get_accountAdmin()# get limit 1 result 

                modelBookingFromDb.AccountBookerId = hasattr(paramModel, 'AccountBookerId') and paramModel.AccountBookerId or modelBookingFromDb.AccountBookerId
                modelBookingFromDb.PropPriceId = hasattr(paramModel, 'PropPriceId') and paramModel.PropPriceId or modelBookingFromDb.PropPriceId
                modelBookingFromDb.DateArrival = hasattr(paramModel, 'DateArrival') and paramModel.DateArrival or modelBookingFromDb.DateArrival
                modelBookingFromDb.DateCheckout = hasattr(paramModel, 'DateCheckout') and paramModel.DateCheckout or modelBookingFromDb.DateCheckout
                modelBookingFromDb.DateActualArrival = hasattr(paramModel, 'DateActualArrival') and paramModel.DateActualArrival or modelBookingFromDb.DateActualArrival
                modelBookingFromDb.DateActualCheckout = hasattr(paramModel, 'DateActualCheckout') and paramModel.DateActualCheckout or modelBookingFromDb.DateActualCheckout
                modelBookingFromDb.TotalPeople = hasattr(paramModel, 'TotalPeople') and paramModel.TotalPeople or modelBookingFromDb.TotalPeople
                modelBookingFromDb.PriceDealed = hasattr(paramModel, 'PriceDealed') and paramModel.PriceDealed or modelBookingFromDb.PriceDealed
                modelBookingFromDb.DepositDealed = hasattr(paramModel, 'DepositDealed') and paramModel.DepositDealed or modelBookingFromDb.DepositDealed
                modelBookingFromDb.PaymentDateInMonth = hasattr(paramModel, 'PaymentDateInMonth') and paramModel.PaymentDateInMonth or modelBookingFromDb.PaymentDateInMonth
                
                modelBookingFromDb.LastModifiedBy = modelAdmin.IndexNo
                modelBookingFromDb.DateLastModified = str(self.util_common.currentDateTime())

                with self.base_service.DbContext() as __context:
                    # update to db
                    result = __context.table(self.Booking).update_by_model(modelBookingFromDb)
                    if result:
                        return modelBookingFromDb
        return None

        


