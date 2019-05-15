
"""
doc: Model class with the decorator
"""


class BookingPayment(object):
    """
    A data descriptor that sets and returns values normally and optional prints a message logging their access.
    """

    def __init__(self):
        pass
        
    @property
    def BookingPaymentId(self):
        return self.__BookingPaymentId

    @BookingPaymentId.setter
    def BookingPaymentId(self, val):
        self.__BookingPaymentId = val

    @property
    def BookingId(self):
        return self.__BookingId

    @BookingId.setter
    def BookingId(self, val):
        self.__BookingId = val

    @property
    def DepositAmount(self):
        return self.__DepositAmount

    @DepositAmount.setter
    def DepositAmount(self, val):
        self.__DepositAmount = val

    @property
    def DepositPaid(self):
        return self.__DepositPaid

    @DepositPaid.setter
    def DepositPaid(self, val):
        self.__DepositPaid = val

    @property
    def FixedAmount(self):
        return self.__FixedAmount

    @FixedAmount.setter
    def FixedAmount(self, val):
        self.__FixedAmount = val

    @property
    def FixedPaid(self):
        return self.__FixedPaid

    @FixedPaid.setter
    def FixedPaid(self, val):
        self.__FixedPaid = val

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
