'''
    Name : Yogesh Porwal
    Roll No : 20CS60R52
    Email Id:yogeshporwal@kgpian.iitkgp.ac.in
    File name : combiner1.py
    command for run: make
'''

import sys

#curr_user1 and curr_user2 denote the current users being processed
curr_user1=None
curr_user2=None

#keep the chat session count of the current pair of users
curr_session_count=0

'''
input came from STDIN(standard input) will be processed here,STDIN will currently be having sorted output from mapper1.py
'''
for line in sys.stdin:

    #removing leading and trailing whitespaces 
    line = line.strip()

    #split the line into words 
    user1,user2,count=line.split('\t')

    #converting count to integer from the string
    try:
        count = int(count)
    except ValueError:
        continue

    if curr_user1 and curr_user2:

        #if this is the same user pair who is being processed from last iteration then just increase 
        # current session count by one
        if curr_user1==user1 and curr_user2==user2:
            curr_session_count+=count
        else:
            
            #writing user1,user2 with chat session count of day-x to STDOUT
            print('%s\t%s\t%s' %(curr_user1,curr_user2,curr_session_count))
            curr_user1=user1
            curr_user2=user2
            curr_session_count=count

    else:
        curr_user1=user1
        curr_user2=user2
        curr_session_count=count

#for the last pair of users 
if curr_user1 and curr_user2:
    print('%s\t%s\t%s' %(curr_user1,curr_user2,curr_session_count))
