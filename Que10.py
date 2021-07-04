def average(array):
    sum=0
    set1=set(array)
    l=len(set1)
    for i in set1:
        sum+=i
    avg=sum/l  
    return avg
    
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)