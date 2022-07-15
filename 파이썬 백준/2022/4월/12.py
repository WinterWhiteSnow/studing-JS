# import sys
# sys.setrecursionlimit(10**7)
# def dfs(x,y):
#     if x <= -1 or x >=r or y <=-1 or y >=l:
#         return False
#     if graph[x][y] == 1:
#         graph[x][y] = 0
#         dfs(x-1,y-1)
#         dfs(x,y-1)
#         dfs(x+1,y-1)
#         dfs(x-1,y)
#         dfs(x+1,y)
#         dfs(x-1,y+1)
#         dfs(x,y+1)
#         dfs(x+1,y+1)        
#         return True
#     return False     


# while True:
#     l,r = map(int,input().split())
#     if l == r == 0:
#         break
#     graph = []
#     for _ in range(r):
#         graph.append(list(map(int,input().split())))
#     result = 0
#     for x in range(r):
#         for y in range(l):
#             if dfs(x,y) == True:
#                 result += 1
#     print(result)
# import sys
# import copy
# sys.setrecursionlimit(10**7)
# r = int(input())
# graph = []
# max_number = []
# for _ in range(r):
#     wow = list(map(int,input().split()))
#     graph.append(wow)
#     max_number.append(max(wow))
# def dfs(x,y,number):
#     if x < 0 or x >= r or y < 0 or y>= r:
#         return False
#     if now_graph[x][y] != 0:
#         now_graph[x][y] = 0
#         dfs(x+1,y,number)
#         dfs(x-1,y,number)
#         dfs(x,y+1,number)
#         dfs(x,y-1,number)
#         return True
#     return False
# max_cnt = 0
# for number in range(max(max_number)): 
#     result = 0     
#     for x in range(r):
#         for y in range(r):
#             if graph[x][y] <= number:
#                 graph[x][y] = 0
#     now_graph = copy.deepcopy(graph)
#     for x in range(r):
#         for y in range(r):
#             if dfs(x,y,number) == True:
#                 result+=1
#     if result > max_cnt:
#         max_cnt = result
# print(max_cnt)
import sys
r = int(sys.stdin.readline().rstrip())
n_dict = {}
max_number = 0
for _ in range(r-1):
    a,b = (sys.stdin.readline().rstrip().split())
    if a not in n_dict:
        n_dict[a] = b
    if b not in n_dict:
        n_dict[b] = a
    if max_number < max(int(a),int(b)):
        max_number = max(int(a),int(b))
for i in range(2,max_number+1):
    if str(i) in n_dict:
        print(n_dict[str(i)])
    else:
        print(0)
            
            
        
















