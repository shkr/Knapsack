#!/usr/bin/python
# -*- coding: utf-8 -*-



def solveIt(inputData):
    # parse the input
    lines = inputData.split('\n')

    firstLine = lines[0].split()

    items = int(firstLine[0])
    global capacity
    capacity = int(firstLine[1])
    global values
    values = []
    global weights
    weights = []
    values.append(0)
    weights.append(0)
    
    for i in range(1, items+1):
        line = lines[i]
        parts = line.split()

        values.append(int(parts[0]))
        weights.append(int(parts[1]))

    global dst
    dst={}
    global lst
    for i in range(1,items+1):
        dst[str(i)]=float(values[i])/float(weights[i])
    
  
    dst=sorted(dst.items(), key=lambda x:x[1], reverse=True)
    lst=[]
    lst.append(0)
    for item in iter(dst):
        lst.append(int(item[0]))
   
    global bestnode
    bestnode = Node(0,0,0,[],[])
    
    #Branch and bound Method
    value=0
    room = capacity
    ptr= 0
  
    rootNode = Node(lst[ptr], capacity, 0, [],[])
    iterativepreorder(rootNode)
   
    taken=[]
    value=0
  
    for i in range(1,items+1):
        if i in bestnode.selected:
            taken.append(1)
           
            value+=values[i]
        else:
          
            taken.append(0)

    outputData = str(value) + ' ' + str(0) + '\n'
    outputData += ' '.join(map(str, list(taken)))
    return outputData

class Node:

    def __init__(self,ptr,room,value,selected,rmlist):
        self.ptr=ptr
        self.room=room
        self.value=value
        self.selected=selected
        self.rmlist=rmlist
        self.left=None
        self.right=None

def iterativepreorder(x):
    parent=[]
   
    while parent or x!=None:
       if x!=None and x.ptr<len(values)-1:
                parent.append(x)
                xleft=Node(x.ptr+1,x.room-weights[lst[x.ptr+1]],x.value+values[lst[x.ptr+1]],x.selected+[lst[x.ptr+1]],x.rmlist)
                if calc_room(xleft.room):
                      x=xleft
                      
                      visit(x)
                else:
                    x=None
       else:
            x=parent[len(parent)-1]
            parent.remove(x)
            
            xright=Node(x.ptr+1,x.room,x.value,x.selected,x.rmlist+[lst[x.ptr+1]])
           
            if calc_bound(xright.rmlist):
                x=xright
                
            else:
                x=None
def visit(x):
    global bestnode
    if (x.value>bestnode.value):
        bestnode=x
        
def calc_room(room):
    if(room<0):
        return False
    else:
        return True

def calc_bound(rmlist):
    fit=0
    best = 0
    for i in range(1,len(dst)+1):
        if (fit>capacity):
                 break
        if((not rmlist) or (not lst[i] in rmlist)):
            best+=float(values[lst[i]])
            fit+=weights[lst[i]]
            #if(fit>capacity):
                #best-=float(values[lst[i]])/float(weights[lst[i]])*(fit-capacity)
                #break
            
                  
    if(best>bestnode.value):
        return True
    else:
        return False

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

