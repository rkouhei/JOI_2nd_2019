N = int(input())
ans = []

for i in range(N) :
  name = input()
  ans.append(name.lower())

for i in range(N) :
  print(ans[i])