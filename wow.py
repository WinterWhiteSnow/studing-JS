# wow = input("").split(" ")
# a = int(wow[0])
# b = int(wow[1])
# b = b-45
# if b<0:
# 	if a == 0 :
# 		a = 24
# 	a = a-1
# 	b = b+60
# print(a,b)

# wow = int(input(""))
# if wow%4==0:
# 	if wow%100!=0:
# 		print("1")
# 	elif wow%400==0:
# 		print("1")
# 	else:
# 		print("0")
# else:
# 	print("0")

# wow = int(input(""))
# for i in range(1,10):
# 	print(f"{wow} * {i} =",wow*i)

# repeat = int(input(""))
# for i in range(0,repeat):
# 	wow = input("").split(" ")
# 	if len(wow) == 1:
# 		pass
# 	else:
# 		a = int(wow[0])
# 		b = int(wow[1])
# 		print(a+b)
	
# wow = int(input(""))
# a = 0
# for i in range(1,wow+1):
# 	a+=i
# print(a)	

# import sys
# repeat =  int(sys.stdin.readline())
# # repeat =  sys.stdin.readline().split()
# for i in range(repeat):
# 	wow = sys.stdin.readline().split(" ")
# 	a=int(wow[0])
# 	b=int(wow[1])
# 	print(a+b)

# import sys	
# wow = int(sys.stdin.readline())
# for i in range(1,wow+1):
# 	print(i)

# import sys	
# wow = int(sys.stdin.readline())
# a = wow
# for i in range(0,wow):
# 	print(a-i)

# import sys	
# wow = int(sys.stdin.readline())
# repeat = wow
# for i in range(1,repeat+1):
# 	how = sys.stdin.readline().split(" ")
# 	a = int(how[0])
# 	b = int(how[1])
# 	print(f"Case #{i}:",a+b)

# import sys	
# wow = int(sys.stdin.readline())
# repeat = wow
# for i in range(1,repeat+1):
# 	how = sys.stdin.readline().split(" ")
# 	a = int(how[0])
# 	b = int(how[1])
# 	print(f"Case #{i}: {a} + {b} =",a+b)

# import sys	
# wow = int(sys.stdin.readline())
# repeat = wow
# for i in range(1,repeat+1):
# 	print("*"*i)

# import sys	
# wow = int(sys.stdin.readline())
# repeat = wow
# for i in range(1,repeat+1):
# 	result = "*"*i
# 	print(result.rjust(wow))

# import sys	
# wow = sys.stdin.readline().split(" ")
# the_number = int(wow[0])
# maximum = int(wow[1])
# def how():
# 	answer = sys.stdin.readline().split(" ")
# 	if len(answer) != the_number:
# 		print("다시적어요")
# 		how()
# 	else:
# 		for i in answer:
# 			i = int(i)
# 			if i < maximum:
# 				print(i)
# 			else:
# 				pass
# how()

# import sys	
# while True:
# 	wow = sys.stdin.readline().split(" ")
# 	a = int(wow[0])
# 	b = int(wow[1])
# 	if a == 0 and b ==0:
# 		break
# 	else:
# 		print(a+b)

# import sys
# while True:
# 	try:
# 		wow = sys.stdin.readline().split(" ")
# 		a = int(wow[0])
# 		b = int(wow[1])
# 		print(a+b)
# 	except:
# 		break

# import sys
# wow = int(sys.stdin.readline())
# count = 1
# a = wow
# while True:
# 	try:
# 		if 0<= a<=99:
# 			if a <10:
# 				a = f"0{a}"
# 			else:
# 				a = f"{a}"
# 			a1=int(a[0])+int(a[1])#8
# 			if a1 < 10:
# 				a1 = f"0{a1}"
# 			else:
# 				a1 = f"{a1}"
# 			a2=a[1]+a1[1]#68
# 			a2=int(a2)
# 			if a2 == wow:
# 				print(count)
# 				break
# 			else:
# 				count+=1
# 				a=a2
# 		else:
# 			break
# 	except:
# 		break

# import sys
# the_number = int(sys.stdin.readline())
# def how():
# 	wow = sys.stdin.readline().split(" ")
# 	if len(wow) !=the_number:
# 		how()
# 	else:
# 		wow_int = [int(i) for i in wow]
# 		wow_int.sort()
# 		max_num = wow_int[-1]
# 		mini_num = wow_int[0]
# 		result = [mini_num,max_num]
# 		return result

# a = how()
# print(a[0],a[-1])

# import sys
# the_number = 9
# num_list = []
# result = []
# def how():
# 	wow = int(sys.stdin.readline())
# 	if wow<100:
# 		num_list.append(wow)
# 		if len(num_list) !=the_number:
# 			how()
# 		else:
# 			wow_sort = sorted(num_list)
# 			max_num = wow_sort[-1]
# 			count = num_list.index(max_num)+1
# 			result.append(max_num)
# 			result.append(count)	
# how()
# for i in result:
# 	print(i)

# import sys
# num_list=[]
# count = []
# def how():
# 	wow = int(sys.stdin.readline())
# 	if 100<=wow<1000:
# 		num_list.append(wow)
# 		if len(num_list) !=3:
# 			how()
# 		else:
# 			bored = str(num_list[0]*num_list[1]*num_list[2])
# 			for i in range(10):
# 				count.append(i)
# 			str_count = [str(i)for i in count]
# 			for i in str_count:
# 				print(bored.count(i))	
# how()		

# import sys
# num_list=[]
# result = []
# def how():
# 	wow = int(sys.stdin.readline())
# 	if 1<=wow<1000:
# 		num_list.append(wow)
# 		if len(num_list) !=10:
# 			how()
# 		else:
# 			for i in num_list:
# 				if i%42 not in result:
# 					result.append(i%42)		
# how()
# print(len(result))

# import sys
# the_number = int(sys.stdin.readline())
# def how():
# 	wow = sys.stdin.readline().split(" ")
# 	if len(wow) !=the_number:#wow.count("0") >=2 or
# 		how()
# 	else:		
# 		num_list = [int(i) for i in wow]
# 		sort_list = sorted(num_list)
# 		result = sum(num_list)/the_number/sort_list[-1]*100
# 		relative_error = sum(num_list)/the_number*100
# 		absolute_error = (relative_error-result)/relative_error*100
# 		print(round(result,6))
# how()	
		
# import sys
# the_number = int(sys.stdin.readline())
# answer_list = []
# def how():
# 	wow = sys.stdin.readline()
# 	answer_list.append(wow)
# 	if len(answer_list) !=the_number:
# 		how()
# 	else:
# 		for l in answer_list:
# 			split_list = l.strip("\n").split("X")
# 			count = 0
# 			count_o = []
# 			for i in split_list:
# 				count_o.append(len(i))
# 			count = 0
# 			for i in count_o:
# 				if i>=2:
# 					for a in range(i+1):
# 						count+=a
# 				elif i==0:
# 					pass		
# 				else:
# 					count+=1
# 			print(count)			
# how()	

# import sys
# the_number = int(sys.stdin.readline())
# answer_list = []
# def how():
# 	boolean_list=[]
# 	answer = sys.stdin.readline().split(" ")
# 	student_num = int(answer[0])
# 	if len(answer) == student_num+1:
# 		answer=[int(i) for i in answer]
# 		ob = {
# 			len(answer_list):answer
# 		}
# 		answer_list.append(ob)
# 		if len(answer_list) !=the_number:
# 			how()
# 		else:
# 			for i in answer_list:
# 				all_values=list(i.values())[0]
# 				calculation = round(sum(all_values[1:])/all_values[0],3)
# 				keys = list(i.keys())[0]
# 				tem_list = []
# 				for a in all_values[1:]:
# 					tem_list.append(a>calculation)
# 				db = {
# 					keys:tem_list
# 				}
# 				boolean_list.append(db)
# 	if boolean_list:
# 		for i in boolean_list:
# 			boolean_values=list(i.values())[0]
# 			result = boolean_values.count(True)/len(boolean_values)*100
# 			print("{result:.3f}%".format(result=result))		
# how()


# the_number = input().split(" ")
# def solve(wow):
# 	a = [int(i) for i in wow]
# 	if 1<=len(a)<=3000000:
# 		a = sorted(a)
# 		if 1<=a[0] and a[-1]<=3000000:
# 			ans = sum(a)
# 			return ans

# wow_list = []
# def self_number(wow):
# 	wow_int = wow
# 	if wow_int>=10:
# 		wow_str = str(wow_int)
# 		for i in wow_str:
# 			a = int(i)
# 			wow_int+=a
# 	else:
# 		wow_int+=wow_int
# 	if wow_int <=10000 and wow_int not in wow_list:
# 		wow_list.append(wow_int)
# 		self_number(wow_list[-1])	

# for i in range(10000+1):
# 	self_number(i)
# 	if i not in wow_list:
# 		print(i)

# yah = []
# answer = input()
# oh = int(answer)
# def num_num(wow):
# 	wow = str(wow)
# 	wow_str = [i for i in wow]
# 	wow_int = [int(i) for i in wow_str]
# 	for i in range(len(wow_int)-(len(wow_int)-1)):
# 		if len(wow_int) == 4:
# 			a,b,c,d = wow_int[i],wow_int[i+1],wow_int[i+2],wow_int[i+3]
# 			if d-c == c-b and c-d == b-a:
# 				yah.append(wow_int)
# 		elif len(wow_int) == 3:
# 			a,b,c = wow_int[i],wow_int[i+1],wow_int[i+2]
# 			if c-b == b-a:
# 				yah.append(wow_int)
# 		else:
# 			yah.append(wow_int)
# for i in range(1,oh+1):
# 	num_num(i)
	
# print(len(yah))	

# answer = input()
# if answer:
# 	print(ord(answer))

# import sys
# the_number = int(sys.stdin.readline())
# sum_number = sys.stdin.readline().strip()
# if len(sum_number) == the_number:
# 	list_sum_number = [i for i in sum_number]
# 	int_sum_number = [int(i) for i in list_sum_number]
# 	print(sum(int_sum_number))

# import sys
# the_number = int(sys.stdin.readline())
# answer_list = []
# def repeat():
# 	answer = sys.stdin.readline().split(" ")
# 	index = int(answer[0])
# 	answer_list.append(answer)
# 	if len(answer_list) == the_number:
# 		for i in answer_list:
# 			before_split = i[1].strip()
# 			after_split = [i for i in before_split]
# 			repeat_num = int(i[0])
# 			list_list = []
# 			for i in range(len(after_split)):
# 				wow = after_split[i]*repeat_num
# 				list_list.append(wow)
# 			print("".join(list_list))	

# 	else:
# 		repeat()

# repeat()
import string
wow = string.ascii_lowercase
wow_list = [i for i in wow]
ob_dict = {}
for i in range(len(wow_list)):
	key = wow_list[i]
	value = i
	ob_dict[key]=value
aa = input("").lower()
result=[]
for i in wow_list:
	if i in aa:
		# result.append(ob_dict[i])
		a = aa.find(i)
	else:
		# result.append("-1")
		a = "-1"
	print( a, end=" ")
