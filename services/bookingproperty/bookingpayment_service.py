
import os, sys
import inspect, types

ROOT_DIR = os.getcwd()  # Get root directory
sys.path.append(os.path.dirname(ROOT_DIR + r'/'))# Add absolute path to current sys.path


from services.base_service import BaseService
from services.account.account_service import AccountService

"""
doc: Service class to process logic
"""
class BookingPaymentService():

    def __init__(self):
        self.base_service = BaseService()
        self.db = BaseService.DbFilePath
        self.ec = self.base_service.Entity()
        self.util_common = self.base_service.UtilCommon()
        self.BookingPayment = self.ec.InitEntityClass('BookingPayment')
        self.service_account = AccountService()


    def get_bookingpayment_all(self):
        with self.base_service.DbContext() as __context:
            result = __context.table(self.BookingPayment).select_all()
            return result
        
        return None

    def get_bookingpayment_byId(self, idValue):
        with self.base_service.DbContext() as __context:
            result = __context.table(self.BookingPayment).select_by_id(idValue)
            return result
        
        return None
   
    def add_bookingpayment(self, paramModel):
        if( paramModel is not None and inspect.isclass(type(paramModel)) and type(paramModel) == self.BookingPayment):
            with self.base_service.DbContext() as __context:
                
                modelAdmin = self.service_account.get_accountAdmin()# get limit 1 result 
                
                # create new object of BookingPayment
                modelBookingPayment = self.BookingPayment()
                modelBookingPayment.BookingPaymentId = str(self.util_common.generateUUID())
                modelBookingPayment.BookingId = hasattr(paramModel, 'BookingId') and paramModel.BookingId or None
                modelBookingPayment.DepositAmount = hasattr(paramModel, 'DepositAmount') and paramModel.DepositAmount or 0
                modelBookingPayment.DepositPaid = hasattr(paramModel, 'DepositPaid') and paramModel.DepositPaid or 0
                modelBookingPayment.FixedAmount = hasattr(paramModel, 'FixedAmount') and paramModel.FixedAmount or 0
                modelBookingPayment.FixedPaid = hasattr(paramModel, 'FixedPaid') and paramModel.FixedPaid or 0
                modelBookingPayment.DateApplied = hasattr(paramModel, 'DateApplied') and paramModel.DateApplied or None
                modelBookingPayment.DateEnd = hasattr(paramModel, 'DateEnd') and paramModel.DateEnd or None
                modelBookingPayment.IsClosed = hasattr(paramModel, 'IsClosed') and paramModel.IsClosed or 0
                
                modelBookingPayment.CreatedBy = modelAdmin.IndexNo
                modelBookingPayment.LastModifiedBy = modelAdmin.IndexNo
                modelBookingPayment.DateCreated = str(self.util_common.currentDateTime())
                modelBookingPayment.DateLastModified = str(self.util_common.currentDateTime())

                # insert to db
                result = __context.table(self.BookingPayment).insert_by_model(modelBookingPayment)
                if result:
                    return modelBookingPayment
        
        return None

    def update_bookingpayment(self, paramModel):
        if(paramModel is not None and inspect.isclass(type(paramModel)) and type(paramModel) == self.BookingPayment):
            
            modelBookingPaymentFromDb = self.get_bookingpayment_byId(paramModel.BookingPaymentId)
            
            if(modelBookingPaymentFromDb is not None):

                modelAdmin = self.service_account.get_accountAdmin()# get limit 1 result 

                modelBookingPaymentFromDb.BookingId = hasattr(paramModel, 'BookingId') and paramModel.BookingId or modelBookingPaymentFromDb.BookingId
                modelBookingPaymentFromDb.DepositAmount = hasattr(paramModel, 'DepositAmount') and paramModel.DepositAmount or modelBookingPaymentFromDb.DepositAmount
                modelBookingPaymentFromDb.DepositPaid = hasattr(paramModel, 'DepositPaid') and paramModel.DepositPaid or modelBookingPaymentFromDb.DepositPaid
                modelBookingPaymentFromDb.FixedAmount = hasattr(paramModel, 'FixedAmount') and paramModel.FixedAmount or modelBookingPaymentFromDb.FixedAmount
                modelBookingPaymentFromDb.FixedPaid = hasattr(paramModel, 'FixedPaid') and paramModel.FixedPaid or modelBookingPaymentFromDb.FixedPaid
                modelBookingPaymentFromDb.DateApplied = hasattr(paramModel, 'DateApplied') and paramModel.DateApplied or modelBookingPaymentFromDb.DateApplied
                modelBookingPaymentFromDb.DateEnd = hasattr(paramModel, 'DateEnd') and paramModel.DateEnd or modelBookingPaymentFromDb.DateEnd
                modelBookingPaymentFromDb.IsClosed = hasattr(paramModel, 'IsClosed') and paramModel.IsClosed or modelBookingPaymentFromDb.IsClosed
                
                modelBookingPaymentFromDb.LastModifiedBy = modelAdmin.IndexNo
                modelBookingPaymentFromDb.DateLastModified = str(self.util_common.currentDateTime())

                with self.base_service.DbContext() as __context:
                    # update to db
                    result = __context.table(self.BookingPayment).update_by_model(modelBookingPaymentFromDb)
                    if result:
                        return modelBookingPaymentFromDb
        return None

        


