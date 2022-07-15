# r = lambda : map(int,input().split())
# l,weight = r()
# cnt = 0
# now = 0
# if l > 0:
#     weight_list = list(r())
#     for i in range(l):
#         if now <= weight:
#             now+=weight_list[i]
#             if now > weight:
#                 now = weight_list[i]
#                 cnt+=1
#             elif now == weight:
#                 now= 0
#                 cnt+=1
#         # print(now,cnt) 
# if now >0:
#     cnt+=1   
# print(cnt)    

# l = int(input())
# n_list = list(map(int,input().split()))
# wow_list = []
# for i in range(1,l-1):
#     wow = n_list[i-1:i+2]
#     if min(wow) != 0:
#         # print(wow,n_list[i])
#         wow_list.append(n_list[i]+min(wow[0],wow[-1]))
# # print(wow_list)
# if wow_list:
#     print(max(max(wow_list),max(n_list)))    
# else:
#     print(max(n_list))
import math
while True:
    a = input().split()
    if len(a) == 1 and a[0] == "0":
        exit()
    l = int(a[0])
    a_list = a[1:]
    a_list.sort()
    if l == 2:
        print(sum(list(map(int, a))))
    else:
        x = []
        y = []
        zero = a_list.count("0")
        if zero > 1:
            for i in range(zero):
                if i%2 == 0:
                    x.append("0")
                else:
                    y.append("0")
            a_list = a_list[zero:]
        if l%2 == 0:
            for i in range(l-zero):
                if i == 0 or i == 1:
                    x.append(a_list[i])
                elif i == 2 or i==3:
                    y.append(a_list[i])
                else:
                    if i%2 == 0:
                        x.append(a_list[i])
                    else:
                        y.append(a_list[i])
        else:
            for i in range(l-zero):
                if i == 0 or i == 1:
                    x.append(a_list[i])
                elif i == 2:
                    y.append(a_list[i])
                else:
                    if i%2 == 1:
                        x.append(a_list[i])
                    else:
                        y.append(a_list[i])
        if len(x) != math.ceil(l/2):
            y.append(x.pop())
        x.sort()
        y.sort()
        x = "".join(x)
        y = "".join(y)
        if "0" in x:
            zero = x.count("0")
            x = x[zero]+x[:zero]+x[zero+1:]
        if "0" in y:
            zero = y.count("0")
            y = y[zero]+y[:zero]+y[zero+1:]
        print(x,y)
                         
            
    