# import sys

# a = list(sys.stdin.readline().rstrip())
# list_list = []
# stack = 0
# for i in range(len(a)):
#     if a[i] == "(":
#         list_list.append(i)
#     else:
#         if a[i-1] == "(":
#             list_list.pop()
#             stack+=len(list_list)
#         else:
#             list_list.pop() 
#             stack+=1
# print(stack)
    
# bar_razor = list(input())
# answer = 0
# stack = []

# for i in range(len(bar_razor)):
#     print(bar_razor[i],stack)
#     if bar_razor[i] == '(': #스택 쌓기
#         stack.append('(')
        
#     else:
#         if bar_razor[i-1] == '(': #()라면 (를 pop하고 현재 스택에 들어있는 ( 수만큼 값을 더해준다.
#             stack.pop()
#             print("더하는거",len(stack))
#             answer += len(stack)
            
#         else:
#             stack.pop() 
#             print("1더함")
#             answer += 1 #끄트머리 막대기 부분을 더해준다

# print(answer)

# import sys
# a = int(sys.stdin.readline().rstrip())-1
# devil = 666
# while a>0:
#     devil+=1
#     if "666" in str(devil):
#         a-=1
# print(devil)    

import sys
a = []
b = []
for _ in range(9): # 0~8
    a.append(int(sys.stdin.readline().rstrip()))
a.sort()
i = 0
while True:
    i = i%9
    print(i,b)
    if len(b) != 7:
        b.append(a[i])
        i+=1
    else:
        if sum(b) != 100:
            b.clear()
            i+=1
for i in b:
    print(i)            
    

    