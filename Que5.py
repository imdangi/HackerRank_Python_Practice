from itertools import product
def getCartesianProduct(A,B):
    res=list(product(A,B))
    print(*res)

l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
getCartesianProduct(l1,l2)