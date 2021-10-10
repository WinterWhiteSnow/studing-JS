ob_list = []
for answer in range(1,50):
	for i in range(1,answer+1):	
		if answer %2 == 0 :
			num = answer+1
			wow = num-i
			first_num = f"{i}/{wow}"
			ob_list.append(first_num)
		elif answer %2 == 1 :
			num = answer+1
			wow = num-i
			first_num = f"{wow}/{i}"	
			ob_list.append(first_num)
print(ob_list)