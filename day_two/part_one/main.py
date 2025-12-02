file_path = "input.txt"
 
def parse_data():
    sequences = []
    data = ""
    total = 0
    with open(file_path, "r") as f:
        data = f.readlines() # Raw data as a single item list
        sequences = data[0].split(",") # Split in to individual items
    for sequence in sequences:
        invalid_ids = parse_sequence(sequence)
        total += sum(invalid_ids)
    print(total)

def parse_sequence(sequence: str):
    if check_valid_range(sequence) is False:
        return [0]
    parts = sequence.split("-")
    lower = int(parts[0])
    higher = int(parts[1])
    invalid_ids = []
    current_num = lower
    
    while current_num in range(lower, higher + 1):
        length = len(str(current_num))
        if length % 2 != 0:
            current_num = 10 ** length # Jump to the next even length number
        num_str = str(current_num)
        s1 = num_str[:len(num_str) // 2]
        s2 = num_str[len(num_str) // 2:]
        if s1 == s2:
            invalid_ids.append(current_num)
            next_half = str(int(s1) + 1)
            current_num = int(next_half + next_half) # Jump to the next possible valid number
            continue
        current_num += 1
    return invalid_ids

def check_valid_range(sequence: str):
    # We can ignore sequences with an odd length where both
    # the lower and higher number have the same length
    # For example - lower is 5 digit, higher is 5 digits...
    # thus none of the numbers in that sequence will be a match
    parts = sequence.split("-")
    if (len(parts[0]) % 2 != 0 and
        len(parts[0]) == len(parts[1])):
        return False

parse_data()