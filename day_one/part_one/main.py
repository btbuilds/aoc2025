file_path = "input.txt"

def parse_data():
    count_zero = 0
    current_location = 50
    with open(file_path, "r") as f:
        for line in f:
            current_location = parse_line(line, current_location)
            if current_location == 0:
                count_zero += 1
    print(count_zero)

def parse_line(line, location) -> int:
    instruction = int(line[1:])
    if line[0] == "R":
        new_location = location + instruction
        while new_location > 99:
            new_location -= 100
        return new_location
    if line[0] == "L":
        new_location = location - instruction
        while new_location < 0:
            new_location += 100
        return new_location
    
parse_data()