# important question

# Problem : we have to find maximum j-i Such That arr [j] > arr [I]
# Approach : first create left min array and right max array and than finding difference b/w them by mergesort concept


l = int(input())
arr = list(map(int,input().split()))

lmin,rmin=[arr[0]],[arr[l-1]]

for i in range(1,l):
    lmin.append(min(lmin[i-1],arr[i]))
    
for i in range(l-2,-1,-1):
    rmin.insert(0,max(arr[i],rmin[0]))

i,j,maxd=0,0,0
while (i<l and j<l):
    if rmin[j]>lmin[i]:
        maxd = max(maxd,j-i)
        j+=1
    else:
        i+=1

print(maxd)