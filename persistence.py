def persistence(n):
    count = 0
    while len(str(n)) > 1:
        length = len(str(n))
        num_list = list(str(n))
        total = 1
        for num in num_list:
            total *= int(num)
        count += 1
        n = total
    return count



print(f'Out final answer is {persistence(127)}') #expected 2