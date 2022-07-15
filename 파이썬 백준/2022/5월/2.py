import sys
inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# l,my_score,limit = wow()
# if l == 0:
#     print(1)
# else:
#     n_list = list(wow())
#     n_list.append(my_score)
#     n_list.sort(reverse=True)
#     a = n_list.index(my_score)+n_list.count(my_score)
#     if a <= limit:
#         print(n_list.index(my_score)+1)
#     else:
#         print(-1)
# cnt = 1
# while True:
#     good,now = wow()
#     if good==now==0:
#         break
#     while True:
#         act,num = inputing().split()
#         if act == "#" and num =="0":
#             break        
#         num = int(num)
#         if now <= 0:
#             pass
#         else:
#             if act == "F":
#                 now+=num
#             else:
#                 now-=num           
#         # print(good,now)
#     if good//2<now<good*2:
#         print(cnt,":-)")
#     elif now <= 0:
#         print(cnt,"RIP")
#     else:
#         print(cnt,":-(")
#     cnt+=1

# num = one()
# wow_list = [0]*(10**6+1)
# for i in range(2,num+1):
#     if i%6 == 0:
#         wow_list[i] = min(wow_list[i-1]+1,wow_list[i//2]+1,wow_list[i//3]+1)
#     else:
#         if i%2 == 0:
#             wow_list[i] =  min(wow_list[i-1]+1,wow_list[i//2]+1)
#         elif i%3 == 0:
#             wow_list[i] = min(wow_list[i-1]+1,wow_list[i//3]+1)
#         else:
#             wow_list[i] = wow_list[i-1]+1
#     # print(wow_list[:num+1])
# print(wow_list[num])

# dict_list = {"AA":"A","AG":"C","GA":"C","AC":"A","CA":"A","AT":"G","TA":"G","GG":"G","GC":"T","CG":"T","GT":"A","TG":"A","CC":"C","CT":"G","TC":"G","TT":"T"}
# l = int(inputing())
# aa = list(inputing())
# while len(aa) != 1:
#     a = aa.pop()
#     b = aa.pop()
#     aa.append(dict_list[a+b])
#     # print(aa)
# print(aa[0])
# r,limit = wow()
# n_list = [one() for _ in range(r)]
# wow_list = [0]*(limit+1)
# for i in n_list:
#     for a in range(i,limit+1,i):
#         wow_list[a]=1
#         # print(wow_list)
# print(sum(wow_list))

















