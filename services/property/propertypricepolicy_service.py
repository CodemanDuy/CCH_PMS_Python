import os, sys
import inspect, types

ROOT_DIR = os.getcwd()  # Get root directory
sys.path.append(os.path.dirname(ROOT_DIR + r'/'))# Add absolute path to current sys.path


from services.base_service import BaseService

from services.account.account_service import AccountService

"""
doc: Service class to process logic
"""
class PropertyPricePolicyService():

    def __init__(self):
        self.base_service = BaseService()
        self.db = BaseService.DbFilePath
        self.ec = self.base_service.Entity()
        self.util_common = self.base_service.UtilCommon()
        self.PropertyPricePolicy = self.ec.InitEntityClass('PropertyPricePolicy')
        self.service_account = AccountService()


    def get_proppricepol_all(self):
        with self.base_service.DbContext() as __context:
            result = __context.table(self.PropertyPricePolicy).select_all()
            return result
        
        return None

    def get_proppricepol_byId(self, idValue):
        with self.base_service.DbContext() as __context:
            result = __context.table(self.PropertyPricePolicy).select_by_id(idValue)
            return result
        
        return None
   
    def add_proppricepol(self, paramModel):
        if( paramModel is not None and inspect.isclass(type(paramModel)) and type(paramModel) == self.PropertyPricePolicy):
            with self.base_service.DbContext() as __context:
                
                modelAdmin = self.service_account.get_accountAdmin()# get limit 1 result 

                modelLastPropertyPricePolicy = __context.table(self.PropertyPricePolicy).select_lastrecord()# get last record of PropertyPricePolicy table to increment IndexNo
                
                # create new object of PropertyPricePolicy
                modelPropertyPricePolicy = self.PropertyPricePolicy()
                modelPropertyPricePolicy.PropPriceId = modelLastPropertyPricePolicy.PropPriceId + 1
                modelPropertyPricePolicy.PropertyItemId = hasattr(paramModel, 'PropertyItemId') and paramModel.PropertyItemId or None
                modelPropertyPricePolicy.TimeUnitId = hasattr(paramModel, 'TimeUnitId') and paramModel.TimeUnitId or None
                modelPropertyPricePolicy.CostActual = hasattr(paramModel, 'CostActual') and paramModel.CostActual or None
                modelPropertyPricePolicy.PriceOrigin = hasattr(paramModel, 'PriceOrigin') and paramModel.PriceOrigin or None
                modelPropertyPricePolicy.PercentageDiscount = hasattr(paramModel, 'PercentageDiscount') and paramModel.PercentageDiscount or None
                modelPropertyPricePolicy.PriceActual = hasattr(paramModel, 'PriceActual') and paramModel.PriceActual or None
                modelPropertyPricePolicy.DepositAmount = hasattr(paramModel, 'DepositAmount') and paramModel.DepositAmount or None
                modelPropertyPricePolicy.DateApplied = hasattr(paramModel, 'DateApplied') and paramModel.DateApplied or None
                modelPropertyPricePolicy.IsConfirmed = hasattr(paramModel, 'IsConfirmed') and paramModel.IsConfirmed or 0

                modelPropertyPricePolicy.CreatedBy = modelAdmin.IndexNo
                modelPropertyPricePolicy.LastModifiedBy = modelAdmin.IndexNo
                modelPropertyPricePolicy.DateCreated = str(self.util_common.currentDateTime())
                modelPropertyPricePolicy.DateLastModified = str(self.util_common.currentDateTime())

                # insert to db
                result = __context.table(self.PropertyPricePolicy).insert_by_model(modelPropertyPricePolicy)
                if result:
                    return modelPropertyPricePolicy
        
        return None

    def update_proppricepol(self, paramModel):
        if(paramModel is not None and inspect.isclass(type(paramModel)) and type(paramModel) == self.PropertyPricePolicy):
            
            modelPropertyPricePolicyFromDb = self.get_proppricepol_byId(paramModel.PropPriceId)
            
            if(modelPropertyPricePolicyFromDb is not None):

                modelAdmin = self.service_account.get_accountAdmin()# get limit 1 result 
           
                modelPropertyPricePolicyFromDb.PropertyItemId = hasattr(paramModel, 'PropertyItemId') and paramModel.PropertyItemId or modelPropertyPricePolicyFromDb.PropertyItemId
                modelPropertyPricePolicyFromDb.TimeUnitId = hasattr(paramModel, 'TimeUnitId') and paramModel.TimeUnitId or modelPropertyPricePolicyFromDb.TimeUnitId
                modelPropertyPricePolicyFromDb.CostActual = hasattr(paramModel, 'CostActual') and paramModel.CostActual or modelPropertyPricePolicyFromDb.CostActual
                modelPropertyPricePolicyFromDb.PriceOrigin = hasattr(paramModel, 'PriceOrigin') and paramModel.PriceOrigin or modelPropertyPricePolicyFromDb.PriceOrigin
                modelPropertyPricePolicyFromDb.PercentageDiscount = hasattr(paramModel, 'PercentageDiscount') and paramModel.PercentageDiscount or modelPropertyPricePolicyFromDb.PercentageDiscount
                modelPropertyPricePolicyFromDb.PriceActual = hasattr(paramModel, 'PriceActual') and paramModel.PriceActual or modelPropertyPricePolicyFromDb.PriceActual
                modelPropertyPricePolicyFromDb.DepositAmount = hasattr(paramModel, 'DepositAmount') and paramModel.DepositAmount or modelPropertyPricePolicyFromDb.DepositAmount
                modelPropertyPricePolicyFromDb.DateApplied = hasattr(paramModel, 'DateApplied') and paramModel.DateApplied or modelPropertyPricePolicyFromDb.DateApplied
                modelPropertyPricePolicyFromDb.IsConfirmed = hasattr(paramModel, 'IsConfirmed') and paramModel.IsConfirmed  or modelPropertyPricePolicyFromDb.IsConfirmed
                
                modelPropertyPricePolicyFromDb.LastModifiedBy = modelAdmin.IndexNo
                modelPropertyPricePolicyFromDb.DateLastModified = str(self.util_common.currentDateTime())

                with self.base_service.DbContext() as __context:
                    # update to db
                    result = __context.table(self.PropertyPricePolicy).update_by_model(modelPropertyPricePolicyFromDb)
                    if result:
                        return modelPropertyPricePolicyFromDb
        return None

        


