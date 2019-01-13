import copy
import numpy as np
import time
class Node(object):
    def __init__(self):
        self.parent = None
        self.children = []
        self.question=None 
        self.state =None
 
    def add_child(self, node):
        self.children.append(node)
        node.parent = self
    def __repr__(self):
        pass
        return "Node: {}, Q: {}, children:{}, state:\n {}".format(
            hash(self), self.question, self.children,self.state)
def check(x,y,s):
    p=''
    for i in range(9):
        p+=s[i][y]+s[x][i]
    l,m=x//3,y//3
    l,m=l*3,m*3
    #print(l,m)
    for i in range(3):
        for j in range(3):
            p+=s[l+i][m+j]
    
    return set(p.replace('0',''))
def eva(q,s):#找到最好解的点，先解决
    global a
    k={}
    for  i in q:
        k[i]=len(a-check(i[0],i[1],s))
    w=()
    for i,j in k.items():
        if j==min(k.values()):
            w=i
    return w
def expand(node):
    if len(node.question)>0:
        current_node=node
        q=eva(current_node.question,current_node.state)#先算最好算的点（可能性最低的点）
        x,y=q[0],q[1]
        print(x,y)
        p=a-check(x,y,current_node.state)
        for i in list(p):
            n=Node()
            n.state=copy.deepcopy(current_node.state)
            n.question=copy.deepcopy(current_node.question)
            n.state[x][y]=i
            n.question.remove((x,y))
            current_node.add_child(n)
        for i in current_node.children:
            current_node=i
            expand(current_node)
    else:
        print(node.state)
        print('Done!')
def solve(sheet):
    global a
    p=[]
    for i in sheet.split():
        p+=list(i)
    S=np.array(p).reshape(9,9)
    a=set([str(i) for i in range(1,10)])
    d=[]
    for i in range(9):
        for j in range(9):
            if S[i][j]=='0':
                d.append((i,j))
    init_state=copy.deepcopy(S)
    init_question=copy.deepcopy(d)
    init_node = Node()
    init_node.state = init_state
    init_node.question= init_question
    current_node = init_node
    expand(current_node)

if __name__='__main__':
  sheet='''
  302700009
  008000045
  004001300
  000059000
  090030060
  000260000
  001400200
  260000100
  400002503
  '''
  solve(sheet)
