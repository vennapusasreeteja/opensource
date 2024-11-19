def winner(v , c):
    if v == c:
        print("NULL")
    elif (v == 'R' and c == 'S') or {v == 'S' and c == 'p'} or (v == 'p' and c == 'R'):
        print("Vignesh")
    else:
        print("Charan")
v, c = input().split()
winner(v,c)
