arr = ["cat", "dog", "tac", "god", "act"]

def all_ana(arr):

    words = [''.join(sorted(i)) for i in arr]
    dct = {}

    for n, i in enumerate(words):
        if i in dct:
            dct[i].append(n)
        else:
            dct[i] = [n]

    print([[arr[i] for i in lst] for lst in dct.values()])


all_ana(arr)

# words = [''.join(sorted(i)) for i in arr]
# dct = defaultdict(list)

# for n, i in enumerate(words):
#     dct[i].append(n)

# return [[arr[i] for i in lst] for lst in dct.values()]