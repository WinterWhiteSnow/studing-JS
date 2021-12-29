# import sys

# a = int(sys.stdin.readline().rstrip())
# b = []
# for _ in range(a):
#     floor,room,number = map(int, sys.stdin.readline().rstrip().split())
#     a_floor =number%floor
#     a_room = number/floor
#     if a_floor == 0:
#         a_floor = floor
#     if int(a_room) != a_room:
#         a_room = int(a_room)+1
#     a_room = int(a_room)
#     if a_room < 10 :
#         a_room = f"0{a_room}"
#     wow = f"{a_floor}{a_room}"
#     b.append(wow)
# for i in b:
#     print(i)

# import sys

# num = int(sys.stdin.readline().rstrip())


# for _ in range(num):
#     floor = int(sys.stdin.readline().rstrip())
#     room = int(sys.stdin.readline().rstrip())
#     person = [i for i in range(1,room+1)]
#     a = []
#     for _ in range(floor):
#         for i in range(room):
#             a.append(sum(person[:i+1]))
#         for b in range(len(a)):
#             person[b]= a[b]
#         a=[]
#     print(person[-1])   

import sys

num = int(sys.stdin.readline().rstrip())
if num%3 == 2:
    a=num//5
