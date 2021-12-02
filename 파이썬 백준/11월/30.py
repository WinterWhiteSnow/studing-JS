# import sys
# from collections import deque

# a = int(sys.stdin.readline().rstrip())
# b = deque()
# for i in range(a):
#     b.append(int(sys.stdin.readline().rstrip()))
# c = b.pop()
# b.reverse()

# count= 0
# while True:
#     for i in b:
#         if i > c:
#             count+=1
#             c=i
#     break
# print(count+1)

# import sys
# from collections import deque

# a = int(sys.stdin.readline().rstrip())
# c = deque()
# for i in range(a):
#     b = sys.stdin.readline().rstrip().split()
#     c.append(b)
# for count,i in enumerate(c):
#     count = count+1
#     print(f"Case #{count}:"," ".join(reversed(i)))
import sys
num = list(map(int,sys.stdin.readline().rstrip().split()))
home_work = []
score = 0
for _ in range(num[0]):
    practice = list(map(int,sys.stdin.readline().rstrip().split()))
    # print("시작",home_work)
    if practice[0] == 1:
        wow = {
            "score":practice[1],
            "time":practice[2]-1
        }
        if practice[2]-1 == 0:
            score+=practice[1]
        else:           
            home_work.append(wow)
    else:
        if len(home_work) > 0:
            home_work[-1]["time"]-=1
            if home_work[-1]["time"] == 0:
                score+=home_work[-1]["score"]
                home_work.pop()
    # print("끝",home_work,score)
print(score)    
     