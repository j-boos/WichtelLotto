from ParticipentManager import *
from ParticipentPicker import *

from rich.console import Console

c = Console()

numOfFailures = 0
numOfNames = 0
listOfNames = []

def test_failure_rate():
    global listOfNames
    global numOfNames

    pm = ParticipentManager()
    pp = ParticipentPicker()

    for x in range(numOfNames):
        pm.addParticipent(listOfNames[x])

    while (True):
        everyoneHasWichtel = pm.everyoneHasWichtel()
        if (everyoneHasWichtel):
            break

        currentParticipent = pp.getRandomParticipent()
        if (currentParticipent.getHasWichtel()):
            continue

        participentsWichtel = pp.getRandomParticipentAsFailureTest(currentParticipent)

        if (currentParticipent.getName() == participentsWichtel.getName()):
            pm.clearParticipentList()
            return False
        
    pm.clearParticipentList()
    return True
    
def main():
    global numOfFailures
    global listOfNames
    global numOfNames

    numOfNames = int(input("How many participents?"))

    with open("first-names.txt") as file:
        listOfNames = file.read().splitlines()

    iterations = int(input("How many iterations?"))
    for x in range(iterations):
        print(x)
        if test_failure_rate():
            continue

        numOfFailures += 1

    print(f"{numOfFailures} or {round((numOfFailures / iterations) * 100, 4)} % of {iterations} iterations with {numOfNames} participents ended with a self pick!")

if __name__ == "__main__":
    main()