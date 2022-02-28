# r,c = map(int,input().split())
# a,b = map(int,input().split())
# num = 1
# for _ in range(r):
#     if num == 1:
#         for _ in range(a):
#             q = (("X"*b+"."*b)*c)[:c*b]
#             print(q)
#         num =2
#     else:
#         for _ in range(a):
#             q = (("."*b+"X"*b)*c)[:c*b]
#             print(q)
#         num=1
# for _ in range(3):
#     maxi = []
#     a = list(input())
#     cnt = 0
#     wow = 0
#     for i in range(len(a)):
#         if i == 0:
#            wow = a[i]
#         else:
#             if a[i] == wow:
#                 cnt+=1
#             else:
#                 maxi.append(cnt)
#                 cnt=0
#                 wow=a[i]
#     maxi.append(cnt)
#     print(max(maxi)+1)
# import string
# wow = list(string.ascii_lowercase)
# wow_dict = {}
# for i in wow:
#     wow_dict[i]=0
# while True:
#     try:
#         a = list(input())
#         for i in a:
#             if i in wow_dict:
#                 wow_dict[i]+=1
#     except:
#         b = max(list(wow_dict.values()))
#         c = [key for key,value in wow_dict.items() if value == b]
#         for i in c:
#             print(i,end="")
#         exit()
# import math        
# n,k = map(int,input().split())
# wow = {"man":{},"girl":{}}
# for _ in range(n):
#     gender,grade = map(int,input().split())
#     grade = str(grade)        
#     if gender == 1:
#         if grade not in wow["man"]:
#             wow["man"][grade] = 1
#         else:
#             wow["man"][grade]+=1
#     else:
#         if grade not in wow["girl"]:
#             wow["girl"][grade] = 1
#         else:
#             wow["girl"][grade]+=1
# cnt = 0
# for key,value in wow.items():
#     why = [math.ceil(i/k) for i in list(value.values())]
#     cnt+=sum(why)
# print(cnt)
# r =int(input())
# a_dict = {}
# l = 0
# for _ in range(r):
#     a = list(input())
#     for i in range(len(a)):
#         if str(i) not in a_dict:
#             a_dict[str(i)]=[a[i]]
#         else:
#             a_dict[str(i)].append(a[i])
# for i in a_dict.values():
#     if len(set(i)) ==1:
#         print(i[0],end="")
#     else:
#         print("?",end="")

# r,a=map(int,input().split())
# a_dict = {}
# a_cnt = 0
# for _ in range(r):
#     b=list(input())
#     for i in range(len(b)):
#         if str(i) not in a_dict:
#             a_dict[str(i)] = [b[i]]
#         else:
#             a_dict[str(i)].append(b[i])
#     if "X" not in b:
#         a_cnt+=1
# cnt=0
# for i in a_dict.values():
#     if "X" not in i:
#         cnt+=1
# print(max(cnt,a_cnt))


            
            
    


        



        
    