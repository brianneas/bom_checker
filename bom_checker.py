import pandas as pd

# Create class for each part.
class Part:
    def __init__(self, partNumber):
        self.partNumber = partNumber

    def addAttributes(attributeList):
        pass

class CheckType:
    def __init__(self, checkName, checkList):
        self.checkName = checkName
        self.checkList = checkList


checkTypes = pd.read_csv('check_types.csv')
listOfChecks = { }

for check in checkTypes:
    listOfChecks[check] = CheckType(check, checkTypes[check].tolist())


