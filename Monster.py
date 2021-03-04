import turtle
from turtle import *
import math
from random import choice

monsters = {}
monsterName = []

aiMonster = []
humanMonster = []
humanKarteText = []
aiKarteText = []
humanPunkte = 0
aiPunkte = 0
result = False

zahlHumanTurtle = []
zahlAiTurtle = []

screen = Screen()
screen.addshape('VK.gif')




# Datenbank initialisieren

file = open ('Monsters.txt', 'r')

for line in file.read().splitlines():
	name, groesse, inititaive, staerke, image = line.split (', ')
	monsters[name] = [groesse, inititaive, staerke, image, name]
	monsterName.append(name)
	screen.addshape(image)
file.close()

# Spiel starten

# Fragen, welche Kategorie wird verglichen
"""
eingabe = input("Wähle eine Eigenschaft(Größe, Initiative, Stärke): ")
if eingabe == "Größe":
	result = humanMonster[0] > aiMonster[0]
	print(humanMonster[0])
	print(aiMonster[0])
	print(result)

if eingabe == "Initiative":
	result = humanMonster[1] > aiMonster[1]
	print(humanMonster[1])
	print(aiMonster[1])
	print(result)
	
if eingabe == "Stärke":
	result = humanMonster[2] > aiMonster[2]
	print(humanMonster[2])
	print(aiMonster[2])
	print(result)

if result == True:
	humanPunkte = humanPunkte + 1
	print("HumanMonster hat gewonnen!^^~")
else:
	aiPunkte = aiPunkte +1
	print("AiMonster hat gewonnen! :<")
print("Menschlicher Verstand: " + str(humanPunkte) + " VS Kümmerliche Technik: " + str(aiPunkte))

"""


# Hauptscreen

screen.setup(800, 600)
screen.bgcolor('white')



# Kasten Punkte Links

humanTurtle = turtle.Turtle()
humanTurtle.speed(0)
humanTurtle.hideturtle()
humanTurtle.penup()
humanTurtle.goto(-400,300)
humanTurtle.pendown()
for i in range(1,4):
	humanTurtle.forward(100)
	humanTurtle.right(90)
	
	
# Kasten Punkte Rechts
	
aiTurtle = turtle.Turtle()
aiTurtle.speed(0)
aiTurtle.hideturtle()
aiTurtle.penup()
aiTurtle.goto(400,300)
aiTurtle.pendown()
for i in range(1,4):
	aiTurtle.forward(-100)
	aiTurtle.left(90)
	
	
# Punkte Aktualisierung	
	
def score():
#	global zahlHumanTurtle
#	global zahlAiTurtle
	zahlHumanTurtle.undo()
	zahlHumanTurtle.write(humanPunkte, font=("Times", 72, "normal"))
	
	zahlAiTurtle.undo()
	zahlAiTurtle.write(aiPunkte, font=("Times", 72, "normal"))
	
	
# Punktestand Links
	
zahlHumanTurtle = turtle.Turtle()
zahlHumanTurtle.speed(0)
zahlHumanTurtle.hideturtle()
zahlHumanTurtle.penup()
zahlHumanTurtle.goto(-375,195)
zahlHumanTurtle.pendown()


# Punktestand Rechts
	
zahlAiTurtle = turtle.Turtle()
zahlAiTurtle.speed(0)
zahlAiTurtle.hideturtle()
zahlAiTurtle.penup()
zahlAiTurtle.goto(325,195)
zahlAiTurtle.pendown()
score()

# VS Text

humanTurtle.penup()
humanTurtle.goto(-80,-45)
humanTurtle.pendown()
humanTurtle.color('#890000', 'white')
humanTurtle.write("VS", font=("Times", 91, "normal"))
humanTurtle.color('#000066', 'white')
aiTurtle.color('#000066', 'white')

# Aufgabe für den Benutzer

aufgabeTurtle = turtle.Turtle()
aufgabeTurtle.speed(0)
aufgabeTurtle.hideturtle()
aufgabeTurtle.penup()
aufgabeTurtle.goto(-375,-260)
aufgabeTurtle.pendown()

humanKarteText = turtle.Turtle()
humanKarteText.speed(0)
humanKarteText.hideturtle()
humanKarteText.penup()

aiKarteText = turtle.Turtle()
aiKarteText.speed(0)
aiKarteText.hideturtle()
aiKarteText.penup()



def hauptScreen():
	screen.onkey(kartenZiehen, "Return")
	aufgabeTurtle.undo()
	aufgabeTurtle.write("Drücke Enter, um eine neue Runde zu beginnen!", font=("Times", 22, "normal"))
	
	humanKarteText.undo()
	humanTurtle.undo()
	aiKarteText.undo()
	aiTurtle.undo()


# Screen mit verdeckten Karten


# 2 random Monster ziehen

def kartenZiehen():
	global humanMonster
	global aiMonster
	screen.onkey(None, "Return")
	humanMonster = monsters[choice(monsterName)]
	aiMonster= monsters[choice(monsterName)]
	aufgabeTurtle.undo()
	
	# Karte 1 verdeckt
	
	humanTurtle.penup()
	humanTurtle.goto(-250,25)
	humanTurtle.pendown()
	humanTurtle.showturtle()
	humanTurtle.shape('VK.gif')
	
	# Karte 2 vedeckt
	
	aiTurtle.penup()
	aiTurtle.goto(250,25)
	aiTurtle.pendown()
	aiTurtle.showturtle()
	aiTurtle.shape('VK.gif')
	
	# Screen übergreifender Tastendruck
	screen.onkey(groesse, "g")
	screen.onkey(initiative, "i")
	screen.onkey(staerke, "s")

	aufgabeTurtle.write("Wähle eine Eigenschaft! Drücke g für Größe, i für Initiative oder s für Stärke !?", font=("Times", 17, "normal"))

#Monsterwerte werden miteinander verglichen

def groesse():
	global result
	result = humanMonster[0] > aiMonster[0]
	ergebnis("\nName: " + str(humanMonster[4]) + "\nGröße:" + str(humanMonster[0]), "\nName: " + str(aiMonster[4]) + "\nGröße:" + str(aiMonster[0]))
	
	
def initiative():
	global result
	result = humanMonster[1] > aiMonster[1]
	ergebnis("\nName: " + str(humanMonster[4]) + "\nInitiative:" + str(humanMonster[1]), "\nName: " + str(aiMonster[4]) + "\nInitiative:" + str(aiMonster[1]))
		
	
def staerke():
	global result
	result = humanMonster[2] > aiMonster[2]
	ergebnis("\nName: " + str(humanMonster[4]) + "\nStärke:" + str(humanMonster[2]), "\nName: " + str(aiMonster[4]) + "\nStärke:" + str(aiMonster[2]))
	

#Letzter Screen, sprich Ergebnis 
	
def ergebnis(humanKartenWerte, aiKartenWerte):
	global humanPunkte, aiPunkte, humanKarteText, aiKarteText

	# Cheatsicherung
	screen.onkey(None, "g")
	screen.onkey(None, "i")
	screen.onkey(None, "s")
	
	aufgabeTurtle.undo()
	
	# Benutzer Karte Text
	humanKarteText.penup()
	humanKarteText.goto(-345,-160)
	humanKarteText.pendown()
	humanKarteText.write(humanKartenWerte, font=("Times", 16, "normal"))
	
	# Benutzer Karte Bild
	humanTurtle.undo()
	humanTurtle.penup()
	humanTurtle.goto(-250,25)
	humanTurtle.showturtle()
	humanTurtle.shape(humanMonster[3])
	
	# KI Karte Text
	
	aiKarteText.penup()
	aiKarteText.goto(155,-160)
	aiKarteText.pendown()
	aiKarteText.write(aiKartenWerte, font=("Times", 16, "normal"))
	
	# KI Karte Bild
	aiTurtle.undo()
	aiTurtle.penup()
	aiTurtle.goto(250,25)
	aiTurtle.showturtle()
	aiTurtle.shape(aiMonster[3])
		
	if result == True:
		humanPunkte = humanPunkte + 1
		aufgabeTurtle.write("Und der menschlicher Verstand hat wieder einmal gewonnen! \nDrücke Esc für eine neue Runde.", font=("Times", 17, "normal"))
	else:
		aiPunkte = aiPunkte +1
		aufgabeTurtle.write("Oh nein! Die Technik gewinnt, der Terminator ist nahe.... \nDrücke Esc für eine neue Runde.", font=("Times", 17, "normal"))
	score()
	
	screen.onkey(hauptScreen, "Escape")




hauptScreen()
screen.listen()
screen.mainloop()















































