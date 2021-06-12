import fileinput
import time

start_time = time.time() #time testing


#PARSING#
f_input = fileinput.input()
L = next(f_input).split() #alphabet used to find index in cost_matrix 
L2 = {c:i for (i,c) in enumerate(L)} # c=char, i=index of char used later to find index faster
k = len(L)
cost_matrix = [[int(x) for x in next(f_input).split()] for i in range(k)] #cost matrix, stores gain of aligning A with B
Q = int(next(f_input))
queries = [next(f_input).split() for x in range(Q)] 
#PARSING DONE#



insert_cost = -4 

def make_align_matrix(str1,str2):
    str1_length = len(str1)+1 # str1_length is the dim of matrix
    str2_length = len(str2)+1
    A = [[None for c in range(str2_length)] for r in range(str1_length)] #stores opt(i,j) at A(i,j)
    A[0][0] = (0,-1) #first letter doesnt have a parent

    for i in range(1,str1_length): #initiate
        A[i][0] = (i*insert_cost,2)
    for j in range(1,str2_length):
        A[0][j] = (j*insert_cost,1)
    
    for i in range(1,str1_length):
        for j in range(1,str2_length):
            str1_c_index = L2[str1[i-1]]
            str2_c_index = L2[str2[j-1]]
            a = cost_matrix[str1_c_index][str2_c_index] + A[i-1][j-1][0]
            b = insert_cost + A[i][j-1][0] #str1 misses char
            c = insert_cost + A[i-1][j][0] #str2 misses char
            temp_v = [a,b,c]
            max_val = max(temp_v)
            A[i][j] = (max_val,temp_v.index(max_val)) 
    return A

def str_builder(str1,str2,A):
    s = str1
    t = str2
    i = len(s)
    j = len(t)

    parent = A[i][j][1]
    while parent != -1: 
        if parent == 0:
            i=i-1
            j=j-1
        elif parent == 1:
            s = s[:i] + "*" + s[i:] 
            j = j-1
        elif parent == 2:
            t = t[:j] + "*" + t[j:] 
            i = i-1
        parent = A[i][j][1]
        
    print( "".join(s) + " " + "".join(t))


algo_time = time.time()
for q in queries:
    s = q[0]
    t = q[1]
    A = make_align_matrix(s,t)
    str_builder(s,t,A)
end_time = time.time()   

def test_time_complexity():
    print("Time test")
    print("Total time: " + str(end_time-start_time))
    print("Algo time: " + str(end_time-algo_time))

#test_time_complexity()
