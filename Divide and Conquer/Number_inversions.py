# @Date:   2020-05-02T16:43:47+05:30
# @Last modified time: 2020-05-02T16:47:26+05:30

# The goal in this problem is to count the number of inversions of a given sequence
def merge(a, b, left, mid, right):

    # Let i is used for indexing the left sublist and j for the right sublist.

    # At any step in the merge process, if a[i] is greater than a[j],
    # then there are (mid - i) inversions, because the left and right sublists are sorted

    number_of_inversions = 0

    i = left # the index for the left sublist
    j = mid  # the index for the right sublist
    k = left # the index for the result sublist

    while (i <= mid - 1) and (j < right):

        if a[i] <= a[j]:
            b[k] = a[i]
            k, i = k+1, i+1
        else:
            b[k] = a[j]
            k, j = k+1, j+1

            number_of_inversions += mid - i

    # copy the remaining elements of the left sublist if any
    while i <= mid - 1:
        b[k] = a[i]
        k, i = k+1, i+1

    # copy the remaining elements of the right sublist if any
    while j < right:
        b[k] = a[j]
        k, j = k+1, j+1

    # move the merged elements to the original list
    for i in range(left, right):
        a[i] = b[i]

    return number_of_inversions

def get_number_of_inversions(a, b, left, right):

    # number of inversions of a sequence in some sense measures how close the sequence is to being sorted
    # sequence sorted in descending order any two elements constitute an inversion (total of n(n−1)/2 inversions )

    number_of_inversions = 0

    if right - left <= 1:
        return number_of_inversions

    mid = (left + right) // 2

    number_of_inversions += get_number_of_inversions(a, b, left, mid )
    number_of_inversions += get_number_of_inversions(a, b, mid, right)
    number_of_inversions += merge(a, b, left, mid, right)

    return number_of_inversions

a = [2, 3, 9, 2, 9]
b = [0, 0, 0, 0, 0]
left = 0
right = len(a)-1

print(get_number_of_inversions(a,b,left,right))
