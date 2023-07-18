def getLowestCommonManager(topManager, reportOne, reportTwo):
    # Write your code here.
    managers = {"A": (None, 0)}
    if reportOne.name == "A":
        return reportOne
    if reportTwo.name == "A":
        return reportTwo
    def getManager(node, lvl = 1):
        if node.directReports:
            for directReport in node.directReports:
                managers[directReport.name] = (node, lvl)
                getManager(directReport, lvl + 1)
    getManager(topManager)
    managerOne, lvlOne = managers[reportOne.name]
    managerTwo, lvlTwo = managers[reportTwo.name]


    if lvlOne > lvlTwo:
        lvlOne, lvlTwo = lvlTwo, lvlOne
        reportOne, reportTwo = reportTwo, reportOne
    for i in range(lvlOne, lvlTwo):
        reportTwo, lvlTwo = managers[reportTwo.name]
    if reportOne.name == reportTwo.name:
        return reportOne
    while managers[reportOne.name] != managers[reportTwo.name]:
        if reportOne.name == reportTwo.name:
            return reportOne
        if reportOne.name == "A":
            return reportOne
        if reportTwo.name == "A":
            return reportTwo
        reportOne, lvlOne = managers[reportOne.name]
        reportTwo, lvlTwo = managers[reportTwo.name]
    return managers[reportOne.name][0]


# This is an input class. Do not edit.
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []

