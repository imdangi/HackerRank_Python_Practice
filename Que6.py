from collections import Counter

def totalSale(dictOfsize,offerForSale):
    totalAmount=0
    for offer in offerForSale:
        for i in range(0,1):
            if offer[0] in dictOfsize.keys():
                if dictOfsize[offer[0]]>0:
                    totalAmount+=offer[1]
                    dictOfsize[offer[0]]-=1
    print(totalAmount)


totalShoes=int(input())
allShoeSize=list(map(int,input().split()))
count=Counter(allShoeSize)
totalCustomers=int(input())
sale=[]
for i in range(totalCustomers):
    temp=list(map(int,input().split()))
    sale.append(temp)
    
totalSale(count,sale)
