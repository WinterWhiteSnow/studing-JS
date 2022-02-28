# enter = lambda : input().split() 
# for _ in range(int(input())):
#     n,l = map(int,enter())
#     x = int("".join(enter()))
#     y = int("".join(enter()))
#     a_list = enter()
#     long_list = a_list+a_list
#     cnt = 0
#     for i in range(len(a_list)):
#         num = int("".join(long_list[i:i+l]))
#         if x<=num<=y:
#             cnt+=1
#     print(cnt)
# import sys
# for _ in range(int(sys.stdin.readline().rstrip())):
#     a,b,s = map(int,sys.stdin.readline().rstrip().split())
#     if a >= b:
#         maxi = a
#         mini = b
#     else:
#         maxi = b
#         mini = a
#     maxi_index = s//maxi
#     mini_index = (s - (maxi*maxi_index))//mini
#     if mini > s :
#         print("Impossible")
#     else:
#         while maxi*maxi_index+mini*mini_index != s:
#             maxi_index-=1
#             mini_index=(s - (maxi*maxi_index))//mini
#             if maxi_index < 0 or mini_index < 0:
#                 break
#             # print(maxi_index,mini_index)
#         if maxi_index < 0 or mini_index < 0:
#             print("Impossible")
#         else:
#             if a >= b:
#                 print(maxi_index,mini_index)
#             else:
#                 print(mini_index,maxi_index)
# a,b = map(int,input().split())
# a_list = []
# cnt = 1
# while len(a_list) < b:
#     a_list.extend([cnt for _ in range(cnt)])
#     cnt+=1
# print(sum(a_list[a-1:b]))  

# for _ in range(int(input())):
#     a = str(int(input()))
#     print(int(a,2))
# r = lambda : int(input())
# for _ in range(r()):
#     a_dict = {}
#     for _ in range(r()):
#         name,num = input().split()
#         num = int(num)
#         a_dict[num]=name
#     key=max(a_dict.keys())
#     print(a_dict[key])
# import string
# a_list = list(string.ascii_lowercase)
# A_list = list(string.ascii_uppercase)
# a = list(input())
# for i in a:
#     if i in a_list:
#         index = (a_list.index(i)+13)%len(a_list)
#         print(a_list[index],end="")
#     elif i in A_list:
#         index = (A_list.index(i)+13)%len(A_list)
#         print(A_list[index],end="")
#     else:
#         print(i,end="")
# import sys
# l = int(sys.stdin.readline().rstrip())
# a = list(map(int,sys.stdin.readline().rstrip().split()))
# for i in range(l):
#     num = a[i]
#     if num ==(int(num**(1/2))**2):
#         print(1,end=" ")
#     else:
#         print(0,end=" ")
# n,l,h = map(int,input().split())
# a_list = list(map(int,input().split()))
# a_list.sort()
# if l>0:
#     a_list = a_list[l:]
# # print(a_list)
# if h>0:
#     a_list = a_list[:-h]
# print(sum(a_list)/len(a_list))
# a_dict ={}
# for _ in range(5):
#     a = list(input())
#     for i in range(len(a)):
#         if i not in a_dict:
#             a_dict[i]=[a[i]]
#         else:
#             a_dict[i].append(a[i])
# a_str = []
# b_dict = {}
# for i in range(len(a_dict)):
#     if a_dict[i] == ['.', 'o', 'm', 'l', 'n']:
#         wow = ['o', 'w', 'l', 'n', '.']          
#     elif a_dict[i] == ['o', 'w', 'l', 'n', '.']: 
#         wow = ['.', 'o', 'm', 'l', 'n']           
#     else:
#         wow = ['.', '.', 'o', 'L', 'n']
#     for i in range(len(wow)):
#         if i not in b_dict:
#             b_dict[i]=wow[i]
#         else:
#             b_dict[i]+=wow[i]
# for i in range(len(b_dict)):
#     print(b_dict[i])
a_dict = {}
for _ in range(int(input())):
    so,dae = input().split()
    a_dict[dae]=so
wow = list(input())
a = ""
start,end= map(int,input().split())
for i in wow:
    a+=a_dict[i]
print(a[start-1:end])
    

                        
            