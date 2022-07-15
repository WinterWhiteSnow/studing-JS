# import sys
# from collections import deque
# r = lambda :int(sys.stdin.readline().rstrip())
# num_range = r()
# repeat = r()
# n_list = []
# graph = [[]]*(num_range+1)
# for _ in range(repeat):
#     n_list.append(list(map(int,sys.stdin.readline().rstrip().split())))
# for i in range(1,num_range+1):
#     list_list = []
#     for index in n_list:
#         if i in index:
#             list_list.extend(index)
#     list_list = set(list_list)
#     if i in list_list:
#         list_list.remove(i)
#     graph[i]=list_list
# if graph[1]:
#     visited = [False]*(num_range+1)
#     def bfs(graph,start,visited):
#         queue=deque([start])
#         visited[start] = True
#         cnt = 0
#         while queue:
#             for _ in range(len(queue)):
#                 b = queue.popleft()
#                 for i in graph[b]:
#                     if not visited[i]:
#                         queue.append(i)
#                         visited[i]=True
#             cnt+=1
#             if cnt == 2:
#                 break
#     bfs(graph,1,visited)
#     print(visited.count(True)-1)
# else:
#     print(0)
from collections import deque
r = int(input())
n_list = []
for _ in range(r):
    n_list.append(list(map(int,input().split())))
dx = [0,0,-1,1]
dy = [1,-1,0,0]
def bfs(x,y):
    queue = deque()
    queue.append((x,y)) 
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            print(nx,ny)
            if nx <=-1 or nx>=r or ny<=-1 or ny>=r:
                continue
            if n_list[nx][ny] == 0:
                continue
            if n_list[nx][ny] == 1:
                n_list[nx][ny] = n_list[x][y]+1
                queue.append((nx,ny))
    return n_list[nx][ny]
for x in range(r):
    for y in range(r):
        print(bfs(x,y))       













