import unittest
from ParticipentManager import *

pm = ParticipentManager()

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

class TestParticipentManager(unittest.TestCase):
    def test_getEmptyParticipent(self):
        p = pm.getEmptyParticipent()

        self.assertEqual(p.getId(), -1)
        self.assertEqual(p.getName(), "Error")

    def test_existing_id(self):
        p = pm.getParticipentById(0)

        self.assertEqual(p.getId(), 0)
        self.assertEqual(p.getName(), "Adams")

    def test_existing_name(self):
        p = pm.getParticipentById(1)

        self.assertEqual(p.getId(), 1)
        self.assertEqual(p.getName(), "Baker")

    def test_non_existing_id(self):
        p = pm.getParticipentById(999999)

        self.assertEqual(p.getId(), -1)
        self.assertEqual(p.getName(), "Error")

    def test_non_existing_name(self):
        p = pm.getParticipentByName("John Doe der Droelfte")
        
        self.assertEqual(p.getId(), -1)
        self.assertEqual(p.getName(), "Error")

if __name__ == '__main__':
    unittest.main()