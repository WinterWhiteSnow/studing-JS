#순서없이 나오는대로 사칙연산 구현하기
# wow = input().split()
# cnt1 =int(wow[0]) #순서대로 했을때
# cnt2 = 0 #정공법으로 했을때
# for i in range(1,len(wow)-1):
#     if i%2 !=0:
#         if wow[i] == "+":
#             cnt1+=int(wow[i+1])
#         elif wow[i] == "-":
#             cnt1-=int(wow[i+1])
#         elif wow[i] == "*":
#             cnt1*=int(wow[i+1])
#         elif wow[i] == "/":
#             cnt1/=int(wow[i+1])
# first = wow.count("*")
# second = wow.count("/")
# if first==second==0:
#     print(cnt1)
#     print(cnt1)
# else:    
#     while True:
#         first = wow.count("*")
#         second = wow.count("/")
#         if first == second == 0:
#             break
        
#         if first>0:
#             index = wow.index("*")
#             a = int(wow[index-1])*int(wow[index+1])
#             del wow[index-1:index+2]
#             wow.insert(index-1,a)
#         elif second>0:
#             index = wow.index("/")
#             a = int(wow[index-1])/int(wow[index+1])
#             del wow[index-1:index+2]
#             wow.insert(index-1,a)
#     print(wow)
#     cnt2 = int(wow[0])
#     for i in range(1,len(wow)-1):
#         if i%2 !=0:
#             if wow[i] == "+":
#                 cnt2+=int(wow[i+1])
#             elif wow[i] == "-":
#                 cnt2-=int(wow[i+1])
#     print(min(cnt1,cnt2))
#     print(max(cnt1,cnt2))

#K만들기
# import math
# n = int(input())
# k = n*5
# for a in range(1,k+1):
#     for b in range(1,k+1):
#         if 1 <=b <= n:
#             print("@",end="")
#         else:#n*(5-(math.ceil(a/n))) >n*3 일때
#             # print(a,b)
#             if a <= n*2:
#                 if n*(5-(math.ceil(a/n)))<=b<=n*(5-(math.ceil(a/n)))+2:
#                     if b != k:
#                         print("@",end="")
#                     else:
#                         print("@")
#                 else:
#                     if b != k:
#                         print(" ",end="")
#                     else:
#                         print(" ")
#             elif n*2 < a <=n*3:
#                 if 1<=b<n*3:
#                     print("@",end="")
#                 else:
#                     if b == k :
#                         print(" ")
#                     else:
#                         print(" ",end="")
#             else:                    
#                 if k-(n*(5-(math.ceil(a/n))))-3<=b<k-(n*(5-(math.ceil(a/n)))):
#                     if b != k:
#                         print("@",end="")
#                     else:
#                         print("@")
#                 else:
#                     if b != k:
#                         print(" ",end="")
#                     else:
#                         print(" ")

#곡과 알람이 동시에 울릴때
# import math
# l = int(input())
# if l == 1:
#     pile = int(input())
#     wow = int(input())
#     if pile > wow:
#         print(wow*(math.ceil(pile/wow)))
#     else:
#         print(wow)
# else:
#     pile = list(map(int,input().split()))
#     wow = int(input())
#     cnt=0
#     for i in pile:
#         if i > wow:
#             cnt+=wow*(math.ceil(i/wow))
#         else:
#             if i == 0:
#                 pass
#             else:
#                 cnt+=wow
#     print(cnt) 

#펫
# cnt=0
# while True:
#     good_weight,now_weight = map(int,input().split())
#     cnt+=1
#     if now_weight==0==good_weight:
#         break
    
#     while True:
#         act,num = map(str,input().split())
#         if act=="#" and num =="0":
#             break
            
#         if act =="F":
#             now_weight+=int(num)
#         else:
#             now_weight-=int(num)
#         if now_weight <=0:
#             break
        
#     if now_weight <= 0:
#         print("RIP")
#     else:   
#         if good_weight/2 < now_weight < good_weight*2:
#             print(cnt,":-)")
#         else:
#             print(cnt,":-(")
a =list("a lot")
for i in a:
    print(len(i))