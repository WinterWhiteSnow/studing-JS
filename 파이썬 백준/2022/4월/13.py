# from collections import deque
# import sys

# num_range = int(sys.stdin.readline().rstrip())
# gx,gy = map(int,sys.stdin.readline().rstrip().split())
# r = int(sys.stdin.readline().rstrip())
# n_list = []
# extend_number = []
# for _ in range(r):
#     wow = list(map(int,sys.stdin.readline().rstrip().split()))
#     n_list.append(wow)
#     extend_number.extend(wow)
# if num_range < max(gx,gy):
#     print(-1)
# else:
#     graph = [[]]*(num_range+1)
#     for number in range(1,num_range+1):
#         number_list = []
#         for n_element in n_list:
#             if number in n_element:
#                 number_list.extend(n_element)
#         number_list = set(number_list)
#         if number in number_list:
#             number_list.remove(number)
#         graph[number]=number_list
#     visited = [False]*(num_range+1)

#     def bfs(graph,start,end,visited):
#         queue = deque([start])
#         visited[start] = True
#         cnt = 0
#         check = "no"
#         while queue:
#             for _ in range(len(queue)):
#                 b = queue.popleft()
#                 for i in graph[b]:
#                     if not visited[i]:
#                         queue.append(i)
#                         visited[i]=True
#             if end in queue:
#                 check = "yes"
#                 cnt+=1
#                 break
#             else:
#                 cnt+=1
#         return cnt,check

#     count,check = bfs(graph,gx,gy,visited)
#     if check == "yes":
#         print(count)
#     else:
#         print(-1)

# from collections import deque
# import sys
# num_range,r = map(int,sys.stdin.readline().rstrip().split())
# n_list = []
# for _ in range(r):
#     wow = list(map(int,sys.stdin.readline().rstrip().split()))
#     n_list.append(wow)
# graph = [[]]*(num_range+1)
# for number in range(1,num_range+1):
#     number_list = []
#     for n_element in n_list:
#         if number in n_element:
#             number_list.extend(n_element)
#     number_list = set(number_list)
#     if number in number_list:
#         number_list.remove(number)
#     graph[number]=number_list

# def bfs(graph,start):
#     visited = [False]*(num_range+1)
#     queue = deque([start])
#     visited[start] = True
#     cnt = 1
#     count = 0
#     while queue:
#         for _ in range(len(queue)):
#             b = queue.popleft()
#             for i in graph[b]:
#                 if not visited[i]:
#                     queue.append(i)
#                     visited[i]=True
#         for _ in range(len(queue)):
#             count+=cnt
#         cnt+=1
#     return start,count
# list_list = []
# for i in range(1,num_range+1):
#     number,count = bfs(graph,i)
#     list_list.append((number,count))
# list_list.sort(key=lambda x : (x[1],x[0]))
# print(list_list[0][0])

# n,k = map(int,input().split())
# result = 0
# while True:
#     if k < n:
#         print(-1)
#         break
#     if n == k:
#         print(result+1)
#         break
#     if k%2 != 0:
#         if str(k)[-1] == "1":
#             k=int(str(k)[:-1])
#             result+=1
#         else:
#             print(-1)
#             break
#     else:
#         k //=2
#         result+=1
#     # print(n,k,result)


















