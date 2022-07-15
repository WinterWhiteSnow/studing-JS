# import math

# def lcm(a,b):
#     return (a*b)//(math.gcd(a,b))

# for _ in range(int(input())):
#     a,b = map(int,input().split())
#     print(lcm(a,b))
# import math
# wow = lambda : map(int,input().split())
# repeat = int(input())
# person = list(wow())
# b,c = wow()
# cnt = 0
# for i in person:
#     if i-b > 0:
#         cnt+=math.ceil((i-b)/c)+1
#     else:
#         cnt+=1
# print(cnt)
# import sys

# wow = lambda : map(int,sys.stdin.readline().rstrip().split())
# r,l = wow()
# n_list = []
# for _ in range(r):
#     n_list.append(tuple(wow()))
# repeat = int(sys.stdin.readline().rstrip())
# for _ in range(repeat):
#     start_x,start_y,end_x,end_y = wow()
#     cnt = 0
#     for x in range(start_x-1,end_x):
#         cnt+=sum(n_list[x][start_y-1:end_y])
#     print(cnt)

