# import time
# from itertools import combinations, permutations

# # start_time = time.time()
# l = int(input())
# r = lambda : list(map(int,input().split()))
# number_list = r()
# str_list = ["+","-","*","//"]
# symbol = r()
# symbol_list = []
# for i in range(len(symbol)):
#     for _ in range(symbol[i]):
#         symbol_list.append(str_list[i])


# wow =list(set(list(permutations(symbol_list,l-1))))
# answer_list = []
# for i in range(len(wow)):
#     ss = wow[i]
#     cnt = number_list[0]
#     for index in range(len(ss)):
#         if ss[index] == "+":
#             cnt+=number_list[index+1]
#         if ss[index] == "-":
#             cnt-=number_list[index+1]
#         if ss[index] == "//":
#             if cnt < 0:
#                 cnt = cnt*(-1)
#                 cnt//=number_list[index+1]
#                 cnt = cnt*(-1)
#             else:
#                 cnt//=number_list[index+1]
#         if ss[index] == "*":
#             cnt*=number_list[index+1]
#     answer_list.append(cnt)
# print(max(answer_list))
# print(min(answer_list))

# end_time = time.time()
# print("time:",end_time-start_time)

from itertools import product
r,l = list(map(int,input().split()))
n_list = [i for i in range(1,r+1)]
a_list = list(product(n_list,repeat=l))
for i in a_list:
    if list(i) == sorted(list(i)):
        print(*i)


