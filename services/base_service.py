import os, sys
import inspect, types

ROOT_DIR = os.getcwd()  # Get root directory
sys.path.append(os.path.dirname(ROOT_DIR + r'/'))# Add absolute path to current sys.path
# print("Root Directory:", ROOT_DIR)
# print('Path: ' + str(sys.path))

from datacontext.sqlite_dbcontext import Database
from datacontext.entities_container import EntitiesContainer

from coreutil.util_common import Core_UtilityCommon
from coreutil.util_security import Core_UtilitySecurity

from config import Configuration

"""
doc: Service class to process logic
"""
class BaseService():

    Config = Configuration()
    DbFilePath = Config.getDbFilePath("CCH_PMS")
    DbConnectionInfo = Config.getDbConnection("CCH_PMS")
    #If want to mock another database incase need to connect two database at the same time, just set another variable here and also setup in config.json file. 
    #Eg: "test" is the name of another database match same name in config.json
    # DbFilePath2 = Config.getDbFilePath("test")
    # DbConnectionInfo2 = Config.getDbConnection("test")

    def __init__(self):
        pass

    def DbContext(self):
        return Database(BaseService.DbFilePath) 
    
    def Entity(self):
        return EntitiesContainer()
    
    def UtilCommon(self):
        return Core_UtilityCommon()

    def UtilSecurity(self):
        return Core_UtilitySecurity


        



