from collections import Counter
def frequency_sort(nums):
    freq = Counter(nums)
    sorted_nums = sorted(nums, key=lambda x: (freq[x], -x))
    return sorted_nums
N = int(input())
nums = list(map(int, input().split()))
result = frequency_sort(nums)
print(" ".join(map(str, result)))
