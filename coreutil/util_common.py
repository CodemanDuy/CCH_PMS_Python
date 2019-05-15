import random
import string
import datetime
import uuid

class Core_UtilityCommon():

    def __init__(self):
        pass

    def parseListToString(self, listItem = []):
        string = '", "'.join(str(x) for x in listItem)
        string = '"{0}"'.format(string)
        return string
            
    def randomString(self, stringLength = 10):
        """Generate a random string of fixed length """
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(stringLength))

    def currentDateTime(self):
        return datetime.datetime.now()

    import uuid

    def generateUUID(self):
        return uuid.uuid4()

    def isUUID(self, val):
        try:
            uuid.UUID(str(val))
            return True
        except ValueError:
            return False