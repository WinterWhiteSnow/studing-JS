# while True:
#     try:
#         n,k = map(int,input().split())
#         total = n
#         wow = n
#         while True:
#             a = wow//k
#             x = wow%k
#             # print(wow,x)
#             total+=a
#             wow = a+x
#             # print("if이전",wow)
#             if wow < k:
#                 break

#         print(total)      
#     except:
#         exit()

# n,k = map(str,input().split())
# count = 0
# start = 1
# list_list = []
# while len(list_list) != int(n):
#     if str(start).count(k) == 0:
#         list_list.append(start)
#     start+=1
# print(max(list_list))

# import string
# a = string.ascii_lowercase
# a_dict = {}
# b_dict = {}
# for i in range(1,len(a)+1):
#     a_dict[a[i-1]]=i
#     b_dict[i]=a[i-1]
# # print(a_dict,b_dict)
# x = list(input())
# y = list(input().replace(" ",""))
# x_index = 0
# y_index = 0
# while True:
#     if x[x_index] == " " or y[y_index] == " ":
#         print(" ",end="")
#     else:
#         t = a_dict[x[x_index]]-a_dict[y[y_index]]
#         if t == 0:
#             t = 26
#         else:
#             t=t%26
#         print(b_dict[t],end="")
#     x_index+=1
#     y_index+=1
#     if x_index > len(x)-1:
#         break
#     if y_index > len(y)-1:
#         y_index=0     

# repeat = int(input())
# a_list = []
# for _ in range(repeat):
#     a = int(input())
#     a_list.append(a)
# if (a_list[2]+a_list[0])%a_list[1] == 0:
#     print(a_list[-1]+(a_list[1]-a_list[0]))
# else:
#     print(a_list[-1]*(a_list[1]//a_list[0]))

# import string
# wow = string.ascii_uppercase
# wow_dict = {}
# for i in range(len(wow)):
#     wow_dict[wow[i]]=i

# repeat = int(input())
# for _ in range(repeat):
#     a = input().split("-")
#     text = list(a[0])
#     num = int(a[1])
#     cnt = 2
#     b = 0
#     for i in text:
#         b+=(wow_dict[i])*(26**cnt)
#         cnt-=1
#     if abs(b-num) <= 100:
#         print("nice")
#     else:
#         print("not nice")

# a = input()
# b = input()
# if len(a)>len(b):
#     x = a
#     y = b
# else:
#     x = b
#     y = a
    
# x_set = set(x)
# x_dict = {}
# cnt = 0
# for i in x_set:
#     x_dict[i]=x.count(i)
# for i in x_set:
#     w = min(x_dict[i],y.count(i))
#     cnt+=w
# print(len(x)-cnt+len(y)-cnt)

wow = input().split()
a = wow[0].split(":")
b = wow[1].split(":")
if int(a[0])>int(b[0]):#235959까지
    cnt = 0
    a = int("".join(a))        
    b = int("".join(b))
    print(a,b)
    for i in range(a,235959+1):
        if i%3==0:
            cnt+=1
    for i in range(3,b+1):
        if i%3==0:
            cnt+=1
    print(cnt)    
else:
    a = int("".join(a))        
    b = int("".join(b))
    print(a,b)
    cnt=0
    for i in range(a,b+1):
        if i%3 == 0:
            cnt+=1  
    print(cnt)  
    
