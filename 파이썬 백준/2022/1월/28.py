# import math
# from random import *

# a = list(range(1,46))
# num_dict = {}
# for _ in range(60):
#     b = sample(a,6)
#     for i in a:
#         if i not in num_dict:
#             num_dict[i] = b.count(i)
#         else:
#             num_dict[i]+=b.count(i)
# maxi = max(num_dict.values())
# mini = min(num_dict.values())
# while True:
#     max_list = {}
#     for key,value in num_dict.items(): 
#         if value >= maxi:
#             if value not in max_list:
#                 max_list[value]=[key]
#             else:
#                 max_list[value].append(key)
#     if sum([len(i) for i in max_list.values()])<6:
#         maxi-=1
#     else:
#         keys = list(max_list.keys())
#         keys.sort(reverse=True)
#         break
# wow = list(input())
# for i in range(len(wow)):
#     if i == 0:
#         if wow[i] == "E":
#             print("I",end="")
#         else:
#             print("E",end="")
#     elif i == 1:
#         if wow[i] == "S":
#             print("N",end="")
#         else:
#             print("S",end="")
#     elif i==2:
#         if wow[i] == "T":
#             print("F",end="")
#         else:
#             print("T",end="")
#     else:
#         if wow[i] == "J":
#             print("P",end="")
#         else:
#             print("J",end="")
# wow = list(map(int,input().split()))
# cnt = 1
# count = 1
# for i in wow:
#     if i%2 == 1:
#         cnt*=i
#     else:
#         count*=i
# if 1 in wow:
#     print(cnt)
# else:
#     if cnt != 1:
#         print(cnt)
#     else:
#         print(count)

# n,k = map(int,input().split())
    
# k = str(k)
# kk = int(k[-1])
# wow = [i for i in range(1,n+1) if str(kk) not in str(i)[-1] if str(kk*2) not in str(i)[-1]]
# print(len(wow))
# print(*wow)

# wow = "100점, 100점, 200점, 200점, 300점, 300점, 400점, 400점, 500점,"
# wow = wow.split("점,")[:-1]
# wow = list(map(int,wow))
# answer = list(map(int,input().split()))
# if sum(answer) < 100:
#     print("none")
# else:
#     for i in range(len(answer)):
#         if answer[i] > wow[i]:
#             print("hacker")
#             exit()
#     print("draw")

# n = int(input())
# n = n+2
# n_range = [i for i in range(1,n-1)]
# for a in range(n):
#     if a == 0 or a == n-1:
#         print("@"*n)
#     else:
#         for b in range(n):
#             if b in n_range:
#                 print(" ",end="")
#             else:
#                 if b == 0:
#                     print("@",end="")
#                 else:
#                     print("@")
# cnt = 0
# while True:
#     a = int(input())
#     if a == -1:
#         break
#     cnt+=a
# print(cnt)

# n = int(input())
# k = n*5
# for a in range(1,k+1):
#     if a <= k//5:
#         print("@"*k)
#     else:
#         print("@"*n)

# n = int(input())
# k = n*5
# for a in range(1,k+1):
#     for b in range(1,k+1):
#         if b<=n or 2*n<b<=n*3 or n*4<b<=n*5:
#             if b == n*5:
#                 print("@")
#             else:
#                 print("@",end="")
#         else:
#             if a <= n:
#                 if n<=b<=n*2:
#                     print("@", end="")
#                 else:
#                     print(" ",end="")
#             elif a > n*4:
#                 if n*3<b<=n*4:
#                     print("@", end="")
#                 else:
#                     print(" ",end="")
#             else:
#                     print(" ",end="")        

# n = int(input())
# k = n*5
# for a in range(1,k+1):
#     for b in range(1,k+1):
#         if b <= n or b > n*4:
#             if b == k:
#                 print("@")
#             else:
#                 print("@",end="")
#         else:
#             if n*5>b>n:
#                 if n*2<a<=n*3 or n*4<a<=k:
#                     print("@",end="")
#                 else:
#                     print(" ",end="")

# n = int(input())
# k = n*5
# for a in range(1,k+1):
#     if a <= n or n*4<a<=k:
#         print("@"*k)
#     else:
#         print("@"*n,end="")
#         print(" "*(k-(n*2)),end="")
#         print("@"*n)
import math
n = int(input())
k = n*5
for a in range(1,k+1):
    for b in range(1,k+1):
        if b <= n :
            print("@",end="")
        else:#n*(5-(math.ceil(a/n))) >n*3 일때
            if a < n*3:
                if n*(5-(math.ceil(a/n)))<b<=n*(5-(math.ceil(a/n)))+2:
                    if b != k:
                        print("@",end="")
                    else:
                        print("@")
                else:
                    if b != k:
                        print("",end="")
                    else:
                        print("")
            else:
                if a<=b<=a+2:
                    print("@",end="")
                else:
                    print("",end="")
                
                
                