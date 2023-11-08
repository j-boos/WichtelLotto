import unittest

from Participent import *

p = Participent(0, "Adams")

class TestParticipent(unittest.TestCase):
    def test_participent(self):
        self.assertEqual(p.getId(), 0)
        self.assertEqual(p.getName(), "Adams")

if __name__ == '__main__':
    unittest.main()