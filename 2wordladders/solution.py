import fileinput
import time

start_time = time.time() #used for time-testing

raw_input = [x for line in fileinput.input() for x in line.split()]
N = int(raw_input.pop(0))
Q = int(raw_input.pop(0))
words = raw_input[0:N]
queries = [raw_input[i:i+2] for i in range(N,len(raw_input),2)]
nodes = {} 
graph = {} # key=word and value=neighbour list

class Node:
    def __init__(self,data):
        self.data = data
        self.visited = False
        self.pred = None


for word in words:
    nodes[word] = Node(word)

#checks for neighbours
def contain_letters(str, set):
    for c in set: 
        if c in str:
            str = str.replace(c,"",1)
    return len(str) == 1
    

#creates graph
for key1 in nodes: #key1 = first word
    graph[key1] = [] 
    for key2 in nodes:
        if contain_letters(key2,key1[1:]) and key1 != key2:
            graph[key1].append(nodes[key2]) #add key2 to key1 neighbour



algo_time = time.time()


def BFS(graph,s,t):
    if s.data == t.data: #special case if s and t are the same node
        print(0) 
        return
    for key in nodes: 
        nodes[key].visited = False
    s.visited = True
    q = [s] 
    while q:
        v = q.pop(0) #closest node
        for w in graph[v.data]: #check neighbours
            if not w.visited:
                w.visited = True
                q.append(w)
                w.pred = v
                if w == t:
                    path_length = 0
                    n = w
                    while n != s:
                        path_length+=1
                        n=n.pred
                    print(path_length)
                    return
    print("Impossible")

for q in range(Q):
    BFS(graph,nodes[queries[q][0]],nodes[queries[q][1]])


end_time = time.time()

def test_time_complexity(): #for time testing
    print("Time test")
    print("input size, N " + str(N))
    print("Total time: " + str(end_time-start_time))
    print("Algo time: " + str(end_time-algo_time))

#test_time_complexity()



def print_grannar():
    for key in graph:
        print("key: " + str(key) + " ,neigbourlist: ", end=" ")
        for i in graph[key]:
            if(i != None):
                print(i.data, end = " ")
        print()