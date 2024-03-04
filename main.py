"""
CMPS 2200  Assignment 2.
See assignment-02.pdf for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.
def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y



def subquadratic_multiply(x, y):
    ### TODO
   xvec = x.binary_vec
   yvec = y.binary_vec
   padnum = pad(xvec, yvec)
   xvec = padnum[0]
   yvec = padnum[1]

   if x.decimal_val <= 1 and y.decimal_val <= 1:
     return BinaryNumber(x.decimal_val*y.decimal_val)
   else:
     x_L = split_number(xvec)[0]
     x_R = split_number(xvec)[1]
     y_L = split_number(yvec)[0]
     y_R = split_number(yvec)[1]
     P1 = subquadratic_multiply(x_L, y_L)
     P2 = subquadratic_multiply(x_R, y_R)
     sum1 = BinaryNumber(x_L.decimal_val+ x_R.decimal_val)
     sum2= BinaryNumber(y_L.decimal_val + y_R.decimal_val)
     product = subquadratic_multiply(sum1, sum2)

     P3= BinaryNumber(product.decimal_val - P1.decimal_val - P2.decimal_val)

     shift1= bit_shift(P3, len(xvec)//2)
     shift2 = bit_shift(P1, len(xvec))
     result = shift1.decimal_val + shift2.decimal_val + P2.decimal_val

   return result






    


def time_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f
    f(x, y)
    return (time.time() - start)*1000

    
    

