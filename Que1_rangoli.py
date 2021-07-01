def drawRangoli(a=[],n=1):

    if n>1:
        for i in range(0,n):

            #printing dash
            sp=(n*2)-(2*(i+1))
            for j in range(0,sp):
                print("-", end="")
            

            #printing characters
            for k in range(n-1,n-2-i,-1):
                print(a[k],end="")
                if(i!=n-1):
                    print("-",end="")
                else:
                    print("-",end="")

            
            #printing inverted end characters
            for k in range(n-1-i,n-1):
                print(a[k+1],end="")
                if(i!=n-1):
                    print("-",end="")
                else:
                    if(a[k+1]==a[n-1]):
                        print("",end="")
                    else:
                        print("-",end="")


                
            #printing inverted end spaces 
            for l in range(0,sp-1):
                print("-",end="")
            print()

        for i in range(n-2,-1,-1):
        
            #printing dash
            sp=(n*2)-(2*(i+1))
            for j in range(0,sp):
                print("-", end="")
            

            #printing characters
            for k in range(n-1,n-2-i,-1):
                print(a[k],end="")
                if(i!=n-1):
                    print("-",end="")
                else:
                    print("-",end="")

            
            #printing inverted end characters
            for k in range(n-1-i,n-1):
                print(a[k+1],end="")
                if(i!=n-1):
                    print("-",end="")
                else:
                    if(a[k+1]==a[n-1]):
                        print("",end="")
                    else:
                        print("-",end="")


                
            #printing inverted end spaces 
            for l in range(0,sp-1):
                print("-",end="")
            print()

    else:
        print(*a)

n=int(input("Enter size : "))
alphabets=[]
alpha = 'a'

#creating list of alphabets
for i in range(0, n):
    alphabets.append(alpha)
    alpha = chr(ord(alpha) + 1)

drawRangoli(alphabets,n)

