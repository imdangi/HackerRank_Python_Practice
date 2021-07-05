import calendar as cc


def printResult(res):
    if res==0:
        return("MONDAY")
    elif res==1:
        return("TUESDAY")
    elif res==2:
        return("WEDNESSDAY")
    elif res==3:
        return("THURSDAY")
    elif res==4:
        return("FRIDAY")
    elif res==5:
        return("SATURDAY")
    elif res==6:
        return("SUNDAY")

inp=list(map(int,input().split()))
day=inp[1]
month=inp[0]
year=inp[2]
res=cc.weekday(year,month,day)
print(printResult(res))
    