# answer = int(input())
# answer_list = []

# if answer>=3:
# 	if (answer%5)%3 == 0 or (answer%3)%5==0 or answer%5 ==0 or answer%3==0:	
# 		if answer - 5*(answer//5) == 0 :
# 			print("1")
# 			one = answer//5
# 			answer_list.append(one)
# 		else:
# 			if (answer-5*(answer//5))%3 ==0:
# 				print("2")
# 				one = answer//5+(answer-5*(answer//5))/3
# 				answer_list.append(one)
# 			else:
# 				pass

# 		if answer - 3*(answer//3) == 0 :
# 			print("3")
# 			two = answer//3
# 			answer_list.append(two)
# 		else:
# 			if (answer - 3*(answer//3))%5 == 0 :
# 				print("4")
# 				two = answer//3+(answer - 3*(answer//3))/5
# 				answer_list.append(two)
# 			else:
# 				pass	
# 	elif (answer-8)%3 == 0:
# 		print(">0<")
# 		num = answer//5 -1
# 		print(int((answer - (5*num))/3) + num)
# 		# print("5") 11->3 | 26 -> 6
# 		# print(int(answer//3))
# 	else:
# 		print("-1")	
# else:
# 	print("-1")

# if len(answer_list)>=1:
# 	if len(answer_list)	>1:
# 		answer_list = [int(i) for i in answer_list]
# 		answer_list.sort()
# 		print(answer_list[0])
# 	else:
# 		print(int(answer_list[0]))

