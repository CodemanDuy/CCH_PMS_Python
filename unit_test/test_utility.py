import unittest
import sys, os


ROOT_DIR = os.getcwd()  # Get root directory
sys.path.append(os.path.dirname(ROOT_DIR + r'/'))# Add absolute path to current sys.path
# print('Path: ' + str(sys.path))

from coreutil.util_common import Core_UtilityCommon
from coreutil.util_security import Core_UtilitySecurity

class UtilityTestCase(unittest.TestCase):

    UtilCommon = Core_UtilityCommon()
    UtilSecure = Core_UtilitySecurity()

    def test_security__generatePasswordByBcrypt(self):
        
        hashedDict = UtilityTestCase.UtilSecure.generatePasswordByBcrypt('123a#$', 6)
        print(hashedDict)
        
        self.assertIsNotNone(hashedDict, '###Error Message: No data')



###########################################################################################################
"""
doc: Code will begin from here
"""
if __name__ == '__main__':

    unittest.main()
