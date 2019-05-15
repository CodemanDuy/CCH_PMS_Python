
"""
doc: Model class with the decorator
"""


class Client(object):
    """
    A data descriptor that sets and returns values normally and optional prints a message logging their access.
    """

    def __init__(self):
        pass
        
    @property
    def ClientId(self):
        return self.__ClientId
    @ClientId.setter
    def ClientId(self, val):
        self.__ClientId = val

    @property
    def IndexNo(self):
        return self.__IndexNo
    @IndexNo.setter
    def IndexNo(self, val):
        self.__IndexNo = val

    @property
    def BookerFgCode(self):
        return self.__BookerFgCode
    @BookerFgCode.setter
    def BookerFgCode(self, val):
        self.__BookerFgCode = val

    @property
    def IdentityPicture(self):
        return self.__IdentityPicture
    @IdentityPicture.setter
    def IdentityPicture(self, val):
        self.__IdentityPicture = val

    @property
    def IdentityCardId(self):
        return self.__IdentityCardId
    @IdentityCardId.setter
    def IdentityCardId(self, val):
        self.__IdentityCardId = val

    @property
    def FullName(self):
        return self.__FullName
    @FullName.setter
    def FullName(self, val):
        self.__FullName = val

    @property
    def FourgramCode(self):
        return self.__FourgramCode
    @FourgramCode.setter
    def FourgramCode(self, val):
        self.__FourgramCode = val


    @property
    def Phone1(self):
        return self.__Phone1
    @Phone1.setter
    def Phone1(self, val):
        self.__Phone1 = val

    @property
    def Phone2(self):
        return self.__Phone2
    @Phone2.setter
    def Phone2(self, val):
        self.__Phone2 = val

    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, val):
        self.__Email = val

    @property
    def TemporaryAddress(self):
        return self.__TemporaryAddress
    @TemporaryAddress.setter
    def TemporaryAddress(self, val):
        self.__TemporaryAddress = val

    @property
    def CurrentJob(self):
        return self.__CurrentJob
    @CurrentJob.setter
    def CurrentJob(self, val):
        self.__CurrentJob = val

    @property
    def SignatureScan(self):
        return self.__SignatureScan
    @SignatureScan.setter
    def SignatureScan(self, val):
        self.__SignatureScan = val

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
