import sys


inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# n,m = wow()
# date = list(wow())

# result=0
# summary=0
# end=0
# for start in range(n):
#     while summary<m and end<n:
#         summary+=date[end]
#         end+=1
#     if summary==m:
#         result+=1
#     summary-=date[start]
# print(result)

# l = one()
# n_list = list(wow())
# n_list.sort()
# total = one()
# result = 0
# start=0
# end=l-1
# while start<end:
#     if n_list[start]+n_list[end] == total:
#         result+=1
#         start+=1
#         end-=1
#     if n_list[start]+n_list[end] < total:
#         start+=1
#     if n_list[start]+n_list[end] > total:
#         end-=1
# print(result)

# l = one()
# goal = one()
# n_list = list(wow())
# n_list.sort()
# start=0
# end = l-1
# result = 0
# while start<end:
#     if n_list[start]+n_list[end]==goal:
#         result+=1
#         start+=1
#         end-=1
#     if n_list[start]+n_list[end]<goal:
#         start+=1
#     if n_list[start]+n_list[end]>goal:
#         end-=1
#     # print(start,end,result)
# print(result)
        
    

















