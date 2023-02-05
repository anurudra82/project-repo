import math
from random import *
 

def gen_OTP() :

    
#     digits = "0123456789"
    OTP = ""
 
   
    print("your 6 digit otp: ",end="")
    for i in range(6) :
        OTP = str(randint(0,9)) + OTP

    
        
      
        
        
        # OTP = digit[math.floor(random.random()*10] + OTP
 
    return OTP
     
print(gen_OTP())
