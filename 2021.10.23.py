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