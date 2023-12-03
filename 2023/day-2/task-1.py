with open('task-1.txt', 'r') as file:
    lines = file.readlines()
    red = 12
    green = 13
    blue = 14
    total = 0
    for line in lines:
        game_id = int(line.split(":")[0].strip().split()[1])
        cubes = line.split(":")[1].replace(";", ",")
        is_valid = True
        for cube in cubes.split(","):
            number = int(cube.strip().split()[0])
            if "red" in cube:
                if number > red:
                    is_valid = False
                    break
            elif "green" in cube:
                if number > green:
                    is_valid = False
                    break
            elif "blue" in cube:
                if number > blue:
                    is_valid = False
                    break
        if is_valid:
            total += game_id
    print(total)




