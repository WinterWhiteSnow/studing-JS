import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())
# import math
# r = one()
# num = "none"
# symbol = ""
# string_string = ""
# for i in range(r*2-1):
#     if not i%2:
#         if num == "none":
#             num = one()
#         else:
#             if symbol == "*":
#                 num*=one()
#             else:
#                 b = one()
#                 if num/b == int(num/b):
#                     num//=b
#                 else:
#                     num/=b
#                     num=math.floor(num)    
#     else:
#         symbol=inputing()
#         if symbol == "+" :
#             string_string+=str(num)+"+"
#             num = "none"
#         elif symbol == "-":
#             string_string+=str(num)+"-"
#             num = "none"
#     # print(num,symbol,string_string)
# if num != "none":
#     string_string+=str(num)
# print(eval(string_string))
a = f"{1/(2**one()):.300f}"
index = 0
for i in list(a)[::-1]:
    if i == "0":
        index+=1
    else:
        print(a[index:])
        break











