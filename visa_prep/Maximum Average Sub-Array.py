def findMaxAverage(nums, k):
    current_sum = sum(nums[:k])
    max_sum = current_sum
    for i in range(k, len(nums)):
         current_sum += nums[i] - nums[i - k]
         max_sum = max(max_sum, current_sum)
    return max_sum / k
N, K = map(int, input().split())
nums = list(map(int, input().split()))
result = findMaxAverage(nums, K)
print(f"{result:.4f}")
        
