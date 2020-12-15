import unittest
from Game import FinalGame as FG


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(FG.Game, FG.Game)


if __name__ == '__main__':
    unittest.main()
