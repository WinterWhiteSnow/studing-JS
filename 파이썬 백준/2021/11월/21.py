import sys
from collections import deque
the_num = int(sys.stdin.readline().rstrip())
a = deque([])
for _ in range(the_num):
    weight,height = map(int,sys.stdin.readline().rstrip().split())
    a.append([weight,height])
    
for i in range(len(a)):
    count = 0
    c = a[i]
    for b in range(len(a)):
        b = a[b]
        if c[0] < b[0] and c[1] < b[1]:
            count+=1
    a[i].append(count)

for i in a:
    print(i[2]+1,end=" ")    