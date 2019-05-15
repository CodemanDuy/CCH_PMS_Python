import sqlite3
import inspect, types
import sys, os


ROOT_DIR = os.getcwd()  # Get root directory
sys.path.append(os.path.dirname(ROOT_DIR + r'/'))# Add absolute path to current sys.path
# print('Path: ' + str(sys.path))

from coreutil.util_database import Core_UtilityDatabase
from coreutil.util_common import Core_UtilityCommon
from datacontext.entities_container import EntitiesContainer


"""
doc: Database class for generic method
"""
class Database():

    """
    Region: common method
    """
    def __init__(self, db_location = None):
        """Initialize db and open connection"""       
        self.__connection = sqlite3.connect(db_location)        
        # self.__connection.row_factory = sqlite3.Row
        self.cursorObj = self.__connection.cursor()
        self.curTable = ''
        self.curPrimaryKey = ''
        self.curAllColumnNames = []
        self.EntityContainer = EntitiesContainer()
        self.util_database = Core_UtilityDatabase()
        self.util_common = Core_UtilityCommon()

    def __enter__(self):
        return self

    def __exit__(self, ext_type, exc_value, traceback):
        """Close connection"""
        self.cursorObj.close()
        if isinstance(exc_value, Exception):
            self.__connection.rollback()
        else:
            self.__connection.commit()
        self.__connection.close()
    
    """
    End Region: common method
    """
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    """
    Region: service method
    """

    def table(self, entityClass):
        try:
            self.entityModel = entityClass

            tableName = entityClass.__name__
            query_table = ('SELECT name FROM sqlite_master WHERE type = "table" AND name = ?')
            cur = self.cursorObj.execute(query_table, (tableName, ))
            self.curTable = cur.fetchone()[0]
            # print('Table: ' + self.curTable)

            query_primarykey = ('SELECT name FROM pragma_table_info(?) as p where p.pk = 1')
            cur = self.cursorObj.execute(query_primarykey, (tableName, ))
            self.curPrimaryKey = cur.fetchone()[0]
            # print('PK: ' + self.curPrimaryKey)

            query_allcolumnnames = ('SELECT name FROM pragma_table_info(?)')
            cur = self.cursorObj.execute(query_allcolumnnames, (tableName, ))
            cols = cur.fetchall()
            self.curAllColumnNames = [str(col[0]) for col in cols]
            # print('Columns: ' + self.util_common.parseListToString(self.curAllColumnNames))

            return self
        
        except Exception as ex:
            print('Error: ', ex)

        # finally:
        #     self.__connection.close()

    
    def select_all(self):
        try:
            query = '''SELECT * FROM {}'''.format(self.curTable)
            cur = self.cursorObj.execute(query)
            lst_item = cur.fetchall()

            lst_entity = self.EntityContainer.map_ToListEntityClass(self.entityModel, self.curAllColumnNames, lst_item)

            return lst_entity
        
        except Exception as ex:
            print('Error: ', ex)


    def select_by_id(self, idValue):
        try:
            idValue = '"{0}"'.format(idValue)
            query = '''SELECT * FROM {0} WHERE {1} = {2}'''.format(self.curTable, self.curPrimaryKey, idValue)
            cur = self.cursorObj.execute(query)
            item = cur.fetchone()

            entity = self.EntityContainer.map_ToAnEntityClass(self.entityModel, self.curAllColumnNames, item)

            return entity

        except Exception as ex:
            print('Error: ', ex)
       

    def select_by(self, conditions = ()):
        try:
            query = '''SELECT * FROM {0} WHERE {1}'''.format(self.curTable, conditions)
            cur = self.cursorObj.execute(query)
            lst_item = cur.fetchall()

            lst_entity = self.EntityContainer.map_ToListEntityClass(self.entityModel, self.curAllColumnNames, lst_item)

            return lst_entity
        
        except Exception as ex:
            print('Error: ', ex)

    def select_lastrecord(self):
        try:
            query = '''SELECT * FROM {} ORDER by ROWID DESC LIMIT 1'''.format(self.curTable)
            cur = self.cursorObj.execute(query)
            item = cur.fetchone()

            entity = self.EntityContainer.map_ToAnEntityClass(self.entityModel, self.curAllColumnNames, item)

            return entity
        
        except Exception as ex:
            print('Error: ', ex)


    def insert(self, columns = (), values = ()):
        try:
            query = '''INSERT INTO {0} ({1}) values{2}'''.format(self.curTable, columns, values)
            cur = self.cursorObj.execute(query)

            return cur
        
        except Exception as ex:
            print('Error: ', ex)


    def insert_by_model(self, model):
        try:
            columns = ''
            values = ''

            if(inspect.isclass(type(model))):
                attrs = [ item[0] for item in inspect.getmembers(model) 
                if (item not in dir(type('dummy', (object,), {}))) 
                and not (item[0].startswith('_') or item[0].endswith('_')) 
                and isinstance(getattr(type(model), item[0], None), property) ]

                columns = self.util_common.parseListToString(attrs)
                
                val = []
                for attr in attrs:
                    if(attr in self.curAllColumnNames):
                        valAttr = getattr(model, attr)
                        
                        if(type(valAttr) is str):
                            valAttr = '"{0}"'.format(valAttr)
                        
                        if(valAttr is None):
                            valAttr = 'NULL'#(None,)
                        
                        val.append(str(valAttr))

                values = '({0})'.format(', '.join(val))
                columns = '({0})'.format(columns)
            
            query = '''INSERT or REPLACE INTO {0} {1} VALUES {2}'''.format(self.curTable, columns, values)
            cur = self.cursorObj.execute(query)

            return cur
        
        except Exception as ex:
            print('Error: ', ex)


    def insert_by_listmodel(self, listmodel = []):
        try:
            columns = ''
            values = ''

            lstValues = []
            for idx, model in enumerate(listmodel):
                if(inspect.isclass(type(model))):
                    attrs = [ item[0] for item in inspect.getmembers(model) 
                    if (item not in dir(type('dummy', (object,), {}))) 
                    and not (item[0].startswith('_') or item[0].endswith('_')) 
                    and isinstance(getattr(type(model), item[0], None), property) ]

                    if(idx == 0):
                        columns = self.util_common.parseListToString(attrs)
                    
                    lstAttrVal = []
                    for attr in attrs:
                        if(attr in self.curAllColumnNames):
                            valAttr = getattr(model, attr)
                            
                            if(type(valAttr) is str):
                                valAttr = '"{0}"'.format(valAttr)
                            
                            lstAttrVal.append(str(valAttr))
                            
                    value ='({0})'.format(', '.join(lstAttrVal))
                    lstValues.append(value)
            
            values = ', '.join(lstValues)
            columns = '({0})'.format(columns)
            query = '''INSERT or REPLACE INTO {0} {1} VALUES {2}'''.format(self.curTable, columns, values)
            cur = self.cursorObj.execute(query)

            return cur
        
        except Exception as ex:
            print('Error: ', ex)


    def update(self, values = [], conditions = ()):
        try:
            values_str = ', '.join(values)
            query = '''UPDATE {0} SET {1} WHERE {2}'''.format(self.curTable, values_str, conditions)
            cur = self.cursorObj.execute(query)

            return cur
        
        except Exception as ex:
            print('Error: ', ex)
    
    def update_by_id(self, values = [], idValue = 0):
        try:
            values_str = ', '.join(values)
            query = '''UPDATE {0} SET {1} WHERE {2} = {3}'''.format(self.curTable, values_str, self.curPrimaryKey, idValue)
            cur = self.cursorObj.execute(query)

            return cur
        
        except Exception as ex:
            print('Error: ', ex)

    def update_by_model(self, model):
        try:
            columns = []
            values = []
            idValue = -1

            if(inspect.isclass(type(model))):
                

                columns = [ item[0] for item in inspect.getmembers(model) 
                if (item not in dir(type('dummy', (object,), {}))) 
                and not (item[0].startswith('_') or item[0].endswith('_')) 
                and isinstance(getattr(type(model), item[0], None), property) ]

                for col in columns:
                    if(col in self.curAllColumnNames):
                        valAttr = getattr(model, col)
                        
                        if(col == self.curPrimaryKey):
                            idValue = self.util_common.isUUID(valAttr) and '"{0}"'.format(valAttr) or valAttr
                            continue

                        if(type(valAttr) is str):
                            valAttr = '"{0}"'.format(valAttr)
                        
                        if(valAttr is None):
                            valAttr = 'NULL'#(None,)
                        
                        values.append(str(valAttr))
            columns = [item for item in columns if item != self.curPrimaryKey]
            set_values = list(map(lambda a, b: str(a + ' = ' + b), columns, values))
            
            cur = self.update_by_id(set_values, idValue)

            return cur
        
        except Exception as ex:
            print('Error: ', ex)


    def remove_by_id(self, booleanColumn, booleanValue, idValue):
        try:
            query = '''UPDATE {0} SET {1} = {2} WHERE {3} = {4}'''.format(self.curTable, booleanColumn, booleanValue, self.curPrimaryKey, idValue)
            cur = self.cursorObj.execute(query)

            return cur
        
        except Exception as ex:
            print('Error: ', ex)


    def delete(self, values = ()):
        try:
            query = '''DELETE FROM {0} WHERE {1}'''.format(self.curTable, values)
            cur = self.cursorObj.execute(query)

            return cur
        
        except Exception as ex:
            print('Error: ', ex)


    def execute(self, query, param = ()):
        cur = self.cursorObj.execute(query, param)
        self.cursorObj.commit()
        return cur.rowcount
    

    def executemany(self, query, param = ()):
        cur = self.cursorObj.executemany(query, param)
        self.cursorObj.commit()
        return cur.rowcount

    """
    End Region: service method
    """


    """
    Region: private method
    """


    
    """
    End Region: private method
    """