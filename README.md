[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# WichtelLotto
A small CLI to generate wichtel pairs

***If you just want to run the program. Execute 'main_cli.py'.***

***'main_gui.py' is unfinished!*** <sup><sub>But there is a cat picture</sub></sup>

## Python module requirements
You will need to install the following modules:\

[rich](https://github.com/Textualize/rich) - Rich is a Python library for rich text and beautiful formatting in the terminal.\
[tkinter](https://github.com/topics/tkinter-python) - This module is only needed for the 'main_gui.py' part of this project.


## Usage
**Please take a look at 'example.py'. This will make it easier to understand the following code snippets.**

You will need to import these modules:

    from ParticipentManager import *
    from ParticipentPicker import *

---
### participentManager()
This module is used to hold a list of participents (Wichtel), aswell as managing access to this list.

Intiate a instance of the ``participentManager()``:

    pm = ParticipentManager()

You can add participents like this *(Names must be unique!*:

    pm.addParticipent("Adams")

You can get participents by name *(Names must be unique!*:

    p = pm.getParticipentByName("Adams")

Or by ID:

    p = pm.getParticipentById(0)

You can print a participent object by calling 'print()':

    p.print()
This is the expected output:

    ID:0
    Name:Adams
    Was picked:False
    Has wichtel:False

---
### ParticipentPicker()
This module is used to generate a wichtel pair. 

Intiate a instance of the ``ParticipentPicker()``:

    pp = ParticipentPicker()

A random participent is picked like this:

    p = pp.getRandomParticipent()

You can pick a random participent from the perspective of a participent like this.
To use this function, you must initiate a participent object from whose perspective the action is being taken.
This is the main function to generate wichtel pairs:

    currentParticipent = pp.getRandomParticipent()
    wichtelOfParticipent = pp.getRandomParticipentAsParticipent(currentParticipent)

The function makes sure to not pick the current participent as a wichtel.

## Example
This example will generate a participent/wichtel pair from a small list of names:

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

      for partners in listOfAssignments:
            print(partners)

This is a possibility of what the output can look like:

    ('Adams', 'Irwin')
    ('Irwin', 'Adams')
    ('Ghosh', 'Evans')
    ('Davis', 'Hills')
    ('Baker', 'Clark')
    ('Hills', 'Ghosh')
    ('Clark', 'Baker')
    ('Frank', 'Jones')
    ('Jones', 'Davis')
    ('Evans', 'Frank')

## Tests

All modules have a unit test file. These files have 'test' at the beginning of the name.

'test_main.py' tests the main function of this project. Assigning wichtel pairs. This is an example output:

    ('Adams', 'Irwin')
    ('Irwin', 'Adams')
    ('Ghosh', 'Evans')
    ('Davis', 'Hills')
    ('Baker', 'Clark')
    ('Hills', 'Ghosh')
    ('Clark', 'Baker')
    ('Frank', 'Jones')
    ('Jones', 'Davis')
    ('Evans', 'Frank')
