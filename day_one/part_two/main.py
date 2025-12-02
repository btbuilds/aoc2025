import math

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
    clicks = 0
    current_location = location
    
    while instruction > 0:
        if direction == "L":
            current_location -= 1
        elif direction == "R":
            current_location += 1

        if current_location == 100:
            current_location = 0 
        elif current_location == -1:
            current_location = 99

        if current_location == 0:
            clicks += 1

        instruction -= 1

    return [current_location, clicks]

parse_data()