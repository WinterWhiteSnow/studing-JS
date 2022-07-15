# r,l = map(int,input().split())
# garo = []
# sero = {}
# for i in range(r):
#     a_list = input().split()
#     garo.append("".join(a_list))
#     for index in range(len(a_list)):
#         if index not in sero:
#             sero[index] = [a_list[index]]
#         else:
#             sero[index].append(a_list[index])
# sero = ["".join(i) for i in list(sero.values())]
# sero_list = []
# garo_list = []
# for i in range(len(garo)):
#     garo_list.append(garo[i].count("9"))
# for i in range(len(sero)):
#     sero_list.append(sero[i].count("9"))
# if max(garo_list)>=max(sero_list):
#     print(sum(garo_list)-max(garo_list))
# else:
#     print(sum(sero_list)-max(sero_list)) 

# l = int(input())
# a = [abs(i) for i in list(map(int,input().split()))]
# b = [abs(i) for i in list(map(int,input().split()))]
# print(sum(a)+sum(b)) 
# for _ in range(int(input())):
#     a = list(map(int,input().split()))[1:]
#     b = list(map(int,input().split()))[1:]
#     cnt = 4
#     while a.count(cnt) == b.count(cnt):
#         if cnt == 0:
#             break
#         cnt-=1
#     if a.count(cnt)>b.count(cnt):
#         print("A")
#     elif a.count(cnt)<b.count(cnt):
#         print("B")
#     else:
#         print("D")
# import string
# a_list = ['3', ' 2', ' 1', ' 2', ' 3', ' 3', ' 2', ' 3', ' 3', ' 2', ' 2', ' 1', ' 2', ' 2', ' 1', ' 2', ' 2', ' 2', ' 1', ' 2', ' 1', ' 1', ' 1', ' 2', ' 2', ' 1']  
# a_list = [int(i.strip()) for i in a_list]
# A_list = list(string.ascii_uppercase)
# a = list(input())
# b = list(input())
# wow = []
# for a,b in zip(a,b):
#     wow.extend([a_list[A_list.index(a)],a_list[A_list.index(b)]])
# while len(wow) != 2:
#     tem_list = []
#     for index in range(1,len(wow)):
#         tem_list.append(sum(wow[index-1:index+1])%10)
#     wow = tem_list
# print(str(wow[0])+str(wow[1]))
# import math
# n = list(input())
# n_dict = {}
# for i in set(n):
#     if i == "9" or i =="6":
#         if "9" not in n_dict:
#             n_dict["9"]=n.count(i)
#         else:
#             n_dict["9"]+=n.count(i)
#     else:
#         if i not in n_dict:
#             n_dict[i]=n.count(i)
#         else:
#             n_dict[i]+=n.count(i)
# if "9" in n_dict:
#     n_dict["9"] = math.ceil(n_dict["9"]/2)
# print(max(n_dict.values())) 


    