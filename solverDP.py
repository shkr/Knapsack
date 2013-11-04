#!/usr/bin/python
# -*- coding: utf-8 -*-

def solveIt(inputData):
   
    # parse the input
    lines = inputData.split('\n')

    firstLine = lines[0].split()
   
    items = int(firstLine[0])
    capacity = int(firstLine[1])

    values = []
    weights = []
    values.append(0)
    weights.append(0)
    
    for i in range(1, items+1):
        line = lines[i]
        parts = line.split()

        values.append(int(parts[0]))
        weights.append(int(parts[1]))

    #Use dynamic programming 

    KN=[]

    for i in range(0, capacity+1):
        KN.append([])
        for j in range(0, items+1):
            KN[i].append([])
            if(i==0 or j==0):
                KN[i][j]=0;
            else:
                if( (i<weights[j])or ( KN[i][j-1]>(KN[i-weights[j]][j-1]+values[j]) ) ):
                    KN[i][j]=KN[i][j-1]
                else:
                    KN[i][j]=(KN[i-weights[j]][j-1]+values[j])
            

    value = KN[capacity][items]
    
    #Do Backtracking
    taken = []
    
    ptr=[capacity,items]
    while (ptr[1]>0):
        if( (KN[ptr[0]][ptr[1]]-KN[ptr[0]][ptr[1]-1]) == 0):
             taken.append(0)
             ptr[1]-=1
        else:
          taken.append(1)
          ptr[0]-=weights[ptr[1]]
          ptr[1]-=1
          

    # prepare the solution in the specified output format
    outputData = str(value) + ' ' + str(0) + '\n'
    outputData += ' '.join(map(str, list(reversed(taken))))
    return outputData


import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        fileLocation = sys.argv[1].strip()
        inputDataFile = open(fileLocation, 'r')
        inputData = ''.join(inputDataFile.readlines())
        inputDataFile.close()
        print solveIt(inputData)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)'

