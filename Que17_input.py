def polCheck(x,k,p):
    res=[]
    sum=[]
    #removing ** from the list
    for ele in p:
        temp=ele.split("*")
        res.append(temp)
    print(res)
    #storing elements after solving the operands
    for i in res:
        if i[0]=="x" and len(i)==2:
            temp=x**int(i[1])
            sum.append(temp)
        elif i[0]=="x" and len(i)==1:
            temp=x**1
            sum.append(temp)
        elif i[0]=='+' or i[0]=='-':
            sum.append(i[0])
        else:
            sum.append(int(i[0]))
    ans=0
    for i in range(len(sum)):
        if i==0:
            ans+=sum[i]
        else:
            if sum[i]=="+":
                ans+=sum[i+1]
                i+=1
            elif sum[i]=="-":
                ans-=sum[i+1]
                i+=1
    if(ans==k):
        return True
    else:
        return False

x,k=input().strip().split()
p=input().strip().split()
print(polCheck(int(x),int(k),p))