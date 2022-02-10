# import sys
# n = int(sys.stdin.readline().rstrip())
# end = 2**n-1
# wow = (end*(end+1))//2
# print(bin(wow)[2:])

# a,b = input().split()
# l = max(len(a),len(b))
# a = a.zfill(l)
# b = b.zfill(l)
# cnt= ""
# for x,y in zip(a,b):
#     cnt+=str(int(x)+int(y))
# print(cnt)

# repeat = int(input())
# for _ in range(repeat):
#     sort = int(input())
#     list_list = []
#     for _ in range(sort):
#         a = list(map(int,input().split()))
#         b = a[0]/a[1]
#         a.append(b)
#         list_list.append(a)
#     list_list.sort(key=lambda x : x[0])
#     list_list=sorted(list_list,key=lambda x : x[2],reverse=True)
#     print(list_list[0][1])

# r = int(input())
# for _ in range(r):
#     a = list(map(int,input().split()))
#     a.sort()
#     a = a[1:-1]
#     if a[-1]-a[0] >=4:
#         print("KIN")
#     else:
#         print(sum(a))

# r = int(input())
# for _ in range(r):
#     a = input()
#     print(a[0]+a[-1])

# while True:
#     a = input()
#     if a == "#":
#         break
    
#     b = ["a","e","i","o","u"]
#     for i in list(a):
#         if i in b:
#             a = a[a.index(i):]+a[:a.index(i)]
#             break
#     print(a+"ay")

# s = int(input())
# a = input()
# c = ""
# b = input()
# for _ in range(s):
#     for i in list(a):
#         if i == "0":
#             c+="1"
#         else:
#             c+="0"
#     a = c
#     c = ""    
# if a == b :
#     print("Deletion succeeded")
# else:
#     print("Deletion failed")

# n,k = map(int,input().split())
# n_dict = {}
# wow = []
# for i in range(1,n+1):
#     a = int(input())
#     n_dict[i]=a
# for i in range(k):
#     a = int(input())
#     b = [key for key,value in n_dict.items() if value <= a]
#     c = min(b)
#     wow.append(c)
# set_wow = set(wow)
# counting_list = []
# for i in set_wow:
#     a = wow.count(i)
#     counting_list.append(a)
# asdf = [i for i in set_wow if wow.count(i) == max(counting_list)]
# print(min(asdf))

# north,east,r = map(int,input().split())
# move_cnt = 0
# start_x = 0
# start_y = 0
# for _ in range(r):
#     x,y = map(int,input().split())
#     if start_x==start_y==0:
#         start_x=x
#         start_y=y
#     else:
#         maxi = max(x-start_x,y-start_y)
#         mini = min(x-start_x,y-start_y)
#         if maxi >=0 and mini >=0:
#             move_cnt+=maxi
#         elif mini < 0 and maxi <0:
#             move_cnt+=abs(mini)
#         else:
#             move_cnt+=abs(mini)+abs(maxi)         
#         start_x=x
#         start_y=y
# print(move_cnt)

# a = list(map(int,input().split()))
# a.sort()
# wow = [i for i in range(a[0]+1,a[1])]
# print(len(wow))
# print(*wow)

# l = int(input())
# a = list(input())
# if len(a) == l:
#     A = a.count("A")
#     B = a.count("B")
#     if A>B:
#         print("A")
#     elif A<B:
#         print("B")
#     else:
#         print("Tie")

# while True:
#     a = input()
#     if a == "EOI":
#         break
    
#     a = a.lower()
#     if "nemo" in a:
#         print("Found")
#     else:
#         print("Missing")
    
# r = int(input())
# for _ in range(r):
#     a = input().lower()
    
#     if a == a[::-1]:
#         print("Yes")
#     else:
#         print("No")

# r = int(input())
# head_list = []
# for index in range(r):
#     head = int(input())
#     act = list(input())
#     for i in act:
#         if i == "c":
#             head+=1
#         else:
#             head-=1
#     if head < 0:
#         head = 0  
#     head_list.append(head)

# for i in range(len(head_list)):
#     num = i+1
#     print(f"Data Set {num}:")
#     print(head_list[i])
#     if i==len(head_list)-1:
#         pass
#     else:
#         print()

# from datetime import datetime, timedelta
# n = int(input())
# date_to_compare = datetime.strptime("20140402", "%Y%m%d")
# a = date_to_compare+timedelta(days=n-1)
# print(a.date())

# a = list(map(int,input().split()))
# b = list(map(int,input().split()))
# A=0
# B=0
# for x,y in zip(a,b):
#     if x > y:       
#         A+=1
#     elif x<y:
#         B+=1
# if A > B:
#     print("A")
# elif A < B:
#     print("B")
# else:
#     print("D")

# r = int(input())
# a = input().split()
# n = input()
# print(a.count(n))

# import string

# a = list(string.ascii_lowercase)
# b = input()
# for i in a:
#     print(b.count(i),end=" ")

# import string
# a = list(string.ascii_lowercase)
# A = list(string.ascii_uppercase)
# while True:    
#     try:        
#         space = ord(" ")
#         so = 0
#         dae = 0
#         num = 0
#         s = 0
#         answer = list(input())
#         for i in answer:
#             if i in a:
#                 so+=1
#             elif i in A:
#                 dae+=1
#             elif ord(i) == space:
#                 s+=1
#             else:
#                 num+=1
#         print(so,dae,num,s)            
                
#     except:
#         exit()

# a = list(map(int,input().split(",")))
# print(sum(a))

# s = ""
# while True:
#     try:
#         a = input()
#         s+=a
#     except:
#         break
# s = list(map(int,s.split(",")))
# print(sum(s))

n = int(input())
print(bin(n)[2:])
    

             


    
    



