# import sys

# start = int(sys.stdin.readline().rstrip())
# end = int(sys.stdin.readline().rstrip())
# sosu_list = {}

# for i in range(2,end+1):
#     if i not in sosu_list:
#         for a in range(i,end+1,i):
#             sosu_list[a]=0
#         sosu_list[i]=1
# sosu_list_list = [key for key,value in sosu_list.items() if value == 1 and key >= start]        
# if sosu_list_list:    
#     print(sum(sosu_list_list))
#     print(min(sosu_list_list))
# else:
#     print(-1)

# import sys
# num = int(sys.stdin.readline().rstrip())
# number = 2
# a_list = []
# while num != 1:
#     if num%number == 0:
#         a_list.append(number)
#         num = num/number
#     else:
#         number+=1
# for i in a_list:
#     print(i)        

# import sys

# start,end = map(int, sys.stdin.readline().rstrip().split())
# sosu_dict = {}

# for a in range(2,end+1):
#     if a not in sosu_dict:
#         for b in range(a,end+1,a):
#             sosu_dict[b]=0
#         sosu_dict[a]=1
# sosu_list = [key for key,value in sosu_dict.items() if value == 1 and start <= key <= end]
# for i in sosu_list:
#     print(i)

# import sys

# sosu_dict = {}
# wow = 123456*2+1
# for i in range(2,wow):
#     if i not in sosu_dict:
#         for b in range(i,wow,i):
#             sosu_dict[b]=0
#         sosu_dict[i]=1
        
# a_list = []
# while True:
#     a = int(sys.stdin.readline().rstrip())
#     if a == 0:
#         break
#     end = 2*a    
#     sosu_list = [key for key,value in sosu_dict.items() if value == 1 and a < key <= end]
#     a_list.append(len(sosu_list)) 
# for i in a_list:
#     print(i)

import sys

sosu_dict = {}
wow = 10000+1
for a in range(2,wow):
    if a not in sosu_dict:
        for b in range(a,wow,a):
            sosu_dict[b]=0
        sosu_dict[a]=1
sosu_list = [key for key,value in sosu_dict.items() if value == 1]
sosu_list.sort()        
repeat = int(sys.stdin.readline().rstrip())

for _ in range(repeat):
    n_list = []
    a = int(sys.stdin.readline().rstrip())
    count = 0
    if a//2 in sosu_list:
        print(a//2,a//2)
    else:
        while a >= sosu_list[count]:
            b = a-sosu_list[count]
            if b in sosu_list:
                if b not in n_list:
                    n_list.append(sosu_list[count])
                    n_list.append(b)
                count+=1            
            else:
                count+=1        
        print(n_list[-2],n_list[-1])   