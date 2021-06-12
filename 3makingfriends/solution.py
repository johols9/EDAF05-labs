import fileinput 
import time 
from queue import PriorityQueue 

start_time = time.time() #udes for time testing

#parse input
f_input = fileinput.input()
first_line = next(f_input).split()
M = int(first_line.pop()) #nbr of pairs predicted to make friends
N = int(first_line.pop()) #nbr of people at event

#initiate graph
graph = [[] for i in range(N)]        

def add_edge(u,v,w): #adds node to graph 
    global graph
    graph[u].append((w,v)) #saves weight, w and the neigbour node v
    graph[v].append((w,u))


for line in f_input: #parse rest of input
    A = line.split()
    u = int(A[0])-1 #vertice 1
    v = int(A[1])-1 #vertice 2
    w = int(A[2]) #weight
    add_edge(u,v,w)



 
def prim(G,r):
    total_weight = 0 
    visited = [False for x in range(N)] #visisted nodes
    visited[r] = True #starting node has been visited
    pq = PriorityQueue() 
    for w,v in G[r]:
        pq.put((w,r,v)) #adds all neighbours weight, from, to
    while not pq.empty(): 
        (edge_w, edge_from, edge_to) = pq.get() #closest node
        if not visited[edge_to]:
            total_weight += edge_w
            visited[edge_to] = True
            for w,v in G[edge_to]:
                if not visited[v]: #only need to add the edge if the node isnt visited (then its already in pq)
                    pq.put((w,edge_to,v))
    print(total_weight)

algo_time = time.time()
prim(graph,0)
end_time = time.time()

                
def test_time_complexity():
    print("Time test")
    print("input size, N " + str(N))
    print("Total time: " + str(end_time-start_time))
    print("Algo time: " + str(end_time-algo_time))

#test_time_complexity()
