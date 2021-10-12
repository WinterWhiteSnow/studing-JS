answer = int(input())
count = 0
total = 0
num = 0
while True:
	num += 1
	count+=num
	if count >= answer:
		total = num+1
		break
wow = count-answer+1 #무조건 감소, 0에 수렴함
if total % 2 == 0 : #홀수, 분모증가
	print("홀수",count,total,answer,wow)
	dd = total-wow
	print(f"{wow}/{dd}")
	# top = total - (answer-start_num)
	# under = total - top
	# print(f"{under}/{top}")
else:#짝수, 분자증가
	print("짝수",count,total,answer,wow)
	dd = total-wow
	print(f"{dd}/{wow}")	
	# top = total - wow
	# under = total-top
	# print(f"{top}/{under}")