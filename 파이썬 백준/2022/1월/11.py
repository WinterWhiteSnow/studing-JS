# wow = list(map(int,input().split("/")))
# k=wow[0]
# d=wow[1]
# a=wow[2]
# if k+a < d or d == 0:
#     print("hasu")
# else:
#     print("gosu")

# so,width,height,mun = map(int,input().split())
# wow = (width//mun)*(height//mun)
# print(so,wow)
# if wow > so:
#     print(so)
# else:
#     print(wow)

# n,m = map(int,input().split())
# if m == 1 or m == 2 :
#     print("NEWBIE!")
# elif m <= n:
#     if m != 1 or m!= 2:
#         print("OLDBIE!")
# else:
#     print("TLE!")    

# wow = int(input())
# a = wow%8

# if a == 1:
#     print(1)
# elif a == 2 or a==0:
#     print(2)
# elif a == 3 or a == 7:
#     print(3)
# elif a == 4 or a == 6:
#     print(4)
# else:
#     print(5)

# a = int(input())
# b = int(input())
# c = int(input())
# count = 0
# while a > b+c*count:
#     count+=1
# print(250+100*count) 

# wow = int(input())
# stack = 2
# count = 0
# repeat = 1
# start = 2
# while repeat != wow:
#     start+=stack
#     count+=1
#     repeat+=1
#     if count == 2:
#         stack +=1
#         count=0
# print(start)

# repeat = int(input())
# for _ in range(repeat):
#     a,b = map(int,input().split())
#     wow = pow(a,b,10)
#     if wow !=0 :
#         print(wow)
#     else:
#         print(10)   

# wow = input()
# a=f"0o{wow}"
# print(str(bin(int(a,8)))[2:])
# import sys
# for _ in range(3):
#     a = int(sys.stdin.readline().rstrip())
#     b = [int(sys.stdin.readline().rstrip()) for _ in range(a)]
#     sun = sum(b)
#     if sun ==0:
#         print("0")
#     elif sun > 0:
#         print("+")
#     else:
#         print("-")
# import math
# a = int(input())
# b = list(map(int,input().split()))
# if len(b) == a:
#     y = 0
#     m = 0
#     for i in b:
#         if int(i/30) == i/30:
#             y+=(math.ceil(i/30)+1)*10
#         else:
#             y+=math.ceil(i/30)*10
#         if int(i/60) == i/60:
#             m+=(math.ceil(i/60)+1)*15
#         else:
#             m+=math.ceil(i/60)*15
#     if y > m :
#         print("M",m)
#     elif y<m:
#         print("Y",y)
#     elif y==m:
#         print("Y","M",y) 

# while True:
#     a = input()
#     if a == "0":
#         break
#     else:
#         a = list(a)
#         count = len(a)+1
#         for i in a:
#             if i == "1":
#                 count+=2
#             elif i == "0":
#                 count+=4
#             else:
#                 count+=3
#         print(count)

d = list(map(int,input().split()))
d.sort()
a = d[0]
b = d[1]
a_x = a/4
a_y = a%4
b_x = b/4
b_y = b%4
if a_x == int(a_x):
    a_x = a//4
else:
    a_x = a//4+1
if b_x == int(b_x):
    b_x = b//4
else:
    b_x = b//4+1
    
if a_y == 0:
    a_y = 4
if b_y == 0:
    b_y = 4
x = abs(b_x - a_x)
y = abs(b_y - a_y)
print(x+y)
# print(a_x,a_y,b_x,b_y)
                           
        