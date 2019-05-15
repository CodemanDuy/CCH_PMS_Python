import unittest
import sys
import os

ROOT_DIR = os.getcwd()  # Get root directory
sys.path.append(os.path.dirname(ROOT_DIR + r'/'))# Add absolute path to current sys.path
# print('Path: ' + str(sys.path))


from datacontext.entities_container import EntitiesContainer

from services.account.client_service import ClientService
from services.account.account_service import AccountService
from services.account.identitycard_service import IdentityCardService
from services.bookingproperty.booking_service import BookingService
from services.bookingproperty.bookingpayment_service import BookingPaymentService
from services.bookingproperty.bookingstatus_service import BookingStatusService
from services.generalunit.city_service import CityService
from services.generalunit.country_service import CountryService
from services.generalunit.district_service import DistrictService
from services.generalunit.measurementunit_service import MeasurementUnitService
from services.generalunit.subdistrict_service import SubdistrictService
from services.generalunit.timeunit_service import TimeUnitService
from services.property.property_service import PropertyService
from services.property.propertyavail_service import PropertyAvailibiltyTypeService
from services.property.propertyitem_service import PropertyItemService
from services.property.propertypricepolicy_service import PropertyPricePolicyService
from services.property.propertystatus_service import PropertyStatusService
from services.property.propertytype_service import PropertyTypeService



class ServiceTestCase(unittest.TestCase):

    Entity = EntitiesContainer()

    ######################################################################################################

    def test_account__get_account_all(self):

        service = AccountService()
        data = service.get_account_all()
        # #Print test data
        # ServiceTestCase.Entity.print_ValueListEntityClass(data)

        self.assertIsNotNone(data, '###Error Message: No data')

    def test_account__get_account_byId(self):

        service = AccountService()
        data = service.get_account_byId('19C715AB-AE97-4A67-B142-CDA388D9F76B')
        # ServiceTestCase.Entity.print_ValueEntityClass(data)

        self.assertIsNotNone(data, '###Error Message: No data')

    # def test_account__add_account(self):

    #     service = AccountService()
    #     modelAcc = ServiceTestCase.Entity.InitEntityClass('Account')()
    #     modelAcc.Username = 'DULE0001'
    #     modelAcc.Pw = 'ASdasd&*cxa*^'
    #     data = service.add_account(modelAcc)
    #     # ServiceTestCase.Entity.print_ValueEntityClass(data)

    #     self.assertIsNotNone(data, '###Error Message: No data')

    def test_account__update_account(self):

        service = AccountService()
        modelAcc = service.get_account_byId(
            '19C715AB-AE97-4A67-B142-CDA388D9F76B')
        modelAcc.Pw = 'ASdwpvb&*euz*^'
        data = service.update_account(modelAcc)
        # ServiceTestCase.Entity.print_ValueEntityClass(data)

        self.assertIsNotNone(data, '###Error Message: No data')

    def test_account__combination(self):

        service = AccountService()
        data = service.get_account_all()
        # #Print test data
        # ServiceTestCase.Entity.print_ValueListEntityClass(data)

        accountId = '19C715AB-AE97-4A67-B142-CDA388D9F76B'
        data2 = service.get_account_byId(accountId)
        # print('#'*10 + 'AccountId: ' + accountId + '#'*10)
        # ServiceTestCase.Entity.print_ValueEntityClass(data2)

        self.assertIsNotNone(data, '###Error Message: No data')
        self.assertIsNotNone(data2, '###Error Message: No data')

    ######################################################################################################
    def test_client__get_client_all(self):

        service = ClientService()
        data = service.get_client_all()
        # #Print test data
        # ServiceTestCase.Entity.print_ValueListEntityClass(data)

        self.assertIsNotNone(data, '###Error Message: No data')

    def test_client__get_client_byId(self):

        service = ClientService()
        data = service.get_client_byId('317FFFC4-2A10-47B0-9FFE-A28D4E38130F')
        # ServiceTestCase.Entity.print_ValueEntityClass(data)

        self.assertIsNotNone(data, '###Error Message: No data')

    # def test_client__add_client(self):

    #     service = ClientService()
    #     modelClient = ServiceTestCase.Entity.InitEntityClass('Client')()
    #     modelClient.FullName = 'tran mai trang'
    #     data = service.add_client(modelClient)
    #     # ServiceTestCase.Entity.print_ValueEntityClass(data)

    #     self.assertIsNotNone(data, '###Error Message: No data')

    # def test_client__update_client(self):

    #     service = ClientService()
    #     modelClient = service.get_client_byId(
    #         'CDCF9992-7AA5-45E1-9095-21EFC992CB3F')
    #     modelClient.Phone2 = '+113'
    #     modelClient.IsAvailable = 1
    #     data = service.update_client(modelClient)
    #     # ServiceTestCase.Entity.print_ValueEntityClass(data)

    #     self.assertIsNotNone(data, '###Error Message: No data')

    ######################################################################################################
    def test_identitycard__get_idcard_all(self):

        service = IdentityCardService()
        data = service.get_idcard_all()
        # #Print test data
        # ServiceTestCase.Entity.print_ValueListEntityClass(data)

        self.assertIsNotNone(data, '###Error Message: No data')

    ######################################################################################################
    
    def test_booking__get_booking_all(self):
        service = BookingService()
        data = service.get_booking_all()
        #Print test data
        # ServiceTestCase.Entity.print_ValueListEntityClass(data)

        self.assertIsNotNone(data, '###Error Message: No data')
    
    ######################################################################################################
    
    def test_bookingpayment__get_bookingpayment_all(self):
        service = BookingPaymentService()
        data = service.get_bookingpayment_all()
        #Print test data
        # ServiceTestCase.Entity.print_ValueListEntityClass(data)

        self.assertIsNotNone(data, '###Error Message: No data')

    ######################################################################################################
    
    def test_bookingstatus__get_bookingstatus_all(self):
        service = BookingStatusService()
        data = service.get_bookingstatus_all()
        #Print test data
        # ServiceTestCase.Entity.print_ValueListEntityClass(data)

        self.assertIsNotNone(data, '###Error Message: No data')

    ######################################################################################################
    
    def test_city__get_city_all(self):
        service = CityService()
        data = service.get_city_all()
        #Print test data
        # ServiceTestCase.Entity.print_ValueListEntityClass(data)

        self.assertIsNotNone(data, '###Error Message: No data')

    ######################################################################################################
    
    def test_country__get_country_all(self):
        service = CountryService()
        data = service.get_country_all()
        #Print test data
        # ServiceTestCase.Entity.print_ValueListEntityClass(data)

        self.assertIsNotNone(data, '###Error Message: No data')       

    ######################################################################################################
    
    def test_district__get_district_all(self):
        service = DistrictService()
        data = service.get_district_all()
        #Print test data
        # ServiceTestCase.Entity.print_ValueListEntityClass(data)

        self.assertIsNotNone(data, '###Error Message: No data')      

    ######################################################################################################
    
    def test_measurementunit__get_measurementunit_all(self):
        service = MeasurementUnitService()
        data = service.get_measurementunit_all()
        #Print test data
        # ServiceTestCase.Entity.print_ValueListEntityClass(data)

        self.assertIsNotNone(data, '###Error Message: No data')     

    ######################################################################################################
    
    def test_subdistrict__get_subdistrict_all(self):
        service = SubdistrictService()
        data = service.get_subdistrict_all()
        #Print test data
        # ServiceTestCase.Entity.print_ValueListEntityClass(data)

        self.assertIsNotNone(data, '###Error Message: No data')    

    ######################################################################################################
    
    def test_timeunit__get_timeunit_all(self):
        service = TimeUnitService()
        data = service.get_timeunit_all()
        #Print test data
        # ServiceTestCase.Entity.print_ValueListEntityClass(data)

        self.assertIsNotNone(data, '###Error Message: No data')     

    ######################################################################################################
    
    def test_property__get_property_all(self):
        service = PropertyService()
        data = service.get_property_all()
        #Print test data
        # ServiceTestCase.Entity.print_ValueListEntityClass(data)

        self.assertIsNotNone(data, '###Error Message: No data')     

    ######################################################################################################
    
    def test_propertyavail__get_propavailtype_all(self):
        service = PropertyAvailibiltyTypeService()
        data = service.get_propavailtype_all()
        #Print test data
        # ServiceTestCase.Entity.print_ValueListEntityClass(data)

        self.assertIsNotNone(data, '###Error Message: No data')     

    ######################################################################################################
    
    def test_propertyitem__get_propitem_all(self):
        service = PropertyItemService()
        data = service.get_propitem_all()
        #Print test data
        # ServiceTestCase.Entity.print_ValueListEntityClass(data)

        self.assertIsNotNone(data, '###Error Message: No data')     

    ######################################################################################################
    
    def test_propertypricepolicy__get_proppricepol_all(self):
        service = PropertyPricePolicyService()
        data = service.get_proppricepol_all()
        #Print test data
        # ServiceTestCase.Entity.print_ValueListEntityClass(data)

        self.assertIsNotNone(data, '###Error Message: No data')  

    ######################################################################################################
    
    def test_propertystatus__get_propstatus_all(self):
        service = PropertyStatusService()
        data = service.get_propstatus_all()
        #Print test data
        # ServiceTestCase.Entity.print_ValueListEntityClass(data)

        self.assertIsNotNone(data, '###Error Message: No data')  

    ######################################################################################################
    
    def test_propertytype__get_proptype_all(self):
        service = PropertyTypeService()
        data = service.get_proptype_all()
        #Print test data
        # ServiceTestCase.Entity.print_ValueListEntityClass(data)

        self.assertIsNotNone(data, '###Error Message: No data')  


###########################################################################################################
"""
doc: Code will begin from here
"""
if __name__ == '__main__':

    unittest.main()

   