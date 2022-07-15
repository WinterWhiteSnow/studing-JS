from audioop import reverse
import sys
inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# num = one()
# n_list = [0]*(41)
# n_list[0]=[1,0]
# n_list[1]=[0,1]
# for _ in range(num):
#     number= one()
#     if n_list[number] == 0:
#         for i in range(2,number+1):
#             n_list[i]=[n_list[i-1][0]+n_list[i-2][0],n_list[i-1][1]+n_list[i-2][1]]
#         print(*n_list[number])
#     else:
#         print(*n_list[number])

r,l,total = wow()
n_list = []
for _ in range(r):
    n_list.extend(list(wow()))
max_height = max(n_list)
min_height = min(n_list)
while True:
    if max_height*r*l-sum(n_list)<=total:
        break
    else:
        max_height-=1
zero_list = [0]*(max_height+1)
for height in range(min_height,max_height+1):
    cnt = 0
    for i in n_list:
        if i > height:
            cnt+=(i-height)*2
        else:
            cnt+=height-i
    zero_list[height]=(cnt,height)
zero_list=zero_list[min_height:]
zero_list.sort(key=lambda x: x[1],reverse=True)
zero_list.sort(key=lambda x: x[0])
print(*zero_list[0])

        
    








