def lis(a): 
    n = len(a) 
    lis = [1]*n 
    for i in range (1 , n): 
        for j in range(0 , i): 
            if a[i] > a[j] and lis[i]< lis[j] + 1 : 
                lis[i] = lis[j]+1
    maximum = 0
    for i in range(n): 
        maximum = max(maximum , lis[i])  
    return maximum




a=int(input()) 
arr = list(map(int,input().split()))
print (lis(a))
