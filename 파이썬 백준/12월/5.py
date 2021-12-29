import sys
from collections import deque
num = int(sys.stdin.readline().rstrip())
a = deque()
for _ in range(num):
    s = int(sys.stdin.readline().rstrip())
    a.append(s)
print(round(sum(a)/len(a)))
a_dict = {}
for i in a:
    if i not in a_dict:
        a_dict[i]=a.count(i)
a_dict = sorted(a_dict.items(), key = lambda x : x[0])
wow = sorted(a_dict, key = lambda x : x[1],reverse=True)
print(wow[num//2][0])

if len(wow) > 1:
    if wow[0][1] == wow[1][1]:
        print(wow[1][0])
    else:
        # print("여긴 첫번째와 두번째가 같지않음")
        print(wow[0][0])
else:
    # print("wow의 길이가 1이하임")
    print(wow[0][0])

print(wow[-1][0]-wow[0][0])
    
    
    