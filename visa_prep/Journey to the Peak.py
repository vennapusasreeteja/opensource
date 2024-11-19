n = int(input())
a = list(map(int, input().split()))
current=0
highest = 0
for height in a:
    current += height
    highest = max(highest, current)
print(highest)
