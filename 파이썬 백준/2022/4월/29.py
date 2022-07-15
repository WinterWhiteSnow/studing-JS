import sys
wow = lambda : map(int,sys.stdin.readline().rstrip().split())
# for _ in range(int(input())):
#     a,b = wow()
#     a_list = list(wow())
#     b_list = list(wow())
#     a_list.sort()
#     b_list.sort()
#     cnt = 0
#     for a_index in a_list:
#         start = 0
#         end = b-1
#         while start<=end:
#             mid = (start+end)//2
#             if a_index > b_list[mid]:
#                 start=mid+1
#             else:
#                 end = mid-1
#             # print(start,end,mid)
#         # print("wow",a_index,b_list[end],end) 
#         cnt+=end+1
#     print(cnt)

# m,n = wow()
# n_list = list(wow())
# n_list.sort()
# start= 1
# end = n_list[-1]
# while start<=end:
#     mid = (start+end)//2
#     cnt = 0
#     for index in n_list:
#         cnt+=index//mid
#     if cnt < m:
#         end = mid-1
#     else:
#         start= mid+1
# if end*m > sum(n_list):
#     print(0)
# else:
#     print(end)
# import math
# length = int(input())
# n = int(input())
# n_list = list(wow())
# if n <2:
#     print(max(abs(n_list[0]-0),length-n_list[0]))
# else:
#     n_list.sort()
#     gap = 0
#     for i in range(len(n_list)-1):
#         if gap < math.ceil((n_list[i+1]-n_list[i])/2):
#             gap = math.ceil((n_list[i+1]-n_list[i])/2)
#     print(max(gap,abs(0-n_list[0]),length-n_list[-1]))

standard,r = wow()
dict_list = {}
for _ in range(standard):
    name,score = sys.stdin.readline().rstrip().split()
    score = int(score)
    dict_list[name]=score
    
list_list.sort(key=lambda x: x[1])
for _ in range(r):
    mark = int(sys.stdin.readline().rstrip())
    for index in list_list:
        if mark<=index[1]:
            print(index[0])
            break
    














