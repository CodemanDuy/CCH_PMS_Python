
"""
doc: Model class with the decorator
"""

class PropertyStatus(object):
    """
    A data descriptor that sets and returns values normally and optional prints a message logging their access.
    """

    def __init__(self):
        pass
        
    @property
    def PropertyStatusId(self):
        return self.__PropertyStatusId
    @PropertyStatusId.setter
    def PropertyStatusId(self, val):
        self.__PropertyStatusId = val

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
