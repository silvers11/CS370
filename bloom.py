#!/usr/bin/env python

import hashlib
import time

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
    #print(filter2)
        
    print("--- %s seconds ---" % (time.time() - start_time))
    
