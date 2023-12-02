def is_possible(cubes, counts):
    for subset in cubes:
        subset_counts = {color: 0 for color in counts}
        for item in subset:
            quantity, color = item.strip().split()
            subset_counts[color] += int(quantity)
        if any(subset_counts[color] > counts[color] for color in counts):
            return False
    return True


def possible_games(input_data, target_counts):
    possible_ids = []
    for line in input_data:
        game_id, cubes_str = line.split(":")
        cubes_list = [subset.strip().split(",") for subset in cubes_str.split(";")]
        if is_possible(cubes_list, target_counts):
            possible_ids.append(int(game_id.split()[1]))
    return possible_ids


if __name__ == "__main__":
    input_file_path = "task-1.txt"

    with open(input_file_path, "r") as file:
        input_data = file.readlines()

    target_counts = {"red": 12, "green": 13, "blue": 14}
    result = possible_games(input_data, target_counts)

    print("Possible Games IDs:", result)
    print("Sum of IDs:", sum(result))
