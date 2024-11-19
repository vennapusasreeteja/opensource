def isomorphic(s, t):
    return len(set(zip(s, t))) == len(set(s)) == len(set(t))
N=int(input())
s=input()
t=input()
print("true" if isomorphic(s, t) else "false")
