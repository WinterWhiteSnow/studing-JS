# a = int(input())
# b = int(input())
# c = int(input())
# wow = str(a*b*c)
# a_list = [str(i) for i in range(10)]
# for i in a_list:
#     print(wow.count(i))

# n = list(input())
# for i in n:
#     print(sum(list(map(int,list(str(ord(i))))))*i)
# l,r = map(int,input().split())
# a = list(map(int,input().split()))
# for _ in range(r):
#     order,start,end = map(int,input().split())
#     if order == 1:
#         a[start-1]=end
#     elif order == 2:
#         a[start-1:end] = [0 if a[i] == 1 else 1 for i in range(start-1,end)]
#     elif order == 3:
#         a[start-1:end] = [0 if a[i] == 1 else 0for i in range(start-1,end)]
#     else:
#         a[start-1:end] = [1 if a[i] == 0 else 1 for i in range(start-1,end)]
# print(*a)

# n = input()
# print(n[:len(n)//2],n[len(n)//2:])
# l = int(input())
# a = input()
# print(a[-5:])
# wow,r = map(int,input().split())
# start = wow
# end = wow
# for _ in range(r):
#     a,b = map(int,input().split())
#     garo = [start,a]
#     sero = [b,end]
#     if garo[0]*garo[1] >= sero[0]*sero[1]:
#         start = garo[0]
#         end = garo[1]
#     else:
#         start = sero[0]
#         end = sero[1]
# print(start*end)

# r = int(input())
# wow_dict = {}
# for _ in range(r):
#     a,n = input().split()
#     n = int(n)
#     wow_dict[n] = a
# a = min(list(wow_dict.keys()))
# print(wow_dict[a])

# a = input()
# wow = ['B', 'C', 'D', 'F']
# if a.count("A")>0:
#     wow = wow
#     for i in wow:
#         a = a.replace(i,"A")
# elif a.count("B")>0:
#     wow = wow[1:]
#     for i in wow:
#         a = a.replace(i,"B")
# elif a.count("C")>0:
#     wow = wow[2:]
#     for i in wow:
#         a = a.replace(i,"C")
# else:
#     a = len(a)*"A"
# print(a)
    
# l = int(input())
# a = list(input())
# for i in range(0,len(a),l):
#     print(a[i],end="")
# import sys
# r = int(sys.stdin.readline().rstrip())
# for _ in range(r):
#     a = int(sys.stdin.readline().rstrip())
#     print(a*23)

# y1,y2,y3,y4,m1,m2,d1,d2 = map(int,list(input()))
# a = [y1,y2,y3,y4,m1,m2,d1,d2]
# r = int(input())
# a_list = {}
# for _ in range(r):#생일-오늘
#     Y1,Y2,Y3,Y4,M1,M2,D1,D2 = map(int,list(input()))
#     b = [Y1,Y2,Y3,Y4,M1,M2,D1,D2]
#     year = 0
#     month = 0
#     day = 0
#     cnt = 0
#     for x in range(len([y1,y2,y3,y4,m1,m2,d1,d2])):
#         cnt+=1
#         if cnt <=4:
#             year+=(a[x]-b[x])**2
#         elif 4<cnt<=6:
#             month+=(a[x]-b[x])**2
#         else:
#             day+=(a[x]-b[x])**2
#     a_list[int("".join(list(map(str,b))))] = year*month*day
# key = sorted(a_list.items(),key=lambda x : x[0])
# key = sorted(key,key=lambda x : x[1],reverse=True)
# print(key[0][0])

# a = input()
# if a.count("d2")>0 or a.count("D2")>0:
#     print("D2")
# else:
#     print("unrated")   

# l = int(input()) 
# p = list(map(int,input().split())) 
# sandae,jurldae = map(int,input().split())
# cnt = 0
# for i in p:
#     if i >= jurldae:
#         cnt+=1
# print(int(len(p)*sandae/100),cnt)   

# a,b = map(int,input().split())
# print(round(a/b,2000))

# a = input().split("(^0^)")
# b = a[0]
# c = a[1]
# print(b.count("@"),c.count("@"))

# r = int(input())
# a_list = []
# for _ in range(r):
#     a = input()    
#     a_list.append(a)
# if a_list.count("anj")>0:
#     print("뭐야;")
# else:
#     print("뭐야?")

