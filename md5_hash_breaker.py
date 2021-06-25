#!/usr/bin/env python3
import sys
def hash_func(sys.argv):
    import hashlib
    #for i in range(1,4096): #SHA-512
    for i in range(100,10000) #md5
        #i=hex(i).lstrip("0x") #SHA-512
        #i=str(i).strip() #md5
        #base_hash="FS{hash-I_had_corned_beef_and_hash_"+i.upper()+"}" #SHA-512
        #base_hash="FS{cabbage-wait_that's_not_right_"+i+"}" #md5
        #hashed = hashlib.sha512(base_hash.encode()) #SHA-512
        #hashed = hashlib.md5(base_hash.encode()) #md5
        comparison=str(hashed.hexdigest())
        #hash_value="a497453fe1eee3e0c4d44f2a74a1518744d247a1c6dd6c902a2b3367987f0e5d21fb1cbdd1af55ea78098be5a336ffaf06f19b8e5a5997e06d20ce00f9907424" #SHA-512
        #hash_value="70dad256878571774efef5fb41661ef1" #md5
        hash_value="6859e1d10d08c1ea91f6e53ba6d601149b08d4efab8f8c2d586f6858ae1773a7"
        if comparison==hash_value:
            print(base_hash)
            break
        value+=1
hash_func()



def class_hash_func():
    import hashlib
    #base_hash="104 101 108 108 111 32 119 111 114 108 100"
    base_hash="hello world"
    hashed = hashlib.md5(base_hash.encode()).hexdigest() #md5
    print(hashed)

#class_hash_func()   

    #ascii: 211115be76def8336b87120df8b5395b
    #"hello world": 5eb63bbbe01eeed093cb22bb8f5acdc3