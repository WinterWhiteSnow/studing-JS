# from math import gcd

# def wow(list_list):
#     def why(x,y):
#         return x*y//gcd(x,y)
#     while True:
#         list_list.append(why(list_list.pop(),list_list.pop()))
#         if len(list_list)==1:
#             return list_list
# num = list(map(int,input().split()))
# print(wow(num)[0])

# l = int(input())
# a_list = input().split()
# for i in range(1,24):
#     print(a_list.count(str(i)),end=" ")

# l = input()
# a_list = input().split()
# print(*a_list[::-1])

# l = input()
# a_list = list(map(int,input().split()))
# print(min(a_list))

# zero_list = [[0 for i in range(19)] for i in range(19)]
# for _ in range(int(input())):
#     x,y=map(int,input().split())
#     zero_list[x-1][y-1]=1
# # print(zero_list)
# for i in range(len(zero_list)):
#     print(*zero_list[i])

# a_list = []
# for _ in range(19):
#     a_list.append(input().split())
# for _ in range(int(input())):
#     x,y = map(int,input().split())
#     for i in range(len(a_list[x-1])):
#         if a_list[x-1][i] == "0":
#             a_list[x-1][i] = "1"
#         else:
#             a_list[x-1][i]="0"
#     for i in range(len(a_list)):
#         if a_list[i][y-1] == "0":
#             a_list[i][y-1] = "1"
#         else:
#             a_list[i][y-1] = "0"
# for i in a_list:
#     print(*i)

# r,l = map(int,input().split())
# a_list = [[0 for _ in range(l)] for _ in range(r)]
# for _ in range(int(input())):
#     l,way,y,x = map(int,input().split())
#     if way == 0: #가로
#         for i in range(x-1,x-1+l):
#             # print(i)
#             a_list[y-1][i]=1
#     else: #세로
#         for i in range(y-1,y-1+l):
#             a_list[i][x-1]=1
# for i in a_list:
#     print(*i)
# a_list = []
# for _ in range(10):
#     a_list.append(input().split())
# x = 1
# y = 1
# while True:
#     if a_list[y][x] == "0":
#         a_list[y][x] = "9"
#         x+=1
#     else:
#         if a_list[y][x] == "1":
#             x = x-1
#             y+=1
#             if a_list[y][x] == "1":
#                 break
#         else:
#             a_list[y][x]="9"
#             break
# for i in range(len(a_list)):
#     print(*a_list[i])
# n,l,k = map(int,input().split())
# cnt = 0
# list_list = []
# for _ in range(n):
#     a_list = list(map(int,input().split()))
#     list_list.append(a_list)
# list_list = [i for i in list_list if i[0] <= l]
# list_list.sort(key=lambda x : x[1])
# # print(list_list)
# if k <= len(list_list):
#     num = k
# else:
#     num = len(list_list)
# for i in range(num):
#     if list_list[i][1] <= l:
#         cnt+=140
#     else:
#         cnt+=100
# print(cnt)
# import string
# a_list = str(string.ascii_uppercase)
# a = list(input())
# index = a_list.index("A")
# cnt = 0
# for i in a:
#     x = abs(index - a_list.index(i))
#     cnt += min(x,26-x)
#     index = a_list.index(i)
# print(cnt)

# l = int(input())
# a_list = input()
# wow = len("".join(a_list.split("pPAp")))
# print((l-wow)//4)

# num = int(input())
# if num == 2:
#     maxi = 2
# else:
#     if num%2 == 0:
#         maxi = num//2
#     else:
#         maxi = num//2+1
# a_list = []
# cnt = 1
# for i in range(num):
#     if cnt <= maxi:
#         a_list.append(cnt)
#     else:
#         cnt = 1
#         a_list.append(cnt)
#     cnt+=1
# print(*a_list)
# wow,r = map(int,input().split())
# a_list = []
# for _ in range(r):
#     a_list.append(list(map(int,input().split())))
# a_list.sort(key=lambda x : x[0],reverse=True)
# cnt = 0
# for i in range(r-1):
#     q = a_list[i]
#     if q[0] >= wow:
#         pass
#     else:
#         cnt+=wow-q[0]
# print(cnt)


    
            


        
    
    