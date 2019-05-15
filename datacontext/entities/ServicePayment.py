
"""
doc: Model class with the decorator
"""


class ServicePayment(object):
    """
    A data descriptor that sets and returns values normally and optional prints a message logging their access.
    """

    def __init__(self):
        pass
        
    @property
    def ServicePaymentId(self):
        return self.__ServicePaymentId

    @ServicePaymentId.setter
    def ServicePaymentId(self, val):
        self.__ServicePaymentId = val

    @property
    def BookingId(self):
        return self.__BookingId

    @BookingId.setter
    def BookingId(self, val):
        self.__BookingId = val

    @property
    def ServPriceId(self):
        return self.__ServPriceId

    @ServPriceId.setter
    def ServPriceId(self, val):
        self.__ServPriceId = val

    @property
    def Name(self):
        return self.__Name

    @Name.setter
    def Name(self, val):
        self.__Name = val

    @property
    def CurrentUsageData(self):
        return self.__CurrentUsageData

    @CurrentUsageData.setter
    def CurrentUsageData(self, val):
        self.__CurrentUsageData = val

    @property
    def Amount(self):
        return self.__Amount

    @Amount.setter
    def Amount(self, val):
        self.__Amount = val

    @property
    def AmountPaid(self):
        return self.__AmountPaid

    @AmountPaid.setter
    def AmountPaid(self, val):
        self.__AmountPaid = val

    @property
    def DateApplied(self):
        return self.__DateApplied

    @DateApplied.setter
    def DateApplied(self, val):
        self.__DateApplied = val

    @property
    def DateEnd(self):
        return self.__DateEnd

    @DateEnd.setter
    def DateEnd(self, val):
        self.__DateEnd = val


    @property
    def IsClosed(self):
        return self.__IsClosed
    @IsClosed.setter
    def IsClosed(self, val):
        self.__IsClosed = val


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
