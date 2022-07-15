import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# from itertools import combinations_with_replacement
# n = one()
# n_list = [i for i in range(n+1)]
# list_list = list(combinations_with_replacement(n_list,r=2))
# cnt = 0    
# for i in list_list:
#     cnt+=sum(i)
# print(cnt)

# start,end,x,y =wow()
# distance = abs(end-start)
# a = abs(max(start,end)-max(x,y))
# b = abs(min(end,start)-min(x,y))
# print(min(distance,a+b))

# total = one()
# r = one()
# if r*(r+1)//2 <= total:
#     n_list = [i for i in range(1,r+1)]
#     remainder = total-r*(r+1)//2
#     average = remainder/r
# elif total>=r:
#     n_list = [1 for i in range(r)]
#     remainder = total-1*r
#     average = remainder/r

# if int(average) == average:
#     for i in range(r):
#         n_list[i]+=int(average)
# else:
#     for i in range(r):
#         if i != r-1:
#             n_list[i]+=int(average)
#         else:
#             n_list[i]+=remainder
#         remainder-=int(average)
# for i in n_list:
#     print(i)

# for _ in range(one()):
#     standard,x,y = wow()
#     x,y = max(x,y),min(x,y)
#     c = standard-x
#     if c>0:
#         x+=c
#     else:
#         c = 0
#     remainder = x-y
#     if remainder>=2:
#         print(c)
#     else:
#         x+=(2-remainder)                
#         c+=(2-remainder)  
#         print(c)

# l = one()
# a_list = inputing().split()
# answer = "yes"
# for i in range(l):
#     if a_list[i].isdigit():
#         if i+1 == int(a_list[i]):
#             pass
#         else:
#             answer="no"
# if answer == "yes":
#     print("makes sense")
# else:
#     print("something is fishy")
# cnt = 0
# for _ in range(one()):
#     a = one()
#     if a != 1:
#         cnt+=1
# print(cnt)
# k = one()
# a,b = wow()
# print(k**2-((a-b)/2)**2)

# a,b= wow()
# print(a/b)

# n = one()
# n_list = set(list(wow()))
# s_list = set([i for i in range(1,n+1)])
# new_list = s_list-n_list
# print(list(new_list)[0])

# a,b= wow()
# if b>20:
#     time = 1/((100-b)/a) #분당 까이는 배터리 -> 1%퍼당 필요한 시간
#     x = (b-20)*time
#     y = min(b,20)*time*2
#     if x >= 0:
#         y+=x
#     print(y)
# else:
#     x_battery = 80
#     y_battery = 100-b-x_battery
#     total = 1/((x_battery+y_battery*2)/a)
#     print(min(20,b)*total*2)














