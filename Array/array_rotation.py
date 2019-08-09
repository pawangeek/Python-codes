#Function to left Rotate arr[] of size n by 1
def leftr(arr, d, n):
  for i in range(d):
    leftrbyone(arr, n)

##Function to left Rotate arr[] of size n by 1
def leftrbyone(arr,n):
  temp=arr[0]
  for i in range(n-1):
    arr[i]=arr[i+1]
  arr[n-1]=temp

def printarr(arr,size):
  for i in range(size):
    print("% d" % arr[i], end=" ")

arr = list()
num = input("Enter the number of elements:")
print ('Enter numbers in array: ')
for i in range(int(num)):
    n = input()
    arr.append(int(n))

print("Select no. at which you want to rotate")
s = input()

print("Your reversed array is")
leftr(arr,int(s),len(arr))
printarr(arr,len(arr))