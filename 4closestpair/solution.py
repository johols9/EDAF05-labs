import fileinput
import math
import time

start_time = time.time() #used for time testing

##PARSING###
f_input = fileinput.input()
N = int(next(f_input))
points = [ 0 ]*N

for i in range(N):
    A = next(f_input).split()
    points[i] = (int(A[0]), int(A[1])) 
##PARSING DONE###

def distance(p1,p2):
     return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def base_case(P,n):
    if n == 3:
        p1 = P[0]
        p2 = P[1]
        p3 = P[2]   
        dist12 = distance(p1,p2)
        dist13 = distance(p1,p3)
        dist23 = distance(p2,p3)
        return min(dist12,dist13,dist23)
    elif n == 2: 
        p1 = P[0]
        p2 = P[1]
        return distance(p1,p2)
    

def closest(P_x,P_y,n): #px sorted on x, n list length
    if n <= 3:
        return base_case(P_x,n)
    L_x = P_x[:n//2] #all points on left side
    R_x = P_x[n//2:]
    mid_point = L_x[-1] #mid point in x direction, used to find y   
    L_y = [None]*len(L_x)
    R_y = [None]*len(R_x)  
    ctr_left = 0
    ctr_right = 0
    for p in P_y: #O(n) #builds L_y and R_y so the same points are used as in L_x and R_x
        if p <= mid_point:
            L_y[ctr_left] = p
            ctr_left +=1
        else:
            R_y[ctr_right] = p
            ctr_right +=1
    min_left = closest(L_x,L_y, len(L_x)) 
    min_right = closest(R_x,R_y,len(R_x))
    delta = min(min_left,min_right)
    line_x = L_x[-1][0]
    S_y = [p for p in P_y if abs(p[0]-line_x) < delta] #O(n)
    for i in range(len(S_y)): #O(n) worst case
        for j in range(i+1,min(len(S_y),i+15)):
            temp_distance = distance(S_y[i],S_y[j])
            if temp_distance < delta:
                delta = temp_distance
          

    return delta
    
    
algo_time = time.time() #time testing

def closest_points(P,n):
    P_x = sorted(P) #sortes on x and on y if two points same x value,  O(nlogn)
    P_y = sorted(P, key=lambda point: point[1]) #sorts on y
    delta = closest(P_x,P_y,n)
    return delta


delta = closest_points(points,N)
print("{:.6f}".format(delta))

end_time = time.time() # time testing

def test_time_complexity():
    print("Time test")
    print("input size, N " + str(N))
    print("Total time: " + str(end_time-start_time))
    print("Algo time: " + str(end_time-algo_time))

#test_time_complexity()