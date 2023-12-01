
#with open("./input.txt", "r") as file:
 #   text = file.read()

text = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f"
, "treb7uchet"]

passes = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

total = 0
for word in text:

    left_ptr = 0
    right_ptr = len(word) - 1

    first_digit = 0
    last_diigt = 0

    stop_left = False
    stop_right = False

    digit_str = ""

    while left_ptr < right_ptr:

        if  word[left_ptr] in passes and not stop_left:
            first_digit = word[left_ptr]
            stop_left = True

        if word[right_ptr] in passes and not stop_right:
            last_digit = word[right_ptr]

            stop_right = True

        print(word[left_ptr])
        print(word[right_ptr])
        left_ptr += 1
        right_ptr -= 1


    if first_digit == 0:
        digit_str = last_digit + last_digit
    elif last_digit == 0:
        digit_str = first_digit + first_digit
    else:
        digit_str = first_digit + last_digit

    print(digit_str)
    total += int(digit_str)

print(total)

