from typing import List
import os
import sys
from typing import Iterable, List, Optional
import re

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
01_elf_safe.py
Advent of Code 2025 - Day 01 - puzzle 01

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

__all__ = [
    "safe_position_tracker",
    "safe_instruction_handler",
]
__author__ = "3seasonal"
__created__ = "2025-12-01"

def main():
    """
    Main function to execute the safe dial tracking and zero counting.
    """
    
    # config
    input_path = os.path.join(os.path.dirname(__file__), '01_input.txt')
    starting_position = 50
    modulus = 100
    
    # initialize tracker and instruction handler
    position_tracker = safe_position_tracker(starting_position=starting_position, modulus=modulus)
    instruction_handler = safe_instruction_handler(input_path)
    
    if has_instructions:
        while instruction_handler.has_instructions():
            instruction = instruction_handler.get_next_instruction()
            if instruction is not None:
                position_tracker.move(instruction)
        print (f"Total zero positions encountered: {position_tracker.get_zero_count()}")
        
    
    
    class safe_position_tracker:
        """
        Tracks a circular dial position and counts how many times it points to zero.

        Args:
          modulus: number of distinct positions on the dial (must be > 0). Default 10.
          start: initial position (int). The initial position is counted as a visit if it equals zero.
          record: if True, keeps a list of visited positions in ._visits which is exposed via .visits.
        """
        self.zero_count = 0
        self.current_position = 0
        self.modulus = 100
    
        def __init__(self, starting_position: int = 50, modulus: int = 100):
            if modulus <= 0:
                raise ValueError("Modulus must be greater than zero.")
            self.modulus = modulus
            self.current_position = starting_position % modulus
            return self.zero_count
        
        def move(self, instruction: str) -> int:
            """Moves the dial according to the instruction and updates zero count if needed.
            
            Instruction format: "<direction> <steps>"
            where <direction> is either "L" or "R", and <steps> is a positive integer.
            Left decreases position, Right increases position.
            """
            # validarte instruction format
            match = re.match(r'^(L|R)\s+(\d+)$', instruction)
            if not match:
                raise ValueError(f"Invalid instruction format: {instruction}")
            
            direction, steps_str = match.groups()
            steps = int(steps_str)
            
            # turn the dial
            if direction == "L":
                self.current_position = (self.current_position - steps) % self.modulus
            elif direction == "R":
                self.current_position = (self.current_position + steps) % self.modulus
            
            if self.current_position == 0:
                self.zero_count += 1
            
            return self.zero_count
            
        def get_zero_count(self) -> int:
            """Returns the number of times the dial has pointed to zero."""
            return self.zero_count
            
            
                    
    class safe_instruction_handler:
        """
        Helper to load and expose safe instructions from a txt file path.
        The constructor accepts a file path, reads the file, and stores parsed lines as items in a list.
        """
        
        self.instruction_list = []
        self.path = None
        
        def __init__(self, path: str):
            self.path = path
            self.instruction_list = self.load_instructions()
            return len(self.instruction_list)
            
        def load_instructions(self) -> List[str]:
            """Loads instructions from the file at self.path and returns them as a list of strings."""
            if not os.path.isfile(self.path):
                raise FileNotFoundError(f"File not found: {self.path}")
            with open(self.path, 'r') as file:
                instruction_list = [line.strip() for line in file if line.strip()]
            return instruction_list
        
        def get_next_instruction(self) -> str:
            """Returns the next instruction from the list and pop the item."""
            if len(self.instruction_list) == 0:
                return None
            return self.instruction_list.pop(0) if self.instruction_list else None
        
        def has_instructions(self) -> bool:
            """Returns True if there are more instructions to process."""
            return len(self.instruction_list) > 0


if __name__ == "__main__":
    main()
    
