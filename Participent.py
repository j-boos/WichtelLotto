class Participent:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.wasPicked = False
        self.hasWichtel = False

    def getId(self):
        return self.id
        
    def getName(self):
        return self.name
    
    def getWasPicked(self):
        return self.wasPicked
    
    def getHasWichtel(self):
        return self.hasWichtel
    
    def print(self):
        print(f"ID:{self.getId()}")
        print(f"Name:{self.getName()}")
        print(f"Was picked:{self.getWasPicked()}")
        print(f"Has wichtel:{'True' if self.getHasWichtel() else 'False'}")
        print('\n')
