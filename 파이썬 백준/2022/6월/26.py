import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# a = one()
# print((100-a)/a+1)
# b = 100-a
# print((100-b)/b+1)
# import math
# a = one()
# x = 0
# y = 0
# for b in range(1,11):
#     for c in range(1,11):
#         if b*c >=a:
#             if x==y==0:
#                 x = b
#                 y = c
#             else:
#                 if abs(x-y)>abs(b-c):
#                     x=b
#                     y=c
# if (x-1)*y >= a:
#     print(x-1,y)
# else:
#     print(x,y)
# n = one()
# if n>198:
#     print(0)
# else:
#     cnt = 0
#     for i in range(1,100):
#         for a in range(1,100):
#             if n-i-a == 0:
#                 cnt+=1
#     print(cnt)

n_list = sorted(list(wow()))
cnt = 0
while (cnt**2)//2 < n_list[0]:
    cnt+=1
if n_list[0]==n_list[1]==0:
    print("Impossible")
else:
    if (cnt**2)//2 <= n_list[0] and (cnt**2)//2 <= n_list[1]:
        print(cnt)
    else:
        print(cnt-1)
















