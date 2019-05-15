
"""
doc: Model class with the decorator
"""
class City(object):
    """
    A data descriptor that sets and returns values normally and optional prints a message logging their access.
    """
    def __init__(self):
        pass

    @property
    def CityId(self):
        return self.__CityId
    @CityId.setter
    def CityId(self, val):
        self.__CityId = val


    @property
    def CountryId(self):
        return self.__CountryId
    @CountryId.setter
    def CountryId(self, val):
        self.__CountryId = val
        

    @property
    def ParentId(self):
        return self.__ParentId
    @ParentId.setter
    def ParentId(self, val):
        self.__ParentId = val

    @property
    def CityCode(self):
        return self.__CityCode
    @CityCode.setter
    def CityCode(self, val):
        self.__CityCode = val 

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

