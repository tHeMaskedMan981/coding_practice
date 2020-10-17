


def search(nums, target):
    if len(nums)==1:
        if nums[0]==target: return 0
        else: return -1

    def binary_search(lo, hi):
        
        while lo<=hi:
            mid = lo + (hi-lo)//2

            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                lo = mid+1
            else:
                hi = mid-1

        return -1
        
        
    l,r = 0, len(nums)-1
    # if sorted, do regular binary search 
    if nums[l]<nums[r]:
        return binary_search(l,r)

    # find pivot, keep closing in without losing the pivot
    # elements, and stop when only 2 elements remain
    while r-l>1:
        
        mid = l+ (r-l)//2
        
        if nums[mid]>nums[r]:
            l = mid
        elif nums[mid]<nums[l]:
            r = mid
        elif nums[mid]==target:
            return mid

    pivot = [l,r]
    print("pivot : ", pivot)
    if nums[0]<=target<=nums[l]:
        lo, hi = 0, l
    else:
        lo, hi = r, len(nums)-1

    return binary_search(lo,hi)
            

# Driver code 
nums = [4,5,6,7,8,1,2,3]
target = 1

res = search(nums, target)
print(res)