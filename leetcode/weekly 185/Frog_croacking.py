# https://leetcode.com/problems/minimum-number-of-frogs-croaking/

# i) Going from left to right, in every step, number of "c", "r", "o", "a", "k" must be monotonically increasing otherwise we should return False
# ii) Any character other than "c", "r", "o", "a", "k" is considered invalid, prompting we return False
# iii) Outside the loop, we need to check c=r=o=a=k, to make sure there is not any number of extra "c" ,"r", "o", or "a" at the end
# iv) watermark is the the number of required Frogs (making sound simultaneously) we have seen so far. It is calculated based on the difference between number of encountered "c"

croakOfFrogs = "crcoakroak"

c = r = o = a = k = 0
watermark = 0
for ch in croakOfFrogs:
    if ch == 'c': 
        c += 1
        watermark = max(watermark, c - k)

    elif ch == 'r': 
        r += 1
    elif ch == 'o': 
        o += 1
    elif ch == 'a': 
        a += 1
    elif ch == 'k': 
        k += 1

    else: 
        print (-1)
    
    if not c >= r >= o >= a >= k:
        print(1)
        break
    else:
        if c == r == o == a == k:
            print(watermark)
        else 
            print(-1)