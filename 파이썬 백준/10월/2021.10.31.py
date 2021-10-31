
# answer = [0,0,1,0,1,5]

the_num = int(input())
count = 0
answer_list = []
while count != the_num:
	count+=1
	answer = input().split(" ")
	answer = [int(i) for i in answer]
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
		if r1+r2 == distance_x or r1+r2 == distance_y:
			answer_list.append(1) # 참
		elif r1+r2 > distance_x or r1+r2 > distance_y:
			answer_list.append(2)
		else:
			answer_list.append(0)
	else:
		answer_list.append(2)
for i in answer_list:
	print(i)