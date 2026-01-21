def migratorybird(arr):
   
    count = Counter(arr)
    
    max_freq = max(count.values())
    
    # smallest id among those with max frequency
    result = min(bird for bird, freq in count.items() if freq == max_freq)
    
    return result

    
    
n=int(input())
arr=list(map(int,input().split()))
x=migratorybird(arr)
print(x)

    
