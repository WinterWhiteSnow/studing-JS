# a,b,c = map(int,input().split())
# wow = 2*a*(0.229*0.324)+2*b*(0.297*0.42)+c*(0.21*0.297)
# print(format(wow,".6f"))

# eight = int(input())
# three = int(input())
# print(eight*8+three*3-28)

# a,b,c,d,e = map(int,input().split())
# A,B,C,D,E = map(int,input().split())
# print(a*6+b*3+c*2+d+e*2,A*6+B*3+C*2+D+E*2)
# r = lambda : int(input())
# wow_list = []
# for _ in range(r()):
#     wow=input()
#     studunt = r()
#     total = 0
#     for _ in range(studunt):
#         total+=r()%studunt
#     if total%studunt == 0:
#         print("YES")
#     else:
#         print("NO")
# r = lambda : map(int,input().split())
# a,b,c,d = r()
# person = list(r())
# cnt = 1
# a_list = ([1]*a+[0]*b)
# b_list = ([1]*c+[0]*d)
# a_list = (max(person)//len(a_list)+1)*a_list
# b_list = (max(person)//len(b_list)+1)*b_list
# total = 0
# for i in person:
#     a = i-1
#     b = i
#     total = 0
#     if a_list[a] != a_list[b]:
#         if a_list[a] == 0:
#             pass
#         else:
#             total+=1
#     else:
#         total+=a_list[a]
#     if b_list[a] != b_list[b]:
#         if b_list[a] == 0:
#             pass
#         else:
#             total+=1
#     else:
#         total+=b_list[a]
#     print(total)

# n = int(input())
# cnt = bin(n)[2:].count("1")
# if cnt == 1:
#     print(1)
# else:
#     print(0)    

# n = int(input())
# cnt = 1
# while n!=1:
#     if n%2 == 0:
#         n//=2
#     else:
#         n = n*3+1
#     cnt+=1
# print(cnt)

# n = int(input())
# n_list = "".join([str(i) for i in range(1,n+1)])
# print(n_list.count("3")+n_list.count("6")+n_list.count("9"))
# import sys
# a = 0
# b = 0    
# for _ in range(int(sys.stdin.readline().rstrip())):
#     x,y=map(int,sys.stdin.readline().rstrip().split())
#     if x>y:
#         a+=1
#     if x<y:
#         b+=1
# print(a,b)


            

        
         
            
            