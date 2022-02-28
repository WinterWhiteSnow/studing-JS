# import sys
# end,l = map(int,sys.stdin.readline().rstrip().split())
# q = list(map(int,sys.stdin.readline().rstrip().split()))
# q.append(end)
# p = []
# for i in range(len(q)):
#     for a in range(i+1,len(q)):
#         # print(q[i],q[a])
#         p.append(abs(q[i]-q[a]))
# p = p+q
# p = list(set(p))
# p.sort()
# print(*p)

# p = int(input())
# stage = int(input())
# main = list(map(int,input().split()))
# if len(main) == stage:
#     p_dict = {}
#     for i in range(stage):
#         a = list(map(int,input().split()))
#         bonus = 0
#         for b in range(len(a)):
#             # print("m",main[i],"종이",a[b],b)
#             if a[b] == main[i]:
#                 if b not in p_dict:
#                     p_dict[b]=1
#                 else:
#                     p_dict[b]+=1
#             else:
#                 if b not in p_dict:
#                     p_dict[b]=0
#                 bonus+=1
#         p_dict[main[i]-1]+=bonus
#     for i in list(p_dict.values()):
#         print(i)
# card = [i for i in range(1,21)]
# for _ in range(10):
#     start, end = map(int,input().split())
#     start = start-1
#     card[start:end]=card[start:end][::-1]
# print(*card)

# num,repeat = map(int,input().split())
# baguni = [i for i in range(1,num+1)]
# baguni_dict= {}
# for i in baguni:
#     baguni_dict[i]=0
# for _ in range(repeat):
#     start,end,select = map(int,input().split())
#     for i in range(start,end+1):
#         baguni_dict[i]=select
# print(*list(baguni_dict.values()))

# n,m = map(int,input().split())
# baguni = [i for i in range(1,n+1)]
# for _ in range(m):
#     start,end=map(int,input().split())
#     start=start-1
#     baguni[start:end]=baguni[start:end][::-1]
# print(*baguni)   

# n,m = map(int,input().split())
# baguni = [i for i in range(1,n+1)]
# for _ in range(m):
#     begin,end,mid = map(int,input().split())
#     begin = begin-1
#     mid = mid-1
#     baguni[begin:end]=baguni[mid:end]+baguni[begin:mid]

# print(*baguni) 

# n,m = map(int,input().split())
# baguni = [i for i in range(1,n+1)]
# for _ in range(m):
#     first,second = map(int,input().split())
#     first=first-1
#     second=second-1
#     a = baguni[first]
#     b = baguni[second]
#     baguni[first]=b
#     baguni[second]=a
# print(*baguni)

# import sys

# n,r = map(int,sys.stdin.readline().rstrip().split())
# n_list = [i for i in range(1,n+1)]
# n_dict = {}
# for i in n_list:
#     n_dict[i]=0
# for _ in range(r):
#     wow = list(map(int,sys.stdin.readline().rstrip().split()))
#     for i in wow:
#         n_dict[i]+=1
# for i in list(n_dict.values()):
#     print(i)
r = int(input())
for rr in range(r):
    a = list(map(int,input().split()))    
    cnt = 0
    for i in range(1,11):
        wow = ((i-1)%5)+1
        if a[i-1] == wow:
            cnt+=1
    if cnt == 10:
        print(rr+1)
    
    
                
            
        
            
        