def divTry(list):
    for ele in list:
        try:
            print(int(ele[0])/int(ele[1]))
        except ZeroDivisionError:
            print("Error Code :integer division or modulo by zero")
        except Exception as e:
            print("Error Code:",e)

inNum=[]
n=int(input())
for i in range(n):
    temp=input().strip().split()
    inNum.append(temp)
divTry(inNum)
