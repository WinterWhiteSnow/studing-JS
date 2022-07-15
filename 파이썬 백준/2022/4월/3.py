# from itertools import product
# n,k = map(int,input().split())
# n_list = [1,2,3]
# wow_list = []
# for number in range(1,n+1):
#     wow = list(product(n_list,repeat=number))
#     wow = [i for i in wow if sum(i) == n]
#     wow_list.extend(wow)
# if len(wow_list) >= k:
#     print(*sorted(wow_list)[k-1],sep="+")
# else:
#     print(-1)
# from itertools import combinations
# r = lambda : map(int,input().split())
# l,s = r()
# n_list = list(r())
# wow_list = []
# for i in range(1,l+1):
#     list_list = list(combinations(n_list,i))
#     list_list = [a for a in list_list if sum(a) == s]
#     wow_list.extend(list_list)
# print(len(wow_list))
# from itertools import permutations,combinations
# is_first="yes"
# while True:
#     n_list = list(map(int,input().split()))
#     if n_list[0] == 0:
#         break
#     else:
#         if is_first == "yes":
#             pass
#         else:
#             print(" ")
#     number_list = n_list[1:]
#     k = n_list[0]
#     wow = list(combinations(number_list,6))
#     for i in wow:
#         print(*i)
#     is_first = "no"













