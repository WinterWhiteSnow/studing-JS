# sosu_list = []
# n,times = map(int,input().split())
# for i in range(2,n+1):
#     if i not in sosu_list:
#         for a in range(i,n+1,i):
#             if a not in sosu_list:
#                 sosu_list.append(a)
# print(sosu_list[times-1])

# n_list = {}
# for _ in range(int(input())):
#     a = int(input())
#     if a not in n_list:
#         n_list[a] = 1
#     else:
#         n_list[a]+=1
# n_list = list(n_list.items())
# n_list.sort(key= lambda x: x[0])
# n_list.sort(key=lambda x : x[1],reverse=True)
# print(n_list[0][0])
# import sys
# wow = lambda : sys.stdin.readline().rstrip()
# r1,r2 = map(int,wow().split())
# wow_dict = {}
# for _ in range(r1):
#     a,b = wow().split()
#     wow_dict[a]=b
# for _ in range(r2):
#     print(wow_dict[wow()])

# n,popo = map(int,input().split())
# n_list = [n]
# while True:
#     wow = list(map(int,list(str(n_list[-1]))))
#     cnt = 0
#     for i in wow:
#         cnt+=i**popo
#     if cnt not in n_list:
#         n_list.append(cnt)
#     else:
#         index = n_list.index(cnt)
#         n_list = n_list[:index]
#         break
# print(len(n_list))

# import math 
# a,b = map(int,input().split())
# print(a*b//(math.gcd(a,b)))

# l = int(input())
# n_list = list(map(int,input().split()))
# cnt = 1
# wow_list = []
# for i in range(l-1):
#     if n_list[i] <= n_list[i+1]:
#         cnt+=1
#     else:
#         wow_list.append(cnt)
#         cnt=1
# wow_list.append(cnt)
# cnt = 1
# n_list = n_list[::-1]
# for i in range(l-1):
#     if n_list[i] <= n_list[i+1]:
#         cnt+=1
#     else:
#         wow_list.append(cnt)
#         cnt=1
# wow_list.append(cnt)
# print(max(wow_list))
# import sys
# test = int(sys.stdin.readline().rstrip())
# for _ in range(test):
#     a = int(sys.stdin.readline().rstrip())
#     a_list = list(map(int,sys.stdin.readline().rstrip().split()))
#     b = int(sys.stdin.readline().rstrip())
#     b_list = list(map(int,sys.stdin.readline().rstrip().split()))
#     dict_list = {}
#     for i in a_list:
#         dict_list[i]=1
#     for i in b_list:
#         if i not in dict_list:
#             dict_list[i]=0
#     for i in b_list:
#         print(dict_list[i])
# import math
# a,b = map(int,input().split(":"))
# wow = math.gcd(a,b)
# print(str(a//wow)+":"+str(b//wow))

n_list = []
for _ in range(int(input())):
    









