# n = int(input())
# if n%2 == 0:
#     cnt = n-4
#     count = 2
# else:
#     cnt = n-3
#     count = 1
# for i in range(n):
#     if i == 0 or i == n-1:
#         print("*"*n)
#     elif n%2 == 0:
#         if n//2-1<=i<=n//2:#중앙2개별
#             print("*"+" "*((n-4)//2)+"**"+" "*((n-4)//2)+"*")
#         elif 0<i<n//2-1:
#             print("*"+" "*(i-1)+"*"+" "*(n-4-(2*(i-1)))+"*"+" "*(i-1)+"*")
#         else:
#             print("*"+" "*((cnt-count)//2)+"*"+" "*(count)+"*"+" "*((cnt-count)//2)+"*")
#             count+=2
#     elif n%2==1:#중앙1개별
#         if i==n//2:
#             print("*"+" "*((n-3)//2)+"*"+" "*((n-3)//2)+"*")
#         elif 0<i<n//2:
#             print("*"+" "*(i-1)+"*"+" "*(n-4-(2*(i-1)))+"*"+" "*(i-1)+"*")
#         else:
#             print("*"+" "*((cnt-count)//2)+"*"+" "*(count)+"*"+" "*((cnt-count)//2)+"*")
#             count+=2

# r = int(input())
# start = int(input())
# cnt = 0
# for _ in range(r):
#     a =int(input())
#     b = abs(a-start)
#     if b > 180:
#         b = 360-b
#     cnt+=b
#     start = a
# print(cnt)

# from collections import deque
# a =deque(list(input()))
# cnt = 0
# for _ in range(len(a)):
#     a.rotate(1)
#     cnt+=int("".join(list(a)))
# print(cnt)

# l = int(input())
# a = list(input())
# cnt = 0
# bonus = 0
# answer= ""
# if len(a) == l:
#     for i in range(1,len(a)+1):
#         if a[i-1] == "O":
#             cnt+=i
#             if answer == "O":
#                 cnt+=bonus
#             answer = "O"
#             bonus+=1
#         else:
#             bonus=0
#             answer="X"
#     print(cnt)

# left = "qwertyasdfgzxcvb"
# right = "uiophjklnm"
# a = list(input())
# wow = 0
# l_point = 0
# r_point = 0
# for i in a:
#     if i.isupper():
#         wow+=1
#         i = i.lower()
#     elif i == " ":
#         wow+=1
#     if i in left:
#         l_point+=1
#     if i in right:
#         r_point+=1
# # print(wow,l_point,r_point)
# if l_point > r_point:
#     while wow !=0:
#         r_point+=1
#         wow-=1
#         if r_point==l_point:
#             break        
# else:
#     while wow !=0:
#         l_point+=1
#         wow-=1
#         if r_point==l_point:
#             break
# if wow>0:
#     for i in range(1,wow+1):
#         wow-=1
#         if i%2 == 1:
#             l_point+=1
#         else:
#             r_point+=1
# print(l_point,r_point)

# l = int(input())
# a = list(input())
# if len(a) == l :
#     if len(a) ==1:
#         if a[0] == "?":
#             print("a")
#         else:
#             print(a[0])
#     else:
#         for i in range(len(a)//2+1):
#             if a[i] =="?":
#                 if a[(i*(-1))-1] == "?":
#                     a[i]=a[(i*(-1))-1]="a"
#                 else:
#                     a[i]=a[(i*(-1))-1]
#             else:
#                 if a[(i*(-1))-1] == "?":
#                     a[(i*(-1))-1]=a[i]
#         print("".join(a))
# r,l = map(int,input().split())
# for _ in range(r):
#     a = list(input())
#     for i in range(len(a)//2+1):
#         if a[i] ==".":
#             if a[(i*(-1))-1] == ".":
#                 a[i]=a[(i*(-1))-1]
#             else:
#                 a[i]=a[(i*(-1))-1]
#         else:
#             if a[(i*(-1))-1] == ".":
#                 a[(i*(-1))-1]=a[i]
#     print("".join(a))
# a = input().split()
# b = input()
# a_dict = {}
# for i in range(1,51):
#     if i<=5:
#         a_dict[i]="A+"
#     elif 5<i<=15:
#         a_dict[i]="A0"
#     elif 15<i<=30:
#         a_dict[i]="B+"
#     elif 30<i<=35:
#         a_dict[i]="B0"
#     elif 35<i<=45:
#         a_dict[i]="C+"
#     elif 45<i<=48:
#         a_dict[i]="C0"
#     else:
#         a_dict[i]="F"
    
# print(a_dict[a.index(b)+1])
# r = int(input())
# for _ in range(r):
#     a = list(input())
#     if len(a) == 7:
#         if len(set(a))==2:
#             if a[0]==a[1]==a[4]:
#                 if a[2]==a[3]==a[5]==a[6]:
#                     print(1)
#                 else:
#                     print(0)
#             else:
#                 print(0)
#         else:
#             print(0)
#     else:
#         print(0)
# count = 2
# while True:
#     a = input()
#     if a == "Was it a cat I saw?":
#         break
#     a = list(a)
#     for i in range(0,len(a),count):
#         print(a[i],end="")
#     count+=1
#     print()
r = int(input())
a_list = []
for _ in range(r):
    a,b = input().split()
    b = int(b)
    a_list.append([a,b])
a_list.sort(key=lambda x : x[0])
a_list.sort(key=lambda x :x[1],reverse=True)
print(a_list[0][0])
    

                
        
                    