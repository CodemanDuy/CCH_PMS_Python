
"""
doc: Model class with the decorator
"""
class Country(object):
    """
    A data descriptor that sets and returns values normally and optional prints a message logging their access.
    """
    def __init__(self):
        pass

    @property
    def CountryId(self):
        return self.__CountryId
    @CountryId.setter
    def CountryId(self, val):
        self.__CountryId = val

    @property
    def CountryCode(self):
        return self.__CountryCode
    @CountryCode.setter
    def CountryCode(self, val):
        self.__CountryCode = val 

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, val):
        self.__Name = val 

    
    @property
    def SortOrder(self):
        return self.__SortOrder
    @SortOrder.setter
    def SortOrder(self, val):
        self.__SortOrder = val 
    
    @property
    def IsAvailable(self):
        return self.__IsAvailable
    @IsAvailable.setter
    def IsAvailable(self, val):
        self.__IsAvailable = val

