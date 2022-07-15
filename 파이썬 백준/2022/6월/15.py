from re import L
import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# l = one()
# n_list = list(wow())
# x,y = 0,0
# for i in range(l-1,0,-1):
#     b=n_list[i]
#     a=n_list[i-1]
#     if a<b:
#         x = i-1
#         y = i
#         for index in range(l-1,0,-1):
#             c = n_list[index]
#             if a<c:
#                 n_list[x],n_list[index]=n_list[index],n_list[x]
#                 new_list = n_list[:x+1]+sorted(n_list[y:])
#                 print(*new_list)
#                 exit()
# print(-1)

# l = one()
# n_list = list(wow())
# for i in range(l-1,0,-1):
#     a = i-1
#     b = i
#     if n_list[a]>n_list[b]:
#         for index in range(l-1,0,-1):
#             if n_list[a]>n_list[index]:
#                 n_list[a],n_list[index]=n_list[index],n_list[a]
#                 new_list = n_list[:a+1]+sorted(n_list[a+1:],reverse=True)
#                 print(*new_list)
#                 exit()
# print(-1)
# import string
# a_dict = {}
# a_list = list(string.ascii_uppercase) 
# answer = {}
# for i in range(len(a_list)):
#     a_dict[a_list[i]]=i
# for _ in range(one()):
#     str_str = list(inputing())
#     if str_str == sorted(str_str,reverse=True):
#         answer["".join(str_str)]="".join(str_str)
#     else:
#         for i in range(len(str_str)-1,0,-1):
#             if a_dict[str_str[i-1]]<a_dict[str_str[i]]:
#                 for index in range(len(str_str)-1,0,-1):
#                     if a_dict[str_str[i-1]]<a_dict[str_str[index]]:
#                         str_str[i-1],str_str[index]=str_str[index],str_str[i-1]
#                         new_list = str_str[:i]+sorted(str_str[i:])
#                         if "".join(str_str) not in answer:
#                             answer["".join(str_str)]="".join(new_list)
#                             break
#                         else:
#                             break
#             if "".join(str_str) in answer:
#                 break
# for i in answer.values():
#     print(i)

for _ in range(one()):
    l = one()
    n_list=list(wow())
    visited=[0]*l
    for i in range(l):
        if n_list[i]>n_list[(l-1)-i]:
            if visited[i] ==0:
                n_list[i],n_list[(l-1)-i]=n_list[(l-1)-i],n_list[i]
                visited[i]=1
                visited[l-1-i]=1
        print(n_list)
    if n_list == sorted(n_list):
        print("YES")
    else:
        print("NO")



















