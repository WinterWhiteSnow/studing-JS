import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# l = one()
# n_list = list(wow())
# sort_list = sorted(n_list)
# # print(sort_list)
# for i in range(l):
#     index =sort_list.index(n_list[i])
#     n_list[i]=index
#     sort_list[index]="X"
#     # print(n_list,sort_list)
# print(*n_list)
# l,k = wow()
# n_list = list(wow())
# n_list.sort()
# print(n_list[k-1])
# r = one()
# num_list = [str(i) for i in range(10)]
# n_dict = {}
# for _ in range(r):
#     a = inputing()
#     cnt = 0
#     for i in list(a):
#         if i in num_list:
#             cnt+=int(i)
#     n_dict[a]=cnt
# list_list = sorted(n_dict.items(),key=lambda x : (len(x[0]),x[1],x[0]))
# for i in list_list:
#     print(i[0])
# r = one()
# n_list =  [one() for _ in range(r)]
# n_list.sort(reverse=True)
# for i in n_list:
#     print(i)

# r = one()
# n_list = []
# for _ in range(r):
#     name,d,m,y = inputing().split()
#     d,m,y = int(d),int(m),int(y)
#     n_list.append([name,d,m,y])
# n_list.sort(key=lambda x : (x[3],x[2],x[1]),reverse=True)
# print(n_list[0][0]+"\n"+n_list[-1][0])

# l = one()
# n_list = list(wow())
# n_list.sort()
# print(*n_list)

# l,k = wow()
# n_list = list(wow())
# first_appear={}
# index = 0
# for i in n_list:
#     if i not in first_appear:
#         first_appear[i]=[n_list.count(i),index]
#         index+=1
# list_list = list(first_appear.items())
# list_list.sort(key=lambda x: (x[1][1]))
# list_list.sort(key=lambda x: (x[1][0]),reverse=True)
# for i in list_list:
#     for _ in range(i[1][0]):
#         print(str(i[0]),end=" ")

# n,m = wow()
# a_list = list(wow())
# b_list = list(wow())
# c_list = list(set(a_list)-set(b_list))
# if len(c_list) == 0:
#     print(0)
# else:
#     print(len(c_list))
#     print(*sorted(c_list))

r = one()
one_list = []
two_list = []
for _ in range(r):
    location,color = wow()
    if color == 1:
        one_list.append(location)
    else:
        two_list.append(location)
one_list.sort()
two_list.sort()
def lines(list_list):
    cnt = 0
    for i in range(len(list_list)):
        if i == 0:
            cnt+=list_list[1]-list_list[0]
        elif i == len(list_list)-1:
            cnt+=list_list[-1]-list_list[-2]
        else:
            cnt+=min(abs(list_list[i]-list_list[i-1]),abs(list_list[i]-list_list[i+1]))
    return cnt
print(lines(one_list)+lines(two_list))













