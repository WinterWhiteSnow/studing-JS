import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# a,b = wow()
# if a==b==0:
#     print("Not a moose")
# elif a==b:
#     print("Even",a*2)
# else:
#     print("Odd",max(a,b)*2)

# a,b,c= wow()
# x,y,z = wow()
# cnt = 0
# if a<x:
#     cnt+=abs(a-x)
# if b<y:
#     cnt+=abs(b-y)
# if c<z:
#     cnt+=abs(c-z)
# print(cnt)
# a,b,c = list(map(int,inputing().split(":")))
# x,y,z = list(map(int,inputing().split(":")))
# answer = (a*60*60+b*60+c)
# answer2 = x*3600+y*60+z
# if answer2 < answer:
#     answer2+=24*60*60
# print(answer2-answer)

# a,b = wow()
# if a-a*b/100 >= 100:
#     print(0)
# else:
#     print(1)

# a,b,c,d = wow()
# f = a/b*c/d*1/2
# if f == round(f):
#     print(1)
# else:
#     print(0)
# import math
# n,a,b,c,d = wow()
# print(min(math.ceil(n/a)*b,math.ceil(n/c)*d))

# a = one()
# b = a**(1/2)*4
# print(b)

# n_list = list(one() for _ in range(4))
# if n_list[0] >= 8 and n_list[1]==n_list[2] and n_list[-1] >= 8:
#     print("ignore")
# else:
#     print("answer")

# n = one()
# print(n**(1/2)*4)
# import math
# a,b = wow()
# x,y = wow()
# x = x*x*math.pi
# # print(a,x,b/a,y/x)
# if b/a < y/x:
#     print("Slice of pizza")
# else:
#     print("Whole pizza")

# x = [0,0]
# y = [0,0]
# a,b = wow()
# c,d = wow()
# x[0]=a+d
# x[1]=d
# y[1]=b
# y[0]=b+c
# if x[0]>y[0]:
#     print("Persepolis")
# elif x[0]==y[0]:
#     if x[1]>y[1]:
#         print("Persepolis")
#     elif x[1]<y[1]:
#         print("Esteghlal")
#     else:
#         print("Penalty")
# else:
#     print("Esteghlal")

# a = 0
# for i in range(3,0,-1):
#     a+=one()*i
# b = 0
# for i in range(3,0,-1):
#     b+=one()*i

# if a>b :
#     print("A")
# elif a<b:
#     print("B")
# else:
#     print("T")
    
# a = inputing()
# if a[:3] == "555":
#     print("YES")
# else:
#     print("NO")





















