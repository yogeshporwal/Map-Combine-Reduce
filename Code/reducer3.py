'''
    Name : Yogesh Porwal
    Roll No : 20CS60R52
    Email Id:yogeshporwal@kgpian.iitkgp.ac.in
    File name : reducer3.py
    command for run: make
'''

import sys

#curr_user1 and curr_user2 denote the current users being processed
curr_i=-1
curr_j=-1
prev_k=-1
last_val=-1

#keep the current count of the triangles for the current pair of users
curr_result=0

'''
input came from STDIN(standard input) will be processed here,STDIN will currently be having sorted output from mapper3.py
'''
for line in sys.stdin:

    #removing leading and trailing whitespaces 
    line = line.strip()

    #split the line into words using alphabet 'y' as a splitter
    i,j,k,val=line.split('y')

    #converting received variables into integer from the string
    try:
        i = int(i)
        j = int(j)
        k = int(k)
        val = int(val)

    except ValueError:
        continue

    #calculating values for diagonals only  
    if i!=j:
        continue

     #doing matrix multipication using key-value pairs received from mapper3.py
    if curr_i==i and curr_j==j:
        if prev_k==k and last_val!=-1:
            curr_result+=val*last_val
            last_val=-1
        else:
            prev_k=k
            last_val=val
    else:
        if curr_i!=-1 and curr_j!=-1:
            #printing user1,user2 and #trianglles going through them in friends.txt
            #As it is directed graph so dividing result by 2
            print("%s,%s" % (curr_i,int(curr_result/2)))
        
        curr_i=i
        curr_j=j
        curr_result=0
        prev_k=k
        last_val=val

#for the last remaining diagonal
if curr_i!=-1 and curr_j!=-1:
    
    print("%s,%s" % (curr_i,int(curr_result/2)))
    