import random
import time


# Pseudo random generation
def pseudo_LCG(seed,a,c,modulus):
    numbers = [seed]
    count = 0
    while True:
        number = (a*seed + c) % modulus
        seed = number
        count+=1
        print(number)
        if(number in numbers):
            break
        else:
            numbers.append(number)
    print(count, " distinct numbers")
        
    
#true random using time    
def true_LCG(seed,a,c,modulus):
    numbers = [seed]
    count = 0
    while True:
        number = (a*seed + c) % modulus
        seed = number
        count+=1
        print(number)
        if(number in numbers):
            break
        else:
            numbers.append(number)
    print(count, " distinct numbers")
    
    
input_seed = random.randint(1, 100)
input_a = 1103515245
input_c = 0
input_modulus = 2**32

pseudo_LCG(input_seed, input_a, input_c, input_modulus)                        
true_LCG(time.time(), input_a, input_c, input_modulus)                        
                        
                        