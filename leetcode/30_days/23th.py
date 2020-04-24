# Bitwise And of Numbers Range

# Given a range [m, n] where 0 <= m <= n <= 2147483647, 
# Return the bitwise AND of all numbers in this range, inclusive.

m,n=5,7
#we have to find "5&6&7"

i = 0
    
# if it gets flip in between entire column will be zero
# All right columns are also flipped 

# Eg. 10 : 1010
#     11 : 1011
#     12 : 1100
#     13 : 1101
#     14 : 1110
#        : 1000

# Leftmost remains same in range

while m != n:
    m >>= 1
    n >>= 1
    i += 1
    
print (n << i)

# So our approach is:

# 16 : 10000
# 19 : 10011

# shift left from right bitwise till we get same
# we get that at 3rd from right

# 100 remains same during and operation
# so answer is (100)(00)