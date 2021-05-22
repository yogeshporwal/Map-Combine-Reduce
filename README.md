# Map-Combine-Reduce

## Problem Description

This assignment is on map-combine-reduce, which is a distributed and scalable way of extracting/mining required information from multiple datasets stored on multiple servers. Map-reduce is common known pair but here we will also use/make combiners.In many real world scenarios, the mapper has to send too many key-value pairs, which then reach the Hadoop/MapReduce management system to be grouped and sorted. Having too many key-value pairs can become a bottleneck for the system. Instead if we introduce some form of grouping in the mapping phase itself, then the load on the whole system will be significantly reduced. So, we plan to use combiners (mini-reducers at local mapping level wherever possible) in the mapping phase before passing the key-value pairs to be shuffled and sorted.

### Dataset

We will be using a dataset on a Facebook (FB) network with only  300 users. The data contains 10 files containing logs of chat sessions from 1st Feb to 10th Feb 2021. You have to extract required information from this data. Below is a sample of data available in the file:

` ( day3.txt ) `
`   276,107 `
`    284,68 `
`    98,246 `
`    97,49 `
`    292,58 `
`    119,213 `
`    229,156  `

For example: each line in the file day3.txt represents a chat session between two users (node-ids separated by comma) on 3rd Feb 2021. Session logs appearing earlier represent earlier chat sessions and later logs represent later chat sessions.

### Tasks to be done:

The queries are to be implemented in the mapper (also combiners wherever asked) and reducer.You need to implement the following queries in this assignment:

1. **Finding the strongly connected network( mapper+combiner+reducer ):**

You have been given the dataset with logs of chat sessions between the users on FB. Rather than relying on the actual friendship network (as we used in the last assignment), this time, we want to find the strongly connected nodes using how many times a pair of nodes chatted in the 10 days. If a pair of nodes have chatted at least 30 times in the 10 days, then only you consider them to be strongly connected and have an edge in between them. Now find all such strongly connected pairs of nodes to create the chat network. As there are 10 different files, you will have to write mapper, combiner, and reducer routines. Save the network in “ **network.txt** ”.

(deliverables :  mapper1.py, combiner1.py, reducer1.py, network.txt )

2. **Finding the number of mutual friends:**

Here, you want to find out how many mutual friends each pair of nodes have in the chat network created in the last question. Write mapper and reducer routines. Save the results as <node-1,node-2,#mutualFriends> in“ **friends.txt** ”. 

( deliverables : mapper2.py, reducer2.py, friends.txt )

3. **Finding the number of triangles in the network :**

If there are edges like (  v1,v2 ) , ( v2 ,v3 ) , and (v3 ,v1 )  then it forms a triangle in the network. Here you have to find out the total number of triangles passing through each node. Write mapper and reducer routines for this, and save the results as <node,#trianglesThrough-node> in “**triangles.txt**”.

**(deliverables :  mapper3.py, reducer3.py, triangles.txt) **


## Instructions to run the code

- Open terminal in same folder and run this command :point_right: $ make
- To clean the ouput files run this command :point_right: $ make clean
 
