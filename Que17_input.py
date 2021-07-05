def polCheck(x,k,p):
    print(p)


    sum=0
    
       
    if(sum==k):
        return True
    else:
        return False
x,k=input().strip().split()
p=input().strip().split()
print(polCheck(int(x),int(k),p))