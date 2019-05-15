import bcrypt

class Core_UtilitySecurity():

    def __init__(self):
        pass

    def generatePasswordByBcrypt(self, pwdPlainText, saltKeySize = 6):
        # gensalt default size is 12        
        saltKey = bcrypt.gensalt(saltKeySize)
        # hash a password for the first time, with a randomly-generated salt
        hashed = bcrypt.hashpw(pwdPlainText.encode('utf-8'), saltKey)

        return hashed.decode()


    def verifyHashed(self, pwdPlainText, pwdHashed):
        if(not pwdPlainText or not pwdHashed):
            return False
        matched = bcrypt.checkpw(pwdPlainText.encode('utf-8'), pwdHashed.strip('\'').encode())
        return matched
        
