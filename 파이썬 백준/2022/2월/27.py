# a = [1,1]
# n = int(input())
# while len(a) != n+1:
#     a.append(a[-2]+a[-1])
# print(a[-1]*2+a[-2]*2)
# evolution = 0
# pokemon = {}
# for i in range(int(input())):
#     name = input()
#     need,inventory = map(int,input().split())
#     evol = 0
#     while inventory >= need:
#         wow = inventory//need
#         evolution+=wow
#         evol+=wow
#         inventory=inventory%need+wow*2
#     pokemon[name]=[evol,i]
# a_list = sorted(pokemon.items(),key=lambda x : x[1][1])
# a_list = sorted(a_list,key=lambda x : x[1][0],reverse=True)
# print(evolution)
# print(a_list[0][0])
# from math import gcd

# a,b = map(int,input().split())
# num = gcd(a,b)
# if a >= b:
#     mini = a
#     maxi = b
# else:
#     mini = b
#     maxi = a
# for i in range(1,num+1):
#     if a%i==b%i==0:
#         print(i,a//i,b//i)
n,q = map(int,input().split())
n_list = list(map(int,input().split()))
for _ in range(q):
    a_list = list(map(int,input().split()))
    a = a_list[1]
    b = a_list[2]
    if len(a_list) == 3:
        print(sum(n_list[a-1:b]))
        wow = n_list[a-1:b]
        n_list[a-1]=wow[-1]
        n_list[b-1]=wow[0]
    if len(a_list) == 5:
        c = a_list[3]
        d = a_list[4]
        print(sum(n_list[a-1:b])-sum(n_list[c-1:d]))
        
    