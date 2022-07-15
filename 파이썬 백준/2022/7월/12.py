import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# num = one()
# cnt = 0
# for i in range(1,num+1):
#     count = 0
#     for c in list(str(i)):
#         count+=int(c)
#     if i%count == 0:
#         cnt+=1
# print(cnt)

# num = one()
# n_list = []
# for index in range(5):
#     if index == 0 or index == 4:
#         for _ in range(num):
#             print("@"*num+" "*(num*3)+"@"*num)
#     elif index == 1 or index == 3:
#         for _ in range(num):
#             print("@"*num+" "*(num*2)+"@"*num)
#     else:
#         for _ in range(num):
#             print("@"*num+"@"*num+"@"*num)

# n,a,b,c = wow()
# n-=1
# if n>0:
#     if min(a,b,c) == a :
#         cnt = a*n
#     elif min(a,b,c,) == b:
#         cnt = b*n
#     else:
#         cnt = min(a,b)+c*(n-1)
#     print(cnt//100,cnt%100)
# else:
#     print(0,0)

# goal = one()
# n,a,b,c = wow()
# if goal == 2:
#     print(min(a,b,c))
# else:
#     n_list = sorted([a,b,c])
#     cnt = n_list[0]-(n-n_list[1])-(n-n_list[2])
#     if cnt < 0:
#         cnt = 0
#     print(cnt)

# n = one()
# now_num = "no"
# for _ in range(n):
#     a = one()
#     if now_num == "no":
#         now_num = a
#     else:
#         if a%now_num == 0:
#             print(a)
#             now_num="no"
# r = one()
# num_list = []
# cnt = 0
# for _ in range(r):
#     n_list = [one() for _ in range(2)]
#     # print(n_list)
#     c = n_list[0]*5+n_list[1]*(-3)
#     if c > 40:
#         cnt+=1
#         num_list.append(c)
# if len(num_list) == r:
#     cnt = str(cnt)+"+"
# print(cnt)

# r,a,b = wow()
# n_list = [one() for _ in range(r)]
# cnt = b/a
# n_list = [round(i*cnt) for i in n_list]
# for i in n_list:
#     print(i)




