def rotate_array(nums, k):
    N = len(nums)
    k = k % N
    rotated_array = nums[-k:] + nums[:-k]
    return rotated_array
N = int(input())
nums = list(map(int, input().split()))
K = int(input())
rotated = rotate_array(nums, K)
print(" ".join(map(str, rotated)))

