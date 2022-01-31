# a = int(input())
# print(int(round((a/2)*(a/2),0)))
# def wow(why,cnt2):
#     why = why
#     cnt2 = cnt2
#     for i in range(1,len(why)-1):
#         if i%2 !=0:            
#             if why[i] == "+":
#                 cnt2+=int(why[i+1])
#             elif why[i] == "-":
#                 cnt2-=int(why[i+1])
#             elif why[i] == "*":
#                 if int(why[i+1]) >0 and cnt2 > 0:
#                     cnt2*=int(why[i+1]) 
#                 else:
#                     cnt2*=int(why[i+1])*(-1)
#                     cnt2 = int(cnt2)*(-1)
#             elif why[i] == "/":
#                 if int(why[i+1]) >0 and cnt2 > 0:
#                     cnt2/=int(why[i+1])
#                 else:
#                     cnt2/=int(why[i+1])*(-1)
#                     cnt2 = int(cnt2)*(-1)
#         cnt2=int(cnt2)
#     return cnt2

# a_list = input().split()
# cnt1 =int(a_list[0])
# cnt1 = wow(a_list,cnt1)

# first = a_list[:2]
# why = a_list[2:]
# a = wow(why,int(why[0]))
# first.append(a)
# b = wow(first,int(first[0]))
# b = int(b)
# print(min(cnt1,b))
# print(max(cnt1,b))

# repeat = int(input())
# cnt = 0
# for _ in range(repeat):
#     wow = list(map(int,input().split()))
#     cnt+=sum(wow)
# print(cnt)

# import sys
# from collections import deque
# num = int(sys.stdin.readline().rstrip())
# a_list = deque()
# for a in range(3,num+1,3):
#     for b in range(3,num+1,3):
#         c=num-a-b
#         if c >0:
#             wow=[a,b,c]
#             a_list.append(wow)
# print(len(a_list))    
# year,k,p = map(int,input().split())
# cnt = 0
# for i in range(1,year+1):
#     cnt+=k*i+p*i*i
# print(cnt)

# a,b,c,x,y = map(int,input().split())
# e = a+b
# cnt = 0

# if x==y:
#     same = x
#     if e>c*2:
#         cnt+=c*mini*2
#     else:
#         cnt+=a*x+b*y
#     print(cnt)
# else:    
#     if x>y:
#         mini = y
#         maxi = x
#     elif x<y:
#         mini = x
#         maxi = y
        
        
#     if e>c*2:
#         cnt+=c*mini*2
#         if maxi==y:
#             cnt+=min(c*(maxi-mini)*2,(maxi-mini)*b)
#         elif maxi ==x:
#             cnt+=min(c*(maxi-mini)*2,(maxi-mini)*a)
#     else:
#         cnt+=a*x+b*y
#     print(cnt)

# a,b = map(int,input().split())
# cnt=a
# while True:
#     cnt+=a//b
#     a= a//b
#     if a == 0:
#         break
# print(cnt)
import sys
now_h,now_m,now_s = map(int,sys.stdin.readline().rstrip().split())
now = now_h*3600 + now_m*60 + now_s
repeat = int(sys.stdin.readline().rstrip())
for _ in range(repeat):
    wow = list(map(int,sys.stdin.readline().rstrip().split()))
    if len(wow) == 2:           
        T = wow[0]
        s = wow[1]
        if T == 1:
            now+=s
        else:
            now-=s
        now = now % 86400                
    else:
        h=now//3600
        m=now%3600//60
        s=now%60    
        print(h,m,s)
            
            

 
    


        

            