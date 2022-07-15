# from collections import deque

# n,m,start = map(int,input().split())
# n_list = []
# number = []
# for _ in range(m):
#     wow = list(map(int,(input().split())))
#     n_list.append(wow)
#     number.extend(wow)

# graph = [
#     []
# ]*(n+1)
# for i in set(number):
#     list_list = []
#     for index in n_list:
#         if i in index:
#             list_list.extend(index)
#     list_list = list(set(list_list))
#     del list_list[list_list.index(i)]
#     graph[i]=list_list
    
# for i in range(len(graph)):
#     graph[i].sort()
    
# visited = [False]*(n+1)

# def dfs(graph, number, visited):
#     visited[number]=True
#     print(number,end=" ")
#     for i in graph[number]:
#         if not visited[i]:
#             dfs(graph, i, visited)
            
# dfs(graph,start,visited)    
# print()
# visited = [False]*(n+1)
# def bfs(graph, number, visited):
#     queue = deque([number])
#     visited[number] = True
#     while queue:
#         element = queue.popleft()
#         print(element, end=" ")
#         for i in graph[element]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True
# bfs(graph,start,visited)

# from collections import deque

# r,l = map(int,input().split())
# graph = []

# for _ in range(r):
#     graph.append(list(map(int,list(input()))))

# dx = [0,0,-1,1]
# dy = [1,-1,0,0]

# def bfs(x,y):
#     queue= deque()
#     queue.append((x,y))
#     while queue:
#         x,y = queue.popleft()
#         for i in range(4):
#             nx = x+dx[i]
#             ny = y+dy[i]
#             if nx < 0 or nx >= r or ny <0 or ny >=l:
#                 continue
#             if graph[nx][ny] == 0:
#                 continue
#             if graph[nx][ny] == 1:
#                 graph[nx][ny] = graph[x][y]+1
#                 queue.append((nx,ny))
#     return graph[r-1][l-1]

# print(bfs(0,0))

# number = int(input())
# n_list = []
# for _ in range(int(input())):
#     n_list.append(list(map(int,input().split())))
    
# graph = [[]]*(number+1)

# for i in range(1,number+1):
#     list_list = []
#     for index in n_list:
#         if i in index:
#             list_list.extend(index)
#     list_list=sorted(list(set(list_list)))
#     if i in list_list:
#         list_list.remove(i)
#     graph[i]=list_list
# visited = [False]*(1+number)
# def dfs(graph, start, visited):
#     visited[start]=True
#     for i in graph[start]:
#         if not visited[i]:
#             dfs(graph,i,visited)
# dfs(graph,1,visited)
# print(visited.count(True)-1)

# import sys
# sys.setrecursionlimit(10**9)
# def dfs(x,y,garo,sero):
#     if x<=-1 or x>=sero or y<=-1 or y>=garo:
#         return False
#     if graph[y][x] == 1:
#         graph[y][x] = 0
#         dfs(x-1,y,garo,sero)
#         dfs(x+1,y,garo,sero)
#         dfs(x,y+1,garo,sero)
#         dfs(x,y-1,garo,sero)
#         return True
#     return False

# repeat = int(input())
# for _ in range(repeat):
#     sero,garo,r = map(int,input().split())
#     graph = [[0]*garo for _ in range(sero)]
#     for _ in range(r):
#         y,x = map(int,input().split())
#         graph[y][x] = 1
#     result = 0
#     for x in range(garo):
#         for y in range(sero):
#             if dfs(x,y,sero,garo)==True:
#                 result+=1
#     print(result)

import sys
sys.setrecursionlimit(10**9)
sero,garo,r = map(int,input().split())
grahp = [[0]*garo for _ in range(sero)]
for _ in range(r):
    start_x,start_y,end_x,end_y = map(int,input().split())
    for x in range(start_x,end_x):
        for y in range(start_y,end_y):
            grahp[y][x]="x"
grahp = grahp[::-1]

def dfs(x,y,cnt,count):
    if x<0 or x>=sero or y<0 or y>=garo:
        return False
    if grahp[x][y] == 0:
        grahp[x][y] = cnt
        count+=1
        dfs(x-1,y,cnt,count)
        dfs(x+1,y,cnt,count)
        dfs(x,y-1,cnt,count)
        dfs(x,y+1,cnt,count)
        return True
    return count

cnt=0
cnt_number = 0
for x in range(garo):
    for y in range(sero):
        print(dfs(x,y,cnt,cnt_number))
        if dfs(x,y,cnt,cnt_number) == True:
            cnt+=1
# cnt_set = [i for i in range(1,cnt+1)]

# list_list = []
# for index in cnt_set:
#     count = 0
#     for i in grahp:
#         count+=i.count(index)
#     list_list.append(count)
# list_list.sort()
# print(cnt)
# print(*list_list)
    













