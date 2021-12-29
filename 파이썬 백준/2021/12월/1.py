# import sys
# from collections import deque

# num = int(sys.stdin.readline().rstrip())
# a = deque()
# for _ in range(num):
#     wow = int(sys.stdin.readline().rstrip())
#     if wow == 0:
#         if len(a) > 0:
#             a.pop()
#     else:
#         a.append(wow)
# print(sum(a))

# import sys
# from collections import deque
# a =sys.stdin.readline().rstrip().split("()")

# while len(a)>1:
#     a = "".join(a).split("()") 

# print(len(a[0]))

import sys
from collections import deque

a = sys.stdin.readline().rstrip().split(" ")
list_list = ["(",")","[","]"]
a_list = deque()
for i in a:
    print(i)
    if i[0] in list_list or i[-2:-1] in list_list:
        a_list.append(i)

print(a_list)

    