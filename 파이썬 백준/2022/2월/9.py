# import string
# wow = list(string.ascii_uppercase)
# wow_dict = {}
# dict_wow = {}
# for i in range(1,len(wow)+1):
#     wow_dict[wow[i-1]]=i
#     dict_wow[i]=wow[i-1]
# a = list(input())
# for i in a:
#     b = wow_dict[i]-3
#     if b <= 0:
#         b+=26
#     print(dict_wow[b],end="")
# cnt = 1
# while True:
#     a = input()
#     if "E" in a:
#         break
#     aa = str(eval(a)).lower()
#     print(f"Case {cnt}: {aa}")
#     cnt+=1

# while True:
#     a,b = map(int,input().split())
#     if a==b==0:
#         break
#     wow = 2*a-b
#     why = 2*b-a
#     print(min(wow,why))

# import string
# a=list(string.ascii_lowercase)
# while True:
#     b = input()
#     if b == "*":
#         break
#     b = b.split()
#     b = list("".join(b))
#     b = set(b)
#     if len(a) == len(b):
#         print("Y")
#     else:
#         print("N")

# while True:
#     a = int(input())
#     if a == 0:
#         break
#     cnt = 0
#     for i in range(1,a+1):
#         cnt+=i**2
#     print(cnt)
# repeat = int(input())

# for _ in range(repeat):
#     a = input()
#     l = len(a)//2
#     a = a[l-1:l+1]
#     if a[0] ==a[1]:
#         print("Do-it")
#     else:
#         print("Do-it-Not")
# n = int(input())
# for _ in range(n):
#     a = int(input())
#     if a%2 == 0:
#         print("even")
#     else:
#         print("odd")

# slot,insert = map(int,input().split())
# a = list(range(1,slot+1))
# b = []
# for _ in range(insert):
#     start,gap = map(int,input().split())
#     for i in range(start,slot+1,gap):
#         b.append(i)
# print(len(a)-len(set(b)))
# import string
# r = int(input())
# a = list(string.ascii_uppercase)
# answer = []
# for wow in range(r):    
#     n = list(input())
#     asdf = ""
#     for i in n:
#         c = a.index(i)+1
#         if c >=26:
#             c=c-26
#         asdf+=a[c]
#     answer.append(asdf)
# for i in range(1,r+1):
#     print(f"String #{i}")
#     print(answer[i-1])
#     if r >1:      
#         print()
# a = input()
# joi = 0
# ioi = 0
# for i in range(0,len(a)+1,1):
#     wow = a[i:i+3]
#     if wow == "JOI":
#         joi+=1
#     elif wow == "IOI":
#         ioi+=1
# print(joi)
# print(ioi)

# repeat = int(input())
# for _ in range(repeat):
#     a = int(input())
#     room = list(range(1,a+1))
#     room_dict = {}
#     for i in room: #열리면0 닫히면1
#         room_dict[i]=0
#     for i in range(2,a+1):
#         for b in range(i,a+1,i):
#             room_dict[b]=(room_dict[b]+1)%2
#     wow = [key for key,value in room_dict.items() if value == 0]
#     print(len(wow))
# cnt = 1
# while True:
#     a = list(map(int,input().split()))
#     if sum(a) == 0:
#         break
#     r,w,l = map(int,a)
#     # print(w*w+l*l,(2*r)*(2*r))
#     if w*w+l*l <= (2*r)*(2*r):
#         print(f"Pizza {cnt} fits on the table.")
#     else:
#         print(f"Pizza {cnt} does not fit on the table.")
#     cnt+=1

# n = 4
# while True:
#     a0 = int(input())
#     if a0 == 0:
#         break    
#     a_list = [a0]
#     while True:
#         a0 = str(a0*a0)
#         a0 = a0.rjust(n*2,"0")
#         a0=int(a0[n//2:n//2+4])
#         if a0 not in a_list:
#             a_list.append(a0)
#         else:
#             break
#     print(len(a_list))
# def div(wow,num):
#     start = wow
#     start_list = []
#     while True:
#         if start == 0:
#             break
#         a = str(start%num)
#         start_list.append(a)
#         start = start//num
#     return start_list

# for i in range(1000,10000):
#     ten = sum(list(map(int,list(str(i)))))
#     sixteen = sum(list(map(int,div(i,16)[::-1])))
#     twelve = sum(list(map(int,div(i,12)[::-1])))    
#     if ten ==sixteen==twelve:
#         print(i)
# a = int(input())
# cnt = 1
# for i in range(1,a+1):
#     cnt*=i
# cnt = str(cnt).replace("0","")
# print(cnt[-1])

# a = list(input())
# start = ""
# cnt = 0
# for i in range(len(a)):
#     if a[i] != start:
#         cnt+=10
#     else:
#         cnt+=5
#     start = a[i]
# print(cnt)
# import string
# while True:
#     a = list(string.ascii_lowercase)    
#     b = list(input().replace(" ","").lower())
#     if len(b) == 0:
#         pass
#     elif len(b) == 1 and b[0] == "#":
#         break
        
#     c = [i for i in b if i in a]
#     print(len(set(c)))



    
        
