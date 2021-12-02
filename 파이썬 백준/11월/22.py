# import sys
# from collections import deque
# sys.setrecursionlimit(10**6)
# Tree,M = map(int, sys.stdin.readline().rstrip().split())
# a = list(map(int, sys.stdin.readline().rstrip().split()))
# a.sort()
# mini = a[0]
# maxi = a[-1]
# limits = []
# def wow(mini,maxi):
#     o = 0
#     limit = (mini+maxi)//2
#     # print("시작",o,mini,maxi,limit)
#     for i in a:
#         # print("i",i)
#         if i >= limit:
#             o+=i-limit
#             # print("for",o,limit)
#     if o == M or limit<=M<=limit+1:  
#         # print("목표",M,limit) 
#         limits.append(limit)
#         return 
#     elif o < M :
#         # print("o<M",mini,maxi,limit)
#         wow(mini,limit-1)
#     elif o > M:
#         # print("o>M",mini,maxi,limit)
#         wow(limit+1,maxi)
    
# if len(a) == Tree:
#     wow(mini,maxi)
#     print(limits[0])
            