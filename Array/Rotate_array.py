import numpy as np
for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))   
    print(*(((np.rot90(np.array([l[i:i+n] for i in range(0, len(l), n)]), axes=(1, 0))).flatten()).tolist()))

print(np.version.version)