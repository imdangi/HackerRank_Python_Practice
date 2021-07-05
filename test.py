print("Welcome all !")

def polCheck(x,k):
    sum=0
    for i in range(k-1,-1,-1):
        sum+=x**i
    if(sum==k):
        return True
    else:
        return False
x,k=input().strip().split()

print(polCheck(int(x),int(k)))