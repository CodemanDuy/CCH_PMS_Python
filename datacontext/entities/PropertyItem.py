
"""
doc: Model class with the decorator
"""


class PropertyItem(object):
    """
    A data descriptor that sets and returns values normally and optional prints a message logging their access.
    """

    def __init__(self):
        pass
        
    @property
    def PropertyItemId(self):
        return self.__PropertyItemId

    @PropertyItemId.setter
    def PropertyItemId(self, val):
        self.__PropertyItemId = val

    @property
    def IndexNo(self):
        return self.__IndexNo

    @IndexNo.setter
    def IndexNo(self, val):
        self.__IndexNo = val

    @property
    def ParentId(self):
        return self.__ParentId

    @ParentId.setter
    def ParentId(self, val):
        self.__ParentId = val

    @property
    def PropertyId(self):
        return self.__PropertyId

    @PropertyId.setter
    def PropertyId(self, val):
        self.__PropertyId = val

    @property
    def PropertyTypeId(self):
        return self.__PropertyTypeId

    @PropertyTypeId.setter
    def PropertyTypeId(self, val):
        self.__PropertyTypeId = val

    @property
    def PropertyStatusId(self):
        return self.__PropertyStatusId

    @PropertyStatusId.setter
    def PropertyStatusId(self, val):
        self.__PropertyStatusId = val

    @property
    def PropAvailTypeId(self):
        return self.__PropAvailTypeId

    @PropAvailTypeId.setter
    def PropAvailTypeId(self, val):
        self.__PropAvailTypeId = val

    @property
    def Name(self):
        return self.__Name

    @Name.setter
    def Name(self, val):
        self.__Name = val

    @property
    def ShortDescription(self):
        return self.__ShortDescription

    @ShortDescription.setter
    def ShortDescription(self, val):
        self.__ShortDescription = val


    @property
    def LongDescription(self):
        return self.__LongDescription
    @LongDescription.setter
    def LongDescription(self, val):
        self.__LongDescription = val

    @property
    def FloorNo(self):
        return self.__FloorNo
    @FloorNo.setter
    def FloorNo(self, val):
        self.__FloorNo = val

    @property
    def RoomName(self):
        return self.__RoomName
    @RoomName.setter
    def RoomName(self, val):
        self.__RoomName = val

    @property
    def Width(self):
        return self.__Width
    @Width.setter
    def Width(self, val):
        self.__Width = val

    @property
    def Length(self):
        return self.__Length
    @Length.setter
    def Length(self, val):
        self.__Length = val

    @property
    def AreaUsage(self):
        return self.__AreaUsage
    @AreaUsage.setter
    def AreaUsage(self, val):
        self.__AreaUsage = val


    @property
    def MaxAllowPeople(self):
        return self.__MaxAllowPeople
    @MaxAllowPeople.setter
    def MaxAllowPeople(self, val):
        self.__MaxAllowPeople = val

    @property
    def LastElectricalUsageNo(self):
        return self.__LastElectricalUsageNo
    @LastElectricalUsageNo.setter
    def LastElectricalUsageNo(self, val):
        self.__LastElectricalUsageNo = val

    @property
    def LastWaterUsageNo(self):
        return self.__LastWaterUsageNo
    @LastWaterUsageNo.setter
    def LastWaterUsageNo(self, val):
        self.__LastWaterUsageNo = val


    @property
    def IsAvailable(self):
        return self.__IsAvailable
    @IsAvailable.setter
    def IsAvailable(self, val):
        self.__IsAvailable = val

    @property
    def IsRemoved(self):
        return self.__IsRemoved
    @IsRemoved.setter
    def IsRemoved(self, val):
        self.__IsRemoved = val

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
