import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# r = one()
# for index in range(1,r+1):
#     n_list = sorted(list(wow())[1:],reverse=True)
#     gap = 0
#     for i in range(len(n_list)-1):
#         gap = max(gap,abs(n_list[i]-n_list[i+1]))
#     print(f"Class {index}")
#     print(f"Max {n_list[0]}, Min {n_list[-1]}, Largest gap {gap}")

# start,end = wow()
# n_dict = {"0":"zero","1":"one","2":"two","3":"three","4":"four","5":"five","6":"six","7":"seven","8":"eight","9":"nine"}
# str_list = {}
# for i in range(start,end+1):
#     str_str = ""
#     for n in list(str(i)):
#         if str_str == "":
#             str_str+=n_dict[n]
#         else:
#             str_str+=" "+n_dict[n]
#     str_list[i]=str_str
# list_list =sorted(str_list.items(),key=lambda x : x[1])
# cnt = 1
# for i in list_list:
#     if cnt == 10:
#         print(i[0])
#         cnt=1
#     else:
#         print(i[0],end=" ")
#         cnt+=1

# r=one()
# n_list = sorted([one() for _ in range(r)])
# for i in n_list:
#     print(i)
# n_list = []
# for _ in range(one()):
#     a = inputing()
#     if a.isdigit():
#         n_list.append(int(a))
#     else:
#         str_str = ""
#         for i in list(a):
#             if i.isdigit():
#                 str_str+=i
#             else:
#                 if str_str:
#                     n_list.append(int(str_str))
#                     str_str=""
#         if str_str:
#             n_list.append(int(str_str))
# for i in sorted(n_list):
#     print(i)













