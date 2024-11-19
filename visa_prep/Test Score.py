def score(n , a , b):
    max = n*a
    if b<= max and b % a ==0:
        print("YES")
    else:
        print("NO")
n, a, b = map(int, input().split())
score(n, a ,b)
