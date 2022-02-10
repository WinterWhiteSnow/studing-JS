# import string

# a = list(string.ascii_uppercase)
# cnt = 0
# num = 2
# a_dict = {}
# for i in range(15):
#     if cnt == 3:
#         cnt=0
#         num+=1
#     a_dict[a[i]]=num
#     cnt+=1
# cnt = 0
# limit = 4
# num = 7
# for i in range(15,15+11):
#     if limit==4:
#         if cnt == 4:
#             limit=3
#             cnt=0
#             num+=1
#     elif limit == 3:
#         if cnt == 3:
#             limit =4
#             cnt=0
#             num+=1
#     a_dict[a[i]]=num
#     cnt+=1
        
# p,w = map(int,input().split())

# import string
# n = list(input())
# a = list(string.ascii_lowercase)
# b = list(string.ascii_uppercase)
# for i in n:
#     if i in a:
#         print(i.upper(),end="")
#     else:
#         print(i.lower(),end="")

# import string
# n = list(input())
# a = list(string.ascii_lowercase)
# b = list(string.ascii_uppercase)
# c = a+b
# a_dict = {}
# for i in range(1,len(c)+1):
#     a_dict[c[i-1]]=i
# c =0
# for i in n:
#     c+=a_dict[i]
# sosu = int(c)
# if sosu < 2 :
#     print("It is a prime word.")
# else:
#     sosu_dict = {}
#     for i in range(2,sosu+1):
#         if i not in sosu_dict:
#             for a in range(i,sosu+1,i):
#                 sosu_dict[a]=0
#             sosu_dict[i]=1
#     if sosu_dict[sosu] == 1:
#         print("It is a prime word.")
#     else:
#         print("It is not a prime word.")

# n = int(input())
# a = ""
# for i in range(1,n+1):
#     a+=str(i)
# print(a.index(str(n))+1)

repeat = int(input())
a_list = ""
for _ in range(repeat*2-1):
    a = input()
    a_list+=a
cnt = 0
while True:
    if "*" not in a_list or "/" not in a_list or "+" not in a_list or "-" not in a_list:
        print(a_list)
        break
    else:
        if "*" in a_list:
            a = a_list.index("*")
            wow=int(a_list[a-1])*int(a_list[a+1])
            cnt+=wow
            a_list=a_list.replace(a_list[a-1:a+2],str(wow))
            
        elif "/" in a_list:
            a = a_list.index("*")
            wow=int(a_list[a-1])/int(a_list[a+1])
            cnt+=wow
            a_list=a_list.replace(a_list[a-1:a+2],str(wow))    
        else:
            if "+" in a_list:
                a = a_list.index("+")
                wow=int(a_list[a-1])+int(a_list[a+1])
                cnt+=wow
                a_list=a_list.replace(a_list[a-1:a+2],str(wow))
            else:
                a = a_list.index("-")
                wow=int(a_list[a-1])-int(a_list[a+1])
                cnt+=wow
                a_list=a_list.replace(a_list[a-1:a+2],str(wow))
    
                         
    