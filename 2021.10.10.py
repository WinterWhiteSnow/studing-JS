lala = int(input())
if lala <=2:
	ob_list = ["1/1","1/2","2/1"]
else:
	ob_list = []
	for answer in range(1,lala):
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
print(ob_list[lala-1])

# for answer in range(1,10):
# 	ob = []
# 	for i in range(1,answer+1):	
# 		if answer %2 == 0 :
# 			right = answer
# 			first_num = f"{i}/{right}"	
# 			right-=i
# 			ob.append(first_num)
# 		elif answer %2 == 1 :
# 			left = answer
# 			first_num = f"{left}/{i}"	
# 			left-=i
# 			ob.append(first_num)
# 	ob_list.append(ob)