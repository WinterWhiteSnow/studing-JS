import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# l = one()
# n_list = list(wow())
# n_dict = {}
# index = 0
# set_list = sorted(list(set(n_list)))
# for i in set_list:
#     if i not in n_dict:
#         n_dict[i]=index
#     index+=1
# for i in n_list:
#     print(n_dict[i],end=" ")

# l,r = wow()
# n_list = list(wow())
# zero_list = [0]*l
# zero_list[0]=n_list[0]
# for i in range(1,l):
#     zero_list[i]=zero_list[i-1]+n_list[i]
# for _ in range(r):
#     a,b = wow()
#     a=a-2
#     b-=1
#     # print(a,b)
#     now = zero_list[b]
#     if a>=0:
#         now-=zero_list[a]
#     print(now)

# r,k = wow()
# n_dict = {}
# for i in range(1,r+1):
#     zero_list = [0]*r
#     n_list = list(wow())
#     zero_list[0]=n_list[0]
#     for index in range(1,r):
#         zero_list[index]=zero_list[index-1]+n_list[index]
#     n_dict[i]=zero_list
# # print(n_dict)
# for _ in range(k):
#     a,b,c,d = wow()
#     cnt=0
#     d-=1
#     b-=2
#     # print(a,b,c,d)
#     for i in range(a,c+1):
#         if b >= 0:
#             cnt+=n_dict[i][d]-n_dict[i][b]
#         else:
#             cnt+=n_dict[i][d]
#     print(cnt)

n_list = [0]*21
for _ in range(one()):
    answer = inputing()
    if answer == "all":
        order = "all"
    elif answer == "empty":
        order = "empty"
    else:
        order,num = answer.split()
        num = int(num)
    if order == "add":
        if type(n_list) == list:
            n_list[num]=1
        else:
            n_list.append(num)
    elif order == "check":
        if type(n_list) == list:
            print(n_list[num])
        else:
            if num in n_list:
                print(1)
            else:
                print(0)
    elif order == "remove":
        if type(n_list) == list:
            if n_list[num]== 1:
                n_list[num] = 0
        else:
            if num in n_list:
                n_list.remove(num)
    elif order == "toggle":
        if type(n_list) == list:
            if n_list[num]== 1:
                n_list[num]=0
            else:
                n_list[num]=1
        else:
            if num in n_list:
                n_list.remove(num)
            else:
                n_list.append(num)            
    elif order =="all":
        n_list = {i for i in range(1,21)}
    elif order == "empty":
        n_list = [0]*(21)
    # print(n_list,type(n_list))































