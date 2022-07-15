# import sys

# number_range,r = map(int,sys.stdin.readline().rstrip().split())
# n_list = []
# number_list = []
# for _ in range(r):
#     a = list(map(int,sys.stdin.readline().rstrip().split()))
#     a.sort()
#     n_list.append(a)
#     number_list.extend(a)
# number_number_list = [i for i in range(1,number_range+1)]
# difference = list(set(number_number_list)-set(number_list))
# n_list.sort(key=lambda x: x[0])
# wow_list = []
# for c in n_list:
#     a,b = c
#     if len(wow_list) == 0:
#         wow_list.append(c)
#     else:
#         is_insert = "no"
#         for n in range(len(wow_list)):
#             if a in wow_list[n] or b in wow_list[n]:
#                 wow_list[n].extend(c)
#                 is_insert = "yes"
#                 break
#         if is_insert == "no":
#             wow_list.append(c)
# print(len(wow_list)+len(difference))

# from itertools import permutations
# import sys

# l = int(sys.stdin.readline().rstrip())
# symbol_list = sys.stdin.readline().rstrip().split()
# n_list = [i for i in range(10)]
# wow = list(permutations(n_list,r=l+1))
# answer = []
# for number in wow:
#     cnt = 0
#     for index in range(len(symbol_list)):
#         symbol = symbol_list[index]
#         if symbol == "<":
#             if number[index]<number[index+1]:
#                 cnt+=1
#             else:
#                 break        
#         if symbol == ">":
#             if number[index]>number[index+1]:
#                 cnt+=1
#             else:
#                 break  
#     if cnt == l:
#         answer.append(number)
# answer.sort()
# print(*answer[-1],sep="")
# print(*answer[0],sep="")
import sys
sys.setrecursionlimit(10**7)
q = lambda : map(int,sys.stdin.readline().rstrip().split())
r,l,k = q()
graph = []
for _ in range(r):
    graph.append(list(q()))
a = []
b = []
for i in range(len(graph)):
    a_list = graph[i]
    if i%2 == 0:
        for x in range(len(a_list)):
            if x%2 == 0:
                a.append(a_list[x])
            else:
                b.append(a_list[x])
    else:
        for x in range(len(a_list)):
            if x%2 == 0:
                b.append(a_list[x])
            else:
                a.append(a_list[x])
a.sort()
b.sort()

if abs(sum(a[-k:])) >= abs(sum(b[-k:])):
    print(sum(a[-k:]))
else: print(sum(b[-k:]))

        
    


