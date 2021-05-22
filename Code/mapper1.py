'''
    Name : Yogesh Porwal
    Roll No : 20CS60R52
    Email Id:yogeshporwal@kgpian.iitkgp.ac.in
    File name : mapper1.py
    command for run: make
'''

import sys

#taking filename as command line argument and opening it
file_ptr=open(sys.argv[1])

for line in file_ptr:

    #removing leading and trailing whitespaces 
    line = line.strip()

    #split the line into words separated by ','
    user_id=line.split(',')
    

    if int(user_id[0])==int(user_id[1]):
        continue
        
    if int(user_id[0])<int(user_id[1]):
        print('%s\t%s\t%s' % (user_id[0],user_id[1],1))
    else:
        print('%s\t%s\t%s' % (user_id[1],user_id[0],1))
 
    #user[0] and user[1] both are chatted so it is being written to STDOUT that they have chatted in 1 new session

#closing the file
file_ptr.close()