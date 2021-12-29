import sys

sosu_dict = {}

for a in range(2,10000+1):
    if a not in sosu_dict:
        for b in range(a, 10000+1, a):
            sosu_dict[b]=0
        sosu_dict[a]=1
sosu_list = [key for key,value in sosu_dict.items() if value == 1]

repeat = int(sys.stdin.readline().rstrip())
for _ in range(repeat):
    a = int(sys.stdin.readline().rstrip())
    if a//2 in sosu_list:
        print(a//2, a//2)
    else:
        b = a//2
        while b not in sosu_list or a-b not in sosu_list:
            b-=1
        print(b,a-b)
            