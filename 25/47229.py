lst = []
for i1 in range(10):
    for i2 in range(1001):
        num = int(f'1{i1}2139{i2}4')
        if i2 == 1000:
            num = int(f'1{i1}21394')
        if num % 2023 == 0:
            lst.append((num, num // 2023))
print(*sorted(lst), sep='\n')
