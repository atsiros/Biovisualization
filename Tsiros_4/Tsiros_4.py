## Alyssa Tsiros
## Project 4
## 26 February, 2015

import numpy as np
from graphics import *

def display(sq1,sq2,scMatch,scMismatch,scGap):
    '''Input two sequences for alignment traceback, and scores for match, mismatch,
        and gaps, respectively.'''

    ## Assigning variables to text strings
    var = traceback(sq1,sq2,scMatch,scMismatch,scGap)
    alSq1 = var[0]
    alSq2 = var[1]
    mString = var[2]
    score = 'SCORE = ' + str(var[3])
    perLap = 'Overlap = ' + str((float(var[3])/len(alSq1))*100) + '%'

    ## Set-up display
    win = GraphWin('Sequence Alignment',1000,300)
    win.setBackground('black')

    ## Place text strings in display
    txt1 = Text(Point(500,190),alSq1)
    txt2 = Text(Point(500,210),alSq2)
    mtxt = Text(Point(500,200),mString)
    stxt = Text(Point(500,75),score)
    ptxt = Text(Point(500,125),perLap)

    ## Set text color to white
    txt1.setTextColor('white')
    txt2.setTextColor('white')
    mtxt.setTextColor('white')
    stxt.setTextColor('white')
    ptxt.setTextColor('white')

    ## Set alignment size to 9pt and score/ percent overlap size to 18pt
    txt1.setSize(9)
    txt2.setSize(9)
    mtxt.setSize(9)
    stxt.setSize(18)
    ptxt.setSize(18)

    ## Set font to FIXED-WIDTH font courier
    txt1.setFace('courier')
    txt2.setFace('courier')
    mtxt.setFace('courier')
    stxt.setFace('courier')
    ptxt.setFace('courier')

    ## Draw alignment, score, and percent overlap into display
    txt1.draw(win)
    txt2.draw(win)
    mtxt.draw(win)
    stxt.draw(win)
    ptxt.draw(win)

    ## Close display after pressing anywhere within the display
    win.getMouse()
    win.close()

def traceback(sq1,sq2,scMatch,scMismatch,scGap):
    '''Input two sequences for alignment traceback, and scores for match, mismatch,
        and gaps, respectively.'''

    ## Assign traceback and path matrix and initialize alignment arrays
    tbMatrix = fill(sq1,sq2,scMatch,scMismatch,scGap)[0]
    path = fill(sq1,sq2,scMatch,scMismatch,scGap)[1]
    alignment1 = []
    alignment2 = []

    ## Initialize values for i and j
    i = len(tbMatrix)-1
    j = len(tbMatrix[0])-1

    ## Traceback algorithm
    while (i >= 0):
        maxPenVal = max(tbMatrix[i])
        while (j >= 0):
            if (tbMatrix[i][j] == maxPenVal):
                ipair = i
                jpair = j
                alignment1 = []
                alignment2 = []
                while(1):
                    if (ipair == 0 and jpair == 0):
                        break
                    if (path[ipair][jpair] == 'M'):
                        alignment1.append(sq1[ipair-1])
                        alignment2.append(sq2[jpair-1])
                        ipair -= 1
                        jpair -= 1
                    elif (path[ipair][jpair] == '-'):
                        alignment1.append('-')
                        alignment2.append(sq2[jpair-1])
                        jpair -= 1
                    elif (path[ipair][jpair] == '|'):
                        alignment1.append(sq1[ipair-1])
                        alignment2.append('-')
                        ipair -= 1
                    elif (path[ipair][jpair] == 'N'):
                        if (ipair > 0):
                            alignment1.append(sq1[ipair-1])
                            ipair -= 1
                        if (jpair > 0):
                            alignment2.append(sq2[jpair-1])
                            jpair -= 1

            j -= 1
        i -= 1

    ## Reverse sequence list and join into string
    alSq1 = ''.join(list(reversed(alignment1)))
    alSq2 = ''.join(list(reversed(alignment2)))

    ## Initialize score and match string to be displayed between alignments
    score = 0
    mString = ''

    ## Add 1 to score upon match
    for i in range(len(alSq1)):
        if (alSq1[i] == alSq2[i]):
            score += 1

    ## Add '|' to mString upon match and '.' upon mismatch or gap.
    for i in range(len(alSq1)):
        if (alSq1[i] == alSq2[i]):
            mString = mString + '|'
        else:
            mString = mString + '.'

    return(alSq1,alSq2,mString,score)
    

def fill(sq1,sq2,scMatch,scMismatch,scGap):
    '''Input two sequences for alignment, and scores for match, mismatch, and
        gaps, respectively.'''

    ## Assign fillMatrix and mMatrix
    fillMatrix = initialize(len(sq1),len(sq2))[0]
    mMatrix = initialize(len(sq1),len(sq2))[1]

    ## Fill matrix algorithm
    for i in range(1,len(sq1)+1):
        for j in range(1,len(sq2)+1):
            if (sq1[i-1] == sq2[j-1]):
                preceding = [fillMatrix[i-1][j-1]+scMatch,
                            fillMatrix[i][j-1]+scGap,
                            fillMatrix[i-1][j]+scGap]
            else:
                preceding = [fillMatrix[i-1][j-1]+scGap,
                            fillMatrix[i][j-1]+scGap,
                            fillMatrix[i-1][j]+scGap]
                
            fillMatrix[i][j] = max(preceding)
            
            if (fillMatrix[i][j] == preceding[0]):
                mMatrix[i][j] = 'M'
            elif (fillMatrix[i][j] == preceding[1]):
                mMatrix[i][j] = '-'
            elif (fillMatrix[i][j] == preceding[2]):
                mMatrix[i][j] = '|'

    return (fillMatrix,mMatrix)
                

def initialize(m,n):
    '''Fill a matrix of size m by n with zeros.'''

    ## Initialize fill matrix with zeros
    iMatrix = np.zeros((m+1,n+1))

    ## Initialize match matrix with 'N's
    mMatrix = []

    for i in range(m+1):
        mMatrix.append(['N']*(n+1))

    return (iMatrix,mMatrix)
