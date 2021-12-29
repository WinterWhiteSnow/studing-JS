# import sys

# a,b,c = map(int, sys.stdin.readline().rstrip().split())
# if c-b > 0:
#     x = a/(c-b)
#     if x > 0:
#         print(int(x+1))
# else:
#     print(-1)

# import sys

# a = int(sys.stdin.readline().rstrip())
# num = 0
# wow = 0
# while num < a:
#     wow +=1
#     num+=wow
# gap = a-(num-wow)
# total = wow+1
# if wow%2 == 0: #wow 짝수 증가 -> 분자up 분모down
#     top = gap
#     bottom = total-top
#     print(f"{top}/{bottom}")
# else: #wow홀수 감소 -> 분자 down 분모 up
#     bottom = gap
#     top = total-bottom
#     print(f"{top}/{bottom}")
    
# import sys
# import math

# run,back,goal = map(int, sys.stdin.readline().rstrip().split())
# goal = goal-run
# wow = run-back
# answer = goal/wow
# print(math.ceil(answer)+1)

import sys

a = int(sys.stdin.readline().rstrip())
b = []
for _ in range(a):
    floor,room,number = map(int, sys.stdin.readline().rstrip().split())
    if number%floor == 0:
        a_floor = number//floor
        a_room = floor
    else:
        a_floor = number//floor +1
        a_room = number%floor
    if a_room < 10 :
        a_room = f"0{a_room}"
    wow = f"{a_floor}{a_room}"
    print(wow)
    b.append(wow)
for i in b:
    print(i)
