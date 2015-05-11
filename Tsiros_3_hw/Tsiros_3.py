## Alyssa Tsiros
## Project 3
## 19 February, 2015

import helper
import matplotlib.pyplot as plt
import matplotlib.patches as pat
from matplotlib.widgets import Slider
import pylab
import numpy as np

def tumorPlots(x):
    """Input a number between 1-10 for what you would like to display on
        the x-axis. Attributes 1-10 are defined as:

        1. Radius
        2. Texture
        3. Perimeter
        4. Area
        5. Smoothness
        6. Compactness
        7. Concavity
        8. Concave Points
        9. Symmetry
        10. Fractal Dimension
    """

    y = [1,2,3,4,5,6,7,8,9,10]

    ## Displays each attribute plotted against the given attribuet
    for i in y:
        tumorPlot(x,i)



def tumorPlot(x,y):
    """ Input a number between 1-10 for x-values and for y-values.
        Attributes 1-10 are defined as:

        1. Radius
        2. Texture
        3. Perimeter
        4. Area
        5. Smoothness
        6. Compactness
        7. Concavity
        8. Concave Points
        9. Symmetry
        10. Fractal Dimension
    """

    ## define output from previous functions
    data = tumorXY(x,y)
    line = threshold(x,y)

    ## make benign tumor data blue and malignant tumor data red
    colors = {0: "blue", 1: "red"}
    classes = ['Benign','Malignant']

    ## legend defining the colors
    legend = [pat.Rectangle((0,0),1,1,fc = colors[0]),
              pat.Rectangle((0,0),1,1,fc = colors[1])]

    ## begin figure
    plt.figure()

    ## plot scatter plot
    plt.scatter(data[1],data[3],c=[colors[x] for x in data[4]])

    ## plot threshold line if applicable
    plt.plot(line[0],line[1],color='black')

    ## set x and y axes minimums
    plt.xlim(xmin=0)
    plt.ylim(ymin=0)

    ## add the legent
    plt.legend(legend, classes, loc=4)

    ## set title
    plt.title((str(data[2]) + ' vs. ' + str(data[0]) +
                             ' of Tumor Cell Nuclei'))

    ## axes labels
    plt.xlabel(data[0])
    plt.ylabel(data[2])

    plt.show()
        

def tumorXY(x, y):
    """ Input a number between 1-10 for x-values and for y-values.
        Attributes 1-10 are defined as:

        1. Radius
        2. Texture
        3. Perimeter
        4. Area
        5. Smoothness
        6. Compactness
        7. Concavity
        8. Concave Points
        9. Symmetry
        10. Fractal Dimension
    """

    ## import wdbc breast cancer data to inputFile and define attribute names
    inputFile = helper.extractAllRecords('wdbc.data.txt')

    attributeNames = ['Radius','Texture','Perimeter','Area','Smoothness',
                      'Compactness','Concavity','Concave Points','Symmetry',
                      'Fractal Dimension']

    ## place all records from inputFile into an array
    dataValues = []

    for line in inputFile:
        dataValues.append(line)

    ## initialize possible arrays for x and y values based on attribute
    malignant = []
    radius = []
    texture = []
    perimeter = []
    area = []
    smoothness = []
    compactness = []
    concavity = []
    concavePoints = []
    symmetry = []
    fractalDimension = []

    ## designate 1 to malignant and 0 to benign in malignant array
    for i in range(len(dataValues)):

        if (dataValues[i][1] == 'M'):
            malignant.append(1)

        if (dataValues[i][1] == 'B'):
            malignant.append(0)

        ## fill attribute arrays
        radius.append(dataValues[i][2])
        texture.append(dataValues[i][3])
        perimeter.append(dataValues[i][4])
        area.append(dataValues[i][5])
        smoothness.append(dataValues[i][6])
        compactness.append(dataValues[i][7])
        concavity.append(dataValues[i][8])
        concavePoints.append(dataValues[i][9])
        symmetry.append(dataValues[i][10])
        fractalDimension.append(dataValues[i][11])

    ## determine which attribute the user wants to plot on the x-axis
    if x == 1:
        xVals = radius
    if x == 2:
        xVals = texture
    if x == 3:
        xVals = perimeter
    if x == 4:
        xVals = area
    if x == 5:
        xVals = smoothness
    if x == 6:
        xVals = compactness
    if x == 7:
        xVals = concavity
    if x == 8:
        xVals = concavePoints
    if x == 9:
        xVals = symmetry
    if x == 10:
        xVals = fractalDimension

    ## determine which attribute the user wants to plot on the y-axis
    if y == 1:
        yVals = radius
    if y == 2:
        yVals = texture
    if y == 3:
        yVals = perimeter
    if y == 4:
        yVals = area
    if y == 5:
        yVals = smoothness
    if y == 6:
        yVals = compactness
    if y == 7:
        yVals = concavity
    if y == 8:
        yVals = concavePoints
    if y == 9:
        yVals = symmetry
    if y == 10:
        yVals = fractalDimension

    ## return x and y attribute names and values and the malignant array
    return(attributeNames[x-1],xVals,attributeNames[y-1],yVals,malignant)

def threshold(x,y):
    """ Input a number between 1-10 for x-values and for y-values.
        Attributes 1-10 are defined as:

        1. Radius
        2. Texture
        3. Perimeter
        4. Area
        5. Smoothness
        6. Compactness
        7. Concavity
        8. Concave Points
        9. Symmetry
        10. Fractal Dimension
    """
    ## if the average of both attributes for the benign tumor cells is less
    ## than that of malignant tumor cells, find the x and y intercept for which
    ## greater attribute values could indicate malignancy

    ## define different output values of tumorXY
    aX = tumorXY(x,y)[1]
    bY = tumorXY(x,y)[3]
    c = tumorXY(x,y)[4]

    ## initialize arrays
    benignXY = [[],[]]
    malignantXY = [[],[]]

    ## fill arrays
    for i in range(len(c)):
        if c[i] == 0:
            benignXY[0].append(aX[i])
            benignXY[1].append(bY[i])
        if c[i] == 1:
            malignantXY[0].append(aX[i])
            malignantXY[1].append(bY[i])

    ## convert from strings to floats
    benignXY[0] = [float(string) for string in benignXY[0]]
    benignXY[1] = [float(string) for string in benignXY[1]]
    malignantXY[0] = [float(string) for string in malignantXY[0]]
    malignantXY[1] = [float(string) for string in malignantXY[1]]

    ## define mean values for x and y attribuets of both benign and malignant
    avBenignX = np.mean(benignXY[0])
    avBenignY = np.mean(benignXY[1])
    avMalignantX = np.mean(malignantXY[0])
    avMalignantY = np.mean(malignantXY[1])

    ## define max/ min for benign
    maxBenignX = max(benignXY[0])
    minBenignX = min(benignXY[0])
    maxBenignY = max(benignXY[1])
    minBenignY = min(benignXY[1])

    ## define max/ min for malignant
    maxMaligX = max(malignantXY[0])
    minMaligX = min(malignantXY[0])
    maxMaligY = max(malignantXY[1])
    minMaligY = min(malignantXY[1])

    ## if benign x and y attributes less than those for malignant,
    ## define p1, p2
    if (avBenignX < avMalignantX):
        if (avBenignY < avMalignantY):
            p1 = [maxBenignX, minMaligY]
            p2 = [minMaligX, maxBenignY]
        elif (avBenignY > avMalignantY):
            p1 = [minMaligX, minBenignY]
            p2 = [maxBenignX, maxMaligY]
    elif (avBenignX > avMalignantX):
        if (avBenignY > avMalignantY):
            p1 = [minBenignX, maxMaligY]
            p2 = [maxMaligX, minBenignY]
        elif (avBenignY < avMalignantY):
            p1 = [minBenignX, minMaligY]
            p2 = [maxMaligX, maxBenignY]

    ## define slope of p1, p2
    m = slope(p1,p2)

    ## define yint from slope, p1
    yint = yInt(m,p1)

    ## define xint from slope, yint
    xint = xInt(m,yint[1])

    ## return x and y intercepts
    return [xint,yint]

def slope(p1,p2):
    """input two points with which you would like to calculate slope"""
    return (p2[1] - p1[1])/(p2[0] - p1[0])
    
def yInt(m,p1):
    """Input a slope and a point with which you would like to calculate
        the y-intercept"""
    return [0,(p1[1] - (m*p1[0]))]

def xInt(m,b):
    """Input a slope and a y-intercept with which you would like to calculate
        the x-intercept"""
    return [((b*-1)/m),0]
