import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# a = 100
# cnt = 0
# while a < 160:
#     cnt+=1
#     a+=a*0.11
#     print(a,cnt)

# r = one()//3
# cnt=0
# for _ in range(r):
#     a = one()
#     b = one()
#     c = one()
#     cnt+=abs(a-b)+abs(b-c)+abs(a-c)
#     print("wow",cnt)
# print(cnt)
# r = one()
# n_list = [one() for _ in range(r)]
# cnt = 0
# for i in range(r-1):
#     number = min(n_list[i],n_list[i+1])
#     if number != 0:
#         cnt+=1
#     n_list[i],n_list[i+1]=n_list[i]-number,n_list[i+1]-number
#     print(n_list,cnt)

# r = one()
# minus_x = []
# plus_x = []
# minus_y =[]
# plus_y = []
# for _ in range(r):
#     a,b = wow()
#     if a > 0:
#         plus_x.append(a)
#     else:
#         minus_x.append(a)
#     if b > 0:
#         plus_y.append(b)
#     else:
#         minus_y.append(b)
# print(plus_x,minus_x,plus_y,minus_y)
# print(min(min(plus_x)-max(minus_x),min(plus_y)-max(minus_y)))
# r = one()
# max_number = 0
# n_list = []
# for _ in range(r):
#     x,y,s = wow()
#     max_number = max(max_number,x,y)
#     n_list.append((x,y,s))
# for i in range()

# test = one()
# for _ in range(test):
#     max_number = one()
#     pibo = [0,1]
#     while True:
#         num = pibo[-1]+pibo[-2]
#         if num > max_number:
#             break
#         pibo.append(num)
#     # print(pibo)
#     cnt = max_number
#     n_list = []
#     for i in range(len(pibo)-1,-1,-1):
#         if pibo[i]<=cnt:
#             n_list.append(pibo[i])
#             cnt-=pibo[i]
#             if cnt == 0:
#                 break
#         print(cnt,n_list,pibo[i])
#     n_list.sort()        
#     print(*n_list)

# l = one()
# n_list = list(wow())
# n_list.sort()
# if l > 2:
#     sum_sum = sum(n_list)
#     average = n_list[l//2+1]
#     total = sum_sum
#     for index in range(average,-1,-1):
#         cnt = 0
#         for number in n_list:
#             cnt+=abs(number-index)
#         if total >= cnt:
#             average=min(average,index)
#             total = cnt
#         else:
#             break
#         # print(average,total)
#     print(average)
# else:
#     print(n_list[0])

l = one()
n_list = list(wow())



































