# a = input().split("-")
# answer= 0
# for i in range(len(a)):
#     # print(i)
#     if i == 0:
#         if "+" in a[i]:
#             q = a[i].split("+")
#             for s in q:
#                 answer+=int(s)
#         else:
#             answer+=int(a[i])
#     else:
#         if "+" in a[i]:
#             q = a[i].split("+")
#             for s in q:
#                 answer-=int(s)
#         else:
#             answer-=int(a[i])
#     # print(answer)
# print(answer)
# import sys
# r = lambda : int(sys.stdin.readline().rstrip())
# for _ in range(r()):
#     person = r()
#     a_list = []
#     for _ in range(person):
#         a_list.append(list(map(int,sys.stdin.readline().rstrip().split())))
#     document = [i for i in a_list if i[0] == 1][0]
#     interview = [i for i in a_list if i[1] == 1][0]
#     a_list = [i for i in a_list if i[0]>=document[0] and i[1] <= document[1]]
#     a_list = [i for i in a_list if i[0]<=interview[0] and i[1] >= interview[1]]
#     a_list.sort(key=lambda x: x[0])
#     maxi = "wa"
#     cnt = 0
#     for i in a_list:
#         if type(maxi) == str:
#             cnt+=1
#             maxi = i[1]
#         else:
#             if maxi > i[1]:
#                 cnt+=1
#                 maxi = i[1]
#     print(cnt) 
# r = lambda : map(int,input().split())
# l,repeat = r()
# n_list = list(r())
# n_list.sort()
# # print(n_list)
# index = 1
# for i in range(repeat):
#     wow = n_list[index-1]+n_list[index]
#     n_list[index-1] = wow 
#     n_list[index] = wow
#     n_list.sort()
#     # print(n_list)
# print(sum(n_list))
# import collections

# for _ in range(int(input())):
#     l = int(input())
#     n_list = list(map(int,input().split()))
#     n_list.sort(reverse=True)
#     wow = collections.deque([])
#     for i in range(l):
#         if i%2 == 0:
#             wow.appendleft(n_list[i])
#         else:
#             wow.append(n_list[i])
#     wow = list(wow) 
#     gap = 0
#     # print(wow)
#     for i in range(1,len(wow)):
#         # print(wow[i],wow[i-1])
#         if gap < abs(wow[i]-wow[i-1]):
#             gap = abs(wow[i]-wow[i-1])
#         # print("gap:",gap)
#     if abs(wow[0]-wow[-1]) > gap:
#         gap = abs(wow[0]-wow[-1])
#     print(gap)
        
        
    

        

        
    
        
        
        








