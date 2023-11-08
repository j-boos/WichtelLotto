from ParticipentManager import *
from ParticipentPicker import *

def main():
    pm = ParticipentManager()
    pp = ParticipentPicker()

    # Add as many participents as you like:
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

    # Get participents by name:
    print("pm.getParticipentByName(\"Adams\"):")
    p0 = pm.getParticipentByName("Adams")
    p0.print()

    # Get participents by ID:
    print("pm.getParticipentById(0):")
    p1 = pm.getParticipentById(0)
    p1.print()

    # Get random participent:
    print("pp.getRandomParticipent():")
    p2 = pp.getRandomParticipent()
    p2.print()

    # Get random participent, but not current participent:
    print("pp.getRandomParticipentAsParticipent(p2):")
    p3 = pp.getRandomParticipentAsParticipent(p2)
    p3.print()

if __name__ == "__main__":
    main()