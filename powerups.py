from turtle import *
class Powerup():

    def __init__(self, gamestate):
        self.powerupList = ['bomb', 'heart', 'jump']
        from random import choice
        self.type = choice(self.powerupList)
        self.gamestate = gamestate
        self.findLocation()
        self.placePowerup()

    def findLocation(self):
        '''finds where to put the powerup on the map'''
        from random import randint
        self.xCord = randint(0,999)
        self.yCord = self.gamestate.hmap[self.xCord] + randint(40,80)

    def placePowerup(self):
        import turtle
        self.drawer = Turtle()
        self.drawer.hideturtle()
        self.drawer.up()
        self.drawer.goto(self.xCord, self.yCord)
        self.drawer.write(self.type, False, 'center')

    def destroy(self):
        self.drawer.clear()
        update()
        

    def onCollect(self, player):
        if self.type == 'heart':
            self.heartCollectHandler(player)

    def onFire(self, player):
        if self.type == 'bomb':
            self.bombHandler(player)
        elif self.type == 'jump':
            self.jumpHandler(player)

    def heartCollectHandler(self, player):
        player.health += 1
        self.gamestate.writeLivesinfo()
