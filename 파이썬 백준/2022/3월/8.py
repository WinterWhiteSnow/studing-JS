# a = list(input())
# b = set(a)
# one_list = []
# a_dict = {}
# for i in b:
#     if a.count(i)%2 == 0:
#         pass
#     else:
#         one_list.append(i)
#         if len(one_list) > 1:
#             print("I'm Sorry Hansoo")
#             exit()
#     a_dict[i]=a.count(i)   
# a_sort = sorted(a_dict.items(),key= lambda x : x[1],reverse=True)
# # print(a_sort)
# wow_str = ""
# while sum(a_dict.values()) != 0:
#     max_list = [(key,value) for key,value in a_dict.items() if value != 0]
#     max_list.sort()
#     # print(max_list,wow_str)
#     if max_list[0][1] != 1:
#         wow_str+=max_list[0][0]*(max_list[0][1]//2)
#         a_dict[max_list[0][0]]-=(max_list[0][1]//2)*2
#     else:
#         if len(max_list) > 1:
#             wow_str+=max_list[1][0]*(max_list[1][1]//2)
#             a_dict[max_list[1][0]]-=(max_list[1][1]//2)*2
#         else:
#             if max_list[0][1] == 1:
#                 wow_str+=max_list[0][0]*max_list[0][1]
#                 a_dict[max_list[0][0]]-=max_list[0][1]
#             else:
#                 wow_str+=max_list[0][0]*(max_list[0][1]//2)
#                 a_dict[max_list[0][0]]-=(max_list[0][1]//2)*2
#     # print(a_dict)
# # print(wow_str)
# if len(a) == len(wow_str)*2:
#     wow_str+=wow_str[::-1]
# else:
#     wow_str+=wow_str[::-1][1:]
# print(wow_str)

# n = input().split()
# wow = list("UCPC")
# index = 0
# for i in n:
#     why = list(i)
#     for a in why:
#         if wow[index] == a:
#             index+=1
#         if index == 4:
#             print("I love UCPC")
#             exit()
# print("I hate UCPC")

# n = input()+"A"
# if n.count("X")%2 == 1:
#     print("-1")
# else:
#     string = ""
#     cnt = 0
#     for i in list(n):
#         if i == "X":
#             cnt+=1
#         else:
#             if cnt%2 == 1:
#                 print("-1")
#                 exit()
#             if cnt > 1:
#                 A = 4
#                 B = 2
#                 a_len = cnt//A
#                 string+=("A"*A)*a_len
#                 b_len = (cnt%A)//B    
#                 string+=("B"*B)*b_len
#                 cnt = 0
#             if i == ".":
#                 string+=i
#                 cnt=0
#     print(string)
    
# l = int(input())
# a_list = list(map(int,input().split()))
# a_list.sort(reverse=True)
# minus = l-1
# for i in range(l):
#     a_list[i]-=minus
#     minus-=1
#     # print(a_list)
# print(max(a_list)+l+1)
import sys
a_list = []
for i in range(int(sys.stdin.readline().rstrip())):
    a_list.append(int(sys.stdin.readline().rstrip()))
a_list.sort(reverse=True)
total = sum(a_list)
# if len(a_list)%3 == 0:
#     for i in range(0,len(a_list),3):
#         total-=a_list[i+2]
#     print(total)

   
    
    
    
    
    
    