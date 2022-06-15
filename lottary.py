'''
Program:lottery.py 
Author: Alexa Ingria 6/14/22

GUI-based app to simulate the mega millions lottery number picks. Five random numbers between 1 and 70 and a "Mega Ball" between 1-25



'''

from breezypythongui import EasyFrame
from tkinter.font import Font
import random
# other imports

class Lottery(EasyFrame):
	#"ApplicationName" will change from project to project

	#definition of the __init__() method whitch is our class constructor
	def __init__(self):
		#call the EasyFrame version of __init__
		EasyFrame.__init__(self, title = "Mega Millions Draw", background = "Limegreen")
		bigFont = Font(family = "Verdana", size = 32, weight = "bold")
		self.addLabel(text = "Mega Millions", row = 0, colunm = 0, colunmspan = 5, sticky = "NSEW", background = "limegreen", foreground = "lemonchiffon", font = bigFont)
		self.addLabel(text = "Winning Number", row = 1, colunm = 0, background = "limegreen", foreground = "white")
		self.field1 = self.addIntegerField( value = 0, row = 2, colunm = 0, state = "readonly")
		self.field2 = self.addIntegerField( value = 0, row = 2, colunm = 1, state = "readonly")
		self.field3 = self.addIntegerField( value = 0, row = 2, colunm = 2, state = "readonly")
		self.field4 = self.addIntegerField( value = 0, row = 2, colunm = 3, state = "readonly")
		self.field5 = self.addIntegerField( value = 0, row = 2, colunm = 4, state = "readonly")
		self.addLabel( text = "Mega Ball", row = 3, colunm = 0, colunmspan = 5, sticky = "NSEW", background = "limegreen", foreground = "yellow")
		self.megaField = self.addIntegerField(value = 0, row = 4, colunm = 0, colunmspan = 5, sticky = "NSEW")
		self.megaField["background"] = "lemonchiffon"
		self.addButton(text = "Draw Numbers", row = 5, colunm = 0 , colunmspan = 5, command = self.drawNumbers)
	# Event handling mehtod fo the button
	def drawNumbers(self): 
		num1 = random.randit(1, 70)
		num2 = random.randit(1, 70)
		num3 = random.randit(1, 70)
		num4 = random.randit(1, 70)
		num5 = random.randit(1, 70)
		mega = random.randit(1, 70)

		self.feild1.setNumber(num1)
		self.feild2.setNumber(num2)
		self.feild3.setNumber(num3)
		self.feild4.setNumber(num4)
		self.feild5.setNumber(num5)
		self.megaField.setNumber(mega)



# definition of the main() method which will establish class odject
def main():
	#instantiate an object from the class into mainloop()
	Lottery().mainloop()

#global call to the main() method
main()

