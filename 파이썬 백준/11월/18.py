# end, step = map(int,input().split())

# a = [i for i in range(1,end+1)]
# step = step-1 #0
# a_list = []
# count = 0
# while len(a_list) < end:
#     # print("a_list",a_list)
#     # print("a",a)
#     if len(a) > step:
#         for i in range(step, end, step+1):
#             # print("i",i)
#             if len(a)-1 >=i:
#                 wow = a[i]
#                 a_list.append(wow)
#                 count = i
#         a = a[count:]+a[:count]
#         # print("재설정 이전 a",a)
#         b = []        
#         for i in a:
#             if i not in a_list:
#                 b.append(i)
#         # print("완료 b",b)
#         a = b
#     else:
#         if len(a) > 1:
#             o = step+1
#             no = o%len(a) -1
#             a_list.append(a[no])
#             a = a[no:]+a[:no]
#             # print("else 재설정 이전 a",a)
#             b = []        
#             for i in a:
#                 if i not in a_list:
#                     b.append(i)
#             # print("else 완료 b",b)
#             a = b
#         else:
#             a_list.append(a[0])
# a_list = [str(i) for i in a_list]
# print("<"+", ".join(a_list)+">")
# 백준기준 31556위

# import sys
# the_num = int(sys.stdin.readline().rstrip())
# a_list = []
# for i in range(the_num):
#     a_list.append(int(sys.stdin.readline().rstrip()))
# a_list.sort()
# a_list = [str(i) for i in a_list]
# print("\n".join(a_list))

# import sys
# the_num = int(sys.stdin.readline().rstrip())
# a_list = [0]*10000
# for _ in range(the_num):
#     a = int(sys.stdin.readline().rstrip())
#     a_list[a-1]+=a
# for i in range(1,10000+1):
#     if a_list[i-1] != 0:
#         for a in range(1,a_list[i-1]//i+1):
#             print(i)
#백준 30376등

# import sys
# from collections import deque

# the_num = int(sys.stdin.readline().rstrip())
# deq = deque([i for i in range(1,the_num+1)])
# while len(deq) > 1:
#     deq.popleft()
#     deq.rotate(-1)
# print(deq[0])


# import sys
# from collections import deque

# the_num = int(sys.stdin.readline().rstrip())
# deq = deque([i for i in range(1,the_num+1)])

# deq.rotate(-2)
# print(deq)

# import sys
# from collections import deque
# the_num = int(sys.stdin.readline().rstrip())
# deq = deque([])
# for _ in range(the_num):
#     b = sys.stdin.readline().rstrip().split()
#     if b[0] == "push":
#         deq.append(b[1])
#     elif b[0] == "pop":
#         if len(deq) > 0:
#             print(deq.popleft())            
#         else:
#             print(-1)
#     elif b[0] == "size":
#         print(len(deq))
#     elif b[0] == "empty":
#         if len(deq) == 0:
#             print(1)
#         else:
#             print(0)
#     elif b[0] == "front":
#         if len(deq) > 0:
#             print(deq[0])
#         else:
#             print(-1)
#     elif b[0] == "back":
#         if len(deq) > 0:
#             print(deq[-1])
#         else:
#             print(-1)



# import sys
# from collections import deque
# the_num = int(sys.stdin.readline().rstrip())
# deq = deque([])
# for _ in range(the_num):
#     b = sys.stdin.readline().rstrip().split()
#     if b[0] == "push":
#         deq.append(b[1])
#     elif b[0] == "pop":
#         if len(deq) > 0:
#             print(deq.pop())            
#         else:
#             print(-1)
#     elif b[0] == "size":
#         print(len(deq))
#     elif b[0] == "empty":
#         if len(deq) == 0:
#             print(1)
#         else:
#             print(0)
#     elif b[0] == "top":
#         if len(deq) > 0:
#             print(deq[-1])
#         else:
#             print(-1)

import sys
from collections import deque
the_num = int(sys.stdin.readline().rstrip())
a_list = deque([])
for _ in range(the_num):
    a = int(sys.stdin.readline().rstrip())
    a_list.append(a)
# 백준 29240위