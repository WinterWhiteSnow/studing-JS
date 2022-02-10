# a = input()
# cnt = 0
# for i in list(a):
#     cnt+=1
#     if cnt == 10:
#         print(i)
#         cnt=0
#     else:
#         print(i,end="")

# n,m = input().split()
# if n==m:
#     print(1)
# else:
#     print(0)

# repeat =int(input())
# a_dict = {1:500,2:300,3:200,4:50,5:30,6:10}
# a_limit = 21
# b_limit = 31
# # print(a_limit,b_limit)
# for _ in range(repeat):
#     a,b = map(int,input().split())
#     if 1 <= a <= a_limit:
#         cnt1=0
#         ai = 1    
#         for i in range(7):
#             cnt1+=i
#             if cnt1 >= a:
#                 # print("11111",cnt1,i,a)
#                 ai = i
#                 break
#         ai = a_dict[ai]
#     else:
#         ai = 0
#     if 1 <= b <= b_limit:
#         cnt2 = 0
#         bi = 0
#         for i in range(1,6):
#             cnt2+=2**(i-1)
#             if cnt2 >= b:
#                 # print("22222",cnt2,i,b)
#                 bi =i
#                 break
#         bi = 2**(10-bi)
#     else:
#         bi=0
#     aa = (ai+bi)*10000
#     print(aa)
# n = int(input())
# for i in range(n):
#     cnt = 0
#     count = 0
#     for _ in range(9):
#         a,b = map(int,input().split())
#         cnt+=a
#         count+=b
#     if cnt>count:
#         print("Yonsei")
#     elif cnt<count:
#         print("Korea")
#     else:
#         print("Draw")
# n= int(input())
# def wow(mini_one,mini):
#     if mini_one <mini:
#         mini_one = mini
#     return mini_one
# for _ in range(n):
#     cnt = 0
#     hp,mp,a,d,HP,MP,A,D=map(int,input().split())
#     cnt+=(wow(hp+HP,1))   
#     cnt+=5*(wow(mp+MP,1))
#     cnt+=2*(wow(a+A,0))
#     cnt+=2*(d+D)
#     print(cnt)

# a,b,c,d=map(int,input().split())
# print(56*a+24*b+14*c+6*d)

# repeat = int(input())
# for _ in range(repeat):
#     a = list(input())
#     b = list(input())
#     cnt =0
#     for x,y in zip(a,b):
#         if x!=y:
#             cnt+=1
#     print(f"Hamming distance is {cnt}.")

# repeat = int(input())
# for _ in range(repeat):
#     a = int(input())
#     num = 0
#     for x in range(1,a):
#         if x*(x+1)/2 > a:
#             break
#         for y in range(1,a):           
#             if y*(y+1)/2 > a:
#                 break
#             for z in range(1,a):                
#                 if z*(z+1)/2 > a:
#                     break
#                 if (x*(x+1)+y*(y+1)+z*(z+1))//2 == a:
#                     # print((x*(x+1)+y*(y+1)+z*(z+1))//2)
#                     # print(x,y,z)
#                     num = 1
#         if num==1:
#             break
#     print(num)
# cnt = 0
# a_list = []
# mini = 0
# maxi = 0
# for _ in range(10):
#     a = int(input())
#     a_list.append(a)
# for i in a_list:
#     if cnt+i <=100:
#         cnt+=i
#     else:
#         mini = cnt
#         maxi = cnt+i
#         break
# mini_m = 100-mini
# maxi_m = maxi-100
# if mini == 100:
#     print(mini)
# elif sum(a_list) < 100:
#     print(sum(a_list))
# else:
#     if mini_m == maxi_m:
#         print(maxi)
#     elif mini_m > maxi_m:
#         print(maxi)
#     else:
#         print(mini)
    
# a,b,c,t = map(int,input().split())
# print(t%a%b%c)
# if t%a%b == 0 or t%a%b%c ==0 or t%a ==0 or t%b == 0 or t%c == 0 or t%a%c == 0:
#     print(1)
# else:
#     print(0)
# import sys
# n = int(sys.stdin.readline().rstrip())
# for i in range(1,n+1):
#     cnt=0
#     a = list(sys.stdin.readline().rstrip())
#     b = list(sys.stdin.readline().rstrip())
#     d = list(set(a) & set(b))
#     if len(d) ==0:
#         cnt = len(a)+len(b)
#         print(f"Case #{i}: {cnt}")
#     else:
#         x_p = 0
#         y_p = 0
#         for q in d:
#             x = a.count(q)
#             y = b.count(q)
#             x_p+=x
#             y_p+=y
#             cnt+=abs(x-y)
#         # print(c,d,cnt)
#         cnt = cnt+(len(a)-x_p+len(b)-y_p)
#         print(f"Case #{i}: {cnt}")
# import sys
# repeat = int(sys.stdin.readline().rstrip())
# for _ in range(repeat):
#     n = int(sys.stdin.readline().rstrip())
#     if n ==1:
#         print(1)
#     else:
#         n_list = [n]
#         while True:
#             if n%2 == 0:
#                 n=n//2
#             else:
#                 n = n*3+1
#             n_list.append(n)
#             if n == 1:
#                 break
#         print(max(n_list))
    
# while True:
#     a = input()
#     a = a[::-1].split()
#     if a[0] == "#":
#         break
#     a_list = []
#     for i in range(len(a)-1,-1,-1):
#         a_list.append(a[i])
#     print(*a_list)

# repeat = int(input())
# for _ in range(repeat):
#     a = input()
#     b = a[::-1]
#     if a == b:
#         print("YES")
#     else:
#         print("NO") 

# repeat = int(input())
# for wow in range(1,repeat+1):
#     a,b,c,d,e,f = map(int,input().split())
#     cnt1 = a+2*b+3*c+3*d+4*e+10*f
#     x,y,z,n,m,k,l = map(int,input().split())
#     cnt2 = x+2*y+2*z+2*n+3*m+5*k+10*l
#     print(f"Battle {wow}: ",end="")
#     if cnt1 == cnt2:
#         print("No victor on this battle field")   
#     elif cnt1>cnt2:
#         print("Good triumphs over Evil")  
#     else:
#         print("Evil eradicates all trace of Good") 

# wow = map(int,input().split())
# print(sum(wow)*5)

# n = int(input())
# print(n%21)
# n = int(input())
# print(n*n*n)

# a = int(input())
# b = int(input())
# print(b-a)
# a = int(input())
# b = int(input())
# c = int(input())
# print((b-c)//a)

# n = int(input())
# for _ in range(n):
#     a = input()
#     b = a.lower()
#     g_cnt = b.count("g")
#     b_cnt = b.count("b")
#     # print(b,g_cnt,b_cnt)
#     if g_cnt==b_cnt:
#         print(f"{a} is NEUTRAL")
#     elif g_cnt > b_cnt:
#         print(f"{a} is GOOD")
#     elif g_cnt < b_cnt:
#         print(f"{a} is A BADDY")

# n = int(input())
# for _ in range(n):
#     a = input()
#     b = a[0].upper()
#     a = a[1:]
#     c = b+a
#     print(c)

# n = int(input())
# for i in range(1,n+1):
#     a = input()
#     print(f"{i}. {a}")

# while True:
#     a = input()
#     a_list = [a]
#     if a == "0":
#         break
#     else:
#         if len(a)>1:
#             while True:
#                 b = list(a)
#                 cnt = 1
#                 for i in b:
#                     cnt*=int(i)
#                 # print(b,cnt)
#                 if cnt <10:
#                     a_list.append(cnt)
#                     break
#                 else:
#                     a_list.append(cnt)
#                     a = str(cnt)
#     print(*a_list)

# while True:
#     a = input()
#     if a == "#":
#         break
    
#     b = list(a[::-1])
#     c = ""
#     for i in range(len(b)):
#         if b[i] == "b":
#             c+="d"
#         elif b[i] == "d":
#             c+="b"
#         elif b[i] == "p":
#             c+="q"
#         elif b[i] == "q":
#             c+="p"
#         else:
#             if b[i] in ["i","o","v","w","x"]:
#                 c+=b[i]
#     if len(c) != len(a):
#         print("INVALID")
#     else:
#         print(c)

while True:
    a = list(map(int,input().split()))
    if sum(a)==0:
        break
    
    l = a[0]
    a = a[1:]
    if l == len(a):
        a= set(a)
        print(*a,"$")
    
           
