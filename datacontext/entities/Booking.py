
"""
doc: Model class with the decorator
"""


class Booking(object):
    """
    A data descriptor that sets and returns values normally and optional prints a message logging their access.
    """

    def __init__(self):
        pass

    @property
    def BookingId(self):
        return self.__BookingId

    @BookingId.setter
    def BookingId(self, val):
        self.__BookingId = val

    @property
    def AccountBookerId(self):
        return self.__AccountBookerId

    @AccountBookerId.setter
    def AccountBookerId(self, val):
        self.__AccountBookerId = val

    @property
    def PropPriceId(self):
        return self.__PropPriceId

    @PropPriceId.setter
    def PropPriceId(self, val):
        self.__PropPriceId = val

    @property
    def DateArrival(self):
        return self.__DateArrival

    @DateArrival.setter
    def DateArrival(self, val):
        self.__DateArrival = val

    @property
    def DateCheckout(self):
        return self.__DateCheckout

    @DateCheckout.setter
    def DateCheckout(self, val):
        self.__DateCheckout = val

    @property
    def DateActualArrival(self):
        return self.__DateActualArrival

    @DateActualArrival.setter
    def DateActualArrival(self, val):
        self.__DateActualArrival = val

    @property
    def DateActualCheckout(self):
        return self.__DateActualCheckout

    @DateActualCheckout.setter
    def DateActualCheckout(self, val):
        self.__DateActualCheckout = val

    @property
    def TotalPeople(self):
        return self.__TotalPeople

    @TotalPeople.setter
    def TotalPeople(self, val):
        self.__TotalPeople = val

    @property
    def PriceDealed(self):
        return self.__PriceDealed

    @PriceDealed.setter
    def PriceDealed(self, val):
        self.__PriceDealed = val


    @property
    def DepositDealed(self):
        return self.__DepositDealed
    @DepositDealed.setter
    def DepositDealed(self, val):
        self.__DepositDealed = val

    @property
    def PaymentDateInMonth(self):
        return self.__PaymentDateInMonth
    @PaymentDateInMonth.setter
    def PaymentDateInMonth(self, val):
        self.__PaymentDateInMonth = val


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
