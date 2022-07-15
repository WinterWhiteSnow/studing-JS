import sys


inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# state = one()
# r = one()
# cnt = 0
# for _ in range(r):
#     a = one()
#     cnt+=state-a
# print(state+cnt)

# price = float(inputing())
# cnt = 0
# for _ in range(one()):
#     a,b = map(float,inputing().split())
#     cnt+=a*b
# print(cnt*price)

# r,l = wow()
# cnt = 0
# for _ in range(r):
#     n_list = list(wow())
#     if 0 not in n_list:
#         cnt+=1
# print(cnt)

# for index in range(1,one()+1):
#     print(f"Case {index}:")
#     for _ in range(one()):
#         a = one()
#         if 1<=a+1<=6:
#             print(a+1)

# for index in range(1,one()+1):
#     a = one()
#     print(f"Case {index}:")
#     list_list = []
#     for x in range(1,7):
#         for y in range(1,7):
#             if x+y == a:
#                 if sorted([x,y]) not in list_list:
#                     list_list.append(sorted([x,y]))
#     for a,b in list_list:
#         print(f"({a},{b})")

# for index in range(1,one()+1):
#     a,b = wow()
#     if a%b==0:
#         c = a//b
#         print(f"Case {index}: {c}")
#     else:
#         c = a//b
#         d = a%b
#         if c != 0:
#             print(f"Case {index}: {c} {d}/{b}")
#         else:
#             print(f"Case {index}: {d}/{b}")

# for index in range(1,one()+1):
#     r = one()
#     x_min=1000
#     x_max=-1000
#     y_min=1000
#     y_max=-1000
#     for _ in range(r):
#         a,b = map(float,inputing().split())
#         x_min = min(x_min,a)
#         x_max = max(x_max,a)
#         y_min = min(y_min,b)
#         y_max = max(y_max,b)
#     x_index = x_max-x_min
#     y_index = y_max-y_min
#     area = x_index*y_index
#     perimeter = x_index*2+y_index*2
#     print(f"Case {index}: Area {area}, Perimeter {perimeter}")

# for index in range(1,one()+1):
#     a,b = wow()
#     time = (a*3600+b*60-(45*60))%(3600*24)
#     h = time//3600
#     m = (time - 3600*h)//60
#     print(f"Case #{index}: {h} {m}") 

# for index in range(1,one()+1):
#     n_list = list(wow())
#     max_max = max(n_list)
#     print(f"Case #{index}: {max_max}")

# for _ in range(one()):
#     a = one()
#     cnt = 0
#     for i in range(1,a+1,2):
#         cnt+=i
#     print(cnt)

for index in range(1,one()+1):
    n_list = sorted(list(wow()))
    if n_list[0]**2+n_list[1]**2==n_list[2]**2:
        print(f"Case #{index}: YES")
    else:
        print(f"Case #{index}: NO")


