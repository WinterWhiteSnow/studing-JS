import sys
import string

lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)
wow = lower+upper

a_list = []
while True:
    a = sys.stdin.readline()[:-1]
    string_list = ["[","(","[]","()"]
    if len(a) == 1 and a == ".":
        break        
    b = list("".join(a).replace(" ",""))
    c = [i for i in b if i not in lower and i not in upper]
    d = "".join(c).replace(".","").replace(" ","")
    while True:
        if len(d) > 1:
            d = d.split("()")
            d = "".join(d)
            d = d.split("[]")
            d = "".join(d)
            if len(d)>1:
                if d[0] == "(":
                    if d[-1] == ")":
                        d =d[1:-1]
                    elif d[1] == ")":
                        d = d[2:]
                    else:
                        break
                elif d[0] == "[":
                    if d[-1] == "]":
                        d =d[1:-1]
                    elif d[1] == "]":
                        d = d[2:]
                    else:
                        break
                else:
                    break
        else:
            break
    x = a.split(" ")
    if x[0] == a:
        x = [i for i in a if i not in lower and i not in upper]
    y = ["pass" if i[0] in string_list or i[-1] in string_list else i for i in x for b in i if b in string_list]
    y = [i for i in y if i != "pass"]
    if len(y) >0:
        a_list.append("no")
    else:
        if len(d) == 0:
            a_list.append("yes")
        else:
            a_list.append("no")
for i in a_list:
    print(i)

# c = ["pass" if i[0] in string_list or i[-1] in string_list else i for i in a.split() for b in i if b in string_list]
# d = [i for i in c if i != "pass"]


# string_list = ["[","(","[]","()"]
# a = "안(녕하세요) 반갑습니다. [오늘도] 좋(은하)루되세요"
# for i in a.split():
#     for b in i:
#         if b in string_list:
#             if i[0] in string_list or i[-1] in string_list:
#                 pass
#             else:
#                 print(i)


            

