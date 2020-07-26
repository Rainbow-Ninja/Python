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
        print(f'Our new num is {n}')
    return count



print(persistence(127))