digits_dict = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

with open('task2.txt', 'r') as file:
    lines = file.readlines()
    total = 0

    for line in lines:
        digits_list = list()
        temp_str = ""
        for number in line:
            if number.isdigit():
                digits_list.append(number)
                continue
            temp_str += number
            for num in digits_dict.keys():
                if num in temp_str:
                    digits_list.append(str(digits_dict[num]))
                    temp_str = temp_str[-1]
                    break
        if len(digits_list) >= 2:
            total += int(digits_list[0] + digits_list[-1])
        elif len(digits_list) == 1:
            total += int(digits_list[0] + digits_list[0])
        digits_list.clear()
    print(total)




