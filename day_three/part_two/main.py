file_path = "input.txt"

def parse_data():
    total = 0
    req_length = 12
    with open(file_path, "r") as f:
        for line in f:
            current_num = ""
            line = line.strip()
            latest_index = 0

            while len(current_num) < req_length:
                remaining = req_length - len(current_num) # How many digits we still need
                max_index = len(line) - remaining + 1 # We must leave room for the remaining digits

                largest_digit = 0
                best_position = latest_index

                for i in range(latest_index, max_index):
                    if int(line[i]) > largest_digit:
                        largest_digit = int(line[i])
                        best_position = i
                
                current_num += str(largest_digit)
                latest_index = best_position + 1  # Start after this digit next time
            total += int(current_num)
    print(total)

parse_data()