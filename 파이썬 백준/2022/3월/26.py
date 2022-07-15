# import sys
# a,b,c,d,e,f = map(int,sys.stdin.readline().rstrip().split())
# for x in range(-999,999+1):
#     for y in range(-999,999+1):
#         if a*x+b*y == c and d*x+e*y==f:
#             print(x,y)      
# while True:
#     a_list = list(map(int,input().split()))
#     if len(a_list) == 1 and a_list[0] == -1:
#         break
    
#     cnt = 0
#     for i in a_list:
#         if i*2 in a_list:
#             if i != 0:
#                 # print(i*2)
#                 cnt+=1
#     print(cnt)
# import sys
# for _ in range(int(sys.stdin.readline().rstrip())):
#     n,m = map(int,sys.stdin.readline().rstrip().split())
#     cnt = 0
#     for a in range(1,n):
#         for b in range(a+1,n):
#             if (a*a+b*b+m)%(a*b) == 0:
#                 cnt+=1
#     print(cnt)
# from math import gcd
# r = lambda : map(int,input().split())
# n,l = r()
# n_list = list(r())
# wow_list = []
# for s in n_list:
#     for i in range(s,n+1):
#         if i%s == 0:
#             if i not in wow_list:
#                 wow_list.append(i)
# print(sum(wow_list))

# n = int(input())
# n_list = []
# for i in range(1,n+1):
#     if n%i == 0:
#         if i not in n_list:
#             n_list.append(i)
# # print(n_list)
# print(sum(n_list)*5-24)
# n_list = []
# for _ in range(int(input())):
#     n_str = ""
#     for _ in range(5):
#         n_str+=input()
#     n_list.append(n_str)
# m_list = []
# for a in range(len(n_list)):
#     for b in range(a+1,len(n_list)): 
#         # print(a,b)
#         cnt = 0
#         a_list = n_list[a]
#         b_list = n_list[b]
#         for index in range(len(a_list)):
#             if a_list[index] != b_list[index]:
#                 cnt+=1
#         m_list.append([cnt,a,b])
# m_list.sort(key=lambda x:x[0])
# print(m_list[0][1]+1,m_list[0][2]+1)
# import sys
# sheep_eat,goat_eat,total,eat_total=map(int,sys.stdin.readline().rstrip().split())
# n_list = []
# for i in range(1,total):
#     if (eat_total - sheep_eat*i)%goat_eat == 0:
#         if ((eat_total - sheep_eat*i)//goat_eat)+i == total:
#             n_list.append(i)
# if len(n_list) == 0 or len(n_list) > 1:
#     print(-1)
# else:
#     print(n_list[0],total-n_list[0])

# from math import gcd
# a_jump,b_jump,a_start,b_start = map(int,input().split())
# def wow(x,y):
#     return x*y//gcd(x,y)
# maxi = wow(a_jump,b_jump)+max(a_start,b_start)
# index = 1
# def why(maxi,n_start,n_jump):
#     list_list = []
#     for i in range((maxi-n_start)//n_jump+1):
#         list_list.append(n_start+n_jump*i)
#     return list_list
# a = why(maxi,a_start,a_jump)
# b = why(maxi,b_start,b_jump)
# total = set(a).intersection(set(b))
# if total:
#     print(list(total)[0])
# else:
#     print(-1)

# l = int(input())
# n_list = list(map(int,input().split()))
# cnt_list = []
# index = l-3
# for i in range(l-index+1):
#     cnt = 1
#     wow = n_list[i:i+index]
#     # print(wow,i,index)
#     for q in wow:
#         cnt*=q
#     cnt_list.append(cnt)
# cnt_max = cnt_list.index(max(cnt_list))
# print(sum(n_list[:cnt_max])+sum(n_list[cnt_max+index:])+max(cnt_list))

for _ in range(int(input())):
    a = int(input())
    a_list = []
    for i in range(1,a+1):
        if a%i == 0:
            a_list.append(i)
    print(a,len(a_list))


    
    