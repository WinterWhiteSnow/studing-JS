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

import sys
wow = int(sys.stdin.readline())
count = 0
a = wow
while True:
	try:
		if 0<= a<=99:
			if a <10:
				a = f"0{a}"
			else:
				a = f"{a}"
			a1=int(a[0])+int(a[1])#8
			a2=a[1]+f"{a1}"#68
			a2=int(a2)
			print(a2,wow)
			if a2 == wow:
				print(count)
				break
			else:
				print(f"이제{count}번째")
				count+=1
				a=a2
		else:
			break
	except:
		break
#백준 while문 3번째