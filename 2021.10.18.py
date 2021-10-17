answer = int(input())
# 11 16 26 27
count = 0

answer_list = []
if answer >2 :
	while answer > count*5:
		count+=1
	if count > 1:	
		for i in range(1,count):
			a = i*5
			if (answer-a)%3 == 0 :
				b = (answer-a)//3
				answer_list.append(i+b)
			else:
				if answer%5 ==0:
					answer_list.append(answer//5)
				elif answer%3 ==0:
					answer_list.append(answer//3)
				else:
					answer_list.append(-1)
	else:
		if answer%3 ==0:
			answer_list.append(answer//3)
		elif answer%5 ==0:
			answer_list.append(answer//5)
		else:
			answer_list.append(-1)
else:
	print(-1)

if len(answer_list)>0:
	if len(answer_list) >1:
		answer_list = list(set(answer_list))
		answer_list.sort()
		if -1 in answer_list:
			answer_list.remove(-1)
			print(answer_list[0])
		else:
			print(answer_list[0])
	else:
		print(answer_list[0])