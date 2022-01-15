# import sys

# sosu,k = map(int,sys.stdin.readline().rstrip().split())
# num = k+1
# sosu_dict = {}
# for i in range(2,num):
#     if i not in sosu_dict:
#         for a in range(i,num,i):
#             sosu_dict[a]=0
#         sosu_dict[i]=1
# sosu_list = [i[0] for i in sosu_dict.items() if i[1] == 1]
# a = []
# index = 0
# while True:
#     if index == len(sosu_list):
#         break
    
#     if sosu%sosu_list[index] == 0:
#         a.append(sosu_list[index])
#     index+=1
# a.sort()
# if len(a) == 0:
#     print("GOOD")
# elif a[0] < k:
#     print("BAD",a[0])
# else:
#     print("GOOD")

# d,h,w = map(int,input().split())
# wow = ((d**2)/(h**2+w**2))**(1/2)
# print(int(h*wow),int(w*wow))


    