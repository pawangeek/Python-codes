def balance(expr):
    
    arr = []
    dct = {'}':'{', ']':'[', ')':'('}

    if len(expr)%2!=0:
        return False

    for i in expr:

        if i in dct and len(arr)>0:
            if arr[-1]==dct[i]:
                arr.pop()
            else:
                return False

        else:
            arr.append(i)

    if len(arr)>0:
        return False

    return True

print(balance('{{()}[)'))
