
"""
doc: Model class with the decorator
"""

class TimeUnit(object):
    """
    A data descriptor that sets and returns values normally and optional prints a message logging their access.
    """

    def __init__(self):
        pass
        
    @property
    def TimeUnitId(self):
        return self.__TimeUnitId
    @TimeUnitId.setter
    def TimeUnitId(self, val):
        self.__TimeUnitId = val

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, val):
        self.__Name = val

    @property
    def Description(self):
        return self.__Description
    @Description.setter
    def Description(self, val):
        self.__Description = val

    @property
    def ToHours(self):
        return self.__ToHours
    @ToHours.setter
    def ToHours(self, val):
        self.__ToHours = val

    @property
    def ToHoursLeapYear(self):
        return self.__ToHoursLeapYear
    @ToHoursLeapYear.setter
    def ToHoursLeapYear(self, val):
        self.__ToHoursLeapYear = val

    @property
    def SortOrder(self):
        return self.__SortOrder
    @SortOrder.setter
    def SortOrder(self, val):
        self.__SortOrder = val

    @property
    def IsAvailable(self):
        return self.__IsAvailable
    @IsAvailable.setter
    def IsAvailable(self, val):
        self.__IsAvailable = val