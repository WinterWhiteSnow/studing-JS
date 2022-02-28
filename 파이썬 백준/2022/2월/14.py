# while True:
#     a = input()
#     if a == "END":
#         break
#     print(a[::-1])
# a_dict={}
# point = 0
# s = 0
# while True:
#     a = input().split()
#     if a[0] == "-1":
#         break
#     time = a[0]
#     q = a[1]
#     a = a[2]
#     if q not in a_dict:
#         a_dict[q]=[time]
#     else:
#         a_dict[q].append(time)
        
#     if a == "right":
#         s+=1
#         point+=20*(len(a_dict[q])-1)
#         point+=int(time)
# print(s,point)

# a = input()
# count = 0
# while len(a) !=1:
#     a = list(map(int,list(a)))
#     cnt = 1
#     for i in a:
#         cnt*=i
#     count+=1
#     if len(str(cnt)) !=1:
#         a = str(cnt)
#     else:
#         break
# print(count)

# wow=list(map(int,input().split()))
# wow.sort()
# start = wow[0]
# end = wow[1]
# for i in range(start+1,end+2):
#     print(i) 

# a = input()
# if a[:2] == "0x":
#     print(int(a,16))
# elif a[0] == "0":
#     print(int(a,8))
# else:
#     print(a)

# r,l = map(int,input().split())
# for _ in range(r):
#     a = input()
#     if len(a) == l:
#         print(a[::-1])     

# a = {}
# b = {}
# start = int(input())
# num = start
# win = 0
# for _ in range(9):
#     line,room = map(int,input().split())
#     if win == 0:
#         if num == 1:
#             if line not in a:
#                 a[line]=[room]
#             else:
#                 a[line].append(room)
#             if str(room) not in a:
#                 a[str(room)]=[line]
#             else:
#                 a[str(room)].append(line)
#             if line==room:
#                 if "diagonal" not in a:
#                     a["diagonal"]=1
#                 else:
#                     a["diagonal"]+=1
#                 if a["diagonal"] == 3:
#                     win = 1
#                     break
#                 if line == 2:
#                     if "incre_diagonal" not in a:
#                         a["incre_diagonal"]=1
#                     else:
#                         a["incre_diagonal"]+=1
#                     if a["incre_diagonal"]==3:
#                         win=1
#                         break
#             if abs(room-line)==2:
#                 if "incre_diagonal" not in a:
#                     a["incre_diagonal"]=1
#                 else:
#                     a["incre_diagonal"]+=1
#                 if a["incre_diagonal"] == 3:
#                     win = 1
#                     break
#             if len(a[line]) == 3 or len(a[str(room)])==3:
#                 win=1
#                 break
#             num = 2
#         else:
#             if line not in b:
#                 b[line]=[room]
#             else:
#                 b[line].append(room)
#             if str(room) not in b:
#                 b[str(room)]=[line]
#             else:
#                 b[str(room)].append(line)
#             if line==room:
#                 if "diagonal" not in b:
#                     b["diagonal"]=1
#                 else:
#                     b["diagonal"]+=1
#                 if b["diagonal"] == 3:
#                     win = 2
#                     # print("여기는 대각선 안")
#                     break
#                 if line == 2:
#                     if "incre_diagonal" not in b:
#                         b["incre_diagonal"]=1
#                     else:
#                         b["incre_diagonal"]+=1
#                     if b["incre_diagonal"]==3:
#                         # print("여기는 증가하는대각선")
#                         win=2
#                         break
#             if abs(room-line)==2:
#                 if "incre_diagonal" not in b:
#                     b["incre_diagonal"]=1
#                 else:
#                     b["incre_diagonal"]+=1
#                 if b["incre_diagonal"] == 3:
#                     # print("여기는 abs안")
#                     win = 2
#                     break
#             if len(b[line]) == 3 or len(b[str(room)])==3:
#                 # print("여기는 len안")
#                 win=2
#                 break
#             num = 1
#     else:
#         pass
#     # print("이후 player:",num)
#     # print("a:",a)
#     # print("b:",b)
# print(win)

# a = input()
# b = input()
# print(a.count(b))

# a = list(input())
# b = list(input())
# first = ""
# second = ""
# third = ""
# fourth = ""
# fifth = ""
# for i in range(len(a)):
#     if a[i] == b[i]:
#         first+=a[i]
#         third+="0"
#     else:
#         first+="0"
#         third+="1"        
#     if a[i] == "1" or b[i] =="1":
#         second+="1"
#     else:
#         second+="0"
#     if a[i] == "1":
#         fourth+="0"
#     else:
#         fourth+="1"
#     if b[i] == "1":
#         fifth+="0"
#     else:
#         fifth+="1"
# for i in [first,second,third,fourth,fifth]:
#     print(i)
# r = int(input())
# for _ in range(r):
#     wow = input().split()
#     wow[0]="god"
#     print("".join(wow))

# a = input()
# if a == a[::-1]:
#     print("true")
# else:
#     print("false")

# a,b = map(int,input().split())
# wow = []
# for i in range(1,b+1):
#     c = int(str(a*i)[::-1])
#     wow.append(c)
# print(max(wow))

# r = int(input())
# for _ in range(r):
#     a = input().replace(" ","")
#     b=a[:a.index("=")]
#     answer = int(a[a.index("=")+1:])
#     if eval(b) == answer:
#         print("correct")
#     else:
#         print("wrong answer")   
    