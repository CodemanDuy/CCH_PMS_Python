
"""
doc: Model class with the decorator
"""

class PropertyPricePolicy(object):
    """
    A data descriptor that sets and returns values normally and optional prints a message logging their access.
    """

    def __init__(self):
        pass
        
    @property
    def PropPriceId(self):
        return self.__PropPriceId
    @PropPriceId.setter
    def PropPriceId(self, val):
        self.__PropPriceId = val

    @property
    def PropertyItemId(self):
        return self.__PropertyItemId
    @PropertyItemId.setter
    def PropertyItemId(self, val):
        self.__PropertyItemId = val

    @property
    def TimeUnitId(self):
        return self.__TimeUnitId
    @TimeUnitId.setter
    def TimeUnitId(self, val):
        self.__TimeUnitId = val

    @property
    def CostActual(self):
        return self.__CostActual
    @CostActual.setter
    def CostActual(self, val):
        self.__CostActual = val

    @property
    def PriceOrigin(self):
        return self.__PriceOrigin
    @PriceOrigin.setter
    def PriceOrigin(self, val):
        self.__PriceOrigin = val

    @property
    def PercentageDiscount(self):
        return self.__PercentageDiscount
    @PercentageDiscount.setter
    def PercentageDiscount(self, val):
        self.__PercentageDiscount = val

    @property
    def PriceActual(self):
        return self.__PriceActual
    @PriceActual.setter
    def PriceActual(self, val):
        self.__PriceActual = val


    @property
    def DepositAmount(self):
        return self.__DepositAmount
    @DepositAmount.setter
    def DepositAmount(self, val):
        self.__DepositAmount = val

    @property
    def DateApplied(self):
        return self.__DateApplied
    @DateApplied.setter
    def DateApplied(self, val):
        self.__DateApplied = val

    @property
    def IsConfirmed(self):
        return self.__IsConfirmed
    @IsConfirmed.setter
    def IsConfirmed(self, val):
        self.__IsConfirmed = val


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
