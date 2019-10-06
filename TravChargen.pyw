#
# Traveller Character Generator v 0.1
# 10/6/2019
# By Dirk T. Collins  collins.dirk@gmail.com
# Classic Traveller Generator Built in Python
#
import random
from tkinter import *
# defining the donothing window
def donothing():
    filewin = Toplevel(top)
    button = Button(filewin, text="Do nothing button")
    button.pack()
#Creating the root window
top = Tk()
#configuring the main window
top.title("Traveller Character Generator")
top.geometry("800x600")
#mainmenu
menubar = Menu(top)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command = donothing)
filemenu.add_command(label="Open", command = donothing)
filemenu.add_command(label="Save", command = donothing)
filemenu.add_command(label="Save as...", command = donothing)
filemenu.add_command(label="Close", command = top.quit)

top.config(menu = menubar)

#Starting the main program
top.mainloop()



#Chargen
charname = input("What is your Characters Name?")
print(charname)
print("Hi,", charname)
die1 = random.randint(1,6)
die2 = random.randrange(6) + 1
strength = die1 + die2
print("Strength = ", strength)
die1 = random.randint(1,6)
die2 = random.randrange(6) + 1
dexterity = die1 + die2
print("Dexterity = ", dexterity)
die1 = random.randint(1,6)
die2 = random.randrange(6) + 1
endurance = die1 + die2
print("Endurance = ", endurance)
die1 = random.randint(1,6)
die2 = random.randrange(6) + 1
intelligence = die1 + die2
print("Intelligence = ", intelligence)
die1 = random.randint(1,6)
die2 = random.randrange(6) + 1
education = die1 + die2
die1 = random.randint(1,6)
die2 = random.randrange(6) + 1
print("Education = ", education)
die1 = random.randint(1,6)
die2 = random.randrange(6) + 1
social = die1 + die2
print("Social Standing = ", social)
charclass = input("What Character Class Would you like to be?")
print (charclass)
input("\n\nYou can press the Enter key to exit this app.")
      
      

