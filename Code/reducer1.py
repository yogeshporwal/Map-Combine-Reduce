'''
    Name : Yogesh Porwal
    Roll No : 20CS60R52
    Email Id:yogeshporwal@kgpian.iitkgp.ac.in
    File name : reducer1.py
    command for run: make
'''

import sys

#curr_user1 and curr_user2 denote the current users being processed
curr_user1=curr_user2=None

#keep the chat session count of the current pair of users
curr_session_count=0

'''
input came from STDIN(standard input) will be processed here,STDIN will currently be having sorted output from combiner1.py
'''
for line in sys.stdin:

    #removing leading and trailing whitespaces 
    line = line.strip()

    if len(line)==0:
        continue
    
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

            #writing user1,user2 to STDOUT if they had chatted atleast 30 times in 10 days
            if curr_session_count>=30:
                print('%s,%s' % (curr_user1,curr_user2))

            curr_user1=user1
            curr_user2=user2
            curr_session_count=count

    else:
        curr_user1=user1
        curr_user2=user2
        curr_session_count=count

#for the last pair of users 
if curr_user1 and curr_user2:
    if curr_session_count>=30:
                print('%s,%s' % (curr_user1,curr_user2))