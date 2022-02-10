# repeat = int(input())
# many = 0
# for _ in range(repeat):
#     a = list(map(int,input().split()))
#     a.sort()
#     a_set = list(set(a))
#     if len(a_set) == 1 :
#         if many < 50000+(a[0]*5000):
#             many = 50000+(a[0]*5000)
#     elif len(a_set) == 2 :
#         if a.count(a_set[0]) == 1 or a.count(a_set[1])== 1:#같은거 3개
#             if a.count(a_set[0]) == 1:
#                 if many < 10000+(a_set[1]*1000):
#                     many = 10000+(a_set[1]*1000)
#             else:
#                 if many < 10000+(a_set[0]*1000):
#                     many = 10000+(a_set[0]*1000)
#         elif a.count(a_set[0])==a.count(a_set[1])==2:
#             if many < 2000+(500*(a_set[0]+a_set[1])):
#                 many = 2000+(500*(a_set[0]+a_set[1]))
#     elif len(a_set) == 3 :
#         wow = [i for i in a_set if a.count(i) == 2]
#         if many < 1000+(wow[0]*100):
#             many = 1000+(wow[0]*100)
#     else:
#         if many < a[-1]*100:
#             many = a[-1]*100
# print(many)

# while True:
#     a = input()
#     x = a[0]
#     y = a[2:].lower()
#     if x == "#":
#         break
    
#     print(x,y.count(x))

# a_list = []
# for _ in range(9):
#     y = int(input())
#     a_list.append(y)
# a_list.sort()
# b_list = []
# cnt = sum(a_list)-100

# while True:
#     if len(b_list) > 0:
#         break     
#     for i in range(len(a_list)):
#         if len(b_list) > 0:
#             break
        
#         for a in range(i+1,len(a_list)):
#             # print(a_list[i],a_list[a])
#             if a_list[i]+a_list[a] == cnt:
#                 b_list.extend([a_list[i],a_list[a]])
#                 break
# for i in b_list:
#     a_list.remove(i)
# for i in a_list:
#     print(i)

# while True:
#     a = int(input())
#     if a == 0:
#         break
#     else:
#         while len(str(a)) != 1:
#             b = [int(i) for i in str(a)]
#             b = sum(b)
#             if str(b) != 1:
#                 a= b
#             else:
#                 break
#         print(a)
# months = [i for i in range(1,13)]
# dict_month = {}
# for i in months:
#     if i == 4 or i == 6 or i== 9 or i == 11:
#         dict_month[i]=30
#     elif i == 2: #윤년일때만 +1해주면됨
#         dict_month[i]=28
#     else:
#         dict_month[i]=31
# while True:
#     d,n,y= map(int,input().split())
#     if d==n==y==0:
#         break
#     else:
#         cnt = 0
#         if n > 2:
#             if y %4 ==0:
#                 if y%400 ==0 or y%100 != 0:
#                     cnt=1
#         cnt+=d
#         for i in range(1,n):
#             cnt+=dict_month[i]
#         print(cnt)
# while True:            
#     name,old,weight = map(str,input().split())
#     if name == "#" and old==weight=="0":
#         break
#     old= int(old)
#     weight = int(weight)
#     if old >17 or weight>=80:
#         print(name,"Senior")
#     else:
#         print(name,"Junior")
import string
a = list(string.ascii_uppercase)
a_dict = {}
cnt = 0
num = 2
for i in range(15):
    if cnt ==3:
        num+=1
        cnt=0
    a_dict[a[i]]=num
    cnt+=1
num = 7
cnt = 0
limit = 4
for i in range(15,len(a)):
    a_dict[a[i]]=num
    cnt+=1
    if cnt == 4:
        if limit ==4:
            num+=1
            cnt=0
            limit =3
    elif cnt == 3:
        if limit ==3:
            num+=1
            cnt=0
            limit=4
p,w = map(int,input().split())
wow = list(input())
cnt = 0
num = 0
for i in wow:
    if i == " ":
        cnt+=2
    else:
        fly = [key for key,value in a_dict.items() if value == a_dict[i]]
        index = fly.index(i)
        if cnt ==0:
            cnt+=p
            num=a_dict[i]
        else:
            if num == a_dict[i]:
                cnt+=p+w*(index+1)
            else:
                cnt+=p*(index+1)
print(cnt)
            
