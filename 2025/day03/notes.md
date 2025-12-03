day 03

function get max value
- length of number

char to left to calc

def get_max_number(length:int, battery_bank:str) -> (str, int)
    joltage2return = ""
    if length > 1:
        return_joltage, char_position = get_max_number(length--, battery_bank[:-1])
    else:
        bank = [int(char) for char in [char_position:battery_bank]
        max = max(bank)
        pos = bank.index(max)
        return_joltage + str(max)
        return (return_joltage, char_position)

