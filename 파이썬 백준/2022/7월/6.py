import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# h,m,s = map(int,input().split(":"))
# time = h*3600+m*60+s
# H,M,S = map(int,input().split(":"))
# TIME = H*3600+M*60+S
# wow = (TIME-time)%86400
# if wow == 0:
#     wow = 86400
# a = str(wow//3600)
# b = str(wow%3600//60)
# c = str(wow%3600%60)
# print(a.rjust(2,"0")+":"+b.rjust(2,"0")+":"+c.rjust(2,"0"))

# import math
# for index in range(1,one()+1):
#     a,b = wow()
#     cnt=0
#     num = math.ceil(a**(1/3))
#     while num**3 <= b:
#         cnt+=1
#         num+=1
#     print(f"Case #{index}: {cnt}")

# a,b = wow()
# min_min = max(min(a/3,b),min(a/2,b/2),min(a,b/3))
# print(min_min)

# for _ in range(one()):
#     k,n = wow()
#     s1 = n*(n+1)//2
#     s2 = n*(2+(n-1)*2)//2
#     s3 = n*(4+(n-1)*2)//2
#     print(k,s1,s2,s3)

for index in range(1,one()+1):
    print(f"Recipe # {index}")
    r,now,goal = wow()
    for _ in range(r):
        name,weight,rate= inputing().split()
        weight,rate= float(weight),float(rate)
        print(name,weight/rate/now*goal*rate)
    print("----------------------------------------")










