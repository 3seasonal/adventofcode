#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from typing import List
"""

- Project: adventofcode
- Year: 2025
- Day: 06
- File: 06_puzzle.py
- Description: Cephlapod homework
- Author: 3seasonal
- Created: 2025-12-06
- License: MIT (SPDX: MIT)

Notes:
- By no means is this a good example of clean code structure. It is intended to be a quick-and-dirty
  solution to the puzzle, with minimal dependencies.
- If you are reading this... Sorry.

General solution structure:
- All in one and one in all messy script.
- Parse / process / print 
"""

__title__ = "Advent of Code 2025 Day 060 Puzzle"
__author__ = "3seasonal"
__created__ = "2025-12-00"


def main():
    """
    Main function to execute pid parsing.
    """
    
    # config
    #input_path = os.path.join(os.path.dirname(__file__), '06_sample_input.txt')
    input_path = os.path.join(os.path.dirname(__file__), '06_input.txt')
    
    # # get homework
    # homework_data = parse_input(input_path)

    # #iterate over columns
    # #print (homework_data)
    # row_count = len(homework_data)
    # col_count = len(homework_data[0]) if row_count > 0 else 0
    # summed_result = 0

    # # iterate acoss homework 
    # for col in range(col_count):
    #     operation = homework_data[row_count-1][col]
    #     current_problem_value = 0
    #     if operation == "+":
    #         # iterate over rows:
    #         for row in range(row_count-1):
    #             current_problem_value += int(homework_data[row][col])
        
    #     elif operation == "*":
    #         # iterate over rows:
    #         current_problem_value = 1
    #         for row in range(row_count-1):
    #             current_problem_value *= int(homework_data[row][col])
    #     else:
    #         print(f"Unknown operation '{operation}' in column {col}")
    #         continue
        
    #     # add to summed result
    #     summed_result += current_problem_value
    
    # print(f"Summed result of all columns: {summed_result}")
        
    # calculate string length matrix
    # calculate max value

    # Start with max {length}- decrement
    #     for each one of {length}
    #         concatinate the last char into an int, add it to the operand list
    
    # length_matrix = [[len(cell) for cell in row] for row in homework_data]
    # # remove last row (operations)
    # length_matrix = length_matrix[:-1]

    # total_new_cephlapod_result = 0
    # print ("---")
    # for r in homework_data:    print (r)
    # print ("---")
    # for r in length_matrix:    print (r)
    # print ("---")
    
    # # iterate over lengths_matrix as a proxy
    # for col in range(col_count):
        
    #     # find max length in column
    #     max_length = max(length_matrix[row][col] for row in range(row_count-1))
    #     operands = []

    #     current_length = max_length
    #     while current_length > 0:
                        
    #         current_number_str = ""

    #         # iterate over rows
    #         for row in range(row_count-1):

    #             # if this cel has a part of the string number in it
    #             if length_matrix[row][col] >= current_length:
    #                 current_number_str += homework_data[row][col][current_length - 1]
    #                 homework_data[row][col] = homework_data[row][col][:-1] # remove last char

    #         operands.append(int(current_number_str) if current_number_str else 0)
    #         current_length -= 1

        
    #     # now process operands with the operation
    #     operation = homework_data[row_count-1][col]

    #     print (operation, operands)


    #     if operation == "+":
    #         total_new_cephlapod_result += sum(operands)
    #     elif operation == "*":
    #         product = 1
    #         for op in operands:
    #             product *= op
    #         total_new_cephlapod_result += product
    #     else:
    #         print(f"Unknown operation '{operation}' in column {col} for new cephlapod")
    #         continue
    
    # print(f"Total result with new cephlapod string parsing: {total_new_cephlapod_result}")


    # New approach:
    raw_homework_data = new_parse_input(input_path)
    

    # calculate split points
    row_count = len(raw_homework_data)
    operand_row = raw_homework_data[row_count-1]
    col_start_points = []
    
    # iterate over the operand row:
    operators = []
    for i,char in enumerate(operand_row):
        if char in ["+","*","\n"]:
            operators.append(char)
            col_start_points.append(i)

    # print (col_start_points)        
    
    # split each column based on the split points
    new_homework_data = []
    for row in raw_homework_data[:-1]:  # exclude last row (operations)
        new_homework_data.append(convert_line_to_list("".join(row), col_start_points, remove_chars=0))
    
    print(raw_homework_data)
    print(operators)
    print(col_start_points)
    print(new_homework_data)

    # verify all columns are same width
    column_count = len(operators)
    row_count = len(new_homework_data)
    for column in range(column_count):
        print (column)
        column_width = len(new_homework_data[0][column])
        for row in range(row_count):
            if len(new_homework_data[row][column]) != column_width:
                raise ValueError(f"Row length mismatch in row {row} column {column}: expected {column_width}, got {len(new_homework_data[row][column])}: {new_homework_data[row][column]}")
    print (f"individual column widths verified. - no need to panic")


    # Process the new homework data
    total_new_cephlapod_result = 0
    result_list = [] # for debugging
    for col in range(column_count):
        operator = operators[col]
        operands = []
        char_count = len(new_homework_data[0][col])
        
        
        #iterate over character positions
        for char_index in range(char_count):
            operand = ""

            # iterate over rows to get the current number
            for row in range(row_count):

                value_char = new_homework_data[row][col][char_count-1-char_index]
                if value_char.isdigit():
                    operand = operand+value_char
            
            # add the calculated operand to the list
            if len(operand) > 0:
                operands.append(int(operand)  )
        
        # calcuate the number based on the operator
        print (operator, operands)
        if operator == "+":
            total_new_cephlapod_result += sum(operands)
            result_list.append(sum(operands))
        elif operator == "*":
            product = 1
            for op in operands:
                product *= op
            total_new_cephlapod_result += product
            result_list.append(product)
            
    print (total_new_cephlapod_result)



def convert_line_to_list(line: str, split_points: List[int], remove_chars:int=1 ) -> list[str]:
    """
    Convert a line of text into a list of strings, splitting based on given split points.
    chars before split points are removed based on the remove_chars parameter.
    
    Args:
        line (str): The line of text to convert.
        split_points (List[int]): List of indices to split the line.
        remove_chars (int): Number of characters to remove before each split point.
    """
    returned_list = []
    start=0
    for point in split_points:
    
        # handle base case:
        if not point == 0:
            
            returned_list.append(line[start:point-remove_chars])
            start = point-remove_chars
    if start < len(line):
        returned_list.append(line[start:])
    #print (returned_list)
    return returned_list
    


    
def new_parse_input(path: str) :
    """
    Parse the input file into a list of strings. one string per line.
    
    Args:
        path (str): Path to the input file.
    
    Returns:
        list[str]: List representing the input data.
    """
    print(f"Parsing input from {path}...")
    data: list[str] = []    
    try:
        with open(path, "r", encoding="utf-8") as fh:
            for line in fh:
                if line:
                    data.append(line)
    except OSError as e:
        raise FileNotFoundError(f"Unable to read file {path}: {e}")
    
    # print("Parsed data:")
    # print (data)
    return data




def parse_input(path: str) :
    """
    Parse the input file into a 2D list of strings.
    columns are separated with a space
    
    Args:
        path (str): Path to the input file.
    
    Returns:
        list[list[str]]: 2D list representing the input data.
    """
    print(f"Parsing input from {path}...")
    data: list[str] = []
    try:
        with open(path, "r", encoding="utf-8") as fh:
            for line in fh:
                stripped_line = line.strip()
                if stripped_line:
                    row = stripped_line.split()
                    data.append(row)
    except OSError as e:
        raise FileNotFoundError(f"Unable to read file {path}: {e}")
   


if __name__ == "__main__":
    main()
    