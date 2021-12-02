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