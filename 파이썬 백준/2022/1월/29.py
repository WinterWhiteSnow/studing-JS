# n = int(input())
# k = n*5
# for i in range(1,k+1):
#     if i <= n or n*2<i<=n*3 or 4*n<i<=k :
#         print("@"*k)
#     else:
#         print("@"*n)

# n = int(input())
# k = n*5
# for i in range(1,k+1):
#     if n<i<=2*n or 3*n<i<=4*n:
#         print("@"*k)
#     else:
#         print("@"*n,end="")
#         print(" "*(k-2*n),end="")
#         print("@"*n)

# n = int(input())
# k = int(input())
# n = n - (n%100)
# for _ in range(1,100):
#     if n%k == 0:
#         n = int(str(n)[-2:])
#         if n <10:
#             print(f"0{n}")
#         else:
#             print(f"{n}")
#         exit()
#     else:
#         n+=1
# import requests
# from bs4 import BeautifulSoup
# url = "https://www.acmicpc.net/problem/1076"
# r = requests.get(url)
# soup = BeautifulSoup(r.text,"html.parser")
# parent_tag = soup.find("div",{"id":"problem_description"}).find("table",{"class":"table"})
# tag = parent_tag.find("tbody").find_all("tr")
# dict_list = {}
# for i in tag:
#     list_list = i.find_all("td")
#     color = list_list[0].string
#     value = list_list[1].string
#     print(color,value)
#     dict_list[color]=value
# print(dict_list)

# wow = {'black': '0', 'brown': '1', 'red': '2', 'orange': '3', 'yellow': '4', 'green': '5', 'blue': '6', 'violet': '7', 'grey': '8', 'white': '9'}
# a_list = []
# for _ in range(3):
#     a = input()
#     a_list.append(a)
# print(int(wow[a_list[0]]+wow[a_list[1]])*(10**(int(wow[a_list[2]]))))
        
    
# cnt = 0    
# for a in range(8):
#     wow = list(input())
#     for i in range(8):
#         if a%2 == 0:
#             if i%2 ==0:
#                 if wow[i]=="F":
#                     cnt+=1
#         else:
#             if i%2==1:
#                 if wow[i]=="F":
#                     cnt+=1
# print(cnt)

# n = int(input())
# dict_list = {}
# for _ in range(n):
#     a = input().rstrip()[0]
#     if a not in dict_list:
#         dict_list[a]=1
#     else:
#         dict_list[a]+=1
# wow = [key for key,value in dict_list.items() if value >=5]
# wow.sort()
# if len(wow) > 0:
#     print("".join(wow))
# else:
#     print("PREDAJA")

# need_time,start,maxi,plus,minus = map(int,input().split())
# mini = start
# total_time = 0
# practice_time = 0
# if start+plus > maxi:
#     print("-1")
# else:
#     while practice_time != need_time:
#         if mini<= start <= maxi: # 운동하는것
#             if start+plus <=maxi:
#                 total_time+=1
#                 practice_time+=1
#                 start+=plus
#             else:
#                 total_time+=1
#                 start-=minus
#                 if start < mini:
#                     start=mini
#     print(total_time)
# import sys
# a,b = map(str,sys.stdin.readline().rstrip().split())
# a = list(map(int,list(a)))
# b = list(map(int,list(b)))
# print(sum(a)*sum(b)) 

# a,b,c = map(int,input().split())
# cnt = {}
# for i in range(1,a+1):
#     for x in range(1,b+1):
#         for y in range(1,c+1):
#             wow = i+x+y
#             if wow not in cnt:
#                 cnt[wow]=1
#             else:
#                 cnt[wow]+=1
# maxi = max(cnt.items(),key=lambda x : x[1])
# print(maxi[0])

# a,b= map(str,input().split())
# a = "0b"+a
# b = "0b"+b
# a = int(a,2)
# b = int(b,2)
# c = bin(a+b)
# print(c[2:])   

# wow = ['a', 'e', 'i', 'o', 'u']
# while True:
#     cnt = 0
#     a = input()
#     if a == "#":
#         break
#     a=a.lower()
#     for i in wow:
#         cnt+=a.count(i)
#     print(cnt)

# wow = "0b"+input()
# wow = int(wow,2)
# a = oct(wow)
# print(a[2:])

import string
al = list(string.ascii_lowercase)
wow_dict = {}
for _ in range(50):
    a = input()
    if len(a) > 0:
        for i in al:
            if i not in wow_dict:
                wow_dict[i]=1
            else:
                wow_dict[i]+=1
list_max = max(list(wow_dict.values))
wow = [key for key,value in wow_dict.items() if value == list_max]
print(*wow)
             


    
       
    

    
    
            
    