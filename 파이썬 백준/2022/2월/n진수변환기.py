def div(wow,num):
    start = wow
    start_list = []
    while True:
        if start == 0:
            break
        a = str(start%num)
        start_list.append(a)
        start = start//num
    return start_list