__author__ = 'gk'

# Implements look up Table for user to ID and ID to user, as the end Result class for storing user rank and score

class ScreenNameIndex:
    nameToIdMap = dict()
    idToNameMap = dict()

    def __init__(self,screen_names):
        super().__init__()
        id = 0
        for item in screen_names:
            self.nameToIdMap[item] = id
            self.idToNameMap[id] = item
            id+=1

    def __str__(self, *args, **kwargs):
        desc = ""
        for key,value in self.nameToIdMap.items():
            desc = desc + " Key: " + key + " Value: " + repr(value) + "\n"
        return desc


class UserRank:
    name = ""
    score = 0

    def __init__(self,name,score):
        super().__init__()
        self.name = name
        self.score = score

    def __str__(self, *args, **kwargs):
        desc = "Name: " + self.name  + " Score: " + repr(format(self.score,".10f"))
        return desc

    def buildUserRankList(screenNameIndex,xMatrix):
        userRankList = list()
        for i,j,v in zip(xMatrix.row,xMatrix.col,xMatrix.data):
            userRankList.append(UserRank(screenNameIndex.idToNameMap[j],v))
        userRankList.sort(key=lambda x: x.score, reverse=True)
        return userRankList







