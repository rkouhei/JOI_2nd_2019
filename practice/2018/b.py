N = int(input())
X = list(map(int, input().split()))
M = int(input())
A = list(map(int, input().split()))

for i in range(len(A)) :
  tmp = X[A[i]-1] + 1
  if tmp not in X and tmp <= 2019 :
    X[A[i]-1] += 1
  else :
    continue

for i in range(len(X)) :
  print(X[i])