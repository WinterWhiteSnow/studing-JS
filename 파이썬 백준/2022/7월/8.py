
import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# while True:
#     r = one()
#     if r == -1:
#         break
#     pre_time = 0
#     cnt = 0
#     for _ in range(r):
#         a,b = wow()
#         if pre_time == 0:
#             cnt+=a*b
#             pre_time = b
#         else:
#             cnt+=a*(b-pre_time)
#             pre_time = b
#     print(cnt,"miles")

# for _ in range(one()):
#     a = one()
#     cnt = 0
#     for i in range(1,a+1):
#         cnt+=i**2
#     print(cnt)

# a,b,c = wow()
# n_list = [a^b]
# while True:
#     d = n_list[-1]^b
#     if d not in n_list:
#         n_list.append(d)
#     else:
#         break
# index = c%len(n_list)-1
# print(n_list[index])
    
# num = one()
# r = one()
# cnt = num
# for i in range(1,r+1):
#     cnt+=num*(10**i)
# print(cnt)

# x,y,n = wow()
# for i in range(1,n+1):
#     if i%x==0 and i%y==0:
#         print("FizzBuzz")
#     else:
#         if i%x ==0:
#             print("Fizz")
#         elif i%y==0:
#             print("Buzz")
#         else:
#             print(i)

# n = inputing().upper()
# print(n)

# n_dict = {0:2,1:1,2:1/2,4:1/4,8:1/8,16:1/16}
# r = one()
# cnt = 0
# n_list = list(wow())
# for i in n_list:
#     cnt+=n_dict[i]
# print(cnt)

# a,b,c = wow()
# x,y,z = wow()
# total = a+b+c
# cnt1 = (total)*((100-x)/100)
# n_list = sorted([a,b,c])
# cnt2 = n_list[-1]*((100-(max(y,z)))/100)+n_list[-2]*((100-min(y,z))/100)+n_list[0]
# if cnt1 >= cnt2:
#     print("two",f"{total-cnt2:.2f}")
# else:
#     print("one",f"{total-cnt1:.2f}")

# a = one()
# n_list=list(wow())
# new_list = [i for i in n_list if i != -1]
# print(sum(new_list)/len(new_list))

# k,p,x = wow()
# start = x+k*p
# index = 2
# while True:
#     cnt = index*x + k/index*p
#     start = min(start,cnt)
#     if cnt != start:
#         break
#     index+=1
# print(f"{start:.3f}")

# a,b = wow()
# cnt = 0
# while b>0:
#     if b-a >=0:
#         b-=a
#         a*=2
#         cnt+=1
#     else:
#         break
# print(cnt)

# for _ in range(one()):
#     n_list = list(wow())
#     if sum(n_list) == 180:
#         print(*n_list,"Seems OK")
#     else:
#         print(*n_list,"Check")

# r = one()
# l = one()
# for _ in range(r):
#     print("*"*l)
# x_list = []
# y_list = []
# for _ in range(one()):
#     a,b = wow()
#     x_list.append(a)
#     y_list.append(b)
# print((max(x_list)-min(x_list))*2+(max(y_list)-min(y_list))*2)
    
# for _ in range(one()):
#     a = one()
#     count = bin(a).count("1")
#     if count == 1:
#         print(1)
#     else:
#         print(0)

# for _ in range(one()):
#     k,day = wow()
#     total = day*(day+1)//2+day
#     print(k,total)

# while True:
#     a,b = wow()
#     if a==b==0:
#         break
#     print(min(30*a+b*40,35*a+30*b,40*a+20*b))

# pre_str = 0
# cnt = 1
# for _ in range(one()):
#     a = inputing()
#     if pre_str == 0:
#         pre_str=a
#     else:
#         if a != pre_str:
#             cnt+=1
#         pre_str=a
# print(cnt+1)

# r = one()
# for _ in range(r):
#     n = one()
#     print(n**2)

# w = one()
# cnt = 0
# for _ in range(one()):
#     a,b = wow()
#     cnt+=a*b
# print(cnt//w)

# x,y= wow()
# a_point = 1
# b_point = 1
# for _ in range(x):
#     a,b = wow()
#     if a != b:
#         a_point = 0
# for _ in range(y):
#     a,b = wow()
#     if a != b:
#         b_point = 0
        
# if a_point==b_point==1:
#     print("Accepted") 
# else:
#     if a_point:
#         print("Why Wrong!!!")
#     else:
#         print("Wrong Answer")

# a,b= wow()
# n_list = list(wow())
# a_list = list(wow())
# print(max(n_list)+max(a_list))

# cup,start,r = wow()
# for _ in range(r):
#     a,b = wow()
#     if a == start:
#         start = b
#     elif b == start:
#         start = a
# print(start)

a,b,x,y = wow()
distance = b-a
min_min = min(x,y)
max_max = max(x,y)
cnt = min(abs(min_min-a)+abs(max_max-b),abs(max_max-a)+abs(min_min-b))
print(min(distance,cnt))






    
