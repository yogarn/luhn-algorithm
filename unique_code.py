def sum_digit(unique_code):
    total_sum = 0
    sum_digit_unique_code = 0
    counter = 0
    while (unique_code != 0):
        digit_unique_code = unique_code % 10
        if (counter % 2 == 0):
            digit_unique_code = digit_unique_code * 2
            if (digit_unique_code > 9):
                sum_digit_unique_code = 0
                while(digit_unique_code != 0):
                    sum_digit_unique_code = sum_digit_unique_code + (digit_unique_code % 10)
                    digit_unique_code = digit_unique_code // 10
            else:
                sum_digit_unique_code = digit_unique_code
        else:
            sum_digit_unique_code = digit_unique_code * 1
        counter = counter + 1
        total_sum = total_sum + sum_digit_unique_code
        unique_code = unique_code // 10
    return total_sum
def check_digit(get_check, unique_code):
    check_digit = unique_code % 10
    if (check_digit == get_check):
        return True
    else:
        return False

unique_code = 17893729974
get_check = 10 - (sum_digit(unique_code // 10) % 10)
print(check_digit(get_check, unique_code))