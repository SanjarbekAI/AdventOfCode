with open('task-2.txt', 'r') as file:
    lines = file.readlines()
    total = 0
    for line in lines:
        set_cubes = line.split(":")[1].replace(";", ',').split(',')
        red = 0
        green = 0
        blue = 0
        for cube in set_cubes:
            if "red" in cube:
                red_number = int(cube.strip().split()[0])
                if red_number > red:
                    red = red_number
            elif "green" in cube:
                green_number = int(cube.strip().split()[0])
                if green_number > green:
                    green = green_number
            elif "blue" in cube:
                blue_number = int(cube.strip().split()[0])
                if blue_number > blue:
                    blue = blue_number

        total += red * green * blue
        print(red, green, blue)
        print(total)





