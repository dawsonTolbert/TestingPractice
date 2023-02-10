import unittest
from scoringDemo import ScoreMachine

class TestAce(unittest.TestCase):
    
    def setUp(self):
        self.machine = ScoreMachine()

    def test_zero(self):
        self.assertEqual(self.machine.aces([6,2,3,4,5]), 0, "Should be 0")
    
    def test_one(self):
        self.assertEqual(self.machine.aces([1,2,3,4,5]), 1, "Should be 1")
        self.assertEqual(self.machine.aces([2,3,4,5,1]), 1, "Should be 1")
    
    def test_two(self):
        self.assertEqual(self.machine.aces([1,2,1,4,5]), 2, "Should be 2")

class TestTwo(unittest.TestCase):
    
    def setUp(self):
        self.machine = ScoreMachine()

    def test_zero(self):
        self.assertEqual(self.machine.twos([6,1,3,4,5]), 0, "Should be 0")
    
    def test_one(self):
        self.assertEqual(self.machine.twos([1,2,3,4,5]), 2, "Should be 2")
        self.assertEqual(self.machine.twos([2,3,4,5,1]), 2, "Should be 2")
    
    def test_two(self):
        self.assertEqual(self.machine.twos([1,2,2,4,5]), 4, "Should be 4")
        
class TestThree(unittest.TestCase):
    
    def setUp(self):
        self.machine = ScoreMachine()

    def test_zero(self):
        self.assertEqual(self.machine.threes([6,1,2,4,5]), 0, "Should be 0")
    
    def test_one(self):
        self.assertEqual(self.machine.threes([1,2,3,4,5]), 3, "Should be 3")
        self.assertEqual(self.machine.threes([2,3,4,5,1]), 3, "Should be 3")
    
    def test_two(self):
        self.assertEqual(self.machine.threes([1,3,3,4,5]), 6, "Should be 6")
        
class TestFour(unittest.TestCase):
    
    def setUp(self):
        self.machine = ScoreMachine()

    def test_zero(self):
        self.assertEqual(self.machine.fours([6,1,3,2,5]), 0, "Should be 0")
    
    def test_one(self):
        self.assertEqual(self.machine.fours([1,2,3,4,5]), 4, "Should be 4")
        self.assertEqual(self.machine.fours([2,3,4,5,1]), 4, "Should be 4")
    
    def test_two(self):
        self.assertEqual(self.machine.fours([1,2,4,4,5]), 8, "Should be 8")
        
class TestFive(unittest.TestCase):
    
    def setUp(self):
        self.machine = ScoreMachine()

    def test_zero(self):
        self.assertEqual(self.machine.fives([6,1,3,4,2]), 0, "Should be 0")
    
    def test_one(self):
        self.assertEqual(self.machine.fives([1,2,3,4,5]), 5, "Should be 5")
        self.assertEqual(self.machine.fives([2,3,4,5,1]), 5, "Should be 5")
    
    def test_two(self):
        self.assertEqual(self.machine.fives([1,2,5,4,5]), 10, "Should be 10")
        
class TestSix(unittest.TestCase):
    
    def setUp(self):
        self.machine = ScoreMachine()

    def test_zero(self):
        self.assertEqual(self.machine.sixes([2,1,3,4,5]), 0, "Should be 0")
    
    def test_one(self):
        self.assertEqual(self.machine.sixes([1,6,3,4,5]), 6, "Should be 6")
        self.assertEqual(self.machine.sixes([2,6,4,5,1]), 6, "Should be 6")
    
    def test_two(self):
        self.assertEqual(self.machine.sixes([1,6,6,4,5]), 12, "Should be 12")

if __name__ == '__main__':
    unittest.main()
