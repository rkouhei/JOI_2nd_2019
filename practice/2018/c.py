N = int(input())
S = input()

ans = 0
flag = True

for i in range(len(S)) :
  if flag :
    tmp = S[i]
    flag = False
  if tmp == S[i] :
    continue
  else :
    ans += 1
    flag = True

print(ans)