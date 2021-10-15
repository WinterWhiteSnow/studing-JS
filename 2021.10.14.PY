the_num = int(input())
answer_list = []
result_list = []
while len(answer_list) != the_num:
	floor = int(input())
	room = int(input())
	answer_list.append([floor,room])
for a in answer_list:
	floor = a[0]#최대수
	room = a[1] #몇번 더 하는가
	people = [i for i in range(1,room+1)]
	for b in range(floor):
		for c in range(1, room):
			people[c]+=people[c-1]
	print(people[-1])
# 	if floor == 1:
# 		for i in range(1,room+1):
# 			people+=i
# 		result_list.append(people)
# 	else:
# 		if room >=2:
# 			if room ==2:
# 				people+=2+floor
# 			else: #방이 세개이상
# 				rest = 2+floor
# 				count = 0
				
# 				for b in range(1,room+1):
# 					count+=b	
# 			result_list.append(people)
# 		else:
# 			result_list.append(people+1)		
# print(result_list)

