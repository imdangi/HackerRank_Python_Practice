'''
https://www.hackerrank.com/challenges/itertools-permutations/problem
You are given a string .
Your task is to print all possible permutations of size  of the string in lexicographic sorted order.
'''
from itertools import permutations
def displayResult(per):
    for tup in per:
        for ele in tup:
            print(ele,end="")
        print()

alpha,pair=input().split()
alpha1=sorted(alpha)
per=list(permutations(alpha1,int(pair)))
displayResult(per)



