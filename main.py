def sumOfDiagonal(arr,row):
    sum=0
    for i in range(row):
            sum+=arr[i][i]
    return sum
#Main Code
l=list(map(int,input().split()))
row,coloum=l[:2]
arr,c=[[]],coloum
for i in l[2:]:
    if c<=0:
        arr.append([i])
        c=coloum
    else:
        arr[-1].append(i)
    c-=1
print(sumOfDiagonal(arr,row))