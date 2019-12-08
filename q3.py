N = int(input())

# ans_list = []
# for i in range(1,N+1) :
#   ans_list = []
#   tmp = i
#   ans_list.append(tmp)
  # while tmp < N :
  #   tmp_str = list(str(tmp))
  #   tmp_sum = sum(int(i) for i in tmp_str)
  #   tmp += tmp_sum
  #   ans_list.append(tmp)
#   if tmp == N :
#     break

# print(len(ans_list))

def find(N) :
  ans_list = [i for i in range(1,N+1)]

  for i in range(N) :
    if len(ans_list) == 1 :
      break
    tmp_ok_list = []
    tmp = ans_list[0]
    while tmp < N :
      tmp_ok_list.append(tmp)
      try :
        ans_list.remove(tmp)
      except :
        break
      tmp_str = list(str(tmp))
      tmp_sum = sum(int(j) for j in tmp_str)
      tmp += tmp_sum
    if tmp == N :
      return tmp_ok_list
  return 0


ans = 0
ans_list = [i for i in range(1,N+1)]
ok_list = []
flag = False

for i in range(N) :
  if len(ans_list) == 1 :
    break
  tmp_ok_list = []
  tmp = ans_list[0]
  while tmp < N :
    tmp_ok_list.append(tmp)
    try :
      ans_list.remove(tmp)
    except :
      flag = True
      break
    tmp_str = list(str(tmp))
    tmp_sum = sum(int(j) for j in tmp_str)
    tmp += tmp_sum
  if tmp == N :
    ans += len(tmp_ok_list)
    break
  
for i in range(len(tmp_ok_list)) :
  ans += len(find(i))

print(ans+1)

# if N < 10 :
#   ans_list = []
#   for i in range(1,N+1) :
#     ans_list = []
#     tmp = i
#     ans_list.append(tmp)
#     while tmp < N :
#       tmp_str = list(str(tmp))
#       tmp_sum = sum(int(i) for i in tmp_str)
#       tmp += tmp_sum
#       ans_list.append(tmp)
#     if tmp == N :
#       break
#   print(len(ans_list))
#   exit()
# else :
#   one_list = [1,3,5,7,9]
#   tmp = 20
#   cnt = 1
#   while tmp <= N :
#     one_list.append(tmp)
#     if cnt < 9 :
#       tmp += 11
#       cnt += 1
#     else :
#       tmp += 2
#       cnt = 1
  
#   ans = []
#   for i in one_list :
#     tmp = i
#     tmp_list = []
#     while tmp < N :
#       tmp_list.append(tmp)
#       tmp_str = list(str(tmp))
#       tmp_sum = sum(int(j) for j in tmp_str)
#       tmp += tmp_sum
#     if tmp == N :
#       print(i)
#       ans += tmp_list

# print(len(set(ans)))

# print(ans+1)