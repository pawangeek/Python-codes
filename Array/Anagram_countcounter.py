# Approach 
# (i)  We use a counter to count the occurance of letters in our given word
# (ii) We get the run the loop times len(text)-len(word)
# (iii) We match the counter of words from this loop and match with previous counter

from collections import Counter
p = int(input())

while p:
    t = input()
    w = input()

    s,lt,lw,cnt = Counter(w),len(t),len(w),0

    for i in range(lt-lw+1):
        word = t[i:i+lw]

        if s == Counter(word):
            cnt+=1

    print(cnt)
    p-=1