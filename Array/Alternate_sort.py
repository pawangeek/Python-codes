# Sort input array using a O(n Log n) algorithm.
'''We maintain two pointers, one from beginning and one from end in sorted array. 
   We alternatively print elements pointed by two pointers and move them toward each other.'''

n = int(input("Number of elemnts in array: "))
arr=list()

print("Print numbers in array:")
for i in range(int(n)):
	m = input()
	arr.append(int(m))

print(arr)

def alternate(arr,n):
	arr.sort()

	i = 0
	j = n-1

	while (i<j):
		print(arr[j])
		print(arr[i])

		j-=1
		i+=1

	if (n%2)==1:
		print(arr[i])


alternate(arr,n)