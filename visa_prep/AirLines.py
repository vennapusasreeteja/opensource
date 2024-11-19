def planes(x,n):
    req = (n + 99) // 100
    addplanes = max(0, req - x)
    print(addplanes)
x, n=map(int, input().split())
planes(x,n)
