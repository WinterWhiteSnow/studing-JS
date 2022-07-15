import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# r = one()
# cnt = 0
# n_dict = {}
# min_start = 1000001
# for _ in range(r):
#     a,b = wow()
#     cnt+=a
#     if b not in n_dict:
#         n_dict[b]=a
#     else:
#         n_dict[b]+=a
# if cnt <= 1000000:
#     n_list = list(map(list,n_dict.items()))
#     n_list.sort(key=lambda x : x[0],reverse=True)
#     for i in range(len(n_list)-1):
#         end = n_list[i][0] 
#         start = n_list[i][1]
#         if end-start < n_list[i+1][0]:
#             n_list[i+1][0]=end-start
#     for i in n_list:
#         end=i[0]
#         start=i[1]
#         if end>=start:
#             min_start=min(min_start,end-start)
#         else:
#             print(-1)
#             exit()
#     print(min_start)
# else:
#     print(-1)

    
















