import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# r = one()
# n_list = [[0 for _ in range(101)] for _ in range(101)]
# for _ in range(r):
#     x,y = wow()
#     for y_index in range(y,y+10):
#         # print(y_index)
#         for x_index in range(x,x+10):
#             if n_list[y_index][x_index] == 0:
#                 n_list[y_index][x_index]=1
# cnt = 0
# for i in range(100):
#     cnt+=n_list[i].count(1)
# print(cnt)

# cnt = 0
# num = inputing()
# l = len(num)
# for i in range(1,l):
#     cnt+=(9*10**(i-1))*i
# now = int(num)-10**(l-1)+1
# print(cnt+now*l)                        

# num = one()
# print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
# def repeat(number,index):
#     if index != number:
#         print("____"*index,end="")
#         print('"재귀함수가 뭔가요?"')
#         print("____"*index,end="")
#         print('"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
#         print("____"*index,end="")
#         print("마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.")
#         print("____"*index,end="")
#         print('그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
#         repeat(number,index+1)
#     else:
#         print("____"*index,end="")
#         print('"재귀함수가 뭔가요?"')
#         print("____"*index,end="")
#         print('"재귀함수는 자기 자신을 호출하는 함수라네"')
#         print("____"*index,end="")
#         print("라고 답변하였지.")
#         return
#     print("____"*index,end="")
#     print("라고 답변하였지.")
# repeat(num,0)















