# while True:
#     total_page = int(input())
#     if total_page == 0:
#         break
#     pages = input().split(",")
#     page_list = []
#     for i in pages:
#         page = i.split("-")
#         if len(page) ==2:
#             start = int(page[0])
#             end = int(page[1])
#             if start>end:
#                 pass
#             elif start>total_page:
#                 pass
#             else:
#                 if end > total_page:
#                     end=total_page
#                 o =[i for i in range(start,end+1)]
#                 page_list.extend(o)
#         else:
#             start = int(page[0])
#             if start>total_page:
#                 pass
#             else:
#                 page_list.append(start)
#     page_list = set(page_list)
#     print(len(page_list))

# list_list = ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"]
# while True:
#     music_list = input().split()
#     if music_list[0] == "***":
#         break
#     for i in range(len(music_list)):
#         if music_list[i] in list_list:
#             music_list[i]=list_list.index(music_list[i])
#         elif "b" in music_list[i]:
#             music_list[i]=list_list.index(music_list[i][0])-1
#         elif "#" in music_list[i]:
#             music_list[i]=list_list.index(music_list[i][0])+1            
#     change = int(input())
#     if change > 0:
#         music_list = [list_list[(i+change)%len(list_list)] for i in music_list]
#     else:
#         music_list = [list_list[i+change] for i in music_list]
#     print(*music_list)      

# r=int(input())
# for _ in range(r):
#     a = list(input())
#     l = int(len(a)**(1/2))
#     a_dict = {}
#     for i in range(0,len(a),l):
#         wow = a[i:i+l][::-1]
#         for i in range(len(wow)):
#             if i not in a_dict:
#                 a_dict[i]=[wow[i]]
#             else:
#                 a_dict[i].append(wow[i])
#     wow = []
#     for i in a_dict.values():
#         wow.extend(i)
#     print("".join(wow))

# r = int(input())
# a_dict = {}
# for i in range(r):
#     a = list(map(int,input().split()))
#     for index in range(len(a)):
#         if index not in a_dict:
#             a_dict[index]=[a[index]]
#         else:
#             a_dict[index].append(a[index])
# b_dict = {}
# for i in range(len(a_dict)):
#     a_list = a_dict[i]
#     for index in range(len(a_list)):
#         if a_list.count(a_list[index])>1:
#             cnt = 0
#         else:
#             cnt = a_list[index]
#         if index not in b_dict:
#             b_dict[index]=cnt
#         else:
#             b_dict[index]+=cnt
# for i in range(len(b_dict)):
#     print(b_dict[i])

# r = int(input())
# cnt = 1
# for _ in range(r):
#     str_r = int(input())
#     str_list = []
#     for _ in range(str_r):
#         a = input()
#         str_list.append(a)
#     participant = int(input())
#     string_list = []
#     for _ in range(participant):
#         string = ""
#         wow = list(map(int,input().split()))
#         l = wow[0]
#         index_list = wow[1:]
#         for ind in range(l):
#             string+=str_list[index_list[ind]]
#         string_list.append(string)   
#     print(f"Scenario #{cnt}:")
#     for i in string_list:
#         print(i)
#     if cnt != r:
#         print()
#     cnt+=1     



# import sys
# import string
# l = int(sys.stdin.readline().rstrip())
# a = sys.stdin.readline().rstrip()+"a"
# index = "none"
# cnt = 0
# count = 0
# num = list(string.ascii_letters)
# for i in range(len(a)):
#     if a[i] not in num:
#         if index == "none":
#             index=i
#         cnt+=1
#     else:
#         if index != "none":
#             x = "".join(a[index:index+cnt])
#             count+=int(x)
#         index="none"
#         cnt=0
# print(count)

# def div(wow,num):
#     start = wow
#     start_list = ""
#     while True:
#         if start == 0:
#             break
#         a = str(start%num)
#         start_list+=a
#         start = start//num
#     return start_list
# n = int(input())
# pal = "no"
# for i in range(2,10):
#     a = div(n,i)
#     if a == a[::-1]:
#         print(i,a)
#         pal = "yes"
# if str(n) == str(n)[::-1]:
#     print(10,n)
#     pal="yes"
# if pal == "no":
#     print("NIE")

# r = int(input())
# for _ in range(r):
#     a = input().replace(" ","")
#     set_a = set(a)
#     a_dict = {}
#     for i in set_a:
#         a_dict[i]=a.count(i)
#     a_list = [key for key,value in a_dict.items() if value == max(a_dict.values())]
#     if len(a_list) == 1:
#         print(*a_list)
#     else:
#         print("?")

# while True:
#     start = input()
#     if start == "#":
#         break
#     else:
#         start=list(start)
#         isladder = "true"
#         while True:
#             count = 0
#             going = input()
#             if going == "#":
#                 break
#             going=list(going)
#             if len(going) != len(start):
#                 isladder="false"
#             else:
#                 for i in range(len(going)):
#                     if start[i]==going[i]:
#                         count+=1
#                 if count !=3:
#                     isladder="false"
#             start=going
#         if isladder == "true":
#             print("Correct")
#         else:
#             print("Incorrect")


        
