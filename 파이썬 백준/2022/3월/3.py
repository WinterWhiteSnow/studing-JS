# cnt = 0
# while True:
#     a = input()
#     if a == "고무오리 디버깅 끝":
#         break
#     if a == "고무오리":
#         if cnt == 0:
#             cnt+=2
#         else:
#             cnt-=1
#     elif a == "문제":
#         cnt+=1
# if cnt == 0:
#     print("고무오리야 사랑해")
# else:
#     print("힝구")
# a = ""
# b = {}
# for _ in range(int(input())):
#     answer = input()
#     a+=answer
#     for i in range(len(list(answer))):
#         if i not in b:
#             b[i]=[answer[i]]
#         else:
#             b[i].append(answer[i])
# c = ""
# for i in b.values():
#     c+="".join(i)          
# if a == c :
#     print("YES")
# else:
#     print("NO") 
# time = int(input())
# a_list = ["up","right","down","left"]
# index = 0
# cnt_cnt = 1
# x =0
# y = 0
# cnt = 0
# while cnt < time:
#     for _ in range(2):
#         for _ in range(cnt_cnt):
#             index = index%4
#             order = a_list[index]
#             if order == "up":
#                 y+=1
#             elif order == "right":
#                 x+=1
#             elif order == "down":
#                 y-=1
#             else:
#                 x-=1
#             cnt+=1
#             if cnt == time:
#                 print(x,y)
#                 exit()
#         index+=1
#     cnt_cnt+=1
# r,y,x = map(int,input().split())
# if y%2 ==0:
#     if x%2 == 0:
#         zero = "first"
#     else:
#         zero = "second"
# else:
#     if x%2 == 0:
#         zero = "second"
#     else:
#         zero = "first"
# for i in range(r):
#     for index in range(r):
#         if zero == "first":
#             if i%2 == 0:
#                 # print(i,index)
#                 if index != r-1:
#                     if index%2 == 0:
#                         print("v",end="")
#                     else:
#                         print(".",end="")
#                 else:
#                     if index%2 == 0:
#                         print("v")
#                     else:
#                         print(".")
#             else:
#                 if index != r-1:
#                     if index%2 == 0:
#                         print(".",end="")
#                     else:
#                         print("v",end="")
#                 else:
#                     if index%2 == 0:
#                         print(".")
#                     else:
#                         print("v")
#         else:
#             if i%2 == 0:
#                 # print(i,index)
#                 if index != r-1:
#                     if index%2 == 0:
#                         print(".",end="")
#                     else:
#                         print("v",end="")
#                 else:
#                     if index%2 == 0:
#                         print(".")
#                     else:
#                         print("v")
#             else:
#                 if index != r-1:
#                     if index%2 == 0:
#                         print("v",end="")
#                     else:
#                         print(".",end="")
#                 else:
#                     if index%2 == 0:
#                         print("v")
#                     else:
#                         print(".")



    
    
            
    
    
        
        
    
            
    