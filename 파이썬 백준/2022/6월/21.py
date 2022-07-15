import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# num = one()
# cnt = 1
# for i in range(2,num+1):
#     cnt=cnt*i%10
# print(cnt)

# n_list = list(wow())
# n_list.sort()
# if len(set(n_list))==1:
#     print(2)
# elif n_list[0]**2+n_list[1]**2==n_list[2]**2:
#     print(1)
# else:
#     print(0)
# import math
# r,c,cctv = wow()
# print(math.ceil(r/cctv)*math.ceil(c/cctv))

# n_list = list(wow())
# n_list.sort()
# if n_list[0]+n_list[1] == n_list[2] or n_list[0]==n_list[1] or n_list[1]==n_list[2]:
#     print("S")
# else:
#     print("N")

# a,b = wow()
# if a==b:
#     print(a)
# else:
#     print(max(a,b))

# a,b,c = wow()
# if a==b==c:
#     print("*")
# else:
#     if a==b:
#         print("C")
#     elif a==c:
#         print("B")
#     elif b==c:
#         print("A")

# a = inputing().replace(" ","")
# answer = a.split("=")[1]
# pr = a.split("=")[0]
# if eval(pr) == int(answer):
#     print("YES")
# else:
#     print("NO")

# cnt = 0
# for _ in range(6):
#     a = inputing()
#     if a == "W":
#         cnt+=1
# if 1<=cnt<=2:
#     print("3")
# elif 3<=cnt<=4:
#     print("2")
# elif 5<=cnt<=6:
#     print(1)
# else:
#     print(-1)


# x_list = []
# y_list = []
# for _ in range(2):
#     a,b,c,d= wow()
#     x_list.extend([a,c])
#     y_list.extend([b,d])

# a = max(max(x_list)-min(x_list),max(y_list)-min(y_list))
# print(a*a)

n = one()
print("FA")











