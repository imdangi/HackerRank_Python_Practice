def sales(n,ar):
    dictSocks={}
    for i in range(len(ar)):
        if ar[i] in dictSocks.keys():
            dictSocks[ar[i]]+=1
        else:
     
             dictSocks[ar[i]]=1
    validPair=0
    value=list(dictSocks.values())
    for i in value:
        validPair+=i//2
    return validPair
    
n=int(input("Num of socks : "))
ar=list(map(int,input("Enter socks size : ").split()))
print(sales(n,ar))