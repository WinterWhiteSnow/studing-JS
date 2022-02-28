# l = int(input())
# a = list(map(int,input().split()))
# if len(a) == l:
#     index = a.index(-1)
#     x = a[:index]
#     y = a[index+1:]
#     print(min(x)+min(y))

# limit_h,k = map(int,input().split())
# k = str(k)
# cnt = 0
# for h in range(limit_h+1):
#     h = str(h).rjust(2,"0")
#     for m in range(60):
#         m = str(m).rjust(2,"0")
#         for s in range(60):
#             s = str(s).rjust(2,"0")
#             if k in str(h) or k in str(m) or k in str(s):
#                 cnt+=1
# print(cnt)

# n = input()
# a = list(map(int,list(n[:len(n)//2])))
# b = list(map(int,list(n[len(n)//2:])))
# if sum(a)==sum(b):
#     print("LUCKY")
# else:
#     print("READY")    
# n,m = map(int,input().split())
# a = list(map(int,input().split()))
# b = list(map(int,input().split()))
# if len(a) == n and len(b)==m:
#     print(sum(a)+sum(b))     
# gossu,brand = map(int,input().split())
# a = input().split()
# a_set = set(a)
# wow = [a.count(i) for i in a_set]
# print(max(wow))
# import sys
# r,hap,l = map(int,sys.stdin.readline().rstrip().split())
# cnt=0
# wow = []
# for _ in range(r):
#     a = list(map(int,sys.stdin.readline().rstrip().split()))
#     a_list = [i for i in a if i >= l]
#     sum_a = sum(a)
#     if sum_a>=hap and len(a_list) == 3:
#         cnt+=1
#         wow.extend(a)
# print(cnt)
# print(*wow)  

# r = int(input())
# cnt=0
# for _ in range(r):
#     a = input()
#     cnt+=len(a)
# print(cnt)

# l = int(input())
# a = input().split()
# for i in range(1,len(a)):
#     if a[i-1][-1] ==a[i][0] or a[i-1][-1] ==a[i][::-1][0]:
#         pass
#     else:
#         print(0)
#         exit()
# print(1)
import sys
r = int(sys.stdin.readline().rstrip())
for _ in range(r):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    cnt = 0
    for x in range(a+b):
        for y in range(a+b):
            for z in range(y):
                cnt+=1
    print(cnt)
            