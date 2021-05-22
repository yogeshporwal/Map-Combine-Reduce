'''
    Name : Yogesh Porwal
    Roll No : 20CS60R52
    Email Id:yogeshporwal@kgpian.iitkgp.ac.in
    File name : mapper2.py
    command for run: make
'''
 
import sys

#taking filename(network file) as command line argument and opening it
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
    for matrix multipication we will send key-value(k-v) pairs to reducer1.py in following format:
        Matrix A (k, v)=((i, k), (j, Aij)) for all k ,in our case k is from 0 to 299
        Matrix B (k, v)=((i, k), (j, Bjk)) for all i ,in our case i is from 0 to 299

    '''
    for k in range(300):
        #if network.txt has current pair (a,b) then:

        #for (a,b) in matrix A
        print("%sy%sy%sy%s" %(i,k,j,1))

        #for (a,b) in matrix B(which is also basically A)
        print("%sy%sy%sy%s" % (k,j,i,1))

        #for (b,a) in matrix A
        print("%sy%sy%sy%s" % (j,k,i,1))

        #for (b,a) in matrix B(which is also basically A)
        print("%sy%sy%sy%s" % (k,i,j,1))

#closing the file
file_ptr.close()