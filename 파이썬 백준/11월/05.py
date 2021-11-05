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
	sort_x = [x,a]
	sort_y = [y,b]
	sort_r = [r1,r2]
	sort_x.sort()
	sort_y.sort()
	sort_r.sort()
	mini = (sort_r[1] - sort_r[0])**2
	maxi = (sort_r[0] + sort_r[1])**2
	distance_x = sort_x[1] - sort_x[0]
	distance_y = sort_y[1] - sort_y[0]
	wow = distance_x**2 + distance_y**2
	if mini < wow < maxi:
		answer_list.append(2)
	elif wow == 0:
		if sort_r[0] == sort_r[1]:
			answer_list.append(-1)
		elif wow < mini or wow > maxi:
			answer_list.append(0)
	elif wow == mini or wow == maxi:
		answer_list.append(1)
for i in answer_list:
	print(i)
	
		
	
