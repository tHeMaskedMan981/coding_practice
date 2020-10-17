import time
nums = [6,8,8,9]
target = 8
l,r = 0, len(nums)-1
found = False

# > and < conditions are same in both the cases (r = mid-1, l = mid+1) 

# For leftmost index, when nums[mid]==target, close in from the right side. r = mid. this way we 
# dont loose the target, and keep on moving towards the leftmost occurence.
while l<=r:
    
    mid = l + (r-l)//2
    if nums[mid]==target:
        if l==r:
            found = True
            break
        else:
            r = mid
    elif nums[mid]<target:
        l = mid+1
    else:
        r = mid-1

if found:
    ans = [l]
else: 
    print(-1)


l,r = 0, len(nums)-1
found = False

# For finding the rightmost, can't just invert the process of above one. The reason is calculating 
# the mid favors l, and if we do l = mid, we might end up in a infinte loop. for ex, [8,8],
# l,r=0,1; mid=0, as equal, l=mid=0, thus starting the same loop again. so when equal, move 1 step
# ahead from left, chances are will loose the target, but not by more than 1. so when the loop ends, 
# use l-1 as the result. 

while l<=r:

    mid = l + (r-l)//2

    if nums[mid]==target:
        found = True
        l = mid+1
    
    elif nums[mid]<target:
        l= mid+1
    else:
        r = mid-1

if found:
    ans+=[l-1]
    print(ans)
else:
    print(-1)

