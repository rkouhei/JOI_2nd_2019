N = int(input())
a = list(input().split())

for i in range(int(N/2)) :
  tmp = a[i]
  a[i] = a[-1-i]
  a[-1-i] = tmp

print(' '.join(a))