# import sys
# r = lambda : int(sys.stdin.readline().rstrip())
# n = r()
# maxi = r()
# sosu_dict = {}
# for i in range(2,maxi+1):
#     if i not in sosu_dict:
#         for index in range(i,n+1,i):
#             sosu_dict[index]=0
#         sosu_dict[i] = 1
# sosu_list = [key for key,value in sosu_dict.items() if value == 1]
# # print(sosu_list)
# cnt = 0
# # print(sosu_list)
# for i in range(2,n+1):
#     index= 0
#     while i != 1:
#         # print(i,index,cnt)
#         if index == len(sosu_list):
#             break            
#         if i%sosu_list[index] == 0:
#             i//=sosu_list[index]
#         elif i%sosu_list[index] != 0:
#             index+=1
            
#     if i == 1:
#         cnt+=1
# print(cnt+1)
# a,b,c = map(int,input().split())
# x,y,z = 1,1,1
# cnt=1
# while a!=x or b!=y or c!=z:
#     x+=1
#     y+=1
#     z+=1
#     x%=16
#     y%=29
#     z%=20
#     if x == 0:
#         x=1
#     if y == 0:
#         y =1
#     if z == 0:
#         z = 1
#     cnt+=1
# print(cnt)

# a,b = input().split()
# a = list(a)
# b = list(b)
# if len(a)==len(b):
#     cnt = 0
#     for i in range(len(b)):
#         if a[i] != b[i]:
#             cnt+=1
#     print(cnt)
# else:
#     cnt_list = []
#     for i in range(len(b)-len(a)+1):
#         b_list = b[i:i+len(a)]
#         cnt= 0
#         for index in range(len(a)):
#             if b_list[index] != a[index]:
#                 cnt+=1
#         cnt_list.append(cnt)
#     print(min(cnt_list))

# for _ in range(int(input())):
#     a,b= map(int,input().split())
#     cnt = 0
#     for i in range(a,b+1):
#         if "0" in str(i):
#             cnt+=str(i).count("0")
#     print(cnt)
    

    
    













