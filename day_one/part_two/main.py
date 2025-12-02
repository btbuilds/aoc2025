file_path = "input.txt"

def parse_data():
    count_zero = 0
    current_location = 50
    with open(file_path, "r") as f:
        for line in f:
            current_location, clicks = parse_line(line, current_location)
            count_zero += clicks
    print(count_zero)

def parse_line(line, location):
    direction = line[0]
    instruction = int(line[1:])
    result = []
    clicks = instruction // 100
    remaining_steps = instruction % 100

    if direction == "L":
        result = move_left(remaining_steps, location)
    elif direction == "R":
        result = move_right(remaining_steps, location)
    clicks += result[1]
    return [result[0], clicks]

def move_left(instruction, location):
    new_location = (location - instruction) % 100
    clicks = 0
    if location > 0:
        clicks = 0 if instruction < location else 1
    return [new_location, clicks]

def move_right(instruction, location):
    new_location = (location + instruction) % 100
    clicks = 0 if (instruction + location < 100) else 1
    return [new_location, clicks]

parse_data()