class ScoreMachine:
    def __init__(self):
        pass
    
    def aces(self,rolls):
        total = 0
        for item in rolls:
            if item == 1:
                total += item
        return total
    
    def twos(self,rolls):
        total = 0
        for item in rolls:
            if item == 2:
                total += item
        return total
    
    def threes(self,rolls):
        total = 0
        for item in rolls:
            if item == 3:
                total += item
        return total
    
    def fours(self,rolls):
        total = 0
        for item in rolls:
            if item == 4:
                total += item
        return total
    
    def fives(self,rolls):
        total = 0
        for item in rolls:
            if item == 5:
                total += item
        return total
    
    def sixes(self,rolls):
        total = 0
        for item in rolls:
            if item == 6:
                total += item
        return total
    
def testAces():
    x = ScoreMachine()
    assert 5 == x.aces([1,1,1,1,1])
    assert 4 == x.aces([1,1,1,1])
    
    print("Aces tests passed!")
    
