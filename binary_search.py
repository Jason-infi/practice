# binary search on a sorted array (desc) with no repetitions

arr = [100,40,25,10,5,1]
#arr.sort()
print(arr)
key = int(input('Key:'))

def binary_search(arr,key):
    low = 0
    high = len(arr)-1

    while low <= high:
        mid = (low + high) >> 1
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            high = mid -1 
        elif arr[mid] > key:
            low = mid + 1
    return -1

print(binary_search(arr,key))
