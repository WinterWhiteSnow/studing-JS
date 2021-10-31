lala = int(input())
count = 0
total = 0
start_num=0
while count<lala:
	for i in range(1,lala+1):
		count+=i
		if count >= lala:
			start_num=i
			total = i+1
			break
if total % 2 == 0 : #홀수, 분모증가
	print("홀수",count,total,start_num,lala)
	top = total - (lala-start_num)
	under = total - top
	print(f"{under}/{top}")
else:#짝수, 분자증가
	print("짝수",count,total,start_num,lala)
	top = total - start_num + (lala-start_num)
	under = total - top
	print(f"{top}/{under}")
# 4 - > 3/1
# 5 - > 2/2
# 6 - > 1/3
# while count<lala:
# 	for a in range(1,total):
# 		count+=1
# 		top = total-a
# 		if i % 2 ==0:
# 			print(a,top)
# 			break
# 		else:
# 			print(top,a)
# 			break

# while count<lala:
# 	for i in range(1,lala+1):
# 		count+=i
# 		total = i+1
# 		if count>lala:
# 			count = i
# 			if i % 2 == 0:
# 				for a in range(1,total):
# 					count+=1
# 					top = total - a
# 					if count == lala:
# 						print("짝수",count,top,a)
# 						break
# 			else:
# 				for a in range(1,total):
# 					count+=1
# 					top = total-a
# 					if count == lala:
# 						print("홀수",count,a,top)
# 						break


# while count<=lala:
# 	count+=1
# 	for i in range(1,lala+1):
# 		if i % 2 == 0:
# 			total = i+1
# 			for a in range(1,total):
# 				top = total-a
# 				wow = f"{a}/{top}"
# 				print(wow)
# 		else:
# 			total = i+1
# 			for b in range(1,total):
# 				top = total-b
# 				wow = f"{top}/{b}"
# 				print(wow)

# while count<lala:
# 	for i in range(1,lala+1):
# 		count+=1
# 		print("count",count,lala)
# 		total = i+1
# 		for a in range(1,total):
# 			top = total-a
# 			if count==lala:		
# 				if i % 2 == 0:
# 					print(f"{a}/{top}")
# 				else:
# 					print(f"{top}/{a}")



		