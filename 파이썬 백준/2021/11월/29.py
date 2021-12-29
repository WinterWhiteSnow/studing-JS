# import sys
# Tree,M = map(int, sys.stdin.readline().rstrip().split())
# a = list(map(int, sys.stdin.readline().rstrip().split()))
# a.sort()
# start,end = 0, a[-1]
# while True:
    
#     limit = (start+end)//2
#     sum_tree = 0
#     sum_tree = sum(i-limit if i-limit > 0 else 0 for i in a)
            
#     if sum_tree >= M:
#         start = limit
#     else:
#         end = limit
        
#     if end-start <= 1:
#         limit = start
#         break
# print(limit)
# 예시 1 : 2 3 / 2 2 answer = 2 
# 예시 2 : 2 5 / 7 9 answer = 5 

# import sys

# a,b = list(map(int, sys.stdin.readline().split()))
# wow= []
# for i in range(a):
#     wow.append(int(sys.stdin.readline()))
# wow.sort()
# start = 1
# end = wow[-1]
# while start<=end:
#     cm = (start+end)//2
#     o = 0
#     o = sum(i//cm if cm >0 else 0 for i in wow)
#     # print("끝",start,end,o,cm)
#     if o >= b : # 너무 많이 잘랐다 -> 자르는 기준을 높일 수 있다
#         # print("o>=b")
#         start = cm+1
#     else: # 너무 적게 잘랐다 -> 자르는 기준을 낮춰서 더 많이 잘라야한다
#         # print("o<b")
#         end = cm-1    
# print(end)

# import sys

# the_num = int(sys.stdin.readline().rstrip())
# a = sys.stdin.readline().rstrip().split()
# a_num = int(sys.stdin.readline().rstrip())
# b = sys.stdin.readline().rstrip().split()
# wow = {}
# if len(a) == the_num and len(b) == a_num:
#     for i in b:
#         wow[i] = 0
#         if i in a:
#             wow[i]+=1 #왜인ㅇ지 모르겠으나 for 리스트 구간에서 if 리스트2 확인작업은
#             #시간초과를 낳음
#         print(wow[i],end=" ")



# import sys

# the_num = int(sys.stdin.readline().rstrip())
# sanguen = sys.stdin.readline().rstrip().split()
# a_num = int(sys.stdin.readline().rstrip()) 
# check = sys.stdin.readline().rstrip().split()
# dict_sanguen = {}
# if len(sanguen) == the_num and len(check) == a_num:
#     for i in sanguen:
#         if i not in dict_sanguen:
#             dict_sanguen[i]=1
#         else:
#             dict_sanguen[i]+=1

#     for i in check:
#         if i in dict_sanguen:
#             wow = str(dict_sanguen[i])
#         else:
#             wow ="0"
#         print(wow, end=" ")       