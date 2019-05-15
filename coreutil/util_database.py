# import inspect

class Core_UtilityDatabase():

    def __init__(self):
        pass

    def getModelAttributeNames(self, className):
        return [a for a, v in className.__dict__.items() if not (a.startswith('__') and a.endswith('__'))]
        # return([item[0] for item in inspect.getmembers(className) if item[0] not in dir(type('dummy', (object,), {}))])


    