import unittest

from ParticipentManager import *
from ParticipentPicker import *

pm = ParticipentManager()
pp = ParticipentPicker()

pm.addParticipent("Jannes")
pm.addParticipent("Bibi")
pm.addParticipent("Ole")

class TestParticipentPicker(unittest.TestCase):
    def test_getRandomParticipent(self):
        for _ in range(999):
            p = pp.getRandomParticipent()
            self.assertNotEqual(p.getId(), -1)
            self.assertNotEqual(p.getName(), "Error")

    def test_getRandomParticipentAsParticipent(self):
        p0 = pp.getRandomParticipent()
        for _ in range(999):
            p1 = pp.getRandomParticipentAsParticipent(p0)
            self.assertNotEqual(p0, p1)

if __name__ == '__main__':
    unittest.main()