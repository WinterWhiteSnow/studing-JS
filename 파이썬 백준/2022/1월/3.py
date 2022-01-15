# import sys
# import string

# lower = list(string.ascii_lowercase)
# upper = list(string.ascii_uppercase)
# wow = lower+upper


# while True:
#     a = sys.stdin.readline()[:-1]
#     string_list = ["[","(","[]","()"]
#     if len(a) == 1 and a == ".":
#         break        
#     b = list("".join(a).replace(" ",""))
#     c = [i for i in b if i not in lower and i not in upper]
#     d = "".join(c).replace(".","").replace(" ","")
#     count = 0
#     why = True
#     a_list = []
#     if len(d) > 0 :
#         while True:
#             if "()" in d or "[]" in d:
#                 d = d.split("()")
#                 d = "".join(d)
#                 d = d.split("[]")
#                 d = "".join(d)
#             else:
#                 break
    
#         while len(d) != 0:  
#             if len(d) == count :
#                 break
            
#             if d[count] == "(":
#                 a_list.append("(")
#                 count+=1
#             elif d[count] == "[":
#                 a_list.append("[")
#                 count+=1
#             else:
#                 if d[count] == ")":
#                     if len(a_list) > 0:
#                         if a_list[-1] == "(":
#                             a_list.pop()
#                             count+=1
#                         else:
#                             why = False
#                             count+=1
#                     else:
#                         why = False
#                         count+=1
                    
#                 elif d[count] == "]":
#                     if len(a_list) > 0:
#                         if a_list[-1] == "[":
#                             a_list.pop()
#                             count+=1
#                         else:
#                             why = False
#                             count+=1
#                     else:
#                         why = False
#                         count+=1  
#     if why == False or len(a_list) >0:
#         print("no")
#     else:
#         print("yes")          

import sys

repeat = int(sys.stdin.readline().rstrip())

for _ in range(repeat):
    leng,order = map(int, sys.stdin.readline().rstrip().split())
    n_list = list(map(int, sys.stdin.readline().rstrip().split()))
    num_goal = n_list[order]
    dict_list = []
    count = 0
    for i in range(len(n_list)):
        wow = {
            "order":i,
            "number":n_list[i]
        }
        dict_list.append(wow)

    while 1:
        max_num = max(n_list)
        if dict_list[0]["number"] != order:
            while dict_list[0]["number"] != max_num:
                dict_list.append(dict_list[0])
                n_list.append(n_list[0])
                del dict_list[0]
                del n_list[0]
            if dict_list[0]["number"] == max_num:
                count+=1
                del dict_list[0]
                del n_list[0]
        else:
            break
    print(count,n_list,dict_list,count)
    
