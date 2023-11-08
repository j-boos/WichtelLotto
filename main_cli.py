from ParticipentManager import *
from ParticipentPicker import *

import sys
from rich.console import Console
import time

pm = ParticipentManager()
pp = ParticipentPicker()

c = Console()

def helper_IsBooleanAnswer(answer):
    if ((len(answer) > 1) or (len(answer) <= 0)):
        return False
    
    if (('y' != answer) and ('n' != answer)):
        return False
    
    return True

def dialog_questionBool():
    c.print('y/n?')
    answer = input()
    
    while (not helper_IsBooleanAnswer(answer)):
        dialog_clearLine(2)
        c.print('y/n?')
        answer = input()

    return True if 'y' in answer else False

def dialog_clearLine(linesToClear):
    for _ in range(linesToClear):
        sys.stdout.write("\033[F") # Cursor up one line
        sys.stdout.write("\033[K") # Clear to the end of line

def dialog_clear():
    dialog_clearLine(255)
    dialog_header()

def dialog_header():
    c.print("Wichtel Lotto - J.Boos\n", style="underline")

def dialog_getParticipentName():
    c.print(f"Name of participent {len(pm.getParticipentList())}:")
    participentName = input()
    dialog_clear()
    c.print(f"Add {participentName}?")
    if (not dialog_questionBool()):
        return

    pm.addParticipent(participentName)

def dialog_questionMoreParticipent():
    dialog_clear()
    c.print(f"Add another participent?")
    return dialog_questionBool()

def dialog_questionReadyToPlay():
    c.print(f"Ready to play?")
    return dialog_questionBool()

def dialog_getParticipentsAWichtel():
    while(True):
        currentParticipent = pm.getEmptyParticipent()
        while (True):
            currentParticipent = pp.getRandomParticipent()
            if (not currentParticipent.getHasWichtel()):
                break

        c.print(f"{currentParticipent.getName()} are you ready to receive your wichtel?")
        while (not dialog_questionBool()):
            dialog_clearLine(2)
            continue

        dialog_clearLine(2)
        participentsWichtel = pp.getRandomParticipentAsParticipent(currentParticipent)
        c.print(f"You received {participentsWichtel.getName()} as your wichtel!")
        input()
        dialog_clearLine(3)

        everyoneHasWichtel = pm.everyoneHasWichtel()
        if (everyoneHasWichtel):
            break

def dialog():
    # get participent
    dialog_clear()
    dialog_getParticipentName()
    while (dialog_questionMoreParticipent()):
      dialog_clear()
      dialog_getParticipentName()

    # everyone ready?
    dialog_clear()
    while (not dialog_questionReadyToPlay()):
      dialog_clear()

    # choose wichtel 
    dialog_clear()
    dialog_getParticipentsAWichtel()

def main():
    dialog()

if __name__ == "__main__":
    main()