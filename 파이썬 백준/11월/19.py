# import sys
# a,b,c = map(int,sys.stdin.readline().rstrip().split())
# days=((c-a)/(a-b))+1
# if days == round(days):
# 	print(int(days))
# else:
# 	print(int(days)+1)

# import sys
# from collections import deque
# the_num = int(sys.stdin.readline().rstrip())
# deq = deque([])
# for _ in range(the_num):
#     b = sys.stdin.readline().rstrip().split()
#     if b[0] == "push_front":
#         deq.appendleft(b[1])
#     elif b[0] == "push_back":
#         deq.append(b[1])
#     elif b[0] == "pop_front":
#         if len(deq) > 0:
#             print(deq.popleft())            
#         else:
#             print(-1)
#     elif b[0] == "pop_back":
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

# the_num = int(sys.stdin.readline().rstrip())
# sanguen = sys.stdin.readline().rstrip().split()
# a_num = int(sys.stdin.readline().rstrip()) 
# check = sys.stdin.readline().rstrip().split()
# dict_sanguen = {}
# if len(sanguen) == the_num and len(check) == a_num:
#     for i in sanguen:
#         if i not in dict_sanguen:
#             dict_sanguen[i]=1
#         else:
#             dict_sanguen[i]+=1

#     for i in check:
#         if i in dict_sanguen:
#             wow = str(dict_sanguen[i])
#         else:
#             wow ="0"
#         print(wow, end=" ")
# a = {"1":"no"}
# print("wow" if "2" in a else "Xq")
# a = [1,2,3,4,5,7]
# print(i for i in a) <generator object <genexpr> at 0x0000024CC2911740>
# import sys
# list_list = []
# repeat = int(sys.stdin.readline().rstrip())
# for _ in range(repeat):
#     a = sys.stdin.readline().rstrip()
#     list_list.append(a)
# for i in list_list:
#     for a in range(len(i)+1):
#         i = "".join(i).split("()")
#     wow = len("".join(i))
#     if wow == 0:
#         print("YES")
#     else:
#         print("NO")
#백준 기준 28160위