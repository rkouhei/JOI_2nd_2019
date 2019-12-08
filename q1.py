import numpy as np

N = int(input())

S = []
for i in range(N) :
  S.append(list(input()))
S = np.array(S)

T = []
for i in range(N) :
  T.append(list(input()))
T = np.array(T)

final = N*N
final_kakudo = 0
kakudo = 0
for i in range(4) :
  diff = 0
  for j in range(N) :
    for k in range(N) :
      if S[j][k] != T[j][k] :
        diff += 1
  if final > diff :
    final = diff
    final_kakudo = kakudo
  S = np.rot90(S)
  kakudo += 90

if final_kakudo == 0 :
  print(final)
elif final_kakudo == 90 or final_kakudo == 270 :
  print(final+1)
elif final_kakudo == 180 :
  print(final+2)