test_case = int(input())


def getCountInversion(arr):
    count_inversion=0

    for i in range(len(arr)-1):
        if (arr[i+1]-arr[i] < 0):
            count_inversion+=1
        
    return count_inversion

for i in range(test_case):
    arr_len = int(input())
    arr=list(map(int, input().split()))
    
    count=0
    maxV=0

    for i in range(len(arr)):
        if(arr[i] < maxV):
            maxV=0
            count+=1
        else:
            maxV=max(maxV, arr[i])
    
    print(count)

