def larg_peri_triangle(n,sticks):
    sticks.sort()
    for i in range(n-1,1,-1):
        a,b,c=sticks[i-2],sticks[i-1],sticks[i]
        if a+b>c:
            return a+b+c
    return -1
n=int(input())
sticks=list(map(int, input().split()))
result = larg_peri_triangle(n,sticks)
print(result)
