from collections import defaultdict as dd
d = dd(list)

def getInd(arr1,arr2):
    res=[]
    for ele in arr2:
        temp=[]
        for j in range(len(arr1)):
            if ele==arr1[j]:
                temp.append(j+1)
        if len(temp)==0:
            temp.append(-1)
        res.append(temp)
    return res

inp = input().strip().split(" ")
groupA=int(inp[0])
groupB=int(inp[1])
for i in range(groupA):
    temp=input()
    d["groupA"].append(temp)
for i in range(groupB):
    temp=input()
    d["groupB"].append(temp)

res=getInd(d['groupA'],d['groupB'])
print("res got : ",res)
for i in range(len(res)):
    print(*res[i])





