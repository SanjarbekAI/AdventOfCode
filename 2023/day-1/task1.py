with open('task1.txt', 'r') as file:
    lines = file.readlines()
    total = 0
    for line in lines:
        digits = list()
        for digit in line:
            if digit.isdigit():
                digits.append(digit)
        if len(digits) >= 2:
            total += int(digits[0] + digits[-1])
        elif len(digits) == 1:
            total += int(digits[0] + digits[0])
        digits.clear()
    print(total)