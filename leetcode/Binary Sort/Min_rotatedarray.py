# @Date:   2020-04-25T09:19:07+05:30
# @Last modified time: 2020-04-27T12:22:51+05:30

numbers = [2,7,11,15]
target = 9
# Get numbers having sum = 9 <- Task

dic = {}
for i,num  in enumerate(numbers):

    # If present then print index of both (num, target-num)
    if target-num in dic:
        print ([dic[target-num]+1, i+1])

    # if target-num not in dic than append to dictionary
    dic[num] = i
