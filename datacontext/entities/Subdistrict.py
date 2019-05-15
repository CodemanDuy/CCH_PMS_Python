
"""
doc: Model class with the decorator
"""
class Subdistrict(object):
    """
    A data descriptor that sets and returns values normally and optional prints a message logging their access.
    """
    def __init__(self):
        pass
        
    @property
    def SubdistrictId(self):
        return self.__SubdistrictId
    @SubdistrictId.setter
    def SubdistrictId(self, val):
        self.__SubdistrictId = val


    @property
    def DistrictId(self):
        return self.__DistrictId
    @DistrictId.setter
    def DistrictId(self, val):
        self.__DistrictId = val
        
    @property
    def SubdistrictCode(self):
        return self.__SubdistrictCode
    @SubdistrictCode.setter
    def SubdistrictCode(self, val):
        self.__SubdistrictCode = val

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

