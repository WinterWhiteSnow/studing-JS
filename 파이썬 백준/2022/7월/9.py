import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# while True:
#     a = one()
#     if a == 0:
#         break
    
#     if 1000000<= a <=5000000:
#         print(int(a*0.9))
#     elif a>5000000:
#         print(int(a*0.8))
#     else:
#         print(a)

# n_list = list(map(int,list(inputing())))
# for i in range(len(n_list)):
#     if i%2==0:
#         n_list[i]=n_list[i]*2
#         if n_list[i]>=10:
#             a,b = list(str(n_list[i]))        
#             n_list[i]=int(a)+int(b)
# if sum(n_list)%10 == 0:
#     print("DA")
# else:
#     print("NE")

# cnt = 0
# for _ in range(one()):
#     a = inputing()
#     b = int(a[-1])
#     a = int(a[:-1])
#     cnt+=a**b
# print(cnt)
# a,b,c = 0,0,0
# for _ in range(one()):
#     x,y,z= wow()
#     a+=x
#     b+=y
#     c+=z
#     index = min(a,b,c)
#     if index>=30:
#         print(min(a,b,c))
#         a-=index
#         b-=index
#         c-=index
#     else:
#         print("NO")

# n_dict = {1:"Yakk",2:"Doh",3:"Seh",4:"Ghar",5:"Bang",6:"Sheesh"}
# num_dict = {1:"Habb Yakk",2:"Dobara",3:"Dousa",4:"Dorgy",5:"Dabash",6:"Dosh"}
# for index in range(1,1+one()):
#     print(f"Case {index}: ",end="")
#     n_list = sorted(list(wow()),reverse=True)
#     str_list = []
#     if n_list[0]==n_list[1]:
#         str_list.append(num_dict[n_list[0]])
#     elif n_list[0]==6 and n_list[1]==5:
#         str_list.append("Sheesh Beesh")
#     else:
#         for i in n_list:
#             str_list.append(n_dict[i])
#     print(*str_list)

# oil,b,s=wow()
# a=oil//b
# while a>=0:
#     if (oil-a*b)%s==0:
#         break
#     else:
#         a-=1
# if a>=0:
#     print(a,(oil-a*b)//s)
# else:
#     print("Impossible")

# l=one()
# d=one()
# x=one()
# n_list = []
# for i in range(l,d+1):
#     if sum(map(int,list(str(i))))==x:
#         n_list.append(i)
# print(min(n_list))
# print(max(n_list))

# a,b=wow()
# c,d = wow()
# n_dict = {}
# for i in range(a+1,b+1):
#     if i not in n_dict:
#         n_dict[i]=1
# for i in range(c+1,d+1):
#     if i not in n_dict:
#         n_dict[i]=1
# print(len(list(n_dict.keys())))

for index in range(1,one()+1):
    a,b,k = wow()
    cnt = 0
    for x in range(a):
        for y in range(b):
            c = x & y
            if c<=k:
                print(x,y,"c",c)
                cnt+=1
                
    print(cnt)

   
        