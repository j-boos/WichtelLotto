from ParticipentManager import *
from ParticipentPicker import *

import tkinter as tk

def main():
    pm = ParticipentManager()
    pp = ParticipentPicker()

    root = tk.Tk()

    root.title('Wichtel Lotto')
    root.geometry("1280x720")
    root.resizable(False, False)

    background_image = tk.PhotoImage(file='./titleIcon.png')
    root.wm_iconphoto(False, background_image)

    background_image = tk.PhotoImage(file='./cat.png')
    background_label = tk.Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    listbox = tk.Listbox(
        root,
        width=24,
        height=6,
    )
    listbox.pack()

    entry_list = []

    def addParticipentToInterface():
        for entry in entry_list:
            listbox.insert(tk.END, entry.get())
            entry.set('')
        listbox.pack()
        
    label = tk.Label(root, text="Wie ist dein Name?")
    label.pack()
    entry_var = tk.StringVar()
    entry = tk.Entry(
        root, textvariable = entry_var
    )
    entry_list.append(entry_var)
    pm.addParticipent(entry_var)
    entry.pack()
    
    button = tk.Button(root, text = 'Ich spiele mit!', command = addParticipentToInterface)
    button.pack()

    currentParticipent = tk.StringVar()
    currentParticipent = pm.getParticipentById(0).getName()

    def play():
        label = tk.Label(root, text=f"{currentParticipent} zieht!")
        label.pack()

    button = tk.Button(root, text = 'Spielen!', command = play)
    button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()