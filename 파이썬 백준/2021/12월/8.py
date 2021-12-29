# import sys
# from collections import deque

# sero,garo = map(int, sys.stdin.readline().rstrip().split())
# wow = deque()
# for _ in range(sero):
#     o = sys.stdin.readline().rstrip()
#     wow.append(o)
# list_list = []
# for y in range(sero-7):
#     for x in range(garo-7):
#         w = 0
#         b = 0
#         for a in range(y,y+8):
#             for c in range(x,x+8):
#                 if (a+c)%2 == 0:#W으로 시작한다고 가정
#                     if wow[a][c] != "W": # == B: -> W로 시작해야하니
#                         w+=1
#                     if wow[a][c] != "B": # == W:
#                         b+=1
#                 else:#B으로 시작한다고 가정
#                     if wow[a][c] != "B": # == W: -> B로시작해야하니
#                         w+=1
#                     if wow[a][c] != "W": # == B:
#                         b+=1
#         list_list.append(w)
#         list_list.append(b)
# print(min(list_list))

import sys

num,repeat = map(int, sys.stdin.readline().rstrip().split())

for x in range(1,num+1):
    for y in range(1,repeat+1):
        