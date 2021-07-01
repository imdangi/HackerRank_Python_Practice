# Todo:-  1. Decimal
#         2. Octal
#         3. Hexadecimal
#         4. Binary 
def decToBin(num):
    '''
    This function will return the binary representation of given decimal number.

    This function take only one argument , i.e. of num whose binary representation 
    is needed to find.

    This function will use only pure logic instead of using predefined function.
    '''
    binNum=[]
    while(num!=0):
        rem=num%2
        binNum.append(str(rem))
        num=num//2
    #reversing the list
    start=0
    end=len(binNum)-1
    while(start<end):
        temp=binNum[start]
        binNum[start]=binNum[end]
        binNum[end]=temp
        start+=1
        end-=1
    res="".join(binNum)
    return res

def decToOct(num):
    '''
    This function will return the octal representation of given decimal number.

    This function take only one argument , i.e. of num whose octal representation 
    is needed to find.

    This function will use only pure logic instead of using predefined function.
    '''
    octNum=[]
    while(num!=0):
        rem=num%8
        octNum.append(str(rem))
        num=num//8
    #reversing the list
    start=0
    end=len(octNum)-1
    while(start<end):
        temp=octNum[start]
        octNum[start]=octNum[end]
        octNum[end]=temp
        start+=1
        end-=1
    resInOct="".join(octNum)
    return resInOct

def decToHex(num):
    '''
    This function will return the hexadecimal representation of given decimal number.

    This function take only one argument , i.e. of num whose hexadecimal representation 
    is needed to find.

    This function will use only pure logic instead of using predefined function.
    
    Here we need to assign character if remainder is above or equal to 10
    '''
    hexNum=[]
    while(num!=0):
        rem=num%16
        #assigning characters for value above 9
        if(rem>9):
            if rem==10:
                hexNum.append("A")
            elif rem==11:
                hexNum.append("B")
            elif rem==12:
                hexNum.append("C")
            elif rem==13:
                hexNum.append("D")
            elif rem==14:
                hexNum.append("E")
            elif rem==15:
                hexNum.append("F")
        else:
            hexNum.append(str(rem))
        num=num//16
    #reversing the list
    start=0
    end=len(hexNum)-1
    while(start<end):
        temp=hexNum[start]
        hexNum[start]=hexNum[end]
        hexNum[end]=temp
        start+=1
        end-=1
    resInHex="".join(hexNum)
    return resInHex

def printValues(n):
    '''
    This function will print all the representations in required order

    Form here , we will call functions and print the values returned by these functions

    '''
    sp=len(decToBin(n))+1
    for i in range(1,n+1):
        #Step 1 print spaces
        for j in range(0,sp-len(str(i))-1):
            print(" ",end="")

        #Step 2 print num in decimal
        print(i,end=" ")

        #Step 3 print spaces
        for k in range(0,sp-len(decToOct(i))):
            print(" ",end="")

        #Step 4 print num in octal
        print(decToOct(i),end="")

        #Step 5 print spaces
        for a in range(0,sp-len(decToHex(i))):
            print(" ",end="")

        #Step 6 print num in hex
        print(decToHex(i),end="")

        #Step 7 print spaces
        for b in range(0,sp-len(decToBin(i))):
            print(" ",end="")

        #Step 8 print num in binary
        print(decToBin(i),end="")
        print()
    
n=int(input());
printValues(n)

