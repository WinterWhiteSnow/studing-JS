# while True:
#     wow = input().split()
#     if wow[0] == "0" and wow[1] == "0":
#         break
    
#     a = list(map(int,wow[0]))
#     b = list(map(int,wow[1]))
#     a = a[::-1]
#     b = b[::-1]
#     l = min(len(a),len(b))
#     plus = 0
#     cnt=0
#     for i in range(l):
#         if a[i]+b[i]+plus > 9:
#             cnt+=1
#             plus+=1
#         else:
#             plus=0
#     if len(a) > l:
#         for i in a[l:]:
#             if i+plus > 9:
#                 cnt+=1
#                 plus+=1
#             else:
#                 plus=0
#     elif len(b) > l:
#         for i in b[l:]:
#             if i+plus > 9:
#                 cnt+=1
#                 plus+=1
#             else:
#                 plus=0
        
#     print(cnt)
# 가위 S 바위 R 보 P
# repeat = int(input())
# for _ in range(repeat):
#     n_repeat = int(input())
#     p1 = 0
#     p2 = 0
#     for _ in range(n_repeat):
#         one,two = input().split()
#         if one == "S":
#             if two == "R":
#                 p2+=1
#             elif two == "P":
#                 p1+=1
#         elif one == "R":
#             if two == "S":
#                 p1+=1
#             elif two == "P":
#                 p2+=1
#         elif one =="P":
#             if two == "S":
#                 p2+=1
#             elif two == "R":
#                 p1+=1
#     if p1 > p2:
#         print("Player 1")
#     elif p1 < p2:
#         print("Player 2")
#     else:
#         print("TIE")

# n = int(input())
# while True:
#     a = int(input())
#     if a == 0:
#         break
    
#     if a%n == 0:
#         print(f"{a} is a multiple of {n}.")
#     else:
#         print(f"{a} is NOT a multiple of {n}.")

# for i in range(6,101):
#     for a in range(2,101):
#         for b in range(a+1,101):
#             for c in range(b+1,101):
#                 if i*i*i == a*a*a+b*b*b+c*c*c:
#                     print(f"Cube = {i}, Triple = ({a},{b},{c})")
#                 if i*i*i<(a*a*a+b*b*b+c*c*c):break

# start = float(input())
# while True:
#     a = float(input())
#     if a == 999:
#         break
#     wow = round(a-start,2)
#     print("{:.2f}".format(wow))
#     start = a

# while True:
#     wow = list(map(int,input().split()))
#     if wow[0] == wow[1] == wow[2] == 0:
#         break
#     a = wow[0]
#     b = wow[1]
#     c = wow[2]
#     if (a+c)/2 == b:
#         if a==b==c:
#             print("GP",a)
#         else:
#             print("AP",b-a+c)
#     else:
#         print("GP",int((b/a)*c))
# cnt = 0
# while True:
#     cnt+=1
#     a0 = int(input())
#     if a0 == 0:
#         break
    
#     a1 = 3*a0
#     if a1%2 == 0:
#         a2 = a1/2
#     else:
#         a2 = (a1+1)/2
#     a3 = 3*a2
#     a4 = a3/9
#     if a1%2 == 0:
#         a0 = 2*a4
#         print(f"{cnt}. even",int(a4))
#     else:
#         a0=(2*a4)+1
#         print(f"{cnt}. odd",int(a4))
# while 1:
#     a = list(map(int,input().split()))
#     if sum(a) == 0:
#         break
#     a.sort()
#     if a[2] >= a[1]+a[0]:
#         print("Invalid")
#     else:    
#         if len(set(a)) == 1:
#             print("Equilateral")
#         elif len(set(a))==3:
#             print("Scalene")
#         elif len(set(a))==2:
#             print("Isosceles")
# while "1":
#     a,b = map(int,input().split())
#     if a == b == 0:
#         break
    
#     if b%a == 0:
#         print("factor")
#     elif a%b ==0:
#         print("multiple")
#     else:
#         print("neither")

repeat = int(input())
for _ in range(repeat):
    a = int(input())
    print(f"Pairs for {a}:",end=" ")
    wow = []
    for x in range(1,a+1):
        for y in range(x+1,a+1):
            if x+y == a:
                wow.append([x,y])
    cnt = 0
    for i in wow:
        print(i)
        a = i[0]
        b = i[1]
        print(f"{a} {b},",end=" ")
        cnt += 1
    print()
                
        
        
        