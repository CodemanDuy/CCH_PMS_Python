
"""
doc: Model class with the decorator
"""

class Account(object):
    """
    A data descriptor that sets and returns values normally and optional prints a message logging their access.
    """

    def __init__(self):
        pass
    
    @property
    def AccountId(self):
        return self.__AccountId
    @AccountId.setter
    def AccountId(self, val):
        self.__AccountId = val

    @property
    def IndexNo(self):
        return self.__IndexNo
    @IndexNo.setter
    def IndexNo(self, val):
        self.__IndexNo = val

    @property
    def Username(self):
        return self.__Username
    @Username.setter
    def Username(self, val):
        self.__Username = val

    @property
    def IsBooker(self):
        return self.__IsBooker
    @IsBooker.setter
    def IsBooker(self, val):
        self.__IsBooker = val

    @property
    def IsMasterAdmin(self):
        return self.__IsMasterAdmin
    @IsMasterAdmin.setter
    def IsMasterAdmin(self, val):
        self.__IsMasterAdmin = val

    @property
    def IpAddress(self):
        return self.__IpAddress
    @IpAddress.setter
    def IpAddress(self, val):
        self.__IpAddress = val

    @property
    def Pw(self):
        return self.__Pw
    @Pw.setter
    def Pw(self, val):
        self.__Pw = val


    @property
    def SaltKey(self):
        return self.__SaltKey
    @SaltKey.setter
    def SaltKey(self, val):
        self.__SaltKey = val

    @property
    def DateLastLogin(self):
        return self.__DateLastLogin
    @DateLastLogin.setter
    def DateLastLogin(self, val):
        self.__DateLastLogin = val

    @property
    def IsAvailable(self):
        return self.__IsAvailable
    @IsAvailable.setter
    def IsAvailable(self, val):
        self.__IsAvailable = val


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
