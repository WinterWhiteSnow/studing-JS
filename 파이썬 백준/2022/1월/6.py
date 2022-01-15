# import sys
# from collections import deque

# wow = int(sys.stdin.readline().rstrip())
# num_list = deque([i for i in range(1,wow+1)])
# a_list = deque()
# for _ in range(wow):
#     d = int(sys.stdin.readline().rstrip())
#     a_list.append(d)
# how = deque()

# new_list = deque()
# text = deque()

# a_num = 0

# while True:
#     if num_list[0] <= a_list[a_num]:
#         # print("첫번째",num_list[0],"a_num:",a_num,a_list[a_num])
#         a = num_list.popleft()
#         new_list.append(a)
#         text.append("+")
#         if len(num_list) == 0:
#             for _ in range(len(new_list)):
#                 how.append(new_list.pop())
#                 text.append("-")
#             break
#     else:
#         # print("두번째",new_list[-1],a_list[a_num])
#         if new_list[-1] == a_list[a_num]:
#             how.append(new_list.pop())
#             text.append("-")
#             a_num+=1
#         else:
#             break
# if a_list == how:
#     print("\n".join(map(str,text)))
# else:
#     print("NO")
