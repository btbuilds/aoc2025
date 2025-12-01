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

def parse_line(line, location) -> list[int]:
    instruction = int(line[1:])
    clicks = 0
    if instruction >= 100:
        clicks = math.floor(instruction / 100)
    if line[0] == "R":
        new_location = location + instruction
        while new_location > 99:
            new_location -= 100
        return [new_location, clicks]
    if line[0] == "L":
        new_location = location - instruction
        while new_location < 0:
            new_location += 100
        return [new_location, clicks]
    
parse_data()