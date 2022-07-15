import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# for index in range(1,one()+1):
#     a,b,c = wow()
#     cnt = 0
#     n_list = []
#     for x in range(a):
#         for y in range(b):
#             d = x & y
#             if d < c:
#                 # list_list = [x,y]
#                 # if list_list not in n_list:
#                 #     n_list.append(list_list)
#                     cnt+=1              
#     print(f"Case #{index}: {cnt}")    
# r,w,h = wow()
# f = int((w**2+h**2)**(1/2))
# max_max = max(w,h,f)    
# for _ in range(r):
#     a = one()
#     if max_max >= a:
#         print("YES")
#     else:
#         print("NO")

# for _ in range(one()):
#     a,b,c,x,y,z = wow()
#     print(c+abs(x-a)+abs(y-b)+z)

# for _ in range(one()):
#     p,c=map(float,inputing().split())
#     print(100*p/(c+100))

# floor,room,penalty = wow()
# n_list = list(wow())
# cnt = 0
# for index in range(room):
#     now_num = "no"
#     for step in range(index,room*floor,room):
#         if now_num == "no":
#             pass
#         else:
#             if now_num*2 < n_list[step]:
#                 cnt+=1
#         now_num = n_list[step]
# print(cnt*penalty)

# for _ in range(one()):
#     a,b,c,d = list(inputing())
#     g = int(a+b)**2+int(c+d)**2
#     if g%7 == 1:
#         print("YES")
#     else:
#         print("NO")  

# num = one()
# if num <= 4:
#     print(0)
# else:
#     index = 4
#     while True:
#         mid = index//2
#         # print("index",index,"remainder",(num-mid)//2,"mid",mid)
#         if (num-mid)//2 >mid:
#             index+=4
#         else:
#             if (num-mid)//2 < mid:
#                 index-=4
#             break
#         # print("end",index)
#     print(index)

# n_list = sorted(list(wow()))
# a = n_list[0]
# b = n_list[1]
# c = n_list[2]
# d = n_list[3]
# print(a,c,b,d)

# l = one()
# n_list = list(wow())
# nn_list = sorted(n_list)
# new_list = sorted(n_list,reverse=True)
# a_list = [0]*l
# for i in range(l):
#     index = n_list.index(nn_list[i])
#     a_list[index]=new_list[i]
# print(*a_list)

answer= inputing()
cnt = answer.count("e")
print("h"+"e"*(cnt*2)+"y")