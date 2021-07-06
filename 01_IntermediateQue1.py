def maxPairs(skillLevel, minDiff):
    count=0
    skillLevel.sort()
    for i in skillLevel:
        for j in skillLevel:
            if i!=j:
                if(i-j>minDiff):
                    count+=1
    return count
arr=[3,4,5,2,1,1]
diff=3
print(maxPairs(arr,diff))