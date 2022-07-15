import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# def zero_no(string):
#     string = list(string)
#     string.sort()
#     index = 1
#     while string[0] == "0":
#         string[0],string[index]=string[index],string[0]
#         index+=1
#     return "".join(string)

# while True:
#     a = list(wow())
#     if a[0] == 0:
#         break
#     l = a[0]
#     list_list = a[1:]
#     x = ""
#     y = ""
#     list_list.sort()
#     zero_list = []
#     state = 0
#     for i in range(l):
#         if list_list[i] == 0:
#             zero_list.append(list_list[i])
#         else:
#             if state == 0:
#                 x+=str(list_list[i])
#                 state = 1
#             else:
#                 y+=str(list_list[i])
#                 state = 0
#     # print(x,y,zero_list)
#     for i in range(len(zero_list)):
#         if len(x) <= len(y):
#             x+=str(zero_list[i])
#         else:
#             y+=str(zero_list[i])
#     # print("바뀌기전",x,y)
#     x = zero_no(x)
#     y = zero_no(y)
#     # print("바꾼후",x,y)
#     print(int(x)+int(y))


    






































