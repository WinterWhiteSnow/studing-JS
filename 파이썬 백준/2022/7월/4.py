import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# n_dict = {}
# num = one()
# for index in range(num):
#     a = one()
#     n_dict[a]=index+1
# for i in range(num):
#     print(n_dict[i+1])

# r,goal = wow()
# cnt = 0
# num = "no"
# for _ in range(r):
#     a = one()
#     if num == "no":
#         num = a
#     else:
#         if num-goal>=a:
#             cnt+=1
#         num=a
# print(cnt)

# while True:
#     a,b,c = wow()
#     if a==b==c==0:
#         break
#     if b ==0:
#         b = c//a
#     if a == 0:
#         a = c//b
#     if c == 0:
#         c = a*b
#     print(a,b,c)


# for _ in range(one()):
#     r,distance = wow()
#     cnt = 0
#     for _ in range(r):
#         a,b,c, = wow()
#         if distance/a <= b/c:
#             cnt+=1
#     print(cnt)

# for _ in range(one()):
#     a = one()
#     n_list = [1]
#     while True:
#         standard = n_list[-1]*3
#         if standard <= a:
#             n_list.append(standard)
#         else:
#             break
#     n_list.sort(reverse=True)
#     n_dict = {}
#     for i in n_list:
#         n_dict[i]=a//i
#         a=a%i
#     new_list = [b for a,b in list(n_dict.items())]
#     print(*new_list)

# a = list(wow())
# b = list(wow())
# cnt = 0
# for a,b in zip(a,b):
#     if a == b:
#         cnt+=1
# if cnt == 0:
#     print("Y")
# else:
#     print("N")

# waist,neck,attack = wow()
# cnt = 0
# for i in list(wow()):
#     if waist<=i<=neck:
#         cnt+=1
# print(cnt)

# for _ in range(one()):
#     a = one()
#     if a%2 == 0:
#         print(a,"is even")
#     else:
#         print(a,"is odd")

# for index in range(1,one()+1):
#     n,a,b,c,d = wow()
#     if (a-1 == c and b+2 == d) or (a-1 == c and b-2 == d) or (a+1 == c and b+2 == d) or (a+1 == c and b-2 ==d ) or (a-2 == c and b+1 ==d) or (a-2 ==c and b-1 ==d) or (a+2 == c and b+1 == d) or (a+2 == c and b-1 ==d):
#         print(f"Case {index}: YES")
#     else:
#         print(f"Case {index}: NO")
# for index in range(1,one()+1):
#     a = inputing().replace(" ","")
#     a,b = a.split("=")
#     b = int(b)
#     if eval(a)==b:
#         print(f"Case {index}: YES")
#     else:
#         print(f"Case {index}: NO")

# for _ in range(one()):
#     a,b = inputing().split()
#     if a == b[::-1]:
#         print("OK")
#     else:
#         print("NO")

# for _ in range(one()):
#     l = one()
#     n_list = list(wow())
#     if sum(n_list)==0:
#         print("Equilibrium")
#     else:
#         if sum(n_list)>0:
#             print("Right")
#         else:
#             print("Left")

# l = one()
# n_dict = {}
# list_list = list(wow())
# for i in list_list:
#     if i not in n_dict:
#         n_dict[i]=1
#     else:
#         n_dict[i]+=1
        
# one_list = [a for a,b in list(n_dict.items()) if b==1]
# if one_list:
#     print(list_list.index(max(one_list))+1)
# else:
#     print("none")

# for _ in range(one()):
#     act,r = wow()
#     cnt = 0
#     for _ in range(r):
#         a = one()
#         if a>act:
#             cnt+=1
#     print(cnt)

# all_clear = {}
# front_list = {}
# back_list ={}
# back_two = {}
# for _ in range(6):
#     d,b = inputing().split()
#     b = int(b)
#     if len(d) == 6:
#         all_clear[d]=b
#     if len(d) == 3:
#         if len(front_list) != 2:
#             front_list[d]=b
#         else:
#             back_list[d]=b
#     if len(d) == 2:
#         back_two[d]=b
# while True:
#     a = inputing()
#     if a == "-1":
#         break
#     cnt = 0
#     if a[:3] in front_list:
#         cnt+=front_list[a[:3]]
#     if a in all_clear:
#         cnt+=all_clear[a]
#     if a[3:] in back_list:
#         cnt+=back_list[a[3:]]
#     if a[4:] in back_two:
#         cnt+=back_two[a[4:]]
#     print(cnt)

# while True:
#     language,r,line,page = wow()
#     if language==r==line==page==0:
#         break
#     one_line = language**r
#     one_ = one_line**line
#     book = one_**page
#     print(book)

import math

for _ in range(one()):
    a,b = wow()
    pi = math.pi
    print(round(pi,a))








