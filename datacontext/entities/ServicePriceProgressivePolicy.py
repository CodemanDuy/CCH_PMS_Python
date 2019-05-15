
"""
doc: Model class with the decorator
"""


class ServicePriceProgressivePolicy(object):
    """
    A data descriptor that sets and returns values normally and optional prints a message logging their access.
    """

    def __init__(self):
        pass
        
    @property
    def ServicePriceProgressivePolicyId(self):
        return self.__ServicePriceProgressivePolicyId

    @ServicePriceProgressivePolicyId.setter
    def ServicePriceProgressivePolicyId(self, val):
        self.__ServicePriceProgressivePolicyId = val

    @property
    def SupplierId(self):
        return self.__SupplierId

    @SupplierId.setter
    def SupplierId(self, val):
        self.__SupplierId = val

    @property
    def PropertyType(self):
        return self.__PropertyType

    @PropertyType.setter
    def PropertyType(self, val):
        self.__PropertyType = val

    @property
    def ParentId(self):
        return self.__ParentId
    @ParentId.setter
    def ParentId(self, val):
        self.__ParentId = val

    @property
    def Level(self):
        return self.__Level
    @Level.setter
    def Level(self, val):
        self.__Level = val   

    @property
    def BeginRange(self):
        return self.__BeginRange
    @BeginRange.setter
    def BeginRange(self, val):
        self.__BeginRange = val

    @property
    def EndRange(self):
        return self.__EndRange
    @EndRange.setter
    def EndRange(self, val):
        self.__EndRange = val

    @property
    def ServiceMeasurementUnitId(self):
        return self.__ServiceMeasurementUnitId
    @ServiceMeasurementUnitId.setter
    def ServiceMeasurementUnitId(self, val):
        self.__ServiceMeasurementUnitId = val


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