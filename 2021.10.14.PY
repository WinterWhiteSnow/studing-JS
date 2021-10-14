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
	people = 0
	piano = 0
	if floor == 1:
		for i in range(1,room+1):
			people+=i
		result_list.append(people)
	else:
		if room >=2:
			if room ==2:
				people+=2+floor
			else: #방이 세개이상
				rest = 2+floor
				for b in range(1,room+1):
					rest+=b	
					piano+=rest
					people+=piano
			result_list.append(people)
		else:
			result_list.append(people+1)		
print(result_list)



# 1 7 (1*5,1) 28 (1,6,21(1,2,3,4,5,6)) 
# 1 6 (1*4,1) 21 (1,5,15(1,2,3,4,5)) 
# 1 5 (1*3,2) 15 (1,4,10(1,2,3,4)) 35 (1,4(1,3),10(1,2,3,4),20(1,2,3,4,5,6))
# 1 4 (1*2,2) 10 (1*2+2,6(1,2,3)) 20 (1,3,6(1,2,3),10(1,2,3,4)) 

# 1 3(1*1,2) 6(1,2,3) 10(1,2,3,4)
# 1 2 3 4