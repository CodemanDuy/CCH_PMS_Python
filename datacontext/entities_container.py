import inspect
import sys


from datacontext.entities.Account import Account
from datacontext.entities.Booking import Booking
from datacontext.entities.BookingPayment import BookingPayment
from datacontext.entities.BookingStatus import BookingStatus
from datacontext.entities.Country import Country
from datacontext.entities.City import City
from datacontext.entities.Client import Client
from datacontext.entities.District import District
from datacontext.entities.IdentityCard import IdentityCard
from datacontext.entities.IdentityCardType import IdentityCardType
from datacontext.entities.MeasurementUnit import MeasurementUnit
from datacontext.entities.Property import Property
from datacontext.entities.PropertyAvailibiltyType import PropertyAvailibiltyType
from datacontext.entities.PropertyItem import PropertyItem
from datacontext.entities.PropertyPricePolicy import PropertyPricePolicy
from datacontext.entities.PropertyStatus import PropertyStatus
from datacontext.entities.PropertyType import PropertyType
from datacontext.entities.ServicePayment import ServicePayment
from datacontext.entities.ServicePricePolicy import ServicePricePolicy
from datacontext.entities.ServicePriceProgressivePolicy import ServicePriceProgressivePolicy
from datacontext.entities.ServiceType import ServiceType
from datacontext.entities.Subdistrict import Subdistrict
from datacontext.entities.Supplier import Supplier
from datacontext.entities.TimeUnit import TimeUnit

"""
doc: Container to declare all entities model
"""
class EntitiesContainer():

    def __init__(self):
        pass

    def get_allEntityClassRegistered(self):

        container = [(name, obj) for name, obj in list(inspect.getmembers(sys.modules[__name__], inspect.isclass)) if name not in EntitiesContainer.__name__]
        return container
            
    def InitEntityClass(self, className):

        clsmembers = self.get_allEntityClassRegistered()
        for name, obj in clsmembers:
            if name in className:
                return obj

    def print_ValueEntityClass(self, model):

        if(model is not None and inspect.isclass(type(model))):
            attrs = [ (key, value) for key, value in inspect.getmembers(model) 
                if (key not in dir(type('dummy', (object,), {}))) 
                and not (key.startswith('_') or key.endswith('_')) 
            ]

            for key, value in attrs:
                print(str(key) + ': ' + str(value))

    def print_ValueListEntityClass(self, listmodel):

        if(listmodel is not None):
            for item in listmodel:
                print('#'*40)
                self.print_ValueEntityClass(item)


    def map_ToAnEntityClass(self, entityModel, listAttrs, obj):

        if entityModel is None or not listAttrs or obj is None:
            return None
        
        entity = entityModel()
        attrsValue = [item for item in obj]
        for idx, value in enumerate(attrsValue):
            setattr(entity, listAttrs[idx], value)#setattr(object, name, value)
        
        return entity

    def map_ToListEntityClass(self, entityModel, listAttrs, listObj):

        if entityModel is None or not listAttrs or not listObj:
            return None

        listEntity = []
        for obj in listObj:
            entity = entityModel()
            attrsValue = [item for item in obj]
            for idx, value in enumerate(attrsValue):
                setattr(entity, listAttrs[idx], value)#setattr(object, name, value)
            listEntity.append(entity)
        
        return listEntity
    
    def map_UpdateValueToAnEntityClass(self, entityModel, attrName, attrValue):
        if attrName is None or attrValue is None:
            return None
            
        setattr(entityModel, attrName, attrValue)
        
        return entityModel

       