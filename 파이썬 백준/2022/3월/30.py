# n_dict = {}
# for i in range(10):
#     if i not in n_dict:
#         n_dict[i] = 0
# a,b = map(int,input().split())
# for i in range(a,b+1):
#     number = list(map(int,list(str(i))))
#     for index in number:
#         n_dict[index]+=1
# print(*list(n_dict.values()))
# import sys
# n = int(sys.stdin.readline().rstrip())
# m = int(n**(1/2))
# cnt = 0
# for a in range(m+1):
#     for b in range(m+1):
#         for c in range(m+1):
#             for d in range(m+1):
#                 if a*a+b*b+c*c+d*d > n:
#                     break
#                 if a*a+b*b+c*c+d*d == n:
#                     cnt+=1
# print(cnt)

# r,l =map(int,input().split())
# n_list = []
# for _ in range(r):
#     n_list.append(input())
# front = []
# back = []
# perpect = []
# for i in n_list:
#     if i[::-1] in n_list:
#         if i == i[::-1]:
#             perpect.append(i)
#         else:
#             if i not in front and i not in back:
#                 front.append(i)
#                 back.append(i[::-1])
# string = ""
# back = back[::-1]
# for i in front:
#     string+=i
# if perpect:
#     string+=perpect[0]
# for i in back:
#     string+=i
# print(len(string))
# if string:
#     print(string)


        
    
                    