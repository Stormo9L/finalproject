#This module creates a bit map stored as 2D array. In each array are zeros and ones
#a zero is a white space and a one a black space.
#The screen will be locked to a certain resolution so that the size of the array
#can stay the same

import random
from turtle import *
terraindrawer = Turtle()
    
def definesize():
    '''sets the coordinate plane to have 0,0 at the bottom left and 1000,1000 in the
    top right'''
    screensize(1000,1000)
    setworldcoordinates(0,0,1000,1000)



def setuparray(): #outdated
    '''makes an array filled with 1000 arrays
    returns the array
    '''
    array = []
    for i in range(50):
        array.append([])
    return array

def testsetuparray(): #outdated
    '''tests the function by printing the array'''
    array = setuparray()
    for count,i in enumerate(array):
        print('Array Number: ' ,count)
    
def fillarrayrandom(array): #outdated
    '''randomly fills the 2D array. Each subarray has 1000 integers, randomly a zero or one'''
    import random
    for subarray in array:
        for item in range(1000):
            number = random.randint(0,1)
            subarray.append(number)
    return array



def arraytopixels(array): #outdated
    '''takes a 2D array of zeroes and ones and fills a turtle screen based off
    the values: 0 = white, 1 = black'''
    up()
    goto(0,0)
    seth(0)
    for coord,row in enumerate(array,0):
        up()
        goto(0,coord)
        
        for pixel in row:
            forward(1)
            if array[coord][pixel+1] == 1:
                down()
                forward(1)
            elif array[coord][pixel+1] == 0:
                up()
                forward(1)
    



#alright new idea
#instead of mapping the entire screen, I will only generate terrain for the surface
#of the 'earth' and map that. Instead of being stored as 0 and 1, I will use a heightmap
#which will make it easier to move the catapults across the terrain

def makeplateu(heightmap, lasty):
    '''generates a plateu.
    plateau must have a minimum length of 300. Maximum length is 500'''
    
    length = random.randint(100,500)
    for i in range(length):
        heightmap.append(lasty)
    return heightmap, lasty

def makehill(heightmap, lasty):  #outdated
    '''generates a hill (for now a pyramid)
    width of hill is between 80 and 150
    height of hill is between 60 and 100'''
    width = random.randint(80,150)
    height = random.randint(60,100)
    yperx = height/(width/2)
    currenty = lasty
    for i in range(int(width/2)):
        currenty += yperx + random.randint(-2,2)
        heightmap.append(currenty)
    for i in range(int(width/2)):
        currenty -= yperx + random.randint(-2,2)
        heightmap.append(currenty)
    return heightmap, currenty
    
def makevalley(heightmap, lasty): #outdated
    '''generates a valley (for now a pyramid)
    width of valley is between 80 and 150
    height of valley is between 60 and 100'''
    width = random.randint(80,150)
    height = random.randint(60,100)
    yperx = height/(width/2)
    currenty = lasty
    for i in range(int(width/2)):
        currenty -= yperx + random.randint(-5,0)
        heightmap.append(currenty)
    for i in range(int(width/2)):
        currenty += yperx + random.randint(0,5)
        heightmap.append(currenty)
    return heightmap, currenty
def makeheightmap():
    lasty = 400
    heightmap = []
    terrains = [makehill, makeplateu, makevalley]
    while len(heightmap) < 1001:
        heightmap, lasty = random.choice(terrains)(heightmap, lasty)
    return heightmap



#issues found when running testmakeheightmap:

#Hills seem to end below where they started, which should not be possible
#this issue has since been resolved

def makehillmap():
    '''identical to makeheightmap but only uses hills'''
    lasty = 400
    heightmap = []
    while len(heightmap) < 1001:
        heightmap, lasty = makehill(heightmap, lasty)
    return heightmap



def generateTerrain(heightmap):
    terraindrawer.clear()
    
    for x, i in enumerate(heightmap):
        terraindrawer.pencolor(0.39,0.26,0.13)
        terraindrawer.up()
        terraindrawer.goto(x,0)
        terraindrawer.down()
        terraindrawer.goto(x,i)
        terraindrawer.color(0.678,0.847,0.902)
        terraindrawer.up()
        terraindrawer.goto(x, 999)
        terraindrawer.seth(270)
        terraindrawer.down()
        terraindrawer.goto(x,i)
        
    terraindrawer.hideturtle()


def screenSpaceToHillSpace(point, hillStart, width, height):
    xp = point[0] - hillStart[0] - (width / 2)
    yp = point[1] - hillStart[1] - height
    return (xp, yp)

def hillSpaceToScreenSpace(point, hillStart, width, height):
    xp = point[0] + hillStart[0] + (width / 2)
    yp = point[1] + hillStart[1] + height
    return (xp, yp)

def screenSpaceToValleySpace(point, hillStart, width, height):
    xp = point[0] - hillStart[0] - (width / 2)
    yp = point[1] - (hillStart[1] - height)
    return (xp, yp)

def valleySpaceToScreenSpace(point, hillStart, width, height):
    xp = point[0] + hillStart[0] + (width / 2)
    yp = point[1] + (hillStart[1] - height)
    return (xp, yp)

def newmakehill(heightmap, lasty):
    #this function is a version of makehill with better logic, to avoid making
    #hills that go beyond the boundaries

    maxHeight = int(850 - lasty) # maxHeight is the distance between the lasty and 850. This is the maximum possible value for the hill, as going beyond 750 is just absurd
    if (maxHeight < 1):
        return heightmap, lasty
    minHeight = min(100, maxHeight - 1) # minHeight is the smallest permitted hill. The default is 100, but it must not be greater maxHeight
    #print(minHeight, maxHeight)
    #print(lasty)
    hillStart = (len(heightmap), lasty)
    width = random.randint(150,250)
    height = random.randint(minHeight, maxHeight)
    # while lasty + height >= 750:
    #    height = random.randint(minHeight, maxHeight)
    #print(height)
    lastx = len(heightmap)
    vertex = (lastx + (width/2), lasty + height)
    currenty = lasty
    yScale = 4 * height / (width ** 2)
    #yperx = height/(width/2)
    #currenty = lasty
    #print('hill start', hillStart)
    #print('(w,h)', (width, height))
    #print('yScale', yScale)
    for i in range(int(width)):
        #currenty += yperx + random.randint(-2,2)
        x = lastx + i
        unscaledPointInHillSpace = screenSpaceToHillSpace((x, 0), hillStart, width, height)
        #print('unscaled point in hill space', unscaledPointInHillSpace)
        y = -(unscaledPointInHillSpace[0] ** 2) * yScale
        parabolicPointInHillSpace = (unscaledPointInHillSpace[0], y)
        #print('y=x^2 point in hill space', parabolicPointInHillSpace)
        point = hillSpaceToScreenSpace(parabolicPointInHillSpace, hillStart, width, height)
        point = (point[0], point[1])
        #print('point in screen space', point)
        # heightmap.append(currenty)
        heightmap.append(point[1]) # + random.randint(-10, 10) )
    #for i in range(random.randint(10,20)):
    #    heightmap.append(currenty)
    #for i in range(int(width/2)):
    #    currenty -= yperx + random.randint(-2,2)
    #    heightmap.append(currenty)
    return heightmap, currenty

def newmakevalley(heightmap, lasty):
    #this function is a version of makehill with better logic, to avoid making
    #hills that go beyond the boundaries

    maxDepth = int(lasty - 150) # maxHeight is the distance between the lasty and 850. This is the maximum possible value for the hill, as going beyond 750 is just absurd
    if (maxDepth < 1):
        return heightmap, lasty
    minDepth = min(100, maxDepth - 1) # minHeight is the smallest permitted hill. The default is 100, but it must not be greater maxHeight
    #print(minDepth, maxDepth)
    #print(lasty)
    hillStart = (len(heightmap), lasty)
    width = random.randint(150,250)
    depth = random.randint(minDepth, maxDepth)
    # while lasty + height >= 750:
    #    height = random.randint(minHeight, maxHeight)
    #print(depth)
    lastx = len(heightmap)
    vertex = (lastx + (width/2), lasty + depth)
    currenty = lasty
    yScale = 4 * depth / (width ** 2)
    #yperx = height/(width/2)
    #currenty = lasty
    #print('hill start', hillStart)
    #print('(w,h)', (width, depth))
    #print('yScale', yScale)
    for i in range(int(width)):
        #currenty += yperx + random.randint(-2,2)
        x = lastx + i
        unscaledPointInHillSpace = screenSpaceToHillSpace((x, 0), hillStart, width, depth)
        #print('unscaled point in hill space', unscaledPointInHillSpace)
        y = (unscaledPointInHillSpace[0] ** 2) * yScale
        parabolicPointInHillSpace = (unscaledPointInHillSpace[0], y)
        #print('y=x^2 point in hill space', parabolicPointInHillSpace)
        point = valleySpaceToScreenSpace(parabolicPointInHillSpace, hillStart, width, depth)
        point = (point[0], point[1])
        #print('point in screen space', point)
        # heightmap.append(currenty)
        heightmap.append(point[1]) # + random.randint(-10, 10))
    #for i in range(random.randint(10,20)):
    #    heightmap.append(currenty)
    #for i in range(int(width/2)):
    #    currenty -= yperx + random.randint(-2,2)
    #    heightmap.append(currenty)
    return heightmap, currenty


def makeheightmapV2():
    '''new terrain generation logic'''
    lasty = 400
    heightmap = []
    terrains = [newmakehill, makeplateu, newmakevalley]
    while len(heightmap) < 1001:
        heightmap, lasty = random.choice(terrains)(heightmap, lasty)
    return heightmap

def destroyTerrainAt(hmap, point):
    '''Destroys terrain at a given point and redraws the terrain'''
    widthofHole = random.randint(60,100)
    startingX = point[0]
    #print(hmap)
    for i in range(widthofHole):
        #print(hmap[i + startingX])
        hmap[i + int(startingX)] -= random.randint(60,100)
        #print(hmap[i + startingX])
        #print('-----------------------')
    #print(hmap)
    generateTerrain(hmap)
    update()
    return hmap
