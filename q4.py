def calc(start, end) :
  if start == end :
    return 0

  if start == 0 :
    rest = end % 3
    if rest != 0 :
      return (start//3) + rest
    else :
      return end + end//3

  


M, R = map(int, input().split())

cnt = 0
while True :
  tmp = M*cnt + R
  tmp = list(str(tmp))
  
