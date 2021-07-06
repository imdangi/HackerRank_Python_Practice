def sortedSum(a):
    li=[]
    sum=0
    for i in a:
        li.append(i)
        li.sort()
        print(li)
        # for j in range(len(li)-1):
        #     min=li[j]
        #     index=j
        #     for k in range(j,len(li)):
        #         if li[k]<min:
        #             min=li[k]
        #             index=k
        #     li[index]=li[j]
        #     li[j]=min 
        for a in range(0,len(li)):
            sum+=(a+1)*(li[a])
    finalResult=sum%(10**9+7)
    return finalResult
    
li=[4,3,2,1]
print(sortedSum(li))