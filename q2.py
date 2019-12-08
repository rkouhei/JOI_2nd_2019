N = int(input())
A_T = []

for i in range(N) :
  A_T.append(list(map(int,input().split())))
A_T.sort(key=lambda x: x[0])

time = A_T[-1][0]
for i in range(N-1) :
  if time < A_T[-1-i][1] :
    time = A_T[-1-i][1]
  time += (A_T[-1-i][0] - A_T[-2-i][0])
time += A_T[0][0]

print(time)