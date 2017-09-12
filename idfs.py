from dirtgenerator import generatedirt

class mystate:
    def __init__(self,dirtylist,row,col):
        self.dirtylist=dirtylist
        self.row=row
        self.col=col
    def __repr__(self):
        return "Row :%s Coloumn :%s List:%s"%(self.row,self.col,self.dirtylist)
 
    def __str__(self):
        return "Row :%s Coloumn :%s List:%s"%(self.row,self.col,self.dirtylist)
    
    def __eq__(self,other):
        return self.__dict__==other.__dict__
    
    def __hash__(self):
        return hash(self.__repr__())


class node:
    def __init__(self,state,parent,action,matrixsize,depth):
        self.state = state
        self.parent=parent
        self.action=action
        self.depth = depth

    def __repr__(self):
        return str(self.state)
 
    def __str__(self):
        return self.state

    def check(self,action,matrixsize):
        if action == "up" and self.state.row>0:
            return True
        elif action == "down" and self.state.row<matrixsize-1:
            return True
        elif action == "left" and self.state.col>0:
            return True
        elif action == "right" and self.state.col<matrixsize-1:
            return True
        elif action == "suck" and (self.state.row,self.state.col) in self.state.dirtylist :
            return True
        else:
            return False

    def do(self,action):
        if action == "up":
            return mystate(self.state.dirtylist,self.state.row-1,self.state.col)
        elif action=="down":
            return mystate(self.state.dirtylist,self.state.row+1,self.state.col)
        elif action =="left":
            return mystate(self.state.dirtylist,self.state.row,self.state.col-1)
        elif action=="right":
            return mystate(self.state.dirtylist,self.state.row,self.state.col+1)
        elif action=="suck":
            ind=self.state.dirtylist.index((self.state.row,self.state.col))
            return mystate(self.state.dirtylist[:ind]+self.state.dirtylist[ind+1:],self.state.row,self.state.col)

    def cost(self,action):
        if action == "suck":
            return 1
        else:
            return 2

def checksol(node,finalstates):
    if node.state in finalstates:
        return True
    else:
        return False

def solution(node,finalstates,matrixsize):
    solarr=[]
    cost = 0
    end= (node.state.row,node.state.col)
    while node.parent!=None:
        solarr.append(node.action)
        cost+=node.cost(node.action)
        node=node.parent
    solarr= list(reversed(solarr))
    begin=(node.state.row,node.state.col)
    return (begin,end,solarr,cost)

def dls(initialstates,finalstates,matrixsize,depth):
    actions=["left","right","up","down"]
    stack=[]
    explored=set()
    k=0
    z=0
    for i in initialstates:
        curnode = node(i,None,None,matrixsize,0)
        if checksol(curnode,finalstates):
            return solution(curnode,finalstates,matrixsize)
        stack.append(curnode)
        explored.add(i)
    while len(stack)>0 :
        k+=1
        if(k%100000==0):
            k=0
            z+=1
            print z
        curnode = stack.pop()
        # print explored
        # print curnode.state
        act="suck"
        if curnode.check(act,matrixsize):
            # print act
            childnode=node(curnode.do(act),curnode,act,matrixsize,curnode.depth+1)
            # print childnode.state
            # print explored
            # print childnode.state in explored
            if checksol(childnode,finalstates):
                return solution(childnode,finalstates,matrixsize)
            elif childnode.state in explored:
                continue
            else :
                if (childnode.depth<depth):
                    stack.append(childnode)
                    explored.add(childnode.state)
        else :
            for act in actions:
                # print act
                if curnode.check(act,matrixsize):
                    childnode=node(curnode.do(act),curnode,act,matrixsize,curnode.depth+1)
                    
                    if checksol(childnode,finalstates):
                        return solution(childnode,finalstates,matrixsize)
                    elif childnode.state in explored:
                        continue  
                    else :
                        if (childnode.depth<depth):
                            stack.append(childnode)
                            explored.add(childnode.state)  
    return None

def idfs(initialstates,finalstates,matrixsize):
    depth = 1#2*len(initialstates[0].dirtylist)-1
    while(True):
        print ("depth : %s"%(depth))
        result=dls(initialstates,finalstates,matrixsize,depth)
        if (result!=None):
            return result
        depth+=1

def getdirtylist(board,matrixsize):
    dirty=[]
    for i in range(matrixsize):
        for j in range(matrixsize):
            if board[i][j]==1:
                dirty.append((i,j))
    return dirty 

def doeverything(board,matrixsize):
    dirty=getdirtylist(board,matrixsize)
    initialstates=[mystate(dirty,0,0),mystate(dirty,matrixsize-1,0),mystate(dirty,0,matrixsize-1),mystate(dirty,matrixsize-1,matrixsize-1)]
    finalstates=[mystate([],0,0),mystate([],matrixsize-1,0),mystate([],0,matrixsize-1),mystate([],matrixsize-1,matrixsize-1)]
    return idfs(initialstates,finalstates,matrixsize)


if __name__=="__main__":
    matrixsize=3
    board=generatedirt(matrixsize)
    print doeverything(board,matrixsize)