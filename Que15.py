# from collections import defaultdict as dd
from collections import OrderedDict
d = OrderedDict()

N = int(input())
for i in range(N):
    *key,value=input().strip().split()
    v=int(value)
    k=' '.join(key)
    if k in d.keys():
        val=d[k]
        d[k]=val+v
    else:    
        d[k]=v

# for key,value in d.items:
#     # for i in range(value):
#     print("Key= ",key,"Value = ",value)
for i in d:
    print(i,d[i])






