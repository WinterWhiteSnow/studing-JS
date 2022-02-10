# while True:
#     a = list(map(int,input().split()))
#     if sum(a)==0:
#         break
    
#     l = a[0]
#     a = a[1:]
#     if len(a) == l:
#         num = 0
#         a_list = []
#         for i in a:
#             if num != i:
#                 a_list.append(i)
#                 num=i
#         print(*a_list,"$")

# while True:
#     a = input()
#     if a == "#":
#         break
    
#     if "e" in a:#1갯수 짝수
#         b = a.count("1")
#         if b%2 == 0:
#             print(a.replace("e","0"))
#         else:
#             print(a.replace("e","1"))
                       
#     elif "o" in a:#1갯수 홀수
#         b = a.count("1")
#         if b%2 == 0:
#             print(a.replace("o","1"))
#         else:
#             print(a.replace("o","0")) 

# while True:
#     a = input()
#     if a == "***":
#         break
#     print(a[::-1])

# while True:
#     try:
#         start,plus,goal = map(float,input().split())
#         cnt = 0
#         while True:
#             cnt+=1
#             start+=start*plus*0.01
#             if start >= goal:
#                 break
#         print(cnt)
#     except:
#         exit()

# a = input()
# b = input()
# if len(a) >=len(b):
#     print("go")
# else:
#     print("no")

# repeat = int(input())
# for _ in range(repeat):
#     a = input()
#     if a == "P=NP":
#         print("skipped")
#     else:
#         print(eval(a))

# a,discover,need = map(int,input().split())
# a = a+discover
# cnt = 0
# b = 0
# while True:
#     c = a//need
#     b = a%need
#     cnt+=c
#     # print(c,b)
#     a = c+b
#     if a < need:
#         break
# print(cnt)
# cnt = 0
# while True:
#     try:
#         a = input()
#         cnt+=1
#     except:
#         print(cnt)
#         exit()

# n,m = map(int,input().split())
# cnt = 0
# for i in range(m+1):
#     cnt+=2**i
# if n>cnt:
#     print("no")
# else:
#     print("yes")

# repeat = int(input())
# for _ in range(repeat):
#     l = int(input())
#     a = list(map(int,input().split()))
#     if len(a) == l :
#         mini = min(a)
#         maxi = max(a)
#         print(2*(maxi-mini))

# repeat = int(input())
# for _ in range(repeat):
#     p,m = map(int,input().split())
#     a = []
#     for _ in range(p):
#         b = input()
#         a.append(b)
#     a_set = set(a)
#     print(len(a)-len(a_set))   

# import string
# a = list(string.ascii_uppercase)
# a_dict = {}
# for i in range(1,len(a)+1):
#     a_dict[a[i-1]]=i
# repeat = int(input())
# for _ in range(repeat):
#     a,b = input().split()
#     a = list(a)
#     b = list(b)
#     print("Distances:",end="")
#     for x,y in zip(b,a):
#         xx = a_dict[y]
#         yy = a_dict[x]
#         if yy >= xx:
#             o = yy-xx
#         else:
#             o = yy+26-xx
#         print(f" {o}",end="")
#     print() 

# repeat = int(input())
# for _ in range(repeat):
#     a = input().split()
#     n = float(a[0])
#     b = a[1:]
#     for i in b:
#         if i == "@":
#             n*=3
#         elif i =="%":
#             n+=5
#         elif i == "#":
#             n-=7
#     print(f"{n:.2f}")   

# repeat =int(input())
# for _ in range(repeat):
#     a = input().split()
#     b = a[2:]
#     c = a[:2]
#     print(*b,*c)   

# repeat =int(input())
# for _ in range(repeat):
#     a = input().lower()
#     print(a)  

# repeat,mini = map(int,input().split())
# order_dict = {}
# start = 1
# dd = []
# for i in range(1,repeat+1):
#     order = int(input())
#     order_dict[i]=order
# for i in range(mini):
#     a = int(input())
#     start+=a
#     if start < repeat:
#         start+=order_dict[start]
#     if start >= repeat:
#         dd.append(i)
# print(dd[0]+1)

# w = []
# k = []
# for _ in range(10):
#     a = int(input())
#     w.append(a)
# for _ in range(10):
#     a = int(input())
#     k.append(a)
# w.sort()
# k.sort()
# print(sum(w[-3:]),sum(k[-3:]))

# a = int(input())
# b = "500엔,100엔,50엔,10엔,5엔,1엔,"
# b = list(map(int,b.split("엔,")[:-1]))
# cnt=0
# a = 1000-a
# for i in b:
#     c = a//i
#     cnt+=c
#     a = a-(i*c)
# print(cnt)

# total = list(range(1,31))
# c = []
# for _ in range(28):
#     a = int(input())
#     c.append(a)
# b = list(set(total)-set(c))
# b.sort()
# for i in b:
#     print(i)


    
    

