def is_sorted(arr):
    for i in range(len(arr) -1):
        if arr[i]> arr[i+1]:
            return False
    return True
n= int(input())
arr = list(map(int, input().split()))
print("true" if is_sorted(arr) else "false")

    
