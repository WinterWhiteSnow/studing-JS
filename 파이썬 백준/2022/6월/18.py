import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# a = inputing()
# if a == a[::-1]:
#     print(len(a))
# else:
#     max_pal = 0
#     if len(a)%2 == 0:
#         end = len(a)-1
#     else:
#         end = len(a)
#     for i in range(end):
#         y = a[i+1:]
#         if y == y[::-1]:
#             max_pal = max(max_pal,len(y))    
#             print(y)
#     print(len(a)+len(a)-max_pal)

# from itertools import combinations
# l = one()
# n_list = list(wow())
# list_list = {}
# for i in range(1,l+1):
#     a = list(combinations(n_list,r=i))
#     for i in a:
#         list_list[sum(i)]=1
# key_list=sorted(list(list_list.keys()))
# # print(key_list)
# check_list = [i for i in range(1,key_list[-1]+1)]
# difference = set(check_list)-set(key_list)     
# if difference:
#     print(sorted(list(difference))[0])
# else:
#     print(key_list[-1]+1)

l = one()
minus_hp=list(wow())
get_happy=list(wow())
sort_list = []
for a,b in zip(minus_hp,get_happy):
    sort_list.append((a,b))
sort_list.sort(key=lambda x : x[1],reverse=True)
sort_list.sort(key= lambda x : x[0])
print(sort_list)
zero_list = [0]*101















