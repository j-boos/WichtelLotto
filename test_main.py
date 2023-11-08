import unittest

from ParticipentManager import *
from ParticipentPicker import *

listOfAssignments = []

pm = ParticipentManager()
pp = ParticipentPicker()

pm.addParticipent("Adams")
pm.addParticipent("Baker")
pm.addParticipent("Clark")
pm.addParticipent("Davis")
pm.addParticipent("Evans")
pm.addParticipent("Frank")
pm.addParticipent("Ghosh")
pm.addParticipent("Hills")
pm.addParticipent("Irwin")
pm.addParticipent("Jones")

def assignParticipents():
    while(True):
        currentParticipent = pm.getEmptyParticipent()
        while (True):
            currentParticipent = pp.getRandomParticipent()
            if (not currentParticipent.getHasWichtel()):
                break

        participentsWichtel = pp.getRandomParticipentAsParticipent(currentParticipent)

        assignment = (currentParticipent.getName(), participentsWichtel.getName())
        listOfAssignments.append(assignment)

        everyoneHasWichtel = pm.everyoneHasWichtel()
        if (everyoneHasWichtel):
            break

class TestParticipentPicker(unittest.TestCase):
    def test_noInvalidAssignments(self):
        assignParticipents()

        for partners in listOfAssignments:
            print(partners)
            self.assertNotEqual(partners[0], partners[1])
        
if __name__ == '__main__':
    unittest.main()