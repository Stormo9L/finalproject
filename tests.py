from setupAndData import Gamestate
from catapult import *
from terrain import *

def testmakehillmap():
    print(makehillmap())

def testmakeheightmap():
    print(makeheightmap())

def testdefinesize():
    '''checks to see if the function works by going to 0,0 and
    drawing a line'''
    definesize()
    goto(0,0)
    left(45)
    forward(500)

def testmovingalongterrain():
    '''stamps a turtle along the terrain'''
    tracer(0,0)
    hmap = makeheightmapV2()
    definesize()
    generateTerrain(hmap)
    update()
    catapult = Turtle()
    catapult.up()
    for x,i in enumerate(hmap):
        catapult.goto(x,i)
        catapult.stamp()
    mainloop()

def make2turtles():
    '''make 2 new turtles and place them on random spots
    on the terrain. These aren't the players, just two arbitrary turtles'''

    definesize()
    tracer(0,0)
    hmap = terrain.makeheightmapV2()
    generateTerrain(hmap)
    
    harry = Turtle('turtle')
    tom = Turtle('turtle')
    import random
    point1 = random.randint(0,999)
    point2 = random.randint(0,999)
    harry.goto(point1, hmap[point1])
    tom.goto(point2, hmap[point2])
    update()
    mainloop()



 





def thirdInputTest():
    '''the first two input tests were virtually identical, and were made as new onkey
    commands were added to the code. This input test is completely up to date, and 
    for the longest time, acted as my main. When I make a main, it will be identical
    to this function.'''
    gamestate = Gamestate()
    listen()
    mainloop()



def testnewTerrainModel():
    '''uses the function makeheightmapV2 to generate terrain'''
    definesize()
    hmap = terrain.makeheightmapV2()
    tracer(0,0)
    generateTerrain(hmap)
    update()
    mainloop()


def testDestroyTerrain():
    #makes 5 random holes
    definesize()
    hmap = terrain.makeheightmapV2()
    tracer(0,0)
    generateTerrain(hmap)
    update()
    for i in range(5):
        import random
        foo = random.randint(0,999)
        poo = hmap[foo]
        hmap = destroyTerrainAt(hmap, (foo,poo))
    mainloop()





    




#test finalization, 7/7
#There are a lack of tests, as much of the bugtesting was done by printing
#to the terminal to see if I got the expected result. For the sake of showing my work
#all of these print statements are intact, just commented out
#some tests were also deleted due to being impossible to update to a working status
#under the current framework

#make2turtles()
#testDestroyTerrain()
#testnewTerrainModel()
#testmovingalongterrain()
#thirdInputTest()
#testmakeheightmap()
#testmakehillmap()