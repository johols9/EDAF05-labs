import sys
import fileinput
import time

# --PARSE INPUT-- #
input_data = [int(x) for line in fileinput.input() for x in line.split(' ')] #collects all input into one array
N = input_data[0]
pref_data = [input_data[i:i+N+1] for i in range(1,len(input_data), N+1)] #array of all pref list one sub array for each person

women_pref_list = {} # dict for storing womens pref, women nr 1 pref list at key 1 
men_pref_list = {}

for pref_list in pref_data: #go trough each pref list
    person_id = int(pref_list[0]) #the first token is the id of the person
    if person_id not in women_pref_list: # i nr1 is woman i nr2 is man
        women_pref_list[person_id] = [None]*N #initiliaze her pref list with space for N men
        position = 1 #keeps track of which rank the current man in her pref list has, see below
        for man in pref_list[1:]: 
           women_pref_list[person_id][man-1] = position # women store preflist by the mans ranking
           position += 1
    else: men_pref_list[person_id] = [x for x in pref_list[1:]] #men store their preflist by most popular
# -- PARSING DONE -- #

time_alg = time.time()
#-- Algorithm -- #
single_men = [m for m in range(1,N+1)] #All the single men
pairs = {} #All pairs
while single_men:  #while there still are single men
    m = single_men.pop() #take out the first man 
    w = men_pref_list[m].pop(0) #the woman m prefers most and has not yet proposed to
    if w not in pairs:
        pairs[w] = m 
    elif women_pref_list[w][m-1] < women_pref_list[w][pairs[w]-1]:
        w_ex = pairs[w]
        pairs[w] = m
        single_men.append(w_ex)
    else:
        single_men.append(m)

end_algo_time = time.time()

#PRINT RESULT
for i in range(1,N+1):
    print(pairs[i])
#print("algotime = " + str(end_algo_time-time_alg))