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

