# import sys
# a_list = []
# for i in range(int(sys.stdin.readline().rstrip())):
#     a_list.append(int(sys.stdin.readline().rstrip()))
# a_list.sort(reverse=True)
# total = sum(a_list)
# wow = len(a_list)//3
# for i in range(0,wow*3,3):
#     total-=a_list[i+2]
# print(total)

# a_list = []
# for i in range(int(input())):
#     a_list.append(int(input()))
# a_list.sort(reverse=True)
# index = 1
# total = 0
# for i in range(len(a_list)):
#     wow = a_list[i]-(index-1)
#     if wow < 0:
#         pass
#     else:
#         total+=wow
#         index+=1
# print(total)

# l,start=map(int,input().split())
# a_list=list(map(int,input().split()))
# a_list.sort()
# for i in range(len(a_list)):
#     q = a_list[i]
#     if q <= start:
#         start+=1
# print(start)

# total,r = map(int,input().split())
# wow = [i for i in range(1,r+1)]
# if sum(wow)<=total:
#     if (sum(wow)-total)%r == 0:
#         print(r-1)
#     else:
#         print(r)
# else:
#     print(-1)
# a_list = []
# for i in range(int(input())):
#     a_list.append(int(input()))
# if len(a_list) == 1:
#     print(0)
# else:
#     num = a_list[0]
#     a_list = a_list[1:]
#     cnt = 0
#     while max(a_list)>=num:
#         a_list.sort()
#         a_list[-1]-=1
#         a_list.sort()
#         num+=1
#         cnt+=1
#         # print(a_list)
#     print(cnt)
# a_list = []
# for i in range(int(input())):
#     o = list(map(int,input().split()))
#     a_list.append(o)
# a_list.sort(key= lambda x: x[0])
# wait = 0
# for wow in a_list:
#     if wow[0] >= wait:
#         wait = sum(wow)
#     else:
#         wait = wait+wow[1]
# print(wait)

# egg,consumer = map(int,input().split())
# a_list = []
# for _ in range(consumer):
#     a_list.append(int(input()))
# a_list.sort()
# b_list = []
# for i in range(len(a_list)):
#     wow = a_list[i:]
#     # print(wow,i)
#     if len(wow) <= egg:
#         b_list.append(len(wow)*a_list[i])
#     else:
#         b_list.append(egg*a_list[i])
        
# print(a_list[b_list.index(max(b_list))],max(b_list))


    


    
    




    