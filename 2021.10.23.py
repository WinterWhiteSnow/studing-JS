import sys
start = int(sys.stdin.readline())
end = int(sys.stdin.readline())
list_list = []
answer_list=[]
for a in range(start,end+1):
	list_list.append(a)
	for i in range(2,int(end/2)+1):
		if a%i == 0:
			if a == 2:
				pass
			elif a not in answer_list:
				answer_list.append(a)
answer = list(set(list_list) - set(answer_list))
print(answer)
# if answer:
# 	answer.sort()
# 	if answer[0] == 1:
# 		answer = answer[1:]
# 	print(answer)
# 	print(sum(answer),answer[0],sep='\n')
# else:
# 	print(-1)

import sys
test_case = int(sys.stdin.readline())
answer = input().split(" ")
if len(answer) == test_case:
	answer = [int(i) for i in answer]
	answer.sort()
	if answer[0] == 1:
		answer = answer[1:]
	answer_list=[]
	for a in answer:
		for i in range(2,a):
			if a%i == 0:
				if a not in answer_list:
					answer_list.append(a)
	answer = list(set(answer) - set(answer_list))
	print(len(answer))