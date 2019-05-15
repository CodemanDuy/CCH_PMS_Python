import unittest
import sys, os


ROOT_DIR = os.getcwd()  # Get root directory
sys.path.append(os.path.dirname(ROOT_DIR + r'/'))# Add absolute path to current sys.path
# print('Path: ' + str(sys.path))

from datacontext.sqlite_dbcontext import Database
from datacontext.entities_container import EntitiesContainer
from config import Configuration


class EntityTestCase(unittest.TestCase):
    
    Config = Configuration()
    Entity = EntitiesContainer()

    def test_entitycontainer_size(self):
        
        ENTITY_DIR = ROOT_DIR + r'/datacontext/entities/'
        entityfiles = [name for name in os.listdir(ENTITY_DIR) if os.path.isfile(os.path.join(ENTITY_DIR, name)) and not name.startswith('__') and name.endswith('.py') ]
        default_size = len(entityfiles)

        entityregistered = EntityTestCase.Entity.get_allEntityClassRegistered()
        actual_size = len(entityregistered)

        self.assertEqual(default_size, actual_size, '###Error Message: Incorrect default size. Missing some entity class')


    def test_entitycontainer_registername(self):
        
        ENTITY_DIR = ROOT_DIR + r'/datacontext/entities/'
        entityfiles = [name for name in os.listdir(ENTITY_DIR) if os.path.isfile(os.path.join(ENTITY_DIR, name)) and not name.startswith('__') and name.endswith('.py') ]
        
        entityregistered = [str(name) for name, obj in EntityTestCase.Entity.get_allEntityClassRegistered()]

        for filename in entityfiles:
            self.assertFalse(filename.replace(".py", "") not in entityregistered, '###Error Message: Missing entity registerd class in EntityContainer: ' + filename)



###########################################################################################################
"""
doc: Code will begin from here
"""
if __name__ == '__main__':

    unittest.main()

