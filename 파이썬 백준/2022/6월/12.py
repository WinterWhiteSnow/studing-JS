import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# n = one()
# zero_list = []
# for i in range(n):
#     if i == 0:
#         zero_list = sorted(list(wow()))
#     else:
#         for i in list(wow()):
#             if zero_list[0]<i:
#                 zero_list[0]=i
#                 zero_list.sort()
#     # print(zero_list)
# print(zero_list[0])

# r = one()
# n_list = [one() for _ in range(r)]
# n_list.sort()
# max_cnt = 0
# max_start = 0
# max_end = 0
# # print(n_list)
# for start in range(r):
#     end = start+1
#     cnt = 0
#     while True:
#         if end <= r-1:
#             if n_list[end]-n_list[start] <=4:
#                 end+=1
#                 cnt+=1
#             else:
#                 if cnt > max_cnt:
#                     max_start=start
#                     max_end=end
#                     max_cnt=cnt
#                 break
#         else:
#             if cnt > max_cnt:
#                 max_start=start
#                 max_end=end-1
#                 max_cnt=cnt
#             break
#         # print(max_cnt,max_start,max_end)
# # print(max_cnt,max_start,max_end)
# print(4-max_cnt if 4-max_cnt >= 0 else 0)

# l,k = wow()
# n_list = list(wow())
# a_list = sorted(n_list)
# print(sum(a_list[-k:])-sum([i for i in range(1,k)]))

# r,min_l=wow()
# n_list = [inputing() for _ in range(r)]
# n_dict = {}
# for i in n_list:
#     if i not in n_dict:
#         n_dict[i]=1
#     else:
#         n_dict[i]+=1
# list_list = [i for i in n_dict.items() if len(i[0])>=min_l]
# list_list.sort(key=lambda x : x[0])
# list_list.sort(key=lambda x : (x[1],len(x[0])),reverse=True)
# for i in list_list:
#     print(i[0])

# n_list = []
# r = "none"
# str_str = ""
# for i in sys.stdin.read():
#     if i.isdigit():
#         str_str+=i
#     else:
#         if str_str.isdigit():
#             if r == "none":
#                 r = int(str_str)
#             else:
#                 n_list.append(int(str_str[::-1]))
#         str_str=""
# n_list.sort()
# for i in n_list:
#     print(i)

