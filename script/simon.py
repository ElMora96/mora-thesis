#SCRIPT FOR GENERATING SIMON CYPHERTEXTS
#import numpy as np
import random 

#reproducibility of output
random.seed(13)

BLOCK_SIZE = 32
KEY_SIZE = 64

# Function to create the 
# random binary string 
def rand_string(p): 
    
    # Variable to store the  
    # string 
    key1 = "" 
  
    # Loop to find the string 
    # of desired length 
    for i in range(p): 
          
        # randint function to generate 
        # 0, 1 randomly and converting  
        # the result into str 
        temp = str(random.randint(0, 1)) 
  
        # Concatenatin the random 0, 1 
        # to the final result 
        key1 += temp 
          
    return(key1) 

#key list
keys = []
for i in range(0,5):
	keys.append(rand_string(KEY_SIZE))


#plaintext list
plaintexts = []
for i in range(0,10):
	plaintexts.append(rand_string(BLOCK_SIZE))


print(plaintexts)

#cyphertext list
#cyphertexts = []
'''for i in range(0,5):
	my_cypher = simon.SimonCipher(keys[i], block_size = BLOCK_SIZE, key_size = KEY_SIZE )
	cyphertexts.append(my_cypher(plaintexts[i]))'''

