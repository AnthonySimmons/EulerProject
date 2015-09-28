class ErrorLogger(object):
    """description of class"""
    _filepath = ''
    _errors = []

    def __init__(self, filepath):
        self._filepath = filepath

    def Save(self):
        file = open(self._filepath, 'w')
        file.writelines(_errors)

    def AddError(self, error):
        self._errors.append(error)

