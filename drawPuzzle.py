import turtle
import math
import csv

### input csv file and size of puzzle
file = r'..\puzzle.csv'
size = 7

colors = ["black","blue","brown","red","yellow","green","orange","beige","turquoise","pink"]

##drawing parameter: triangle side length, starting point of drawing
sideLength = 100
start = [0,200]

turt = turtle.Turtle()
turt.hideturtle()
turt.speed(50)

## Draw one triangle
def drawTriangleColored(clr, startPos = [0,0], heading = 0, inverse = False):
    invert = 1
    if(inverse): invert = -1
    turt.penup()
    turt.setpos(startPos[0],startPos[1])
    turt.setheading(heading)
    turt.pendown()
    turt.begin_fill()
    turt.color(colors[clr[0]])
    turt.forward(sideLength)
    turt.left(150*invert)
    turt.forward(sideLength/math.sqrt(3))
    turt.left(60*invert)
    turt.forward(sideLength/math.sqrt(3))
    turt.setheading(heading)
    turt.end_fill()
    turt.begin_fill()
    if inverse: turt.color(colors[clr[2]]) 
    else: turt.color(colors[clr[1]])
    turt.left(60*invert)
    turt.forward(sideLength)
    turt.right(150*invert)
    turt.forward(sideLength/math.sqrt(3))
    turt.setpos(startPos[0],startPos[1])
    turt.setheading(heading)
    turt.end_fill()
    turt.penup()
    turt.left(60*invert)
    turt.forward(sideLength)
    turt.right(120*invert)
    turt.pendown()
    turt.begin_fill()
    if inverse: turt.color(colors[clr[1]]) 
    else: turt.color(colors[clr[2]])
    turt.forward(sideLength)
    turt.right(150*invert)
    turt.forward(sideLength/math.sqrt(3))
    turt.right(60*invert)
    turt.forward(sideLength/math.sqrt(3))
    turt.end_fill()
    
##draw the puzzle
def drawPuzzle(size, pieces):
    rows = size
    rowNumTriangles = list()
    rowStartingPoint = list()
    
    heading = 0
    totalPieces = 0
    for i in range(rows):
        rowNumTriangles.append(i*2+1)
        totalPieces = totalPieces + i*2+1
        startX = start[0] - (sideLength/2)*i
        startY = start[1] -i*math.sqrt((math.pow(sideLength,2)-math.pow(sideLength/2,2)))
        rowStartingPoint.append([startX,startY])

    piecesDrawn = 0
    for i in range(rows):
        invert = False
        heading = 0
        for j in range(rowNumTriangles[i]):
            startP = list(rowStartingPoint[i])
            startP[0] = startP[0]+j*sideLength/2
            if invert:
                startP[1] = rowStartingPoint[i-1][1]
            print(i, j, startP)
            drawTriangleColored(pieces[piecesDrawn],\
                startPos=startP, heading= heading, inverse= invert)
            piecesDrawn = piecesDrawn+1
            invert = not invert



##load the pieces from the file
pieces = list()

with open(file, 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        pieces.append([int(row[0]),int(row[1]), int(row[2])])



##check if the number of pieces is correct based on the size
totalPieces = 0
for i in range(size):
        totalPieces = totalPieces + i*2+1
if totalPieces != len(pieces):
    print("missing pieces")
    exit()


##draw the loaded pieces
drawPuzzle(size, pieces)

#drawTriangleColored([0,1,2], startPos=[0,0], heading = 0)
#drawTriangleColored([0,1,2], startPos=[300,math.sqrt((math.pow(sideLength,2)-math.pow(sideLength/2,2)))], heading = 0, inverse=True)

##Use turtle.done() to keep the canvas open
##if you want to save the drawing in .eps file comment turtle.done() and uncomment the line under it
## although taking a screenshot would be better as .eps is not really supported anymore
turtle.done()
#turt.getscreen().getcanvas().postscript(file="piece.eps")
