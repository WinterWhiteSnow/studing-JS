# the_num = int(input())
# count = 0
# dict_list = {}
# list_list = []
# while count!=the_num:
#     count+=1
#     a = input()
#     list_list.append(a)
# list_list = list(set(list_list))
# list_list.sort(key = len)
# for i in range(1,len(list_list[-1])+1):
#     dict_list[i] = []
#     for a in list_list:
#         if i == len(a):
#             dict_list[i].append(a)
# for key,value in dict_list.items():
# 	if len(value) =>2:
# 		value.sort()
# 	for i in value:
# 		print(i)


# lst.sort(key = len)
# lst.sort()
# 왜 길이대로 정렬한 후 사전대로 정렬하면 사전정렬만 되고
# 사전정렬 후 길이대로 정렬하면 길이정렬+사전정렬이 되는가?

# num = int(input())
# a_list = ""
# count = 0
# for i in range(num):
#     b = (i//11)+3
#     count
#     number = "6"*b
#     count+=1
#     if count < 6:
#         a_list=f"{count}{number}"
#     else:
#         if count == 11:
#             count=0
#         else:
#             wow= count-5
#             a_list=f"{number}{wow}"
# print(a_list)

# a = input().split(" ")
# the_num = int(a[0])
# total = int(a[1])
# b = input().split()
# a_list = []
# if len(b) == the_num:
#     b = [int(i) for i in b]
#     for i in range(len(b)):
#         print(b[i],b[i+1],b[i+2])

# a = int(input())
# wow = []
# for i in range(1,a+1):
#     b = [int(x) for x in str(i)]
#     c = i +sum(b)
#     if c == a:
#         wow.append(i)
# wow.sort()
# if wow:
#     print(wow[0])
# else:
#     print(0)

# a = input().split()
# the_num = int(a[0])
# goal = int(a[1])
# b = input().split()
# a_list = []
# if len(b) == the_num:
#     b = [int(i) for i in b]
#     for i in range(0,len(b)):
#         for x in range(i+1,len(b)):
#             for y in range(x+1,len(b)):
#                 wow = b[i]+b[x]+b[y]
#                 if wow <= goal:
#                     a_list.append(wow)
# a_list.sort()    
# print(a_list[-1])                

# a = input().split()
# start = int(a[0])
# end = int(a[1])
# a_list = {}
# def split(potato):
#     tomato = potato
#     list_list=[]
#     while tomato !=1:
#         for i in range(2,int(potato/2)+1):
#             if tomato%i == 0:
#                 list_list.append(i)
#                 tomato = tomato//i
#                 break
#         if tomato == 1:
#             return list_list
# a_list[start]=split(start)
# a_list[end] = split(end)
# print(a_list)

a = input().split()
start = int(a[0])
end = int(a[1])
def wow (potato,tomato):
    a = [potato,tomato]
    x = potato
    y = tomato
    a.sort()
    greatest = 1
    for i in range(2,(a[-1]//2)+1):
        while True:
            if x % i == 0 and y % i == 0:
                x = x//i
                y = y//i
                greatest*=i
            else:
                break    
    return greatest,greatest*x*y
print(wow(start,end)[0])
print(wow(start,end)[1])

