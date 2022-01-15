# repeat = int(input())
# start = 1
# for _ in range(repeat):
#     a,b = map(int,input().split())
#     if a == start or b == start:
#         if a == start:
#             start = b
#         else:
#             start = a
# print(start)
import sys
sosu,k = map(int,sys.stdin.readline().rstrip().split())
wow = k+1
sosu_dict = {}
for i in range(2,wow):
    if i not in sosu_dict:
        for a in range(i,wow,i):
            sosu_dict[a] = 0
        sosu_dict[i]=1
sosu_list = [i[0] for i in sosu_dict.items() if i[1] == 1]
count = 0
while True:
    if sosu/sosu_list[count] in sosu_list:
        print("BAD",sosu_list[count])
        break
    elif count == len(sosu_list)-1:
        print("GOOD")
        break
    else:
        count+=1