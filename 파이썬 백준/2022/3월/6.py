# def hope(a_list,a):
#     cnt=0
#     for i in range(len(a_list)):
#         wow = list(a_list[i])
#         for x,y in zip(a,wow):
#             if x == "S":
#                 if y == "P":
#                     cnt+=2
#                 elif y =="S":
#                     cnt+=1
#             elif x == "P":
#                 if y =="R":
#                     cnt+=2
#                 elif y=="P":
#                     cnt+=1
#             else:
#                 if y =="S":
#                     cnt+=2
#                 elif y == "R":
#                     cnt+=1
#     return cnt

# l=int(input())
# a = input()
# if len(a) == l:
#     repeat = int(input())
#     a_list = []
#     for _ in range(repeat):
#         b = input()
#         a_list.append(b)
#     a = list(a)
#     print(hope(a_list,a))
#     cnt = 0
#     a_dict = {}
#     for i in range(len(a_list)):
#         q = list(a_list[i])
#         for index in range(len(q)):
#             if index not in a_dict:
#                 a_dict[index]=[q[index]]
#             else:
#                 a_dict[index].append(q[index])
#     new_alist = list(a_dict.values())
#     close = ""
#     # print(new_alist)
#     total_cnt = 0
#     for ind in range(len(new_alist)):
#         cnt_list=[]
#         for i in ["R","S","P"]:
#             cnt = 0
#             for v in range(len(new_alist[ind])):
#                 if i == "S":
#                     if new_alist[ind][v] == "P":
#                         cnt+=2
#                     elif new_alist[ind][v] == "S":
#                         cnt+=1
#                 elif i == "R":
#                     if new_alist[ind][v] == "R":
#                         cnt+=1
#                     elif new_alist[ind][v] == "S":
#                         cnt+=2
#                 else: #보일때
#                     if new_alist[ind][v] == "R":
#                         cnt+=2
#                     elif new_alist[ind][v] == "P":
#                         cnt+=1
#             cnt_list.append(cnt)
#         total_cnt+=max(cnt_list)
#     print(total_cnt)
# correct = int(input())
# a = list(input())
# b = list(input())
# cnt=0
# l = len(a)
# for x,y in zip(a,b):
#     if x == y:
#         cnt+=1
# if cnt == 0:
#     print(l-correct)
# else:
#     if cnt == correct:
#         print(l)
#     else:
#         print(l-abs(cnt-correct))
# r = int(input())
# a = 0
# b = 0
# state = 0
# a_list = list(map(int,input().split()))
# a_list.sort()
# for _ in range(r):
#     if state == 0:
#         a+=a_list.pop()
#         state = 1
#     else:
#         b+=a_list.pop()
#         state=0
# print(a,b)
# l = int(input())
# a_list = list(map(int,input().split()))
# gap = max(a_list)
# for i in range(1,len(a_list)):
#     gaap = max(a_list[i-1:i+1])-min(a_list[i-1:i+1])
#     if gaap < gap:
#         gap = gaap
# print(gap)
# l = int(input())
# a = list(map(int,input().split()))
# b = list(map(int,input().split()))
# b_list = sorted(b,reverse=True)
# a_list = sorted(a)
# a_dict = {}
# for i in range(l):
#     if b_list[i] not in a_dict:
#         a_dict[b_list[i]]=[a_list[i]]
#     else:
#         a_dict[b_list[i]].append(a_list[i])
# cnt = 0
# for key,value in a_dict.items():
#     cnt+= key*sum(value)
# print(cnt)
# import sys
# r = int(sys.stdin.readline().rstrip())
# a_list = []
# for _ in range(r):
#     a_list.append(int(sys.stdin.readline().rstrip()))
# a_list.sort()
# cnt_list = []
# l = len(a_list)
# for i in range(l):
#     cnt_list.append(l*a_list[i])
#     l-=1
# print(max(cnt_list))
# num = int(input())
# start = 3
# l = 2
# stack = 3
# if num < start:
#     print(1)
# elif num == 3:
#     print(l)
# else:
#     while start <= num:
#         start+=stack
#         stack+=1
#         l+=1
#     print(l-1)

# a = input()
# x = [i for i in a.split("0") if i != ""]
# y = [i for i in a.split("1") if i != ""]
# print(min(len(x),len(y)))

# cnt = 1
# while True:
#     l,p,v = map(int,input().split())
#     if l==p==v==0:
#         break
#     wow = (v//p)*l + min(l,v%p)
#     print(f"Case {cnt}: {wow}")
#     cnt+=1

# change,r = map(int,input().split())
# set_list = []
# piece_list = []
# for _ in range(r):
#     set_price,piece_price = map(int,input().split())
#     set_list.append(set_price)
#     piece_list.append(piece_price)
# set_item = change//6
# piece_item = change%6
# if set_item*min(set_list) <= 6*min(piece_list)*set_item:
#     cnt = set_item*min(set_list)
# else:
#     cnt = 6*min(piece_list)*set_item
# if min(set_list)<=piece_item*min(piece_list):
#     cnt+= min(set_list)
# else:
#     cnt+=piece_item*min(piece_list)
# print(cnt)
# a = input()
# b = input()
# ho = len(a)
# wow = len(b)
# # print(ho,wow,len(a.replace(b,"")))
# print((ho-len(a.replace(b,"")))//wow)

sero,garo = map(int,input().split())


        
    



    