#contains functions that setup the game, as well as a collection of information vital
#to the game state

import terrain
from random import *
from turtle import *
from tkinter import *

import powerups
poo = randint(0,999)
foo = randint(0,999)
def setup():
    '''sets up the game, returns all the information that it created as a part of setting up'''
    terrain.definesize()
    hmap = terrain.makeheightmapV2()
    tracer(0,0)
    terrain.generateTerrain(hmap)
    update()
    return hmap

from catapult import Catapult
class Gamestate():
    def __init__(self):
        self.endTutorialDisplay = False
        self.doTitleScreen()
        self.doDemoScreen()

    def startGame(self):
        self.hmap = setup()
        self.player1 = Catapult(self.firstname, self, poo, 'red')
        self.player2 = Catapult(self.secondname, self, foo, 'blue')
        self.PowerupList = []
        
        self.livesDrawer = Turtle()
        self.livesDrawer.hideturtle()
        self.livesDrawer.up()
        self.writeLivesinfo()

        self.movementPointsDrawer = Turtle()
        self.movementPointsDrawer.hideturtle()
        self.movementPointsDrawer.up()
        
        self.hitDrawer = Turtle()
        self.hitDrawer.hideturtle()
        self.hitDrawer.up()

        self.informerDrawer = Turtle()
        self.informerDrawer.hideturtle()
        self.hitDrawer.up()
        update()
        self.currentPlayer = self.player2
    
    def switchplayer(self):
        #print(self.currentPlayer.name)
        if self.currentPlayer is self.player1:
            self.currentPlayer = self.player2
            self.currentPlayer.turt.color('yellow', self.currentPlayer.turtlecolor)
            self.player1.turt.color(self.player1.turtlecolor, self.player1.turtlecolor)
        else:
            self.currentPlayer = self.player1
            self.currentPlayer.turt.color('yellow', self.currentPlayer.turtlecolor)
            self.player2.turt.color(self.player2.turtlecolor, self.player2.turtlecolor)
        self.player1.turt.clearstamps()
        self.player2.turt.clearstamps()
        self.player1.turt.stamp()
        self.player2.turt.stamp()
        update()
        #print("{0}'s turn!".format(self.currentPlayer.name))
        self.setbuttons()
        self.writeMPinfo()
        #print(self.currentPlayer.name)
        sloo = randint(1,4)
        if sloo == 4:
            self.PowerupList.append(powerups.Powerup(self))

    def setbuttons(self):
        '''assigns the keys 1-5 to the Catapult setVelo functions, with the object
        being the current player
        '''
        onkey(self.currentPlayer.setVelo1, '1')
        onkey(self.currentPlayer.setVelo2, '2')
        onkey(self.currentPlayer.setVelo3, '3')
        onkey(self.currentPlayer.setVelo4, '4')
        onkey(self.currentPlayer.setVelo5, '5')
        onkey(self.currentPlayer.animateParabola, 'f')
        onkey(self.currentPlayer.moveRight, 'd')
        onkey(self.currentPlayer.moveLeft, 'a')
        onkey(self.currentPlayer.drawHitbox, 'p')
        onkey(self.currentPlayer.faceRight, 'm')
        onkey(self.currentPlayer.faceLeft, 'n')
        onkey(self.currentPlayer.poweruphandler, 'j')

    def endgame(self):
        print(self.currentPlayer.name, ' wins!',)

    def writeLivesinfo(self):
        self.livesDrawer.clear()
        self.livesDrawer.goto(0,950)
        self.livesDrawer.write("{0}'s Lives (Red): {1}".format(self.player1.name, self.player1.health), False, 'left', ('Terminal', 12, 'normal'))
        self.livesDrawer.goto(0, 920)
        self.livesDrawer.write("{0}'s Lives (Blue): {1}".format(self.player2.name, self.player2.health), False, 'left', ('Terminal', 12, 'normal'))
       
    def writeMPinfo(self):
        self.movementPointsDrawer.clear()
        self.movementPointsDrawer.goto(0,880)
        self.movementPointsDrawer.write("Movement Points Remaining: {0}".format(self.currentPlayer.movementPoints), False, 'left', ('Terminal', 12, 'normal'))

    def writeHitinfo(self):
        self.hitDrawer.clear()
        if self.currentPlayer is self.player1:
            otherplayer = self.player2
        else:
            otherplayer = self.player1
        self.hitDrawer.goto(999, 950)
        self.hitDrawer.write('{0} has been hit!'.format(otherplayer.name), False, 'right',  ('Terminal', 14, 'normal'))
        import time
        time.sleep(1)
        self.hitDrawer.clear()

    def writeInformerinfo(self):
        self.informerDrawer.clear()
        self.informerDrawer.goto(0,800)
        self.informerDrawer.down()
        self.informerDrawer.write('You cant go any further!', False, 'right',  ('Terminal', 14, 'normal'))
        import time
        time.sleep(1)
        self.informerDrawer.clear()
    def applyPowerup(self, powerup):
        self.currentPlayer.mypowerup = powerup
        powerup.onCollect(self.currentPlayer)
        powerup.destroy()
        self.PowerupList.remove(powerup)

    def doWinScreen(self):
        clearscreen()
        bob = Turtle()
        bob.write('{0} Wins!'.format(self.currentPlayer.name))
        onscreenclick(self.endTutorial)

    def doTitleScreen(self):
        terrain.definesize()
        titledrawer = Turtle()
        tracer(0,0)
        titledrawer.fillcolor(0.39,0.26,0.13)
        titledrawer.begin_fill()
        titledrawer.hideturtle()
        for i in range(4):
            titledrawer.forward(999)
            titledrawer.left(90)
        titledrawer.end_fill()
        titledrawer.up()
        titledrawer.goto(500,500)
        titledrawer.down()
        
        titledrawer.write('Kings of The Valley', False, 'center', ('Terminal', 30,'normal'))
        update()
        import time
        time.sleep(2)
        titledrawer.up()
        titledrawer.goto(500,300)
        titledrawer.down()
        titledrawer.write('Kings, Give Thee Thy Names', False, 'center', ('Terminal', 20,'normal'))
        #self.firstname = input("Player 1's Name: ")
        #self.secondname = input("Player 2's Name: ")
        self.firstname = titledrawer.screen.textinput('Setup', 'Name of player 1')
        self.secondname = titledrawer.screen.textinput('Setup', 'Name of player 2')

    def endTutorial(self, x, y):
        onscreenclick(None)
        self.endTutorialDisplay = True
        # clearscreen()
        resetscreen()
        self.startGame()
        self.switchplayer()

    def doDemoScreen(self):
        clearscreen()
        redTurtle = Turtle('turtle')
        redTurtle.color('red', 'red')
        
        redTurtle.hideturtle()
        redTurtle.seth(90)
        redTurtle.up()
        blueTurtle = Turtle('turtle')
        blueTurtle.color('blue', 'blue')
        
        blueTurtle.hideturtle()
        blueTurtle.seth(90)
        blueTurtle.up()
        self.textdrawer = Turtle()
        self.textdrawer.up()
        self.textdrawer.hideturtle()
        self.textdrawer.goto(500,500)
        
        redTurtle.width(60)
        blueTurtle.width(60)
        redTurtle.goto(333,300)
        redTurtle.stamp()
        redTurtle.showturtle()
        blueTurtle.goto(666,300)
        blueTurtle.stamp()
        blueTurtle.showturtle()
        self.textdrawer.write('Two Turtles are locked in a struggle \n for control over the Land', False, 'center', ('Terminal', 16,'normal'))
        onscreenclick(self.endTutorial)
        ontimer(self.doDemoScreen2, 3000)

    def doDemoScreen2(self):
        if (not self.endTutorialDisplay):
            onscreenclick(None)
            self.textdrawer.clear()
            self.textdrawer.write('These Turtles wield the power of sharp stones.\n Primitive to us, but to them, deadly', False, 'center', ('Terminal', 16,'normal'))
            onscreenclick(self.endTutorial)
            ontimer(self.doDemoScreen3, 3000)

    def doDemoScreen3(self):
        if (not self.endTutorialDisplay):
            onscreenclick(None)
            self.textdrawer.clear()
            self.textdrawer.write("Controls:\n'A' to move left\n'D' to move right\n'1-5' determine the power of your throw\nand 'F' fires!\nWhen you grab a powerup, press 'J' to activate it!\n\nClick anywhere to continue", False, 'center', ('Terminal', 16,'normal'))
            onscreenclick(self.endTutorial)
    