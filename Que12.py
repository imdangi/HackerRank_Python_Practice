import numpy as np

def arrays(arr):
    nparr=np.array(arr,float)
    res=nparr[::-1]
    return res

arr = input().strip().split(' ')
result = arrays(arr)
print(result)