# l,k = map(int,input().split())
# n_list = list(input())
# for i in range(l):
#     if n_list[i] == "P":
#         # print(n_list[i-k:i],n_list[i+1:i+k+1])
#         # print(i)
#         index = i-k
#         if index <0:
#             index = 0
#         if "H" in n_list[index:i]: #왼쪽
#             # print(n_list[index:i].index("H"),i,k)
#             n_list[n_list[index:i].index("H")+index]="E"
#             # print("".join(n_list))
#         elif "H" in n_list[i+1:i+k+1]:
#             n_list[n_list[i+1:i+k+1].index("H")+i+1]="E"
#         # print("".join(n_list))
# print(n_list.count("E"))

# for _ in range(int(input())):
#     l = int(input())
#     a = input()
#     b = input()
#     if a.count("W") ==b.count("W"):
#         cnt=0
#         for i in range(l):
#             if a[i]!=b[i]:
#                 cnt+=1
#         print(cnt//2)
#     else:
#         gap = abs(a.count("W")-b.count("W"))
#         cnt=0
#         swift = 0
#         for i in range(l):
#             if a[i]!=b[i]:
#                 cnt+=1
#         if cnt == gap:
#             print(cnt)
#         else:
#             print((cnt-gap)//2+gap)
# import sys
# n_list = []
# for _ in range(int(sys.stdin.readline().rstrip())):
#     n_list.append(int(sys.stdin.readline().rstrip()))
# n_list.sort()
# if len(n_list) == 3:
#     if n_list[-1] < sum(n_list[:-1]):
#         print(sum(n_list))
#     else:
#         print(-1)
# else:
#     index = len(n_list)-1
#     while index != 1:
#         if n_list[index] < sum(n_list[index-2:index]):
#             print(sum(n_list[index-2:index+1]))
#             exit()
#         # print(index)
#         index-=1
#     print(-1)
# from collections import deque
# r = lambda : int(input()) 
# for _ in range(r()):
#     l = r()
#     n_list = deque(input().split())
#     start = [n_list.popleft()]
#     for i in n_list:
#         if ord(start[0]) >= ord(i):
#             start.insert(0,i)
#         else:
#             start.append(i)
#         # print(start)
#     print("".join(start))

# team = int(input())
# n_list = list(map(int,input().split()))
# n_list.sort()
# a = team-1
# b = team
# a_list = []
# while b != 2*team:
#     a_list.append(n_list[a]+n_list[b])
#     a-=1
#     b+=1
# print(min(a_list))
# r = lambda:map(int,input().split())
# subject,m = r()
# a_list = []
# for _ in range(subject):
#     people,limit = r()
#     n_list = list(r())
#     n_list.sort(reverse=True)
#     if people>=limit:
#         n_list= n_list[:limit][-1]
#     else:
#         n_list= 1
#     a_list.append(n_list)
# a_list.sort()
# cnt = 0
# total = 0
# # print(a_list)
# for i in a_list:
#     if total < m:
#         cnt+=1
#         total+=i
#         if total > m:
#             print(cnt-1)
#             exit()
# print(cnt)    

# days,base = map(int,input().split())
# n_list = []
# total_list = []
# for _ in range(days):
#     n_list.append(int(input()))
# # print(n_list)
# for i in range(days-1):
#     if n_list[i] < n_list[i+1]:
#         if len(total_list) == 0:
#             total = base//n_list[i]
#             total = total*n_list[i+1]+base%n_list[i]
#         else:
#             total = total_list[-1]//n_list[i]
#             total = total*n_list[i+1]+total_list[-1]%n_list[i]
#         total_list.append(total)
# if total_list:
#     print(max(total_list))
# else:
#     print(base)

topping_sort = int(input())
dough_price,topping_price= map(int,input().split())
dough_k = int(input())
dough_avarage = int(dough_k/dough_price)
topping_list = [int(input()) for _ in range(topping_sort)]
total_avarage = int((dough_k+sum(topping_list))/(dough_price+topping_price*topping_sort))
topping_list = [i for i in topping_list if i/topping_price > total_avarage]
print(max(dough_avarage,int((dough_k+sum(topping_list))/(dough_price+topping_price*len(topping_list)))))
    
