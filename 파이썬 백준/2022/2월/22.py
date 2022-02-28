# g_dict = {"A+": 4.3, "A0": 4.0, "A-": 3.7,"B+": 3.3, "B0": 3.0, "B-": 2.7,"C+": 2.3, "C0": 2.0, "C-": 1.7,"D+": 1.3, "D0": 1.0, "D-": 0.7,"F":0.0}
# total = 0
# total_sum = 0
# r = int(input())
# for _ in range(r):
#     n,t,g=input().split()
#     t=int(t)
#     g=g_dict[g]
#     total+=t
#     total_sum+=t*g
# a = total_sum/total
# a_str = str(a).split(".")
# if len(a_str[1]) >= 3:
#     sosu = int(a_str[1][:3])
#     verify = int(str(sosu)[-1])
#     if verify >= 5:
#         sosu+=10-verify
#     a = float(str(int(a))+"."+str(sosu))
# print(f"{a:.2f}")
# r,l = map(int,input().split())
# wow = [str(i) for i in range(1,10)]
# a_list = {}
# for i in range(r):
#     a = list(input().replace("S","").replace("F","")[::-1])
#     if len(set(a))==1:
#         pass
#     else:
#         cnt = 1
#         for i in a:
#             if i == ".":
#                 cnt+=1
#             else:
#                 index = int(i)
#                 break
#         a_list[index]=cnt
# a = sorted(a_list.items(),key=lambda x : x[0])
# b = list(set(sorted(a_list.values())))
# for i in sorted(a_list.keys()):
#     print(b.index(a_list[i])+1)
# oh = ['a','e','i','o','u']
# a = list(input())
# while True:
#     for i in range(len(a)):
#         if len(a)==i:
#             break
        
#         if a[i] in oh:
#             a[i:i+3] = a[i]
#     print("".join(a),end="")
#     break

import sys
r,l,box = map(int,sys.stdin.readline().rstrip().split())
a_list = []
for _ in range(r):
    a = list(map(int,sys.stdin.readline().rstrip().split()))
    a_list.extend(a)
a_set = list(set(a_list))
a_set.sort()
mini = min(a_set)

maxi_index= -1
while True:  
    cnt_box = box
    maxi = a_set[maxi_index]
    cnt = 0
    for i in a_list:
        if i != maxi:
            # print("i",i,"maxi",maxi)
            if i < maxi:
                cnt+=(maxi-i)
                cnt_box-=maxi-i
            else:
                cnt+=(i-maxi)*2
                cnt_box+=i-maxi
    if cnt_box<0:
        maxi_index-=1
    else:
        break    
 
count = 0
count_box = box
for i in a_list:
    if i != mini:
        if i < mini:
            count+=abs(mini-i)
        else:
            count+=abs(mini-i)*2
# print(cnt,cnt_box,maxi)
# print(count,count_box,mini)
if cnt == count:
    print(cnt,maxi) 
elif cnt > count:
    print(count,mini)
else:
    print(cnt,maxi)