# test_case = int(input())
# for _ in range(test_case):
#     input()
#     garo = []
#     sero = {}
#     r,l = map(int,input().split())
#     for _ in range(r):
#         wow = input()
#         garo.append(wow)
#         for i in range(len(wow)):
#             if i not in sero:
#                 sero[i] = wow[i]
#             else:
#                 sero[i]+=wow[i]
#     cnt = 0
#     for i in garo:
#         cnt+=i.count(">o<")
#     for i in sero.values():
#         cnt+=i.count("vo^")
#     print(cnt)

# r = int(input())
# n_list = []
# for _ in range(r):
#     n_list.append(list(map(int,input().split())))
# n_list.sort(key=lambda x : x[2],reverse=True)
# cnt = 0
# list_list = []
# for i in n_list:
#     if cnt == 3:
#         break
#     if list_list.count(i[0]) != 2:
#         print(i[0],i[1])
#         list_list.append(i[0])
#         cnt+=1

# r = int(input())
# for _ in range(r):
#     a,b = input().split()
#     a="0b"+a
#     b="0b"+b
#     a = int(a,2)
#     b = int(b,2)
#     c = a+b
#     print(bin(c)[2:])     

# n_list = [0,1,1]
# index = int(input())
# start = 3
# while len(n_list)<= index:
#     n_list.append(n_list[-1]+n_list[-2])
# print(n_list[-1])
# import sys
# while True:
#     r1,r2= map(int,sys.stdin.readline().rstrip().split())
#     if r1==r2==0:
#         break
#     n_list = []
#     for _ in range(r1):
#         n_list.append(int(sys.stdin.readline().rstrip()))
#     cnt=0
#     m_list = []
#     for _ in range(r2):
#         m_list.append(int(sys.stdin.readline().rstrip()))
#     print(len(set(n_list).intersection(set(m_list))))
        # wow = list(map(int,input().split()))
#         for i in range(len(wow)):
#             if i not in num_dict:
#                 num_dict[i] = wow[i]
#             else:
#                 num_dict[i]=wow[i]*num_dict[i]
#     wow_list = sorted(num_dict.items(),key=lambda x : (x[1],x[0]),reverse=True)
#     print(wow_list[0][0]+1)

# for _ in range(int(input())):
#     n_list = []
#     r = int(input())
#     for _ in range(r):
#         n_list.append(int(input()))
#     index = 1
#     while True:
#         wow = [i%index for i in n_list]
#         if len(set(wow)) == r:
#             break
#         else:
#             index+=1
#     print(index)
# from collections import deque
# n,k = map(int,input().split())
# n_list = deque([i for i in range(1,n+1)])
# wow_list = []
# while len(n_list) != 0:
#     n_list.rotate(-(k-1))
#     wow_list.append(n_list[0])
#     n_list.remove(n_list[0])
# print("<",end="")
# print(*wow_list,sep=", ",end="")
# print(">")

            
        
    
    




















