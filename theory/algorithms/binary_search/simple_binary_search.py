
# Driver Code 
arr = [ 2, 3, 4, 10, 40 ] 
x = 3
l,r = 0, len(arr)-1

while l <= r: 

    # Use this to avoid overflow problems 
    mid = l + (r - l) // 2 
        
    # Check if x is present at mid 
    if arr[mid] == x: 
        print(mid)
        break 

    # If x is greater, ignore left half 
    elif arr[mid] < x: 
        l = mid + 1

    # If x is smaller, ignore right half 
    else: 
        r = mid - 1
    
# If we reach here, then the element 
# was not present 
# print(-1)  
