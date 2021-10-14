# import sys
# the_num = int(sys.stdin.readline())
# answer_list = []
# while len(answer_list) != the_num:
# 	answer = sys.stdin.readline().split(" ")
# 	answer = [int(i) for i in answer]
# 	answer_list.append(answer)

# for i in answer_list:
# 	H = i[0]
# 	W = i[1]
# 	C = i[2]
# 	top = C%H
# 	under = round(C//H)+1
# 	if top >= 1 :
# 		if under < 10:
# 			print(f"{top}0{under}")
# 		else:
# 			print(f"{top}{under}")
# 	else:
# 		top = H
# 		under = under-1
# 		if under < 10:
# 			print(f"{top}0{under}")
# 		else:
# 			print(f"{top}{under}")	

1 7 (1,6) 28(1,6,21)
1 6(1,5) 21(1,5,15)
1 5(1,4) 15(1,4,10)
1 4(1,3) 10(1,3,6)
1 3(1+2) 6(1,2,3)
1 2 3 
