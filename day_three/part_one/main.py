file_path = "input.txt"

def parse_data():
    total = 0
    first_index = 0
    first_digit = 0
    second_digit = 0
    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            iteration = 0
            largest_digit = 0
            
            for digit in line[:-1]:
                if int(digit) > largest_digit:
                    largest_digit = int(digit)
                    first_index = iteration
                iteration += 1
            
            first_digit = largest_digit
            largest_digit = 0

            for digit in line[first_index + 1:]:
                if int(digit) > largest_digit:
                    largest_digit = int(digit)
            
            second_digit = largest_digit
            total += int(str(first_digit) + str(second_digit))
    print(total)

parse_data()