
"""
doc: Model class with the decorator
"""


class ServicePricePolicy(object):
    """
    A data descriptor that sets and returns values normally and optional prints a message logging their access.
    """

    def __init__(self):
        pass

    @property
    def ServPriceId(self):
        return self.__ServPriceId

    @ServPriceId.setter
    def ServPriceId(self, val):
        self.__ServPriceId = val

    @property
    def PropertyItemId(self):
        return self.__PropertyItemId

    @PropertyItemId.setter
    def PropertyItemId(self, val):
        self.__PropertyItemId = val

    @property
    def SupplierId(self):
        return self.__SupplierId

    @SupplierId.setter
    def SupplierId(self, val):
        self.__SupplierId = val

    @property
    def TimeUnitId(self):
        return self.__TimeUnitId
    @TimeUnitId.setter
    def TimeUnitId(self, val):
        self.__TimeUnitId = val

    @property
    def ServicePriceProgressivePolicyRootId(self):
        return self.__ServicePriceProgressivePolicyRootId
    @ServicePriceProgressivePolicyRootId.setter
    def ServicePriceProgressivePolicyRootId(self, val):
        self.__ServicePriceProgressivePolicyRootId = val   

    @property
    def CostActual(self):
        return self.__CostActual
    @CostActual.setter
    def CostActual(self, val):
        self.__CostActual = val

    @property
    def CommissionPercentage(self):
        return self.__CommissionPercentage
    @CommissionPercentage.setter
    def CommissionPercentage(self, val):
        self.__CommissionPercentage = val

    @property
    def PriceActual(self):
        return self.__PriceActual
    @PriceActual.setter
    def PriceActual(self, val):
        self.__PriceActual = val


    @property
    def DateApplied(self):
        return self.__DateApplied
    @DateApplied.setter
    def DateApplied(self, val):
        self.__DateApplied = val


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