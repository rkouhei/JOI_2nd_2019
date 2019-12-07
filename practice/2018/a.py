A, B, C = map(int, input().split())

# day_a = -(-C // A)
# coin = day_a * A
# if day_a > 6 :
#   day_b = day_a // 7
#   coin += (day_b * B)
#   ans = day_a -(-(C - coin) // A)
#   print(ans)
# else :
#   print(day_a)

D = A*7 + B
if C > D :
  week = C // D
  ans = 7*week -(-(C % D) // A)
  print(ans)
else :
  print(-(-C // A))