# from itertools import permutations,combinations

# r = lambda : map(int,input().split())
# l,k = r()
# n_list = list(r())
# wow = sorted(list(map(list,list(permutations(n_list,r=k)))))
# w_set = []
# for i in wow:
#     if set(i) not in w_set:
#         w_set.append(set(i))
#         print(*i)

# from itertools import permutations,combinations,product

# l,k = map(int,input().split())
# n_list = list(map(int,input().split()))
# wow =sorted(list(set(list(permutations(n_list,r=k)))))

# for i in wow:
#     print(*i)

# from itertools import permutations,product,combinations

# l,k = map(int,input().split())
# n_list = sorted(list(map(int,input().split())))
# wow = sorted(list(set(list(combinations(n_list,r=k)))))
# for i in wow:
#     print(*i)


# from itertools import permutations,product,combinations

# l,k = map(int,input().split())
# n_list = sorted(list(map(int,input().split())))
# wow = sorted(list(set(list(product(n_list,repeat=k)))))
# for i in wow:
#     print(*i)
# from itertools import combinations_with_replacement

# n,k = map(int,input().split())
# n_list = [i for i in range(1,n+1)]
# wow = sorted(list(combinations_with_replacement(n_list,r=k)))
# s_wow = []
# for i in wow:
#     print(*i)

# from itertools import combinations_with_replacement

# n,k = map(int,input().split())
# n_list = sorted(list(map(int,input().split())))
# wow = sorted(list(set(list(combinations_with_replacement(n_list,r=k)))))
# s_wow = []
# for i in wow:
#     print(*i)

# from itertools import permutations
# answer = input()
# number = int(answer)
# n = list(answer)
# wow = list(permutations(n,r=len(n)))
# big_list = [int("".join(i)) for i in wow if int("".join(i)) > number]
# if big_list:
#     print(min(big_list))
# else:
#     print(0)












