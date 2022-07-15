import sys
inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())


# string = []
# a,b = inputing().split()
# for aa in list(a):
#     for bb in list(b):
#         if aa == bb:
#             string.append(aa)
#             break

# gap = a.index(string[0])
# index = b.index(string[0])
# # print(index)
# for x in range(len(b)):
#     for y in range(len(a)):
#         if x != index:
#             if y != gap:
#                 if y == len(a)-1:
#                     print(".")
#                 else:
#                     print(".",end="")
#             else:
#                 if y == len(a)-1:
#                     print(b[x])
#                 else:
#                     print(b[x],end="")
#         else:
#             print(a)
#             break

# l,total = wow()
# n_list = list(wow())
# start = 0
# end = max(n_list)*total
# while start<=end:
#     mid = (start+end)//2
#     cnt = 0
#     for i in n_list:
#         cnt+=mid//i
#     if cnt < total:
#         start=mid+1
#     else:
#         end=mid-1
# # print(start)
# num,string = inputing().split()
# if num == "1":
#     index = []
#     for i in range(len(string)):
#         if string[i].isupper():
#             index.append(i)
#     print(string)
#     for i in range(len(string)):
#         if i == len(string)-1:
#             if i in index:
#                 print("_"+string[i].lower())
#             else:
#                 print(string[i])
#         else:
#             if i in index:
#                 print("_"+string[i].lower(),end="")
#             else:
#                 print(string[i],end="")
#     print(string[0].upper()+string[1:])
# elif num == "2":
#     index = []
#     for i in range(len(string)):
#         if string[i]=="_":
#             index.append(i)
#     string_list = list(string)
#     for i in range(len(string)):
#         if i in index:
#             string_list[i+1]=string_list[i+1].upper()
#     first = "".join(string_list).replace("_","")
#     print(first) 
#     print(string)
#     print(first[0].upper()+first[1:]) 
# else:
#     index = []
#     for i in range(len(string)):
#         if string[i].isupper():
#             index.append(i)
#     index=index[1:]
#     print(string[0].lower()+string[1:])
#     two_string = string.lower()
#     for i in range(len(string)):
#         if i == len(string)-1:
#             if i in index:
#                 print("_"+two_string[i].lower())
#             else:
#                 print(two_string[i])
#         else:
#             if i in index:
#                 print("_"+two_string[i].lower(),end="")
#             else:
#                 print(two_string[i],end="")
#     print(string)

# h,x = wow()
# cnt = 0
# start = x
# for i in range(1,h+1):
#     a = one()
#     cnt+=(start*a)%(1000000000 + 7)
#     start*=x
#     start%=(1000000000 + 7)
# print(cnt%(1000000000 + 7))

# total,k = wow()
# total=total*1000
# k = k*1000
# a = [k,k*2,k*2*2]
# b = [k/2,k,k*2]
# c = [k/2/2,k/2,k]
# list_list = [i for i in [a,b,c] if sum(i) <= total]
# list_list.sort(key=lambda x: sum(x),reverse=True)
# if list_list:
#     list_list = [i for i in list_list if i[0]*2==i[1] and i[1]*2==i[2]]
#     if list_list:
#         print(int(sum(list_list[0])))
#     else:
#         print(0)
# else:
#     print(0)




    
           
            






















