# num=int(input())
# for i in range(1,num+1):
#     empty = num-i
#     print("*"*i)
# for b in range(num-1,0,-1):
#     empty = num-b
#     print("*"*b)

# a_list = []
# for i in range(1,10):
#     a = list(map(int,input().split()))
#     num = max(a)
#     location = a.index(num)+1 
#     wow = {
#         "num":num,
#         "hang":i,
#         "index":location
#     }
#     a_list.append(wow)
# b = max([i["num"] for i in a_list])
# c = [i for i in a_list if i["num"] == b][0]
# print(c["num"],end="\n"), print(c["hang"],c["index"])

# a_list = []
# for _ in range(7):
#     a = int(input())
#     if a%2 == 1:
#         a_list.append(a)
# if len(a_list) > 0:
#     print(sum(a_list),end="\n"), print(min(a_list))
# else:
#     print(-1)

# repeat = int(input())
# for _ in range(repeat):
#     a= int(input())
#     x = a//25
#     y = (a-(25*x))//10
#     z = (a-(25*x)-(10*y))//5
#     b = (a-(25*x)-(10*y)-(5*z))//1
#     print(x,y,z,b)

# repeat = int(input())
# for _ in range(repeat):
#     num = int(input())
#     cnt = 0
#     for i in range(1,num+1):
#         wow = [i for i in range(1,i+2)]
#         cnt+=i*sum(wow)
#     print(cnt)

# a = [0,1]
# repeat = int(input())
# for i in range(2,repeat+1):
#     x = a[i-2]
#     y = a[i-1]
#     a.append(x+y)
# print(a[-1])

# wow = input()
# cnt = 0
# if len(wow) ==2:
#     a = wow[0]
#     b = wow[1]
    
#     if a == "A":
#         cnt+=4
#     elif a == "B":
#         cnt+=3
#     elif a == "C":
#         cnt+=2
#     elif a == "D":
#         cnt+=1

#     if b =="+":
#         cnt+=0.3
#     elif b == "-":
#         cnt-=0.3
    
# else:
#     a = wow    
#     if a == "A":
#         cnt+=4
#     elif a == "B":
#         cnt+=3
#     elif a == "C":
#         cnt+=2
#     elif a == "D":
#         cnt+=1


# print("{cnt:.1f}".format(cnt=cnt))

# pi = 3.1415927
# cnt = 1
# while True:
#     inch,spin,second = map(float,input().split())
#     if spin == 0:
#         break
    
#     miles = (((inch*pi*spin)/12)/5280)
#     mph = miles/((second/60)/60)
#     miles = round(miles,2)
#     mph = round(mph,2)
#     print(f"Trip #{cnt}: {miles:.2f} {mph:.2f}".format(miles=miles,mph=mph))
#     cnt+=1

# a,b =map(int,input().split())
# a = a*(1000/b)
# a = round(a,2)
# mini = a
# repeat = int(input())
# for _ in range(repeat):
#     price,gram = map(int,input().split())
#     x = (1000/gram)*price
#     x = round(x,2)
#     if mini > x:
#         mini = x

# print(f"{mini:.2f}".format(mini=mini))

# a,b = map(int,input().split())
# c,d = map(int,input().split())
# l = [(a/c)+(b/d),(c/d)+(a/b),(d/b)+(c/a),(b/a)+(d/c)]
  
# print(l.index(max(l)))

# a,b = map(int,input().split())

# print(min([a,b])//2)

# a,b,k = map(int,input().split())
# minus = "a"
# while k != 0:    
#     x = a//2
#     y = b//1
#     if x > y :
#         a-=1
#         k-=1
#     elif x < y:
#         b-=1
#         k-=1
#     else:
#         if minus == "a":
#             a-=1
#             k-=1
#             minus="b"
#         else:
#             b-=1
#             k-=1
#             minus="a"
        
# print(min([a//2, b//1]))

# num = int(input())
# cnt = 2
# for i in range(num):
#     cnt+=2**i
# print(cnt**2)
# num = int(input())
# cnt = 0
# for i in range(1,num+1):
#     wow = [a for a in range(i,i*2+1)]
#     wow = sum(wow)
#     cnt+=wow
# print(cnt)

# a = int(input())
# what = input()
# b = int(input())
# if what == "+":
#     print(a+b)
# else:
#     print(a*b)

# wow = []
# for _ in range(5):
#     a = list(map(int,input().split()))
#     a = sum(a)
#     wow.append(a)
# b = max(wow)
# print(wow.index(b)+1,b)
# wow = list(map(int,input().split()))
# a =  wow[-1]-wow[1]-1
# b =wow[1]-wow[0]-1
# print(max([a,b]))
# a,b,c = map(int,input().split())
# if a+b == c:
#     print(f"{a}+{b}={c}")
# elif b+c == a:
#     print(f"{a}={b}+{c}")
# elif a-b == c:
#     print(f"{a}-{b}={c}")
# elif a == b-c:
#     print(f"{a}={b}-{c}")
# elif a*b == c:
#     print(f"{a}*{b}={c}")
# elif b*c == a:
#     print(f"{a}={b}*{c}")
# elif a/b == c:
#     print(f"{a}/{b}={c}")
# elif b/c == a:
#     print(f"{a}={b}/{c}")

# a = list(map(int,input().split()))
# a.sort()
# b = a[-1]-a[1]
# c = a[1]-a[0]
# if b > c:
#     print(a[1]+c)
# elif b < c:
#     print(a[1]-b)
# else:
#     print(a[-1]+b)


    
    
    



        