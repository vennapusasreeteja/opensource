a = int(input())
for _ in range(a):
    x,n = map(int, input().split())
    score = (x // 10)*n
    print(score)
