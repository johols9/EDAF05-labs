import fileinput
from collections import deque

f_input = fileinput.input()
next_line = next(f_input).split()

N = int(next_line[0]) #nbr of nodes 
M = int(next_line[1]) #nbr of edges
C = int(next_line[2]) #nbr of students to transfer from node 0 to node N-1
P = int(next_line[3]) #nbr of routes to remove

class Node:
    def __init__(self,id):
        self.id = id
        self.visited = False 
        self.pred = None 
        self.edges = []
    def __repr__(self):
        return str(self.id)
    

class Edge:
    def __init__(self,u,v,c):
        self.node_from = u
        self.node_to = v
        self.capacity = c
        self.flow = 0
        self.oppositeEdge = None
    def __repr__(self):
        return (str(("n1", "n2", "c", "f")) + " = " + str((self.node_from,self.node_to,self.capacity, self.flow)))
        
    

nodes = [Node(x) for x in range(N)]
edges_in_graph = []

all_edges = [None]*M
for i in range(M): #parses and stores all edges
    next_line = next(f_input).split()
    u = nodes[int(next_line[0])]
    v = nodes[int(next_line[1])]
    c = int(next_line[2])
    edgeuv = Edge(u,v,c)
    edgevu = Edge(v,u,c)
    edgeuv.oppositeEdge = edgevu
    edgevu.oppositeEdge = edgeuv
    all_edges[i] = edgeuv


remove_list = [int(x) for x in f_input]

for i in range(M): #goes through edges and add those not in remove_list
    if i in remove_list:
        continue
    e = all_edges[i]
    u = e.node_from
    v = e.node_to
    c = e.capacity
    u.edges.append(e)
    v.edges.append(e.oppositeEdge)
    edges_in_graph.append(e) 

def get_edge(node_from,node_to): #O(E) worst case 
    neigbours = nodes[node_from.id].edges
    for e in neigbours:
        if e.node_to == node_to:
            return e
    return None

def ford_fulkerson():
    if len(nodes[0].edges) == 0 or len(nodes[-1].edges) == 0: #If these are not in the graph we do not have to continue
        return 0
    p = find_path() #O(E)
    while p != None: #while we have s-t walk  O(C*E). 
        delta = float('Inf')
        for e in p: 
            remaining = e.capacity - e.flow
            if remaining < delta:
                delta = remaining
        for e in p:
            e.flow+= delta
        p = find_path()
    max_flow = 0 
    for e in nodes[0].edges: #O(C)
        max_flow += e.flow
    return max_flow


#O(E+V) = O(E) 
def find_path(): # BFS search for a path between first and last node
    s = nodes[0]
    t = nodes[-1]
    for n in nodes:
        n.visited = False
        n.pred = None
    s.visited = True
    q = deque()
    q.append(s)
    while q:  
        v = q.popleft() 
        for e in v.edges: 
            w = e.node_to
            remaining = e.capacity - e.flow
            if w.visited or remaining <= 0 :
                continue
            w.visited = True
            q.append(w)
            w.pred = v
            if w == t:
                path = []
                n = w
                while n.id != 0: 
                    edge = get_edge(n.pred,n)
                    path.append(edge)
                    n = n.pred
                return path
    return None    

max_flow = ford_fulkerson()
counter = P-1

while max_flow < C: #goes through remove_list and adds edges one by one until max_flow > C
    new_e_index = remove_list[counter]
    e = all_edges[new_e_index]
    edges_in_graph.append(e)
    u = e.node_from
    v = e.node_to
    u.edges.append(e)
    v.edges.append(e.oppositeEdge)
    max_flow = ford_fulkerson() 
    counter-=1

print(counter+1, max_flow)
