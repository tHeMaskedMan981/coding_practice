def partition(arr, low, high):
    # use the last element as pivot, put it at its correct place, with all smaller elements on the left, larger elements
    # on the right
    pivot = arr[high]
    i = low-1
    for j in range (low, high):
        # place all elements smaller than pivot in the start of the array
        if (arr[j]<pivot):
            i+=1
            arr[j], arr[i] = arr[i], arr[j]

    # place the pivot after all elements smaller than itself
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1 


def quickSort(arr, low, high):
    # sort the arr by moving one element at a time to its correct place, recursively
    if low<high:

        k = partition(arr, low, high)

        quickSort(arr, low, k-1)
        quickSort(arr, k+1, high)


arr = [10,4,7,2,8,56, 3, 34,54,67,12]
print(arr)
n = len(arr)

quickSort(arr, 0, n-1)
print(arr)

