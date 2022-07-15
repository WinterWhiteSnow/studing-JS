import sys
inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# l,k = wow()
# n_list = list(wow())
# summary = sum(n_list[:k])
# result = summary
# for start in range(l-k):
#     end = start+k
#     summary = summary-n_list[start]+n_list[end]
#     result = max(result,summary)
# print(result)

r = one()
for _ in range(r):
    string = inputing()
    start= 0
    end = len(string)-1
    difference = 0
    while start<end:
        if string[start] != string[end]:
            print("on going...",start,end)
            difference+=1
            start_plus = 1
            end_minus=1
            if string[start+1] == string[end]:
                new_string = string[start+1:]
                ll = len(new_string)//2
                a = new_string[:ll+1]
                b = new_string[ll:][::-1]
                if a==b:
                    pass
                else:
                    start_plus=difference+1
            print()
            if string[start] == string[end-1]:
                new_string = string[:end]
                ll = len(new_string)//2
                a = new_string[:ll+1]
                b = new_string[ll:][::-1]
                if a==b:
                    pass
                else:
                    end_minus=difference+1
            difference = min(start_plus,end_minus)
            break
            # print("going..",start,end,difference)
        # print("end!!",start,end,difference)
    print(difference)























