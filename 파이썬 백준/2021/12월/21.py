# import sys

# repeat = int(sys.stdin.readline().rstrip())
# for _ in range(repeat):
#     list_list = []
#     floor = int(sys.stdin.readline().rstrip())
#     room = int(sys.stdin.readline().rstrip())
#     default = [int(i) for i in range(1,room+1)]
#     for a in range(floor):
#         for b in range(room):
#             if b > 0:
#                 default[b] = default[b-1]+default[b]
#                 # print(default)
#     print(default[room-1])        

# import sys
# a = sys.stdin.readline().rstrip()
# if len(a) >1:
#     number = int(a[:-1]+"0")//5
#     num = int(a[-1])
#     while num%3 != 0:
#         number-=1
#         num +=5
#     num = num//3
#     if num >= 5:
#         number += num//5*3
#         num = num%5       
#     print(number+num)
# else:
#     a = int(a)
#     if a%5 == 0:
#         print(a//5)
#     elif a%3 == 0:
#         print(a//3)
#     elif a%8 == 0:
#         print(a//8*2)
#     else:
#         print(-1)
        
import sys

the_num = int(sys.stdin.readline().rstrip())
for _ in range(the_num):
    start,end = map(int, sys.stdin.readline().rstrip().split())
    move = [0,1,2]
    end = end-2
    count = 2
    print(end-start)

