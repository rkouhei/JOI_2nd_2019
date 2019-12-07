import numpy as np

N = int(input())
A = np.array(list(map(int, input().split())))
sea_level = np.ones(N)

max_islands = 0
series = False

while True :
  islands = 0
  for i in range(N) :
    if series :
      if A[i] <= 0 :
        series = False
        islands += 1
      continue

    if A[i] <= 0 :
      series = False
    else :
      series = True
  
  if series :
    islands += 1
    series = False
  
  if islands > max_islands :
    max_islands = islands
  
  A = A - sea_level
  if all([i <= 0 for i in A]) :
    break

print(max_islands)