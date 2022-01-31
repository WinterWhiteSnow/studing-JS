# num = int(input())
# total = 2
# b = 1
# repeat = 1
# cnt = 1
# for i in range(num-1):
#     if repeat == cnt:
#         cnt = 1
#         repeat+=1
#         b=1
#         total+=1
#     else:
#         cnt+=1
#         b+=1
# a = total-b
# print(a,b)   

# wow = list(map(int,input().split()))
# cnt = 0
# for i in wow:
#     if i > 0:
#         cnt+=1
 
# print(cnt)

# a,d,k = map(int,input().split())
# if (k-a)%d != 0 or k-a>0 and d<0 or k-a<0 and d>0:
#     print("X")
# else:
#     print((k-a)//d+1)

# num = int(input())
# num = num-1
# for i in range(1,num):
#     if i*i+i == num:
#         print(i)
#         break

# a,b,c = map(int,input().split())
# if a==b:
#     print(min(a,b)*2+(c//2)*2)
# else:
#     if a>b:
#         gap = a-b
#         plus = b
#         other = a
#     elif a<b:
#         gap = b-a
#         plus = a
#         other = b        
#     for _ in range(c):
#         if gap==0 or c ==0:
#             break
#         else:
#             gap -=1
#             plus+=1
#             c-=1
#     print(min(plus,other)*2+(c//2)*2)

# n,k = map(int,input().split())
# limit = 2*n
# cnt= 0
# method = "plus"
# for _ in range(k):
#     if method == "plus":
#         cnt+=1
#         if cnt==limit:
#             cnt=limit
#             method="minus"
#     else:
#         cnt-=1
#         if cnt == 1:
#             cnt=1
#             method="plus"
# print(cnt)

# x,y = map(int,input().split())
# a = 2*x
# b = y
# if a < 0:
#     a = a*(-1)
# if b < 0:
#     b = b*(-1)
    
# for i in range(-a,a+1):
#     for n in range(-b,b+1):
#         if i+n == 2*x and i*n == y:
#             wow = [-i,-n]
#             wow.sort()
#             if wow[0] != wow[1]:
#                 print(wow[0],wow[1])
#             else:
#                 print(wow[0])
#             exit()

# n,repeat = map(int,input().split())
# start = 1
# first_plus = n-1
# for i in range(repeat):
#     d = n-2
#     if i == 0:
#         start+=first_plus
#     else:
#         first_plus+=d
#         start+=first_plus
# print(start)
# import string
# wow = list(string.ascii_lowercase)
# n = wow.index("l")+1
# repeat = int(input())
# for _ in range(repeat):
#     sero,garo = map(int,input().split())
#     garo_l = garo-4
#     if sero < 12:
#         print(-1)
#     else:
#         if garo <4:
#             print(-1)
#         else:
#             print(garo*n-garo_l)

# sosu_dict = {}
# n = int(input())
# for i in range(2,1001):
#     if i not in sosu_dict:
#         for a in range(i,1001,i):
#             sosu_dict[a]=0
#         sosu_dict[i]=1
# sosu_list = [key for key,value in sosu_dict.items() if value == 1]
# a = [i for i in range(1,n+1)][:-1]
# print(n)
# for i in a:
#     print(i,end=" ")
# print(sosu_list[-1])

# a,b,c = map(int,input().split())
# y = round((a-b+c)/2,1)
# x = round(a - y,1)
# z = round(c - y,1)
# if min([x,y,z]) <= 0:
#     print(-1)
# else:
#     print(1)
#     print(x,y,z)



        
    
    
    
        
        