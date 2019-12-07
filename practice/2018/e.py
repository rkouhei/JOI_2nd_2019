N, M = map(int, input().split())
A = list(map(int, input().split()))

L_R = []
for i in range(M) :
  L_R.append(list(map(int, input().split())))
L_R.append([N+1,N+1])
L_R.sort(key=lambda x: x[0])

dp = [0] * (N+1) # DPテーブル
nowlr = 0 # 今どの範囲をみているか(L_R)

for i in range(N) :
  while L_R[nowlr][1] < i+1 :
    nowlr += 1
  if L_R[nowlr][0] > i+1 :
    dp[i+1] = dp[i] + A[i]
  else :
    dp[i+1] = max(dp[i], dp[L_R[nowlr][0]-1] + A[i])

print(dp[N])