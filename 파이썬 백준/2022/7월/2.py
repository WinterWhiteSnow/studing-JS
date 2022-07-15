from re import A
import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# r = one()
# a,b = wow()
# state = "No"
# for _ in range(r):
#     x,y,q,w = wow()
#     if min(x,q)<=a<=max(x,q)  and min(w,y)<=q<=max(y,w):
#         state ="Yes"
# print(state)
# for _ in range(one()):
#     A,B,C = 0,0,0
#     for _ in range(10):
#         a,b,c = wow()
#         A+=a
#         B+=b
#         C+=c
#     A/=10
#     B/=10
#     C/=10
#     n_list = [A,B,C]
#     for i in range(len(n_list)):
#         if n_list[i]-int(n_list[i])>=0.5:
#             n_list[i]=int(n_list[i])+1
#         else:
#             n_list[i]=int(n_list[i])
#     print(*n_list)

# n = one()
# if n%2:
#     min_num = 2
#     max_num = n-1
# else:
#     max_num=n-1
#     for i in range(3,n):
#         if n%i:
#             min_num=i
#             break
# print(min_num,max_num)

# distance,a,b = wow()
# distance%=(a+b)
# if distance>=a:
#     print(0)
# else:
#     print(1)

# for _ in range(one()):
#     a,b = wow()
#     if b%a:
#         print("NIE")
#     else:
#         print("TAK")

# l = one()
# n_list = inputing().split()
# print(min(n_list.count("0"),n_list.count("1")))

# for _ in range(one()):
#     a,b = wow()
#     cnt = 0
#     while a < b:
#         cnt+=1
#         a*=2
#     print(cnt)

# for _ in range(one()):
#     a,b = wow()
#     print(a*b//2)

now = one()
goal = one()

if now > goal:
    x = -(now-goal) #시계반대
    y = 360-now+goal #시계방향
else:
    y = goal-now
    x = -(now+(360-goal))
print(y if abs(x)>=abs(y) else x)




    





