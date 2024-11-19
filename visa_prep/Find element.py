def binary(arr, x):
    low , high = 0, len(arr)-1
    while low<= high:
        mid = (low + high)//2
        if arr[mid] == x: return mid
        elif arr[mid] < x: low = mid + 1
        else: high = mid - 1
    return -1
n = int(input())
arr = list(map(int, input().split()))
x = int(input())
print(binary(arr, x))
