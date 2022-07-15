# from collections import deque


# l = int(input())
# n_list = list(map(int,input().split()))
# n_sort = sorted(n_list)
# stack = deque([])
# list_list = []
# index = 0
# i = 0
# while i != l:
#     if n_list[i] == n_sort[index]:
#         list_list.append(n_list[i])
#         index+=1
#         i+=1
#     elif len(stack) > 0 and stack[-1] == n_sort[index]:
#         list_list.append(stack.pop())
#         index+=1
#     else:
#         stack.append(n_list[i])
#         i+=1
#     # print(list_list,stack)
# if stack:
#     for _ in range(len(stack)):
#         list_list.append(stack.pop())
# if list_list == n_sort:
#     print("Nice")
# else:
#     print("Sad")
# cnt=0
# for _ in range(int(input())):
#     stack = []
#     answer = list(input())
#     for i in answer:
#         if stack :
#             if stack[-1] == i:
#                 stack.pop()
#             else:
#                 stack.append(i)
#         else:
#             stack.append(i)
#     if len(stack) == 0:
#         cnt+=1

# print(cnt)

        










