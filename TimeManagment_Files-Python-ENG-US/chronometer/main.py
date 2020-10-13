# Coding using UTF-8

# Imports all necessary libraries
from tkinter import *
from time import sleep
from bibliotecas.add import add
from bibliotecas.iniciar import program
import os

a = s = 0
active, r, reset = True, False, []

def resource_path(relative_path):
    # Get the absolute path to the resource, works for dev and PyInstaller
    try:
        # PyInstaller creates a temporary folder and stores the path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def splash_screen():
    spl = Tk() # Creates the window
    spl.geometry('500x300+420+220') # Defines window geometry
    spl.overrideredirect(True) # Removes the edges of the window (minimize, close, maximize, etc.), displaying only the content contained within it, as a splash screen
    spl.config(bg = '#000000') # Sets the background color of the window
    spl.iconbitmap(resource_path('C:\\Users\\Paulo Thiago\\Documents\\Meus Projetos\\TimeManagment_Files-Python-ENG-US\\chronometer\\media\\icons\\icons\\main.ico')) # Specify the exact location of the main.ico file EX .: 'C:\\Users\\Usuario1\\project\\timer\\media\\icons\\icons\\main.ico'

    # Abrindo as imagens
    ani1 = PhotoImage(file = 'C:\\Users\\Paulo Thiago\\Documents\\Meus Projetos\\TimeManagment_Files-Python-ENG-US\\chronometer\\media\\animations\\before\\watch\\tmp-0.gif') # Specify the exact location of the file tmp-0.gif EX.: 'C:\\Users\\Usuario1\\project\\chronometer\\media\\icons\\icons\\tmp-0.gif'
    tit = PhotoImage(file = 'C:\\Users\\Paulo Thiago\\Documents\\Meus Projetos\\TimeManagment_Files-Python-ENG-US\\chronometer\\media\\animations\\before\\title\\tmpt-0.gif') # Specify the exact location of the file tmpt-0.gif EX.: 'C:\\Users\\Usuario1\\project\\chronometer\\media\\icons\\icons\\tmpt-0.gif'
    
    # Resize images
    ani1 = ani1.subsample(6, 6)
    tit = tit.subsample(5, 5)

    def title():
        global tit;global c1;global c # Defines the variables tit, c1 and c as global
        for c1 in range(2):
            for c in range(2):
                tit = PhotoImage(file = f'C:\\Users\\Paulo Thiago\\Documents\\Meus Projetos\\TimeManagment_Files-Python-ENG-US\\chronometer\\media\\animations\\before\\title\\tmpt-{c}.gif') # Specify the exact location of the file tmpt-{c}.gif EX.: 'C:\\Users\\Usuario1\\project\\chronometer\\media\\icons\\icons\\tmpt-{c}.gif'
                tit = tit.subsample(5, 5)
                t.config(image = tit)
                sleep(.3) # Wait 0.3 seconds
                spl.update() # Update window

    def watch():
        global ani1;global c # Defines the variables ani1 and c as being global
        for c in range(119):
            # If a splash screen is being displayed for the first time it will wait 0.1 seconds to start running the animation
            if c == 1:
                sleep(.1)
            ani1 = PhotoImage(file = f'C:\\Users\\Paulo Thiago\\Documents\\Meus Projetos\\TimeManagment_Files-Python-ENG-US\\chronometer\\media\\animations\\before\\watch\\tmp-{c}.gif') # Specify the exact location of the file tmpt-{c}.gif EX.: 'C:\\Users\\Usuario1\\project\\chronometer\\media\\icons\\icons\\tmp-{c}.gif'
            ani1 = ani1.subsample(6, 6)
            a1.config(image = ani1)
            sleep(.001)
            spl.update()

    # Create the Labels with the images
    t = Label(spl, image = tit, bg = '#000000')
    t.pack(side = BOTTOM)
    a1 = Label(spl, image = ani1, bg = '#000000')
    a1.pack()

    watch() # Calls the function that animates the clock image
    title() # Calls the function that animates the title image
    spl.after(2500, spl.destroy) # Wait 2.5 seconds, then close the splash screen
    spl.mainloop() # Loop the window

def start():
    window = Tk()
    window.title('Time managment')
    window.geometry('550x200+547+243')
    window.iconbitmap('C:\\Users\\Paulo Thiago\\Documents\\Meus Projetos\\TimeManagment_Files-Python-ENG-US\\chronometer\\media\\icons\\icons\\main_window.ico') # Sets the window icon
    window.config (bg = '#000000')
    window.minsize(500, 150) # Defines a minimum size for the window, the user will not be able to resize lessque isso

    program(window, a, s, active, reset, r) # Calls the program () function, which contains the program's features

    window.mainloop()

splash_screen() # Calls the splash_screen() function, causing the splash screen to be displayed
start() # Calls the start() function, causing the main window to be created
