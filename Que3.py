def captalize(s):
    li=[]
    sp=0
    for i in s:
        if(i!=" "):
            li.append(s)
        else:
            if(i==" " and sp==0):
                sp+=1
            elif(i==" " and sp>=1):
                li.append(i)
                sp+=1
    print(li)
    res=[]
    for i in li:
        if i.isnumeric==True or i[0].isnumeric==True:
            res.append(i)
        elif i==" ":
            res.append(i)
            res.append(" ")
        res.append(i.capitalize())
    return res

        

s=input("Enter your name :- ")
result=captalize(s)
print(*result)