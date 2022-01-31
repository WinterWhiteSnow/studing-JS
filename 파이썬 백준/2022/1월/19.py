# repeat = int(input())
# for _ in range(repeat):
#     a = int(input())
#     wow = []
#     cnt = 0
#     print(f"Pairs for {a}:",end="")
#     for x in range(1,a+1):
#         for y in range(x+1,a+1):
#             if x+y == a:
#                 wow.append([x,y])
#     for i in range(len(wow)):     
#         s = wow[i]
#         a = s[0]
#         b = s[1]
#         if 1<=i<=len(wow)-1:
#             print(f", {a} {b}".format(a=a,b=b),end="")
#         else:
#             print(f" {a} {b}".format(a=a,b=b),end="")
#     print()

# repeat = int(input())
# for _ in range(repeat):
#     cnt = 0
#     a,b,c,d,e = map(int,input().split())
#     cnt+=a*350.34+b*230.90+190.55*c+125.30*d+e*180.90
#     print(f"${cnt:.2f}")

# repeat = int(input())
# for _ in range(repeat):
#     wow = int(input())
#     for a in range(wow):
#         for b in range(wow):
#             if a == 0 or a == wow-1:
#                 if a == wow-1 and b == wow-1:
#                     print("#")
#                     print()
#                 elif b == wow-1:
#                     print("#")
#                 else:
#                     print("#",end="")
#             else:
#                 if 0<b<wow-1:
#                     print("J",end="")
#                 else:
#                     if b == wow-1:
#                         print("#")
#                     else:
#                         print("#",end="")

# repeat = int(input())
# a = 0
# b = 0
# for _ in range(repeat):
#     A,B = map(int,input().split())
#     if A<=100 and B<=100:
#         if A>B:
#             a+=1
#         elif B>A:
#             b+=1
# print(a,b)   

# total = int(input())
# cnt = 0
# for _ in range(9):
#     a = int(input())
#     cnt+=a
# print(total-cnt)    6731
# start = int(input())
# while True:
#     a = input()
#     if a == "=":
#         break
#     b = int(input())
#     if a == "+":
#         start +=b
#     elif a == "-":
#         start -=b
#     elif a == "/":
#         start/=b
#         start = int(start)
#     elif a == "*":
#         start*=b
# print(start)
# import sys
# while True:
#     a = sys.stdin.readline().rstrip()
#     if a == "0":
#         break
#     wow = [i for i in range(1,len(a)+1)]
#     wow = wow[::-1]
#     a = list(a)
#     cnt = 0
#     for x,y in zip(a,wow):
#         z = 1
#         for i in range(1,y+1):
#             z*=i
#         cnt+=int(x)*z
#     print(cnt)

# while True:
#     a,b=map(int,input().split())
#     if sum([a,b]) == 0:
#         break
    
#     print(a+b)

# n = int(input())
# cnt = 0
# for a in range(1,500+1):
#     for b in range(1,500+1):
#         if (a*a)-(b*b) == n:
#             cnt+=1
            
# print(cnt)
# repeat = int(input())
# for i in range(1,repeat+1):
#     a = list(map(int,input().split()))
#     a.sort()
#     print(f"Scenario #{i}:")
#     if a[0]*a[0]+a[1]*a[1] == a[2]*a[2]:
#         print("yes \n")
#     else:
#         print("no \n")
# cnt = 1
# wow = []
# while True:
#     a = list(map(float,input().split()))
#     if a[0]==a[1]==a[-1]==0:
#         break
#     print(f"Triangle #{cnt}")
#     if a[-1] == -1:
#         if a[0] == 0 or a[1] ==0:
#             print("Impossible.")
#         else:
#             b = (a[0]*a[0]+a[1]*a[1])**(1/2)
#             print("c = {b:.3f}".format(b=b))
#     elif a[0] == -1:
#         if a[1] >= a[-1] or a[1]==0 or a[-1]==0:
#             print("Impossible.")
#         else:
#             b = ((a[-1]*a[-1])-(a[1]*a[1]))**(1/2)
#             print("a = {b:.3f}".format(b=b))
#     elif a[1] == -1:
#         if a[0]==0 or a[-1]==0 or a[0] >= a[-1]:   
#             print("Impossible.")
#         else:
#             b = ((a[-1]*a[-1])-(a[0]*a[0]))**(1/2)
#             print("b = {b:.3f}".format(b=b))    
#     cnt+=1
#     print()

# repeat = int(input())
# for i in range(1,repeat+1):
#     a,b = map(int,input().split())
#     c = a+b
#     print(f"Case {i}: {c}")
import sys
repeat = int(sys.stdin.readline().rstrip())
for _ in range(repeat):
    cnt = 0
    a,b = map(int,sys.stdin.readline().rstrip().split())
    for x in range(1,a):
        for y in range(x+1,a):
            if (x*x+y*y+b)/(x*y) > a:
                break
            elif (x*x+y*y+b)%(x*y) == 0:
                cnt+=1
    print(cnt)