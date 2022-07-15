import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# total,r = wow()
# n_list=[one() for _ in range(r)]
# start = 1
# end = sum(n_list)//r
# import math
# while start<=end:
#     mid = (start+end)//2
#     cnt = 0
#     for i in n_list:
#         cnt+=math.ceil(i/mid)
#     if cnt > total:
#         start=mid+1
#     else:
#         end=mid-1
#     # print(start,end,mid,cnt)
# print(start)

# def power(a, n,c):
#     if n == 0:
#         return 1
#     x = power(a, n//2,c)

#     if n % 2 == 0:
#         return x * x % c
#     else:
#         return x * x * a % c
# a,b,c = wow()
# print(power(a,b,c))

# x,y,a0,a1,n = wow()
# if n == 0:
#     if a0 <0:
#         print("-"+str(a0).zfill(2))
#     else:
#         print(str(a0).zfill(2))
# elif n == 1:
#     if a1 < 0:
#         print(str(a1).zfill(2))
#     else:        
#         print("-"+str(a1).zfill(2))
# else:
#     a_list = [0]*(n+1)
#     a_list[0]=a0
#     a_list[1]=a1
#     for r in range(2,n+1):
#         a_list[r]=(x*a_list[r-1]+y*a_list[r-2])
#         if a_list[r] < 0:
#             a_list[r] = (abs(a_list[r])%100)*(-1)
#         else:
#             a_list[r] = a_list[r]%100

#         # print(a_list)
#     answer = a_list[n]
#     if answer < 0:
#         answer = abs(answer)
#         print("-"+str(answer).zfill(2))
#     else:
#         print(str(answer).zfill(2))

# a = one()
# b = one()
# d = 1000000007
# def times(a,b,d):
#     if b == 0:
#         return 1
#     c = times(a,b//2,d)
#     if b%2 == 0:
#         return c*c%d
#     else:
#         return c*c*a%d
# print(times(a,b,d))

    













