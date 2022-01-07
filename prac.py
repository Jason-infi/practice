arr = []

def check_mid(arr,mid,high):

    if mid-1 >= 0 and arr[mid-1] > arr[mid]:
        return 'found'
    elif arr[mid] > arr[high]:
        return 'right'
    else :
        return 'left'


def count_rotations(arr):

    low = 0
    high = len(arr)-1

    while low <= high:

        mid = (low + high) >> 1

        if check_mid(arr,mid,high) == 'found':
            return mid
        elif check_mid(arr,mid,high) == 'left':
            high = mid -1 
        elif check_mid(arr,mid,high) == 'right':
            low = mid + 1
    return 0

print(count_rotations(arr))

        