def drawTriange(n):
    for i in range(n):
        for j in range(n-1-i):
            print(" ",end="")
        for k in range(i+1):
            print("*",end="")
        print()

        
inp=int(input("Enter size: "))
drawTriange(inp)
