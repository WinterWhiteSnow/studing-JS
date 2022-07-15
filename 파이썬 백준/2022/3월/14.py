# r,l = map(int,input().split())
# wow = [1]*2
# for a in range(3,r+1):
#     why = [0]*a
#     for i in range(len(why)):
#         if i == 0 or i == len(why)-1:
#             why[i]=1
#         else:
#             why[i]=wow[i-1]+wow[i]
#     why[a-1]=1
#     wow=why
# print(wow[l-1])

# n = int(input())
# n_list = [1]
# for a in range(1,n+1):
#     if a == 1:
#         n_list.append(1)
#     else:
#         cnt = 0
#         for i in range(a):
#             # print(a,i)
#             cnt+=n_list[i]*n_list[a-i-1]
#         n_list.append(cnt)
# print(n_list[-1])
# import sys
# x,y = 0,1
# n = int(sys.stdin.readline().rstrip())
# for _ in range(n):
#     x,y = (x+y)%1000000,x%1000000
# print(x)
import math
n = int(input())
if n == 1:
    print(0)
else:
    n_list = [0,2]
    total = 0
    cnt = 0
    for i in range(1,n-2):
        cnt+=i
        n_list.append(cnt+n_list[-1])
        print(n_list)
        
    print(n_list[n-1])
        
        
        
        
        





