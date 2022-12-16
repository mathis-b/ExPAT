#!/usr/bin/env python3
# coding: utf-8

'''
Created on 7 juin 2021

@author: Alexandre
'''


import shutil
import os
import tkinter
from tkinter import messagebox

parent = tkinter.Tk() # Create the object
parent.overrideredirect(1) # Avoid it appearing and then disappearing quickly
#parent.iconbitmap(Drive_directory + "/PythonIcon.ico") # Set an icon (this is optional - must be in a .ico format)
parent.withdraw() # Hide the window as we do not want to see this one

yesno = messagebox.askyesno('Question', 'Are you boring?', parent=parent) # Yes / No
yesno.geometry("1000x500")
if yesno == True:
    print("Warning","Keep it cool rasta!!!")

yesno = messagebox.askyesno('Question', 'Are you boring?', parent=parent) # Yes / No
if yesno == True:
    messagebox.showwarning("Warning","Keep it cool rasta!!!")
else:
    messagebox.showwarning('Réponse', "Do a thesis and you will!!!")




import tkinter as tk
def submitFunction() :
    print('Submit button is clicked.')

class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.creer_widgets()

    def creer_widgets(self):
        self.label = tk.Label(self, text = "J'adore Python!")
        self.bouton1 = tk.Button(self, text = "Quitter", command = self.destroy) #self.destroy or self.quit
        self.bouton2 = tk.Button(self, text = "Submit", command = submitFunction) 
        self.label.pack()
        self.bouton1.pack()
        self.bouton2.pack()

if __name__ == "__main__":
    app = Application()
    app.geometry("1000x500")
    app.title(" Ma Première App : -)")
    app.mainloop()




button_submit = tkinter.Button(window_main, text ="Submit", command=submitFunction)
button_submit.config(width=20, height=2)


racine = tk.Tk()
label = tk.Label( racine , text ="J'adore Python!")
bouton = tk.Button ( racine , text ="Quitter", command = racine.quit )
bouton ["fg"] = "red"
label.pack ()
bouton.pack ()
racine.mainloop ()
print ("C'est fini!")