
"""
doc: Model class with the decorator
"""

class Supplier(object):
    """
    A data descriptor that sets and returns values normally and optional prints a message logging their access.
    """

    def __init__(self):
        pass
        
    @property
    def SupplierId(self):
        return self.__SupplierId
    @SupplierId.setter
    def SupplierId(self, val):
        self.__SupplierId = val


    @property
    def ServiceTypeId(self):
        return self.__ServiceTypeId
    @ServiceTypeId.setter
    def ServiceTypeId(self, val):
        self.__ServiceTypeId = val

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, val):
        self.__Name = val

    @property
    def FullName(self):
        return self.__FullName
    @FullName.setter
    def FullName(self, val):
        self.__FullName = val

    @property
    def Abbreviation(self):
        return self.__Abbreviation
    @Abbreviation.setter
    def Abbreviation(self, val):
        self.__Abbreviation = val

    @property
    def TaxIdentificationNo(self):
        return self.__TaxIdentificationNo
    @TaxIdentificationNo.setter
    def TaxIdentificationNo(self, val):
        self.__TaxIdentificationNo = val

    @property
    def OfficialAddress(self):
        return self.__OfficialAddress
    @OfficialAddress.setter
    def OfficialAddress(self, val):
        self.__OfficialAddress = val