from re import L
import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# n,k = wow()
# not_list = [str(k)[-1],str(k*2)[-1]]
# n_list = []
# for i in range(1,n+1):
#     if str(i)[-1] not in not_list:
#         n_list.append(i)
# print(len(n_list))
# print(*n_list) 

# import decimal
# a,b,c,d = wow()
# cnt = 0
# x = int(decimal.Decimal(str(min(a,b))))
# y = int(decimal.Decimal(str(min(c,d))))
# cnt+=x
# cnt+=y
# print(int(decimal.Decimal(str(cnt)).sqrt()))

# cnt = 0
# cnt_cnt = 0
# for _ in range(one()):
#     a = one()
#     if a == 0:
#         cnt+=1
#     else:
#         cnt_cnt+=1
# print(min(cnt,cnt_cnt))

# n,k = wow()
# a,b = wow()
# num = (n*a-k*b)/(n-k)
# if num >100 or num<0:
#     print("impossible")
# else:
#     if num == int(num):
#         print(f"{num:.2f}")
#     else:
#         print(f"{num:.7f}")
# num = 100001
# for _ in range(one()):
#     a,b = wow()
#     num = min(num,b//a)
# print(num)

# n,p,r = wow()
# for i in range(r):
#     n_list = list(wow())
#     if p in n_list[1:]:
#         print("KEEP")
#     else:
#         print("REMOVE")

# n = one()
# a = 0
# cnt = 0
# for i in range(n):
#     b = one()
#     if i%2 == 0:
#         a = b
#     else:
#         cnt+=b-a
# if n%2:
#     print("still running")
# else:
#     print(cnt)     

# a = one()
# n_list =  [i for i in range(1,101)]
# if a == 1:
#     print("Either")    
# else:
#     list_list = []
#     for i in range(100-a+1):
#         if sum(n_list[i:i+a])%2==0:
#             list_list.append("Even")
#         else:
#             list_list.append("Odd")
#     if len(set(list_list)) == 2:
#         print("Either")
#     else:
#         print(list(set(list_list))[0])

# l = one()
# n_list = list(wow())
# z_list = [i if i<=7 else 7 for i in n_list]
# a= sum(z_list)
# if l%2:
#     total = 5*(l//2)+2
# else:
#     total = 5*(l//2)
# print(a-total)

# n = one()
# start= "no"
# cnt = 0
# for _ in range(n):
#     a = one()
#     if start == "no":
#         start = a
#     elif start > a:
#         start = a
#     else:
#         c = a-start
#         if c<0:
#             c =0
#         cnt+=c
# print(cnt)  

# a = one()
# if a%3 == 0:
#     print(0,a//3)
# else:
#     two = 0
#     three = 0
#     five = 0
#     if a%2 == 0:
#         two += a//2
#         if two>=3:
#             three+=two//3*2
#         two%=3
#         print(two,three)
#     else:
#         while True:
#             if ((a-5*five)%2 == 0) or ((a-5*five)%3 == 0):
#                 break
#             five+=1
#         a-=five*5
#         if a%3 == 0:
#             three+=a//3
#             a%=3
#         if a%2 == 0:
#             two+=a//2
#             a%=2
#         two+=five
#         three+=five
#         if two>=3:
#             three+=two//3*2
#             two%=3
#         print(two,three)

# a = one()
# n_list = []
# list_list = bin(a)[2:][::-1]
# for i in range(len(list_list)):
#     if list_list[i]== "1":
#         n_list.append(i)
# print(*n_list)

# a = one()
# x= 0
# y= 0
# for i in range(1,10**6+1,2):
#     if a%i == 0:
#         x = i
#         for index in range(1,a//x+1):
#             c = x*2**index
#             if c > a:
#                 break
            
#             if c == a:
#                 y=index
#                 break
#         if y != 0:
#             break
# print(x,y) 
# a = one()
# n_list  = list(wow())
# if sum(n_list)%3 == 0:
#     print("yes")
# else:
#     print("no")   

# n = one()
# n_list = list(wow())
# start = n_list[0]
# over = 0
# lack = 0
# for i in n_list[1:]:
#     c = i-start
#     if c == 0:
#         pass
#     else:
#         if c > 0:
#             over+=c
#         else:
#             lack+=c
#     start=i
# print(abs(lack),over)

# move_direction = "none"
# while True:
#     a = inputing()
#     if a == "99999":
#         break
#     direction = sum(map(int,list(a[:2])))
#     num = a[2:]
#     if direction==0:
#         print(move_direction,num)
#     else:
#         if direction%2:
#             print("left",num)
#             move_direction="left"
#         else:
#             print("right",num)
#             move_direction="right"

# n,m,k = wow()
# k_index = 0
# index = 0
# if m>=k:
#     k_index = m//k
#     index = k-1
#     print((k_index+index)*n)
# else:
#     print(m*n)

# w,h = wow()
# n_list = []
# z_list = []
# for _ in range(h):
#     n_list.append(list(inputing()))
# for i in range(h):
#     list_list = list(inputing())
#     z_list.append(list_list)
# cnt = list(inputing())
# real_list = []
# for r in range(h):
#     str_str = ""
#     for index in range(w):
#         if n_list[r][index] == "0" and z_list[r][index]=="0":
#             str_str+=cnt[0]
#         elif n_list[r][index] == "0" and z_list[r][index]=="1":
#             str_str+=cnt[1]
#         elif n_list[r][index] == "1" and z_list[r][index]=="0":
#             str_str+=cnt[2]
#         elif n_list[r][index] == "1" and z_list[r][index]=="1":
#             str_str+=cnt[3]
#     real_list.append(str_str)
# for i in real_list:
#     print(i)
# n_dict = {}
# index = one()
# n_list = list(wow())
# for i in range(1,index+1):
#     n_dict[i]=n_list[i-1]
# r = one()
# z_list = list(wow())
# for i in z_list:
#     n_dict[i]-=1
# for i in list(n_dict.values()):
#     if i < 0:
#         print("yes")
#     else:
#         print("no")

a = one()
print((a*2/3/3**(1/2))**(1/2)*6)
    


