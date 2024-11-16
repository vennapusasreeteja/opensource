def max_consecutive_absent_days(N,attendance):
    max_absent=0
    current_absent=0
    for i in range(N):
        if attendance[i]==0:
            current_absent += 1
        else:
            max_absent = max(max_absent, current_absent)
            current_absent = 0
    max_absent = max(max_absent, current_absent)
    return max_absent
N=int(input())
attendance = list(map(int, input().split()))
print(max_consecutive_absent_days(N, attendance))
