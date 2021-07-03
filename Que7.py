# Finding hcf of two numbers using common factor method 
def hcf(a,b):
    resHcf=1
    # Finding common factors of num 1
    factOfNum1=[]
    for i in range(1,a+1):
        if a%i==0:
            factOfNum1.append(i)
    
    # Finding common factors of num2
    factOfNum2=[]
    for i in range(1,b+1):
        if b%i==0:
            factOfNum2.append(i)

    #checking status of the program
    # print(factOfNum1)
    # print(factOfNum2)

    #finding highest common factor now
    for i in factOfNum1:
        for j in factOfNum2:
            if i==j:
                if resHcf<j:
                    resHcf=j
    print(resHcf)



num1=int(input("Enter number 1 : "))
num2=int(input("Enter number 2 : "))
hcf(num1,num2)