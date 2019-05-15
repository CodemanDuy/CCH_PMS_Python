import os, sys
import inspect, types

ROOT_DIR = os.getcwd()  # Get root directory
sys.path.append(os.path.dirname(ROOT_DIR + r'/'))# Add absolute path to current sys.path


from services.base_service import BaseService

from services.account.account_service import AccountService

"""
doc: Service class to process logic
"""
class PropertyItemService():

    def __init__(self):
        self.base_service = BaseService()
        self.db = BaseService.DbFilePath
        self.ec = self.base_service.Entity()
        self.util_common = self.base_service.UtilCommon()
        self.PropertyItem = self.ec.InitEntityClass('PropertyItem')
        self.service_account = AccountService()


    def get_propitem_all(self):
        with self.base_service.DbContext() as __context:
            result = __context.table(self.PropertyItem).select_all()
            return result
        
        return None

    def get_propitem_byId(self, idValue):
        with self.base_service.DbContext() as __context:
            result = __context.table(self.PropertyItem).select_by_id(idValue)
            return result
        
        return None
    
    def get_propitem_byName(self, searchText):
        with self.base_service.DbContext() as __context:
            conditions = ''' FullName like '%{0}%' '''.format(searchText)
            result = __context.table(self.PropertyItem).select_by(conditions) 
            return result
        
        return None
   
    def add_propitem(self, paramModel):
        if( paramModel is not None and inspect.isclass(type(paramModel)) and type(paramModel) == self.PropertyItem):
            with self.base_service.DbContext() as __context:
                
                modelAdmin = self.service_account.get_accountAdmin()# get limit 1 result 

                modelLastPropertyItem = __context.table(self.PropertyItem).select_lastrecord()# get last record of PropertyItem table to increment IndexNo
                
                # create new object of PropertyItem
                modelPropertyItem = self.PropertyItem()
                modelPropertyItem.PropertyItemId = str(self.util_common.generateUUID())
                modelPropertyItem.IndexNo = hasattr(paramModel, 'IndexNo') and paramModel.IndexNo or (modelLastPropertyItem.IndexNo + 1)
                modelPropertyItem.ParentId = hasattr(paramModel, 'ParentId') and paramModel.ParentId or None
                modelPropertyItem.PropertyId = hasattr(paramModel, 'PropertyId') and paramModel.PropertyId or None
                modelPropertyItem.PropertyTypeId = hasattr(paramModel, 'PropertyTypeId') and paramModel.PropertyTypeId or None
                modelPropertyItem.PropertyStatusId = hasattr(paramModel, 'PropertyStatusId') and paramModel.PropertyStatusId or None
                modelPropertyItem.PropAvailTypeId = hasattr(paramModel, 'PropAvailTypeId') and paramModel.PropAvailTypeId or None
                modelPropertyItem.Name = hasattr(paramModel, 'Name') and paramModel.Name or None
                modelPropertyItem.ShortDescription = hasattr(paramModel, 'ShortDescription') and paramModel.ShortDescription or None
                modelPropertyItem.LongDescription = hasattr(paramModel, 'LongDescription') and paramModel.LongDescription or None
                modelPropertyItem.FloorNo = hasattr(paramModel, 'FloorNo') and paramModel.FloorNo or None
                modelPropertyItem.RoomName = hasattr(paramModel, 'RoomName') and paramModel.RoomName or None
                modelPropertyItem.Width = hasattr(paramModel, 'Width') and paramModel.Width or 0
                modelPropertyItem.Length = hasattr(paramModel, 'Length') and paramModel.Length or 0
                modelPropertyItem.AreaUsage = hasattr(paramModel, 'AreaUsage') and paramModel.AreaUsage or 0
                modelPropertyItem.MaxAllowPeople = hasattr(paramModel, 'MaxAllowPeople') and paramModel.MaxAllowPeople or None
                modelPropertyItem.LastElectricalUsageNo = hasattr(paramModel, 'LastElectricalUsageNo') and paramModel.LastElectricalUsageNo or None
                modelPropertyItem.LastWaterUsageNo = hasattr(paramModel, 'LastWaterUsageNo') and paramModel.LastWaterUsageNo or None
                modelPropertyItem.IsAvailable = hasattr(paramModel, 'IsAvailable') and paramModel.IsAvailable or 1
                modelPropertyItem.IsRemoved = hasattr(paramModel, 'IsRemoved') and paramModel.IsRemoved or 0

                modelPropertyItem.CreatedBy = modelAdmin.IndexNo
                modelPropertyItem.LastModifiedBy = modelAdmin.IndexNo
                modelPropertyItem.DateCreated = str(self.util_common.currentDateTime())
                modelPropertyItem.DateLastModified = str(self.util_common.currentDateTime())

                # insert to db
                result = __context.table(self.PropertyItem).insert_by_model(modelPropertyItem)
                if result:
                    return modelPropertyItem
        
        return None

    def update_propitem(self, paramModel):
        if(paramModel is not None and inspect.isclass(type(paramModel)) and type(paramModel) == self.PropertyItem):
            
            modelPropertyItemFromDb = self.get_propitem_byId(paramModel.PropertyItemId)
            
            if(modelPropertyItemFromDb is not None):

                modelAdmin = self.service_account.get_accountAdmin()# get limit 1 result 
           
                modelPropertyItemFromDb.IndexNo = hasattr(paramModel, 'IndexNo') and paramModel.IndexNo or modelPropertyItemFromDb.IndexNo
                modelPropertyItemFromDb.ParentId = hasattr(paramModel, 'ParentId') and paramModel.ParentId or modelPropertyItemFromDb.ParentId
                modelPropertyItemFromDb.PropertyId = hasattr(paramModel, 'PropertyId') and paramModel.PropertyId or modelPropertyItemFromDb.PropertyId
                modelPropertyItemFromDb.PropertyTypeId = hasattr(paramModel, 'PropertyTypeId') and paramModel.PropertyTypeId or modelPropertyItemFromDb.PropertyTypeId
                modelPropertyItemFromDb.PropertyStatusId = hasattr(paramModel, 'PropertyStatusId') and paramModel.PropertyStatusId or modelPropertyItemFromDb.PropertyStatusId
                modelPropertyItemFromDb.PropAvailTypeId = hasattr(paramModel, 'PropAvailTypeId') and paramModel.PropAvailTypeId or modelPropertyItemFromDb.PropAvailTypeId
                modelPropertyItemFromDb.Name = hasattr(paramModel, 'Name') and paramModel.Name or modelPropertyItemFromDb.Name
                modelPropertyItemFromDb.ShortDescription = hasattr(paramModel, 'ShortDescription') and paramModel.ShortDescription or modelPropertyItemFromDb.ShortDescription
                modelPropertyItemFromDb.LongDescription = hasattr(paramModel, 'LongDescription') and paramModel.LongDescription or modelPropertyItemFromDb.LongDescription
                modelPropertyItemFromDb.FloorNo = hasattr(paramModel, 'FloorNo') and paramModel.FloorNo or modelPropertyItemFromDb.FloorNo
                modelPropertyItemFromDb.RoomName = hasattr(paramModel, 'RoomName') and paramModel.RoomName or modelPropertyItemFromDb.RoomName
                modelPropertyItemFromDb.Width = hasattr(paramModel, 'Width') and paramModel.Width or modelPropertyItemFromDb.Width
                modelPropertyItemFromDb.Length = hasattr(paramModel, 'Length') and paramModel.Length or modelPropertyItemFromDb.Length
                modelPropertyItemFromDb.AreaUsage = hasattr(paramModel, 'AreaUsage') and paramModel.AreaUsage or modelPropertyItemFromDb.AreaUsage
                modelPropertyItemFromDb.MaxAllowPeople = hasattr(paramModel, 'MaxAllowPeople') and paramModel.MaxAllowPeople or modelPropertyItemFromDb.MaxAllowPeople
                modelPropertyItemFromDb.LastElectricalUsageNo = hasattr(paramModel, 'LastElectricalUsageNo') and paramModel.LastElectricalUsageNo or modelPropertyItemFromDb.LastElectricalUsageNo
                modelPropertyItemFromDb.LastWaterUsageNo = hasattr(paramModel, 'LastWaterUsageNo') and paramModel.LastWaterUsageNo or modelPropertyItemFromDb.LastWaterUsageNo
                modelPropertyItemFromDb.IsAvailable = hasattr(paramModel, 'IsAvailable') and paramModel.IsAvailable or 1
                modelPropertyItemFromDb.IsRemoved = hasattr(paramModel, 'IsRemoved') and paramModel.IsRemoved or 0
                
                modelPropertyItemFromDb.LastModifiedBy = modelAdmin.IndexNo
                modelPropertyItemFromDb.DateLastModified = str(self.util_common.currentDateTime())

                with self.base_service.DbContext() as __context:
                    # update to db
                    result = __context.table(self.PropertyItem).update_by_model(modelPropertyItemFromDb)
                    if result:
                        return modelPropertyItemFromDb
        return None

        


