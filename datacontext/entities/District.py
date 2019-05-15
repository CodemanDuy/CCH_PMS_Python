
"""
doc: Model class with the decorator
"""
class District(object):
    """
    A data descriptor that sets and returns values normally and optional prints a message logging their access.
    """
    def __init__(self):
        pass
        
    @property
    def DistrictId(self):
        return self.__DistrictId
    @DistrictId.setter
    def DistrictId(self, val):
        self.__DistrictId = val


    @property
    def CityId(self):
        return self.__CityId
    @CityId.setter
    def CityId(self, val):
        self.__CityId = val
        

    @property
    def DistrictCode(self):
        return self.__DistrictCode
    @DistrictCode.setter
    def DistrictCode(self, val):
        self.__DistrictCode = val


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

