# import sys
# import collections

# repeat = int(sys.stdin.readline().rstrip())
# a_list = []
# for _ in range(repeat):
#     number = int(sys.stdin.readline().rstrip())
#     a_list.append(number)
# a_list.sort()
# a_sum = round(sum(a_list)/repeat,1)
# wow = abs(a_sum-int(a_sum))
# if wow > 0.4:
#     if a_sum > 0:
#         print(int(a_sum)+1)
#     else:
#         print(int(a_sum)-1)
# else:
#     print(int(a_sum))
 
# center = len(a_list)//2
# print(a_list[center])

# cnt = collections.Counter()
# for i in a_list:
#     cnt[i]+=1
# wow = sorted(cnt.items(), key = lambda x : x[1],reverse=True)
# wow = [key for key,value in wow if value == wow[0][1]]
# wow.sort()
# if len(wow) > 1:
#     print(wow[1])
# else:
#     print(wow[0])


# if len(a_list)>1:
#     print(a_list[-1]-a_list[0])
# else:
#     print(0)
    

import sys
import string

lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)

while True:
    a = sys.stdin.readline().rstrip()
    string_list = ["[","(","[]","()"]
    if a == ".":
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
    x = d.split(" ")
    y = [i for i in x for a in string_list if a in i if i[0] in string_list or i[-1] in string_list]
    print(y)
    if len(d) == 0:
        print("yes")
    else:
        print("no")
# 반례 ((()))[][] , (())[][], [((()))]