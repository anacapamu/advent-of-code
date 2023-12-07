# --- Day 1: Trebuchet?! ---
import re

# --- Part One ---

def get_calibration_values(file_name):
    '''
    Takes the first and last digits in a line, combine them into an integer, and add it to
    a list

    Parameters:
    file_name (str): name of input txt file in same directory as this one

    Returns:
    calibration_values (array): list of integers
    '''

    calibration_values = []

    with open(file_name, 'r') as file:
        for line in file:
            temp_nums = []
            for char in line:
                if char.isdigit():
                    temp_nums += char
            temp_value = temp_nums[0] + temp_nums[-1]
            calibration_values.append(int(temp_value))

    return calibration_values

def sum_calibration_values(calibration_values):
    '''
    Adds up all the calibration values provided

    Parameters:
    calibration_values (array): list of integers

    Returns:
    sum (int): sum of all calibration values
    '''

    sum = 0

    for calibration_value in calibration_values:
        sum += calibration_value

    print("The sum of all of the calibration values = ", sum)
    return sum

# --- Part Two ---

def get_correct_calibration_values(file_name):
    '''
    Takes the first and last numbers in a line, whether or not the number is a digit or
    spelled out. Combine them into an integer, and add it to a list.

    Parameters:
    file_name (str): name of input txt file in same directory as this one

    Returns:
    calibration_values (array): list of integers
    '''

    nums_map = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

    calibration_values = []
    num_words = '|'.join(nums_map.keys())
    num_pattern = fr'(?=({num_words}|\d))'

    with open(file_name, 'r') as file:
        for line in file:
            temp_nums = []
            found_nums = re.findall(num_pattern, line)

            for nums in found_nums:
                if nums.isdigit():
                    temp_nums += nums
                else:
                    temp_nums += str(nums_map[nums])

            temp_value = temp_nums[0] + temp_nums[-1]
            calibration_values.append(int(temp_value))

    return calibration_values

if __name__ == "__main__":
    # calibration_values = get_calibration_values("day_one_input.txt")
    # sum_calibration_values(calibration_values)

    correct_calibration_values = get_correct_calibration_values("day_one_input.txt")
    sum_calibration_values(correct_calibration_values)
