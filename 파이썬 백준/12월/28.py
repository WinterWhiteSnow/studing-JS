# import sys

# x,y,w,h = map(int, sys.stdin.readline().rstrip().split())
# a = [x,y,w-x,h-y]
# a.sort()
# print(a[0])

# import sys

# x_list = {}
# y_list = {}

# for _ in range(3):
#     x,y = map(int, sys.stdin.readline().rstrip().split())
#     if x not in x_list:
#         x_list[x]=1
#     else:
#         x_list[x]+=1
#     if y not in y_list:
#         y_list[y]=1
#     else:
#         y_list[y]+=1

# x = list(filter(lambda x : x[1] == 1, x_list.items()))
# y = list(filter(lambda x : x[1] == 1, y_list.items()))
# print(x[0][0],y[0][0])

import sys

while True:
    x,y,h = map(int, sys.stdin.readline().rstrip().split())
    if x == 0:
        break
    a = x**2+y**2
    if a == h**2:
        print("right")
    else:
        print("wrong")