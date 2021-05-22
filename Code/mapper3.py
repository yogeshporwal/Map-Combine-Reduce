'''
    Name : Yogesh Porwal
    Roll No : 20CS60R52
    Email Id:yogeshporwal@kgpian.iitkgp.ac.in
    File name : mapper3.py
    command for run: make
'''

import sys

#taking filename(network file) as 1st command line argument and opening it
file_ptr=open(sys.argv[1])

for line in file_ptr:
    #removing leading and trailing whitespaces 
    line = line.strip()

    if len(line)==0:
        continue

    #split the line into words separated by ','
    user=line.split(',')
    i=user[0]
    j=user[1]

    '''
    for matrix multipication we will send key-value(k-v) pairs to reducer3.py in following format:
        Matrix A (k, v)=((i, k), (j, Aij)) for all k ,in our case k is from 0 to 299

    '''
    for k in range(300):
        #if network.txt has current pair (a,b) then:

        #for (a,b) in matrix A
       print("%sy%sy%sy%s" %(i,k,j,1))

       if i!=j:
           #for (b,a) in matrix A when a!=b
            print("%sy%sy%sy%s" % (j,k,i,1))
        
#closing the file network.txt
file_ptr.close()

#taking filename(friends file) as second command line argument and opening it
file_ptr=open(sys.argv[2])

for line in file_ptr:

    #removing leading and trailing whitespaces 
    line = line.strip()

    if len(line)==0:
        continue

    #split the line into words separated by ','
    user=line.split(',')
    i=user[0]
    j=user[1]
    count=user[2]

    '''
    for matrix multipication we will send key-value(k-v) pairs to reducer1.py in following format:
        Matrix B (k, v)=((i, k), (j, Bjk)) for all i ,in our case i is from 0 to 299

    '''
    for k in range(300):
        #if friends.txt has current entry (a,b,mutual friends) then:

        #for (a,b) in matrix B
        print("%sy%sy%sy%s" % (k,j,i,count))

        if i!=j:
            #for (b,a) in matrix B when a!=b
            print("%sy%sy%sy%s" % (k,i,j,count))

#closing the file friends.txt
file_ptr.close()