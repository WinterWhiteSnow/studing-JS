# import sys

# a = sys.stdin.readline().rstrip().split()
# if len(a)>1:
#     start = int(a[0])
#     jump = int(a[1])
# else:
#     start = int(a[0])
#     jump = int(a[0])
# count =0
# a_list = []
# while True:
#     count+=1
#     print("여긴 while",count)
#     if jump == 0:
#         break
#     elif jump*count <= start:
#         print("여긴 <start", jump*count,count,jump)
#         if start-jump*count == 0:
#             print("0일때")
#             if jump*count not in a_list:
# 	            a_list.insert(len(a_list)//2,jump*count)
#         else: 
#             if jump*count not in a_list:
#                 a_list.insert(len(a_list)//2,start-jump*count)
#                 a_list.insert(len(a_list)//2,jump*count)
    
#     else:
#         print("다시다시")
#         jump=jump-1
#         count = 0
# print("<",end="")
# for i in a_list[:-1]:
#     print(str(i),end=", ")
# print(str(a_list[-1]),end="")
# print(">",end="")

# import sys

# a = sys.stdin.readline().rstrip().split()
# if len(a)>1:
#     start = int(a[0])
#     jump = int(a[1])
# else:
#     start = int(a[0])
#     jump = int(a[0])
# a_list = []
# count = 0
# for aa in range(jump,-1,-1):
#     count+=1
#     for i in range(1,count+2):
#         print("i",i)
#         if aa*i <= start:
#             if aa*i not in a_list and start-aa*i not in a_list:
#                 print("not in",aa*i, len(a_list))
#                 if len(a_list) == 0:
#                     a_list.extend([aa*i,start-aa*i])
#                 else:
#                     if start-aa*i == aa*i or start-aa*i == 0:
#                         a_list.insert(len(a_list)//2,aa*i)
#                     else:
#                         if start-aa*i != 0:
#                             a_list.insert(len(a_list)//2,start-aa*i)
#                         if aa*i !=0:
#                             a_list.insert(len(a_list)//2,aa*i)
# print(a_list)

end, step = map(int,input().split())

a = [i for i in range(1,end+1)]
step = step-1
a_list = []
count = 0
while len(a) != 0:
    print(a_list)
    print("a",a)
    if len(a) >=3:
        for i in range(step, end, 3):
            print("i",i)
            if len(a)-1 >i:
                wow = a[i]
                a_list.append(wow)
                count = i
                
        a = list(set(a)-set(a_list))
        b = []
        for i in a:
            if i <= count:
                b.append(i)
            else:
                b.insert(0,i)
        a=b
    else:
        for i in a:
            a_list.append(i)
        
