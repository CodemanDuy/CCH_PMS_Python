

"""
doc: Model class with the decorator
"""


class IdentityCard(object):
    """
    A data descriptor that sets and returns values normally and optional prints a message logging their access.
    """

    def __init__(self):
        pass
        
    @property
    def IdentityCardId(self):
        return self.__IdentityCardId

    @IdentityCardId.setter
    def IdentityCardId(self, val):
        self.__IdentityCardId = val

    @property
    def IndexNo(self):
        return self.__IndexNo

    @IndexNo.setter
    def IndexNo(self, val):
        self.__IndexNo = val

    @property
    def IdentityCardType(self):
        return self.__IdentityCardType

    @IdentityCardType.setter
    def IdentityCardType(self, val):
        self.__IdentityCardType = val

    @property
    def IdentityNo(self):
        return self.__IdentityNo

    @IdentityNo.setter
    def IdentityNo(self, val):
        self.__IdentityNo = val

    @property
    def FullName(self):
        return self.__FullName

    @FullName.setter
    def FullName(self, val):
        self.__FullName = val

    @property
    def DOB(self):
        return self.__DOB

    @DOB.setter
    def DOB(self, val):
        self.__DOB = val

    @property
    def Gender(self):
        return self.__Gender

    @Gender.setter
    def Gender(self, val):
        self.__Gender = val


    @property
    def HomeTownAddress(self):
        return self.__HomeTownAddress

    @HomeTownAddress.setter
    def HomeTownAddress(self, val):
        self.__HomeTownAddress = val

    @property
    def PermanentAddress(self):
        return self.__PermanentAddress

    @PermanentAddress.setter
    def PermanentAddress(self, val):
        self.__PermanentAddress = val

    @property
    def CountryId(self):
        return self.__CountryId

    @CountryId.setter
    def CountryId(self, val):
        self.__CountryId = val    

    @property
    def DateIssued(self):
        return self.__DateIssued

    @DateIssued.setter
    def DateIssued(self, val):
        self.__DateIssued = val

    @property
    def DateExpired(self):
        return self.__DateExpired

    @DateExpired.setter
    def DateExpired(self, val):
        self.__DateExpired = val

    @property
    def ScanFile(self):
        return self.__ScanFile

    @ScanFile.setter
    def ScanFile(self, val):
        self.__ScanFile = val


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
