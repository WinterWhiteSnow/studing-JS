# import sys
# max_num,r = map(int,sys.stdin.readline().rstrip().split())
# name_list = []
# number_list = []
# check_dict = {}
# for index in range(r):
#     name,price = sys.stdin.readline().rstrip().split()
#     price = int(price)
#     name_list.append(name)
#     number_list.append(price)
#     if price not in check_dict:
#         check_dict[price] = 1
#     else:
#         check_dict[price]+=1
# min_value = min(check_dict.values())
# check_list = [key for key,value in check_dict.items() if value == min_value]
# check_list = min(check_list)
# index = number_list.index(check_list)
# print(name_list[index],check_list)

# from itertools import combinations
# r = int(input())
# n_list = [list(map(int,input().split())) for _ in range(r)]
# number_list = []
# for i in range(r):
#     list_list = n_list[i]
#     wow = list(combinations(list_list,r=3))
#     wow.sort(key=lambda x : sum(x)%10,reverse=True)
#     number_list.append((sum(wow[0])%10,i))
# number_list.sort(key= lambda x : (x[0],x[1]),reverse=True)
# print(number_list[0][1]+1)

import sys
from itertools import combinations
total,no = map(int,sys.stdin.readline().rstrip().split())
num_list = [i for i in range(1,total+1)]
list_list = list(combinations(num_list,r=3))
liist = []
for _ in range(no):
    wow = set(num_list)
    a = set(map(int,input().split()))
    remainder = list(wow-a)
    for i in remainder:
        c = list(a)
        c.append(i)
        c.sort()
        if c not in liist:
            liist.append(c)
print(len(list_list)-len(liist))














