#!/usr/bin/env python

import hashlib
import time

open('output3.txt', 'w').close()    #removes data from previous runs
open('output5.txt', 'w').close()
start_time = time.time()

filter1 = []
filter2 = []
for i in range(3000000):
    filter1.append(0)
    filter2.append(0)
  

with open('dictionary.txt') as f:
    #next(f)
    count = 0
    for line in f:
        line.strip('\n')            #strip newlines
        hash1 = hashlib.md5(line.encode())      #3 hashes for first filter
        hash2 = hashlib.sha256(line.encode())   #need to encode to get proper hash
        hash3 = hashlib.sha1(line.encode())
        hash4 = hash(line)                      #default python hash function
        hash5 = hashlib.blake2b(line.encode())

        pos = int(hash1.hexdigest(), 16)        #setting bits in both filters
        pos = pos % 3000000
        filter1[pos] = 1
        filter2[pos] = 1
        
        pos = int(hash2.hexdigest(), 16)
        pos = pos % 3000000
        filter1[pos] = 1
        filter2[pos] = 1
        
        pos = int(hash3.hexdigest(), 16)
        pos = pos % 3000000
        filter1[pos] = 1
        filter2[pos] = 1

        pos = hash4 % 3000000
        filter2[pos] = 1

        pos = int(hash5.hexdigest(), 16)
        pos = pos % 3000000
        filter2[pos] = 1
        
    #out = open('test.txt', 'w')
    #out.write(str(filter1))
    print("--- %s seconds ---" % (time.time() - start_time))

#Bloom filters have been created, now to compare sample input

with open('sample_input.txt') as f:
    next(f)                         #need to skip first line
    for line in f:
        line.strip('\n')            #strip newlines and hash to compare
        hash1 = hashlib.md5(line.encode())      
        hash2 = hashlib.sha256(line.encode())   
        hash3 = hashlib.sha1(line.encode())
        hash4 = hash(line)
        hash5 = hashlib.blake2b(line.encode())

        pos1 = int(hash1.hexdigest(), 16)
        pos1 = pos1 % 3000000
        
        pos2 = int(hash2.hexdigest(), 16)
        pos2 = pos2 % 3000000

        pos3 = int(hash3.hexdigest(), 16)
        pos3 = pos3 % 3000000
        out = open('output3.txt', 'a')  #check first filter, write result
        
        if filter1[pos1] == 1 or filter1[pos2] == 1 or filter1[pos3] == 1:
            out.write('maybe\n')
        else:
            out.write('no\n')
        out.close()


        pos4 = hash4 % 3000000      #additional hashes for filter 2

        pos5 = int(hash5.hexdigest(), 16)
        pos5 = pos5 % 3000000

        out = open('output5.txt', 'a')  #check second filter, write result
        
        if filter2[pos1] == 1 or filter2[pos2] == 1 or filter2[pos3] == 1 or filter2[pos4] == 1 or filter2[pos5] == 1:
            out.write('maybe\n')
        else:
            out.write('no\n')
        out.close()
        
    print("--- %s seconds ---" % (time.time() - start_time))
    
