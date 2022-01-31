
# repeat = int(input())
# for _ in range(repeat):
#     a = int(input())
#     for i in range(1,a+1):
#         if i+i*i > a:
#             print(i-1)
#             break

# l = int(input())
# wow = list(map(int,input().split()))
# b = []
# for i in range(1,l+1):
#     a = wow[i-1]*i
#     b.append(a)
# a = [b[0]]    
# for i in range(1,l):
#     c = b[i]-b[i-1]
#     a.append(c)
# for i in a:
#     print(i,end=" ")

# repeat = int(input())
# for _ in range(repeat):
#     dot,line = map(int,input().split())
#     print(2+line-dot)
    
# while True:
#     a,b,c,d= map(int,input().split())
#     if a==b==c==d==0:
#         break
#     print(c-b,d-a)

# while True:
#     a,b = map(int,input().split())
#     if a==b==0:
#         break
#     print(a//b,a%b,"/",b)

# a = list(map(int,input().split()))
# a.sort()
# print(a[1])
# a,b,c,d = map(str,input().split())
# a = a+b
# b = c+d
# print(int(a)+int(b))

# repeat = int(input())
# cnt = 0
# for _ in range(repeat):
#     a,b = map(int,input().split())
#     cnt+=b%a
# print(cnt)
    
# repeat = int(input())
# one = 0
# cnt = 1
# for _ in range(repeat):
#     a,b,c = map(int,input().split())
#     if c != 0:
#         one+=1
#     cnt*=b/a
# cnt = int(cnt)
# if one%2 == 1:
#     print(1,cnt)
# else:
#     print(0,cnt)

# repeat = int(input())
# for i in range(repeat):
#     cnt = 1
#     cnt+=2*i
#     print(" "*(repeat-i-1),end="")
#     if i <repeat-1:
#         for a in range(cnt):
#             if a == cnt-1:
#                 print("*")
#             elif a ==0 :
#                 print("*",end="")
#             else:
#                 print(" ",end="")
#     else:
#         print("*"*cnt)

# repeat = int(input())
# one=0
# zero=0
# for _ in range(repeat):
#     a = int(input())
#     if a == 1:
#         one+=1
#     else:
#         zero+=1
# if one>zero:
#     print("Junhee is cute!")
# else:
#     print("Junhee is not cute!")

# repeat = int(input())
# for _ in range(repeat):
#     rep = int(input())
#     a = 0
#     b = 0
#     for _ in range(rep):
#        x,y = map(float,input().split())
#        a+=x
#        b+=y*x
#     a = int(a)
#     b = b/a
#     print(f"{a} {b:.1f}") 

# repeat = int(input())
# for _ in range(repeat):
#     a,b = map(int,input().split())
#     x = a-b
#     y = 2*b-a
#     print(y,x)

# repeat = int(input())
# for _ in range(repeat):
#     wow = list(map(int,input().split()))
#     print(sum(wow))

# for _ in range(2):
#     a,b,c = map(int,input().split())
#     print(max([b-a,c-b])-1)

# repeat = int(input())
# for _ in range(repeat):
#     a,b,c,d = map(int,input().split())
#     x = (c*b)
#     y = (d*b)+a
#     if x<y:
#         print("do not parallelize")
#     elif x>y:
#         print("parallelize")
#     else:
#         print("does not matter")
# repeat = int(input())
# for _ in range(repeat):
#     a,b= map(int,input().split())
#     if a%b == 0:
#         print(a//b)
#     else:
#         print((a//b)+1)
# repeat = int(input())
# for _ in range(repeat):
#     a,b = map(int,input().split())
#     print(int((a/b)*(a/b)))

# repeat = int(input())
# for _ in range(repeat):
#     a,b = map(int,input().split())
#     wow = int(a/b)
#     print(wow*wow)

# l = int(input())
# wow = list(map(int,input().split()))
# if len(wow) == l :
#     wow.sort()
#     print(sum(wow[:-1]))

# a_atk,a_life = map(int,input().split())
# b_atk,b_life = map(int,input().split())
# b_act = a_life//b_atk
# a_act = b_life//a_atk

# if a_life%b_atk > 0:
#     b_act+=1
    
# if b_life%a_atk > 0:
#     a_act+=1
    
# if a_act>b_act:
#     print("PLAYER B")
# elif a_act<b_act:
#     print("PLAYER A")
# else:
#     print("DRAW")    

# wow = list(map(int,input().split()))
# x,y,r = map(int,input().split())
# if x in wow:
#     print(wow.index(x)+1)
# else:
#     print(0)

repeat = int(input())
for _ in range(repeat):
    days= int(input())
    cnt = 0
    for _ in range(days):
        wow=list(map(int,input().split()))
        a = max(wow)
        if a > 0:
            cnt+=a
    print(cnt)
    