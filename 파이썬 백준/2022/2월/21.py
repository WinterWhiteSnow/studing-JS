# count = 0
# index = 1
# n = int(input())
# l = len(str(n))
# while int(n) > 10**(index):
#     num = list(str(n))
#     num[-index]="0"
#     num = int("".join(num))
#     a = int(str(n)[-index])
#     if a >= 5:
#         num+=10**(index)
#     index+=1
#     n=num
# print(n)

# from collections import deque
# n = int(input())
# n_list = deque([i for i in range(1,n+1)])
# while len(n_list) != 1:
#     print(n_list.popleft(),end=" ")
#     n_list.rotate(-1)
# print(n_list[0])
# r = int(input())
# a_dict = {}
# for _ in range(r):
#     a = list(map(int,input().split()))
#     for i in range(len(a)):
#         if i not in a_dict:
#             a_dict[i]={"total":a[i],"list":{"1":0,"2":0,"3":0}}
#             a_dict[i]["list"][str(a[i])]=1
#         else:
#             a_dict[i]["total"]+=a[i]
#             a_dict[i]["list"][str(a[i])]+=1
# total_list = [i["total"] for i in list(a_dict.values())]
# if total_list.count(max(total_list))>1:
#     num_list = [i["list"] for i in list(a_dict.values())]
#     num_list_list = [list(i.values()) for i in num_list]
#     # print(num_list_list)
#     num_sort = sorted(num_list_list,key=lambda x : (x[2],x[1]),reverse=True)
#     # print(num_sort)
#     if num_sort[0]==num_sort[1]:
#         print(0,max(total_list))
#     else:
#         print(num_list_list.index(num_sort[0])+1,max(total_list))
# else:
#     print(total_list.index(max(total_list))+1,max(total_list))
# a_list = [0,1]
# n = int(input())
# if n >= 2:
#     n = n-len(a_list)+1
#     for _ in range(n):
#         a_list.append((a_list[-1]+a_list[-2]))
#     # print(len(a_list))
#     print(a_list[-1])
# else:
#     print(a_list[n])
# n,m = map(int,input().split())
# a_list = {}
# b_list = {}
# b_b_list = {}
# for index in range(n):
#     a = list(map(int,input().split()))
#     a_list[index] = a
# x,y = map(int,input().split())
# for index in range(x):
#     b = list(map(int,input().split()))
#     b_list[index]=b
# wow = list(b_list.values())
# for i in wow:
#     l = [i for i in range(len(i))]
#     for ll in l:
#         if ll not in b_b_list:
#             b_b_list[ll]=[i[ll]]
#         else:
#             b_b_list[ll].append(i[ll])

# for index in range(len(a_list)):
#     for b_index in range(len(b_b_list)):
#         cnt = 0
#         for real_index in range(len(a_list[index])):
#             cnt+=a_list[index][real_index]*b_b_list[b_index][real_index]
#         print(cnt,end=" ")
#     print()
# from math import gcd
# r = int(input())
# for _ in range(r):
#     a,b = map(int,input().split())
#     wow = gcd(a,b)
#     a = a//wow
#     b = b//wow
#     print(a*b*wow,wow)
# r = int(input())
# for _ in range(r):
#     a = list(input())
#     a_dict = {}
#     for i in range(8):
#         a_dict[i]=0
#     for i in range(len(a)-2):
#         b = "".join(a[i:i+3])
#         if b == "TTT":
#             index = 0
#         elif b == "TTH":
#             index = 1
#         elif b == "THT":
#             index = 2
#         elif b == "THH":
#             index = 3
#         elif b == "HTT":
#             index = 4
#         elif b == "HTH":
#             index = 5
#         elif b == "HHT":
#             index = 6
#         elif b == "HHH":
#             index = 7
#         a_dict[index]+=1
#     print_t = list(a_dict.values())
#     print(*print_t)
# while True:
#     try:
#         a = input()
#         print(a)
#     except:
#         exit()
# a = input()
# b = a[::-1]
# if a ==b:
#     print("1")
# else:
#     print(0)
# a_dict = {}  
# for _ in range(5):
#     a = list(input())  
#     for i in range(len(a)):
#         if i not in a_dict:
#             a_dict[i]=[a[i]]
#         else:
#             a_dict[i].append(a[i])
# wow = ""
# for i in list(a_dict.values()):
#     st = "".join(i)
#     wow+=st
# print(wow)
# r = int(input())
# for _ in range(r):
#     a = input().split()
#     for i in range(len(a)):
#         a[i] = a[i][::-1]
#     print(*a)
# r = int(input())
# for _ in range(r):
#     a,b = input().split()
#     a = a.lower()
#     b = b.lower()
#     aa = list(set(a))
#     bb = list(set(b))
#     aa.sort()
#     bb.sort()
#     is_anagram = "1"
#     if len(aa)==len(bb) and aa==bb and len(a)==len(b):
#         for i in aa:
#             if a.count(i) != b.count(i):
#                 is_anagram = "0"
#                 break
#         if is_anagram == "1":
#             print(a,"&",b,"are anagrams.")
#         else:
#             print(a,"&",b,"are NOT anagrams.")
#     else:
#         print(a,"&",b,"are NOT anagrams.")

# a = input()
# happy = a.count(":-)")
# sad = a.count(":-(")
# if happy==sad:
#     if happy>0:
#         print("unsure")
#     else:
#         print("none")
# elif happy>sad:
#     print("happy")
# else:
#     print("sad")

# n,m = map(int,input().split())
# a_list = {}
# b_list = {}
# for index in range(n):
#     a = list(map(int,input().split()))
#     a_list[index] = a
# for index in range(n):
#     b = list(map(int,input().split()))
#     b_list[index]=b

# for i in range(len(a_list)):
#     a = a_list[i]
#     b = b_list[i]
#     for index in range(len(a)):
#         print(a[index]+b[index],end=" ")
#     print()

        
        
    
    

      


        
        
        
       