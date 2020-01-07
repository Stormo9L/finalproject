from setupAndData import Gamestate
from catapult import *

def testmovingalongterrain():
    tracer(0,0)
    hmap = terrain.makeheightmap()
    terrain.definesize()
    terrain.generateTerrain(hmap)
    update()
    catapult = Turtle()
    catapult.up()
    for x,i in enumerate(hmap):
        catapult.goto(x,i)
        catapult.stamp()
    mainloop()

def make2players():
    '''make 2 new turtles and place them on random spots
    on the terrain'''
    tracer(0,0)
    hmap = terrain.makeheightmap()
    terrain.definesize()
    terrain.generateTerrain(hmap)
    update()
    player1 = Turtle()
    player2 = Turtle()
    player1.up()
    player2.up()
    import random
    pos1 = random.randint(1,1000)
    pos2 = random.randint(1,1000)
    player1.goto(pos1, hmap[pos1 + 1])
    player2.goto(pos2, hmap[pos2 + 1])
    player1.stamp()
    player2.stamp()
    mainloop()

def testplayerclass():
    player1 = Catapult()
    print(player1.health)
    import time
    time.sleep(2)
    player1.turt.forward(100)
    mainloop()

def testparabola():
    '''makes a new catapult and puts it at a random position. It then fires a volley
    and prints out the coords of where it landed
    
    Bug: Can't always find the ground, and will pass through it into the infinite
    void raising an index error
    '''
    tracer(0,0)
    hmap = terrain.makeheightmap()
    terrain.definesize()
    terrain.generateTerrain(hmap)
    update()
    guy = Catapult()
    import random
    randompos = random.randint(0,999)
    guy.turt.up()
    guy.turt.goto(randompos, hmap[randompos+1])
    guy.getVelocities(4,10)
    guy.animateParabola(hmap)
    print(guy.turt.pos())
    mainloop()


def testmovingcatapult(): #test out of date
    '''tests moving a catapult across the terrain'''
    terrain.definesize()
    hmap = terrain.makeheightmap()
    tracer(0,0)
    terrain.generateTerrain(hmap)
    update()
    catapult = Catapult()
    import random
    
    catapult.turt.goto(500, hmap[500]+1)
    catapult.turt.stamp()
    catapult.moveCatapult('left', 300, hmap)
    catapult.turt.stamp()
    mainloop()

# def firstInputTest():
#     import setupAndData
#     hmap = setupAndData.setup()
#     player1 = Catapult('Henry')
#     player2 = Catapult('Todd')
#     setcurrentPlayer(player1)
#     setbuttons()
#     listen()
#     mainloop()

def secondInputTest(): #sees if the firing mechanism works using input from the player
    gamestate = Gamestate()    
    gamestate.player1.turt.up()
    gamestate.player2.turt.up()
    gamestate.player1.turt.goto(300, gamestate.hmap[300])
    gamestate.player2.turt.goto(500, gamestate.hmap[500])
    gamestate.player1.turt.down()
    gamestate.player2.turt.down()
    gamestate.switchplayer()
    listen()
    mainloop()

def testmake2players(): 
    make2players()

def thirdInputTest():# sees is the movement mechanism works using input from the player
    gamestate = Gamestate()
    listen()
    mainloop()

#thirdInputTest() this is the most up to date and stable test. 
#the features that worked with this test were firing and moving

#now i will fix terrain generation, as some of the logic is pretty messy
#what i want to fix specifically is terrain being generated above the screen
#boundaries, and turtles spawning above the screen boundary.

def testnewTerrainModel():
    '''uses the function makeheightmapV2 to generate terrain'''
    terrain.definesize()
    hmap = terrain.makeheightmapV2()
    tracer(0,0)
    terrain.generateTerrain(hmap)
    update()
    mainloop()

#testnewTerrainModel()
#raise ValueError("empty range for randrange() (%d,%d, %d)" % (istart, istop, width))
#ValueError: empty range for randrange() (60,-173, -233)

#thirdInputTest()

def testDestroyTerrain():
    #makes 5 random holes
    terrain.definesize()
    hmap = terrain.makeheightmapV2()
    tracer(0,0)
    terrain.generateTerrain(hmap)
    update()
    for i in range(5):
        import random
        foo = random.randint(0,999)
        poo = hmap[foo]
        hmap = terrain.destroyTerrainAt(hmap, (foo,poo))
    mainloop()

#testDestroyTerrain()

#thirdInputTest()

def winScreenTest():
    game = Gamestate()
    game.switchplayer()
    game.doWinScreen()
    mainloop()

def TitleScreenTest(): #this test only works if mainloop is put into the doTitleScreen class method
    game = Gamestate()
    
def DemoScreenTest():
    Gamestate.doDemoScreen()

#DemoScreenTest()
thirdInputTest()