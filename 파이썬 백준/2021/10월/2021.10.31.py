
# answer = 0 0 1 0 1 5

the_num = int(input())
count = 0
answer_list = []
while count != the_num:
	count+=1
	answer = input().split(" ")
	answer = [float(i) for i in answer]
	x = answer[0]
	y = answer[1]
	r1 = answer[2]
	a = answer[3]
	b = answer[4]
	r2 = answer[5]
	distance_x = abs(a)+abs(x)
	distance_y = abs(b)+abs(y)
	if distance_x == distance_y:
		if r1 == r2:
			answer_list.append(-1)
		else:
			answer_list.append(0)
	elif distance_x == 0 or distance_y == 0:
		if distance_x ==0: #x가 0일때
			if r2-r1 < b < r1+r2:
				answer_list.append(2)
			elif r2-r1 == b or r1+r2 == b:
				answer_list.append(1)
			else:
				answer_list.append(0)
		elif distance_y ==0: #y가 0일때
			if r2-r1 < a < r1+r2:
				answer_list.append(2)
			elif r2-r1 == a or r1+r2 == a:
				answer_list.append(1)
			else:
				answer_list.append(0)
	else:
		answer_list.append(2)
for i in answer_list:
	print(i)