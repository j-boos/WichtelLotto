from Participent import *

class ParticipentManager:
    __participentList = []

    def addParticipent(self, name):   
        p = Participent(0 if not self.__participentList else self.__participentList[-1].getId() + 1, name)
        self.__participentList.append(p) 

    def everyoneHasWichtel(self):
        for p in self.getParticipentList():
            if (not p.getHasWichtel()):
                return False
            
        return True

    def getEmptyParticipent(self):   
        return Participent(-1, "Error")
    
    def getParticipentById(self, id):
        if (id >= len(self.__participentList)):
            return self.getEmptyParticipent()

        return self.__participentList[id]
    
    def getParticipentByName(self, name):
        for p in self.__participentList:
            if (p.getName() != name):
                continue

            return p
        
        return self.getEmptyParticipent()
    
    def getParticipentList(self):
        return self.__participentList
    
    def getNumOfParticipent(self):
        return len(self.__participentList)


    