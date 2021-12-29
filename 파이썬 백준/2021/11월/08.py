# the_num = int(input())
# a =input().split()
# list_list = []
# if len(a) == the_num:
# 	a = [int(i) for i in a]
# 	a.sort()
# 	maxi = a[-1]
# 	for i in a:
# 		list_list.append(i/maxi)
# print(round((sum(list_list)/len(a)*100),6))

# import sys
# the_num = int(sys.stdin.readline())
# count = 0
# a_list = []
# while count != the_num:
#     count+=1
#     a= sys.stdin.readline().split("X")
#     score = 0
#     for i in a:
#         i = i.strip("\n")
#         for a in range(1,len(i)+1):
#             score+=a
#     a_list.append(score)
# for i in a_list:
#     print(i)

# import sys
# the_num = int(sys.stdin.readline().rstrip())
# count = 0
# list_list = []
# while count != the_num:
#     count +=1
#     a = sys.stdin.readline().rstrip().split()
#     a = [int(i) for i in a]
#     person_num = a[0]
#     score = a[1:]
#     average = sum(score)/person_num
#     average_up = 0
#     for i in score:
#         if i > average:
#             average_up+=1
#     list_list.append(round((average_up/person_num)*100,3))
# for i in list_list:
#     print(f"{i:.3f}%")

# a_int = list(range(1,10000+1))
# a_str = [str(i) for i in a_int]
# list_list = []
# def d():
#     for i in a_str:
#         count = 0
#         count+=int(i)
#         for b in i:
#             count+=int(b)
#         list_list.append(count)    
#     wow = list(set(a_int)-set(list_list))
#     wow.sort()
#     for i in wow:
#         print(i)
# d()

# def wow(a):
#         count= 99
#         for d in range(100,a+1):
#             a = [i for i in str(d)]
#             score = []
#             for i in range(1,len(a)):
#                 if int(a[i])-int(a[i-1]) not in score:
#                     score.append(int(a[i])-int(a[i-1]))
#             score = set(score)
#             if len(score) == 1:
#                 count+=1
#         print(count)

# a = int(input())
# if a < 100:
#     print(a)
# else:
#     wow(a)

# 함수까지 완료