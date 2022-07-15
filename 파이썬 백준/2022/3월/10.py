# l = int(input())
# a_list = list(map(int,input().split()))
# a_list.sort()
# total_l = sum(a_list)
# price = 0
# for i in a_list:
#     price+=total_l*i-i**2
#     # print(price)
#     total_l-=i
# print(price)

# participant,genre,main = map(int,input().split())
# a_list = []
# for _ in range(genre):
#     a = list(map(float,input().split()))
#     num = []
#     score = []
#     for i in range(len(a)):
#         if i%2 == 0:
#             num.append(int(a[i]))
#         else:
#             score.append(a[i])
#     for i in range(len(num)):
#         a_list.append([num[i],score[i]])
# a_list.sort(key=lambda x:x[1],reverse=True)
# num_list = []
# total_score = 0
# index = 0
# while len(num_list) != main:
#     wow = a_list[index]
#     number = wow[0]
#     score = wow[1]
#     if number not in num_list:
#         num_list.append(number)
#         total_score+=score
#     else:
#         pass
#     index+=1
# print(format(total_score,".1f"))
# import sys
# start_list = []
# end_list = []
# for _ in range(int(sys.stdin.readline().rstrip())):
#     start,end = list(map(int,sys.stdin.readline().rstrip().split()))
#     start_list.append(start)
#     end_list.append(end)
# a = max(start_list)
# b = min(end_list)
# if b>=a:
#     print(0)
# else:
#     print(abs(b-a))

# test = int(input())
# for _ in range(test):
#     candy,boxes = map(int,input().split())
#     box = []
#     for _ in range(boxes):
#         sero,garo = map(int,input().split())
#         box.append(sero*garo)
#     box.sort(reverse=True)
#     cnt = 0
#     total = 0
#     index= 0
#     while total < candy:
#         total+=box[index]
#         index+=1
#         cnt+=1
#     print(cnt)
#     box=[]
# while True:
#     try:
#         a,b = input().split()
#         if a in b:
#             print("Yes")
#         else:
#             for i in list(b):
#                 if i not in a:
#                     if i in b:
#                         b = b.replace(i,"")
#             if a in b:
#                 print("Yes")
#             else:
#                 wow = "YES"
#                 for i in list(a):
#                     if i in b:
#                         b=b[b.index(i)+1:]
#                     else:
#                         print("No")
#                         wow = "NO"
#                         break
#                 if wow =="YES":
#                     print("Yes")        
#     except:
#         exit()
  
        


    
    


        
