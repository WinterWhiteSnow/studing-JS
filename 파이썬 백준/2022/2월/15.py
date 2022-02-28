# days,r = map(int,input().split())
# wow = {}
# for _ in range(r):
#     standard,a,b = map(int,input().split())
#     if standard == 1:
#         if a not in wow:
#             wow[a]=b
#         else:
#             wow[a]+=b
#     else:
#         start = a
#         end = b
#         list_list = [value for key,value in wow.items() if start<=key<=end]
#         print(sum(list_list))

# a,b = map(int,input().split())
# wow =a*b
# if wow%3 == 0:
#     print("YES")
# else:
#     print("NO")
# l = int(input())
# a = list(map(int,input().split()))
# if len(a) == l:
#     print(sum(a)-max(a))

# r = int(input())
# for _ in range(r):
#     n,zinsu = map(int,input().split())
#     wow = div(n,zinsu)
#     a = "".join(wow)
#     b = "".join(wow[::-1])
#     # print(a,b)
#     if a == b:
#         print("1")
#     else:
#         print(0)
# l = int(input())
# a = input().split()
# for i in a:
#     n = int(i)
#     wow = []
#     for b in range(1,n//2):
#         if n%b == 0:
#             wow.extend([b,n//b])
#     wow = list(set(wow))
#     wow.sort()
#     if sum(wow[:-1]) == n:
#         print("Perfect")
#     elif sum(wow[:-1]) > n :
#         print("Abundant")
#     else:
#         print("Deficient")
# n = input()
# for i in range(3):
#     if i ==1:
#         print(":fan:",end="")
#         print(f":{n}:",end="")
#         print(":fan:")
#     else:
#         print(":fan:"*3)

# r=int(input())
# a_dict = {}
# for i in range(r):
#     a = list(map(int,input().split()))
#     a_dict[i]=a
# a = list(a_dict.values())
# a.sort(key=lambda x : (x[1],x[2]))
# a.sort(key=lambda x : x[0],reverse=True)
# wow = [key for key,value in a_dict.items() if value == a[0]]
# print(wow[0]+1)

# n = int(input())
# if n%2 == 0:
#     print("I LOVE CBNU")
# else:
#     print("*"*n)
#     count = 1
#     for i in range(n//2+1):
#         if i == 0:
#             print(" "*(n//2),end="")
#             print("*")
#         else:
#             print(" "*(n//2-count),end="")
#             print("*",end="")
#             print(" "*(n-((n//2-count)*2+2)),end="")
#             print("*")
#             count+=1
# n = list(map(int,input().split()))
# a = sorted(n)
# if n == a :
#     print("Good")
# else:
#     print("Bad")
    
# r = int(input())
# for _ in range(r):
#     a = list(map(int,list(input())[::-1]))
#     cnt = ""
#     for i in range(1,len(a)+1):
#         if i%2 == 0:
#             b = a[i-1]*2
#             if b>9:
#                 b = sum(map(int,list(str(b))))
#                 # print(b)
#             cnt+=str(b)
#         else:
#             cnt+=str(a[i-1])
#     cnt = sum(map(int,list(cnt)))
#     if cnt%10 == 0:
#         print("T")
#     else:
#         print("F")
# l = int(input())
# num = 0
# maxi = 0
# wow_dict = {}
# cc = "PROBRAIN, GROW, ARGOS, ADMIN, ANT, MOTION, SPG, COMON, ALMIGHTY,"
# cc = [i.strip() for i in cc.split(",")]
# for i in range(1,10):
#     wow_dict[i]=cc[i-1]
# for i in range(9):
#     a = list(map(int,input().split()))
#     b = max(a)
#     if b > maxi:
#         maxi=b
#         num =i+1
# print(wow_dict[num])

#rating 767    

# import string
# a = list(string.ascii_uppercase)
# a_dict = {}
# for i in range(1,27):
#     a_dict[a[i-1]]=i
# l = int(input())
# b = list(input())
# if len(b) == l:
#     cnt = 0
#     for i in b:
#         cnt+=a_dict[i]
#     print(cnt)

# a = list(input())
# r = int(input())
# for _ in range(r):
#     x,y = map(int,input().split())
#     X = a[x]
#     Y = a[y]
#     a[x]=Y
#     a[y]=X
# print("".join(a))
# import string
# a = list(string.ascii_uppercase)
# a_dict = {}
# for i in range(1,27):
#     a_dict[a[i-1]]=i
# r = int(input())
# for _ in range(r):
#     b = list(input().replace(" ",""))
#     cnt = 0
#     for i in b:
#         cnt+=a_dict[i]
#     if cnt == 100:
#         print("PERFECT LIFE")
#     else:
#         print(cnt)

# l = int(input())
# a = list(map(int,input().split()))
# if len(a) == l:
#     print(max(a)-min(a))

# a = int(input())
# b = input()
# if b.replace("12","") == "" or b.replace("21","")  == "":
#     print("Yes")
# else:
#     print("No")
import sys
l = int(sys.stdin.readline().rstrip())
a=list(map(int,sys.stdin.readline().rstrip().split()))
if len(a) == l:
    for i in a:
        cnt = 0
        for x in range(1,i+1):
            if x%3 == 0 or x%7 ==0:
                cnt+=x
        print(cnt)             
         
        
    