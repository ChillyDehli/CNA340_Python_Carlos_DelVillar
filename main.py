n = int(input())
minVal = n
maxVal = n
while(n>0):
    if(minVal>n):
        minVal = n
    if(maxVal<n):
        maxVal = n
    n = int(input())
print(minVal,maxVal)