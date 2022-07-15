# r1,r2 = map(int,input().split())
# r1_list = [input() for _ in range(r1)]
# r2_list = [input() for _ in range(r2)]
# r1_list = set(r1_list)
# r2_list = set(r2_list)
# wow = list(set(r1_list.intersection(r2_list)))
# wow.sort()
# print(len(wow))
# for i in wow:
#     print(i)

# r = int(input())
# n_list = []
# for _ in range(r):
#     n_list.append(input())
# k = 1
# while True:
#     wow = [i[-k:] for i in n_list]
#     if len(set(wow)) == r:
#         break
#     else:
#         k+=1
# print(k)

# r = int(input())
# n_list = []
# for _ in range(r):
#     n_list.append(input())
# name_list = list(set(n_list))
# name_list.sort()
# max_count = 0
# max_name = ""
# for i in name_list:
#     if n_list.count(i) > max_count:
#         max_count = n_list.count(i)
#         max_name = i
# print(max_name)

# n = int(input())
# cnt = 1
# for i in range(1,n+1):
#     cnt*=i
# cnt = list(str(cnt)[::-1])
# if "0" in cnt :
#     check = []
#     count = 0
#     for i in range(len(cnt)):
#         if cnt[i] == "0":
#             count+=1
#         else:
#             if count != 0:
#                 print(count)
#                 break            
# else:
#     print(0)
# from collections import deque
# import sys
# r = int(sys.stdin.readline().rstrip())
# queue = deque([])
# for _ in range(r):
#     wow = sys.stdin.readline().rstrip()
#     if "push" in wow:
#         a,b = wow.split()
#         queue.append(b)
#     else:
#         if wow == "front":
#             if queue:
#                 print(queue[0])
#             else:
#                 print(-1)
#         elif wow == "back":
#             if queue:
#                 print(queue[-1])
#             else:
#                 print(-1)
#         elif wow == "size":
#             print(len(queue))
#         elif wow == "pop":
#             if queue:
#                 print(queue.popleft())
#             else:
#                 print(-1)
#         elif wow == "empty":
#             if len(queue) > 0:
#                 print(0)
#             else:
#                 print(1)
# import sys
# r1,r2 = map(int,sys.stdin.readline().rstrip().split())
# wow_dict={}
# for index in range(r1):
#     a = sys.stdin.readline().rstrip()
#     wow_dict[str(index+1)]=a
#     wow_dict[a]=index+1
# for _ in range(r2):
#     a = sys.stdin.readline().rstrip()
#     print(wow_dict[a])
# import sys
# n_list = []
# for _ in range(int(sys.stdin.readline().rstrip())):
#     name,k,e,m = sys.stdin.readline().rstrip().split()
#     k = int(k)
#     e = int(e)
#     m = int(m)
#     n_list.append((name,k,e,m))

# n_list.sort(key=lambda x : x[0])
# n_list.sort(key=lambda x : x[3],reverse=True)
# n_list.sort(key=lambda x : x[2])
# n_list.sort(key=lambda x : x[1],reverse=True)
# for i in n_list:
#     print(i[0])

# n = input()
# n_list = []
# for i in range(len(n)):
#     n_list.append(n[i:])
# n_list.sort()
# for i in n_list:
#     print(*i,sep="")


    




















