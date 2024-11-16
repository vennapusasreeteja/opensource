def rotate_array(N,arr):
    if N==1:
        print(arr[0])
        return
    rotated_arr=arr[1:]+[arr[0]]
    print(" ".join(map(str,rotated_arr)))
N=int(input())
arr=list(map(int, input().split()))
rotate_array(N,arr)
        
