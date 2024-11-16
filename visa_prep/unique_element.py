def unique_element(n,arr):
    seen = set()
    result = []
    for num in arr:
        if num not in seen:
            seen.add(num)
            result.append(num)
    print(" ".join(map(str, result)))
n=int(input())
arr=list(map(int, input().split()))
unique_element(n,arr)
