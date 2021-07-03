#finding hcf of unlimited numbers passed
# Finding hcf of two numbers using common factor method 
def hcf(num):
    resHcf=1
    factOfAllNum=[]
    for i in range(len(num)):
        factOfNum=[]
        for k in range(1,num[i]+1):
            if num[i]%k==0:
                factOfNum.append(k)
        factOfAllNum.append(factOfNum)

    #setting list with least length
    minLenList=factOfAllNum[0]
    for i in range(len(factOfAllNum)):
        if len(factOfAllNum[i])<len(minLenList):
            minLenList=factOfAllNum[i]
    
    temp=minLenList
    for i in range(len(temp)):  
        for checkItem in factOfAllNum:
            for j in range(len(checkItem)):
                #updating hcf if condition is ture
                if temp[i]==checkItem[j]:
                     if resHcf<checkItem[j]:
                        resHcf=checkItem[j]
    
    #printing result
    print(resHcf)

num=list(map(int,input("Enter all numbers ,separated by space : ").split()))
hcf(num)