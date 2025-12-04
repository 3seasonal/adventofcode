#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from classes01 import Safe_Position_Tracker as spt
from classes01 import Safe_Instruction_Handler as sih
"""

01_elf_safe.py
Advent of Code 2025 - Day 01

- Project: adventofcode
- Year: 2025
- Day: 01
- Puzzle: 01
- File: 01_elf_safe.py
- Description: counting the number of times the safe dial points to zero
- Author: 3seasonal
- Created: 2025-12-01
- License: MIT (SPDX: MIT)

Notes:
- By no means is this a good example of clean code structure. It is intended to be a quick-and-dirty
  solution to the puzzle, with minimal dependencies.
- If you are reading this. Sorry.

Solution approach:
- use a 'safe_instruction_handler' class to manage the input data and provide easy access to parsed instructions
- use a 'safe_position_tracker' class to track the dial pointer and count zero positions
- main function to tie everything together and output the result 
"""

__author__ = "3seasonal"
__created__ = "2025-12-01"


def main():
    """
    Main function to execute the safe dial tracking and zero counting.
    """
    
    # config

    #input_path = os.path.join(os.path.dirname(__file__), '01_sample_input.txt')
    input_path = os.path.join(os.path.dirname(__file__), '01_input.txt')
    starting_position = 50
    modulus = 100
    
    # initialize tracker and instruction handler
    position_tracker = spt(starting_position=starting_position, modulus=modulus)
    instruction_handler = sih(input_path)
    
    while instruction_handler.has_instructions():
        instruction = instruction_handler.get_next_instruction()
        if instruction is not None:
            position_tracker.move(instruction)
            
    print ("--")            
    print (f"Total zero positions encountered: {position_tracker.get_zero_count()}")
    print (f"Total instructions processed: {position_tracker.get_instruction_count()}")
    print (f"Total traversals past zero: {position_tracker.get_traverse_zero_count()}")
    print (f"Final dial position: {position_tracker.get_current_position()}")

if __name__ == "__main__":
    main()
    
