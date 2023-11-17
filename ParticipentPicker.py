from Participent import *
from ParticipentManager import *
import random

class ParticipentPicker:
    __pm = ParticipentManager()

    def getRandomParticipent(self):   
        if (not self.__pm.getParticipentList()):
            return self.__pm.getEmptyParticipent()

        maxId = self.__pm.getNumOfParticipent()
        p = self.__pm.getParticipentById(random.randrange(maxId))
        return p
    
    def getRandomParticipentAsParticipent(self, currentParticipent):
        # Brute force fitting wichtel
        while True:
            p = p = self.getRandomParticipent()

            if (p == currentParticipent):
                continue

            if (p.getWasPicked() == True):
                continue

            break

        currentParticipent.hasWichtel = True 
        p.wasPicked = True
        return p
    
    def getRandomParticipentAsFailureTest(self, currentParticipent):
        while True:
            p = p = self.getRandomParticipent()

            if (p.getWasPicked() == True):
                continue

            break

        currentParticipent.hasWichtel = True 
        p.wasPicked = True
        return p
    