from collections import Counter

a = 'b'
b = 'd'

def check_ana(a,b):
    ar = Counter(a)

    for i in b:
        if i in ar:
            ar[i]-=1
        else:
            return False

    print(ar)

    sm = 0
    for k, v in ar.items():
        sm+=v

        if sm!=0:
            return False

    return True

print(check_ana(a,b))
print(True) if sorted(a)==sorted(b) else print(False)

def check_ana2(a, b):

    if len(a)!=len(b):
        return False
    
    count = [0 for i in range(26)]

    for i in range(len(a)):
        count[ord(str(a[i))-ord('a')]+=1
        count[ord(str(b[i))-ord('a')]-=1

    for i in count:
        if i!=0:
            return False

    return True
