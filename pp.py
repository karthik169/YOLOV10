def minDiff(arr):  
    # Sort the array to minimize the absolute differences  
    arr.sort()  
    
    # Initialize the sum of differences  
    total_diff = 0  
    
    # Calculate the sum of absolute differences of adjacent elements  
    for i in range(1, len(arr)):  
        total_diff += abs(arr[i] - arr[i - 1])  
        
    return total_diff  

# Input handling  
if __name__ == "__main__":  
    n = int(input())  
    arr = list(map(int, input().split()))  
    
    if len(arr) != n:  
        print()  
    else:  
        result = minDiff(arr)  
        print(result)  