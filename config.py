import json
import sys, os
#use pathlib to auto convert file path formatted between os platforms
from pathlib import Path, PureWindowsPath


ROOT_DIR = os.getcwd()# Get root directory
sys.path.append(os.path.dirname(ROOT_DIR + r'/'))# Add absolute path to current sys.path
# print('Path: ' + str(sys.path))

class Configuration():
    

    def __init__(self):
        Configuration.ConfigFileName = "config.json"
        Configuration.Platform = self.getOSplatform()

        
    def getOSplatform(self):        
        os = ""

        if sys.platform == "linux" or sys.platform == "linux2":            
            os = "Linux"
        elif sys.platform == "darwin":            
            os = "OSX"
        elif sys.platform == "win32":
            os = "Window"
        
        return os
    

    def getDbConnection(self, dbName):
        
        try:
            filename = Path(ROOT_DIR + r'\\' + Configuration.ConfigFileName)
            with open(filename, 'rt') as config_file:
                config = json.load(config_file)
                # print(config)  
                for cf in list(config['configurations']):
                    if(cf['type'] == "db_connection" and cf['platform_os'] == self.Platform and cf['db_name'] == dbName):
                        return cf
            
            return None

        except Exception as ex:
            print('Error: ', ex)


    def getDbFilePath(self, dbName):

        db_conn = self.getDbConnection(dbName)
        if db_conn:
            path = PureWindowsPath(ROOT_DIR + db_conn['db_file_path'] + r'\\' + db_conn['db_name'] + db_conn['db_file_extension'])
            return Path(path)

        return None

    

        
