
"""
doc: Model class with the decorator
"""

class Property(object):
    """
    A data descriptor that sets and returns values normally and optional prints a message logging their access.
    """

    def __init__(self):
        pass
        
    @property
    def PropertyId(self):
        return self.__PropertyId
    @PropertyId.setter
    def PropertyId(self, val):
        self.__PropertyId = val

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, val):
        self.__Name = val

    @property
    def Description(self):
        return self.__Description
    @Description.setter
    def Description(self, val):
        self.__Description = val

    @property
    def CountryId(self):
        return self.__CountryId
    @CountryId.setter
    def CountryId(self, val):
        self.__CountryId = val

    @property
    def AreaId(self):
        return self.__AreaId
    @AreaId.setter
    def AreaId(self, val):
        self.__AreaId = val

    @property
    def CityId(self):
        return self.__CityId
    @CityId.setter
    def CityId(self, val):
        self.__CityId = val

    @property
    def DistrictId(self):
        return self.__DistrictId
    @DistrictId.setter
    def DistrictId(self, val):
        self.__DistrictId = val


    @property
    def SubDistrictId(self):
        return self.__SubDistrictId
    @SubDistrictId.setter
    def SubDistrictId(self, val):
        self.__SubDistrictId = val

    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, val):
        self.__Address = val

    @property
    def IsAvailable(self):
        return self.__IsAvailable
    @IsAvailable.setter
    def IsAvailable(self, val):
        self.__IsAvailable = val

    @property
    def IsRemoved(self):
        return self.__IsRemoved
    @IsRemoved.setter
    def IsRemoved(self, val):
        self.__IsRemoved = val

    @property
    def DateCreated(self):
        return self.__DateCreated
    @DateCreated.setter
    def DateCreated(self, val):
        self.__DateCreated = val

    @property
    def DateLastModified(self):
        return self.__DateLastModified
    @DateLastModified.setter
    def DateLastModified(self, val):
        self.__DateLastModified = val

    @property
    def CreatedBy(self):
        return self.__CreatedBy
    @CreatedBy.setter
    def CreatedBy(self, val):
        self.__CreatedBy = val

    @property
    def LastModifiedBy(self):
        return self.__LastModifiedBy
    @LastModifiedBy.setter
    def LastModifiedBy(self, val):
        self.__LastModifiedBy = val
