# @Date:   2020-05-02T16:15:46+05:30
# @Last modified time: 2020-05-02T16:48:07+05:30

# Approach div and conquer
# goal is replace a 3-way partition to handle equal elements in quick_sort

import random

def partition3(data, left, right):

    """This function partitions a[] in three parts:
    a) a[left..l - 1] contains all elements smaller than the pivot element
    b) a[l..r] contains all occurrences of the pivot element
    c) a[r + 1..right] contains all elements greater than the pivot element
    """

    mid = left+1
    pivot = data[left]

    while mid<=right:

        if data[mid]<pivot:

            # Change with mid in left
            data[left], data[mid] = data[mid], data[left]
            left += 1
            mid += 1

        elif data[mid]>pivot:

            # change with mid in right
            data[mid], data[right] = data[right], data[mid]
            right -= 1

        else:
            mid += 1

    return (left-1,right+1)

def randomized_quick_sort(a, l, r):

    if l >= r:
        return a

    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]

    i,j = partition3(a, l, r)
    randomized_quick_sort(a, l, i);
    randomized_quick_sort(a, j, r);



a = [2, 3, 9, 2, 2]
l = 0
r = len(a)-1

print(randomized_quick_sort(a,l,r))
