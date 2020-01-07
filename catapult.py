#make a test that moves the turtle icon along the terrain
import terrain
from turtle import *



class Catapult():

    def __init__(self, name, gamestate, startingpoint, turtlecolor):
        self.turt = Turtle('turtle')
        self.cannonball = Turtle('circle')
        self.cannonball.up()
        self.vx = 5
        self.vy = 1
        self.name = name
        self.gamestate = gamestate
        self.health = 3
        self.location = (startingpoint, gamestate.hmap[startingpoint])
        self.direction = 'right'
        self.movementPoints = 5
        #self.amount = 0 #this is movement amount
        self.turt.up()
        self.turt.goto(self.location)
        self.turtlecolor = turtlecolor
        #self.turt.color(self.turtlecolor, self.turtlecolor)
        self.turt.color('purple', 'purple')
        self.turt.stamp()
        self.mypowerup = None
        self.destroyTerrainmod = False

    def getVelocities(self,vx,vy):
        self.vx = vx
        self.vy = vy

    def setVelo1(self):
        self.vy = 3
        print(self.vy)

    def setVelo2(self):
        self.vy = 5
        print(self.vy)

    def setVelo3(self):
        self.vy = 8
        print(self.vy)

    def setVelo4(self):
        self.vy = 9
        print(self.vy)

    def setVelo5(self):
        self.vy = 10
        print(self.vy)
    
    def setAmountandDirection(self):
        self.amount = int(input('Enter New Distance '))
        self.direction = input("Set direction, please enter 'left' or 'right' ")
        self.moveCatapult()
    
    def animateParabola(self):
        if self.direction == 'right' and self.location[0] > 950:
            print('too far')
            return
        elif self.direction == 'left' and self.location[0] <50:
            print('too far')
            return 
        originalVelo = self.vy
        originalPosition = self.turt.pos()
        self.cannonball.goto(originalPosition)
        self.cannonball.showturtle()
        
        while (True):
            update()
            position = self.cannonball.pos()
            dx = originalVelo/2
            if self.direction == 'left':
                dx = -dx
            newx = position[0] + self.vx * dx
            newy = position[1] + (self.vy * 10)
            hmapy = self.gamestate.hmap[int(newx)]
            newy = max(newy, hmapy)
            self.cannonball.goto(newx, newy)
            self.vy -=1
            
            newpos = self.cannonball.pos()
            if hmapy <= newpos[1]-0.5 and newx >= 0 and newx < 1000:
                self.location = newpos
                powerup = self.isHitPowerup()
                if not powerup == None:
                    print('it hits')
                    self.gamestate.applyPowerup(powerup)
            else:
                break
        #self.turt.shape('turtle')
        #self.turt.color('black', 'black')
        #self.cannonball.clearstamps(-1)
        update()
        self.cannonball.hideturtle()
        self.location = newpos
        if self.isHit():
            self.dodamage()
        if self.destroyTerrainmod:
            from terrain import destroyTerrainAt
            self.gamestate.hmap = destroyTerrainAt(self.gamestate.hmap, self.location)
            self.destroyTerrainmod = False
        self.location = originalPosition
        print(self.cannonball.stampItems)
        update()
        self.movementPoints = 5
        self.vy = originalVelo
        self.gamestate.switchplayer()

    def moveRight(self):
        print(self.location)
        if self.movementPoints == 0:
            return
        if self.location[0] + 50 >= 999:
            self.gamestate.writeInformerinfo()
            return
        self.direction = 'right'
        self.movementPoints -= 1
        currentpos = self.turt.pos()
        newxCoord = currentpos[0] + 50
        newyCoord = self.gamestate.hmap[newxCoord]
        self.location = (newxCoord, newyCoord)
        #print(self.location)
        self.turt.clearstamps()
        update()
        self.turt.goto(self.location)
        self.turt.stamp()
        update()
        self.gamestate.writeMPinfo()

    def moveLeft(self):
        print(self.location)
        if self.movementPoints == 0:
            return
        if self.location[0] - 50 <= 0:
            self.gamestate.writeInformerinfo()
            return()
        
        self.direction = 'left'
        self.movementPoints -= 1
        currentpos = self.turt.pos()
        newxCoord = currentpos[0] - 50
        newyCoord = self.gamestate.hmap[newxCoord]
        self.location = (newxCoord, newyCoord)
        #print(self.location)
        self.turt.clearstamps()
        update()
        self.turt.goto(self.location)
        self.turt.stamp()
        update()
        self.gamestate.writeMPinfo()


    def isHit(self):
        
        if self.gamestate.currentPlayer is self.gamestate.player1:
            otherplayer = self.gamestate.player2
        else:
            otherplayer = self.gamestate.player1
        print("Current player" ,self.gamestate.currentPlayer.name)
        print('Other player', otherplayer.name)
        zoneofEffectMinX = otherplayer.location[0] - 120
        zoneofEffectMaxX = otherplayer.location[0] + 120
        ZoneofEffectMinY = otherplayer.location[1] -130
        ZoneofEffectMaxY = otherplayer.location[1] +130
        print(zoneofEffectMinX, zoneofEffectMaxX)
        print(ZoneofEffectMinY, ZoneofEffectMaxY)
        print(self.location[0])
        print(self.location[1])
        if (self.location[0] > zoneofEffectMinX and self.location[0] < zoneofEffectMaxX) and (self.location[1] > ZoneofEffectMinY and self.location[1] < ZoneofEffectMaxY):
            return True
        else: 
            return False

    def dodamage(self):
        if self.gamestate.currentPlayer is self.gamestate.player1:
            otherplayer = self.gamestate.player2
        else:
            otherplayer = self.gamestate.player1
        otherplayer.health -= 1
        #print('{0} has been hit!'.format(otherplayer.name))
        self.gamestate.writeHitinfo()
        self.gamestate.writeLivesinfo()
        if otherplayer.health == 0:
            self.gamestate.doWinScreen()

    def faceLeft(self):
        self.direction = 'left'

    def faceRight(self):
        self.direction = 'right'

    def drawHitbox(self):
        hitbox = Turtle()
        hitbox.hideturtle()
        hitbox.up()
        hitbox.goto(self.location)
        hitbox.seth(0)
        hitbox.forward(120)
        hitbox.down()
        hitbox.left(90)
        hitbox.forward(130)
        hitbox.left(90)
        hitbox.forward(240)
        hitbox.left(90)
        hitbox.forward(260)
        hitbox.left(90)
        hitbox.forward(260)
        # hitbox.down()
        # hitbox.seth(0)
        # hitbox.forward(90)
        # hitbox.left(90)
        # hitbox.forward(90)
        # hitbox.up()
        # hitbox.goto(self.location)
        # hitbox.down()
        # hitbox.seth(180)
        # hitbox.forward(90)
        # hitbox.right(90)
        # hitbox.forward(90)
        update()

    def isHitPowerup(self):
        
        zoneofEffectMinX = self.location[0] - 50
        zoneofEffectMaxX = self.location[0] + 50
        ZoneofEffectMinY = self.location[1] -50
        ZoneofEffectMaxY = self.location[1] +50
        for i, powerup in enumerate(self.gamestate.PowerupList):

            if ((powerup.xCord > zoneofEffectMinX) and\
                (powerup.xCord < zoneofEffectMaxX) and\
                (powerup.yCord > ZoneofEffectMinY) and\
                (powerup.yCord < ZoneofEffectMaxY)):
                    return powerup
        return None

    def poweruphandler(self):
        if self.mypowerup == None:
            return
        elif self.mypowerup.type == 'jump':
            self.vy *= 2
            print(self.vy)
        elif self.mypowerup.type == 'bomb':
            self.destroyTerrainmod = True
        self.mypowerup = None

        
        