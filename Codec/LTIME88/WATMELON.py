for _ in range(int(input())):

    n = int(input())
    arr = list(map(int, input().split()))
    print("NO") if sum(arr)<0 else print("YES")