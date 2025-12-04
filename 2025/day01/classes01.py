from typing import List
import os
import sys
from typing import Iterable, List, Optional
import re

class Safe_Position_Tracker:
    """
    Tracks a circular dial position and counts how many times it points to zero.

    Args:
        modulus: number of distinct positions on the dial (must be > 0). Default 10.
        start: initial position (int). The initial position is counted as a visit if it equals zero.
        record: if True, keeps a list of visited positions in ._visits which is exposed via .visits.
    """
    # Counters semantics:
    # - zero_count: number of times the dial RESTS on position 0 after a move.
    # - traverse_zero_count: number of times the dial PASSES over position 0 during moves.
    #   This excludes the case where a move ends exactly on 0 (that landing is counted in
    #   `zero_count` but not in `traverse_zero_count`).
    def __init__(self, starting_position: int = 50, modulus: int = 100):
        if modulus <= 0:
            raise ValueError("Modulus must be greater than zero.")
        # instance-level state (avoid shared class attributes)
        self.modulus = modulus
        self.current_position = starting_position % modulus
        self.zero_count = 0
        self.traverse_zero_count = 0
        self.instruction_count = 0
        
    
    def move(self, instruction: str) -> int:
        """Moves the dial according to the instruction and updates zero count if needed.
        
        Instruction format: "<direction><steps>"
        where <direction> is either "L" or "R", and <steps> is a positive integer.
        Left decreases position, Right increases position.

                Returns: 
                        int: the number of instructions processed so far (`instruction_count`).

                Semantics summary:
                - `zero_count` is incremented when the new `current_position` equals 0 (a rest-on-zero).
                - `traverse_zero_count` counts how many times the dial passed over 0 during the move,
                    excluding a final landing on 0 (the landing is not considered a "pass").
                - Example: starting at position 7 in modulus 10, `R3` results in landing at 0.
                    That increases `zero_count` by 1 and does NOT increase `traverse_zero_count`.
        """
        # validarte instruction format
        match = re.match(r'^(L|R)(\d+)$', instruction)
        if not match:
            raise ValueError(f"Invalid instruction format: {instruction}")
        
        direction, steps_str = match.groups()
        steps = int(steps_str)
        zeros_this_move = 0
        
        
        # turn the dial 
        previous_position = self.current_position
        if direction == "L":
            self.current_position = (previous_position - steps) % self.modulus
          
        elif direction == "R":
            self.current_position = (previous_position + steps) % self.modulus
                           
        # update counts
        self.instruction_count += 1
        
        
        # check if we traversed past zero
        # For a right move the number of times we cross the 0 boundary is
        # floor((previous_position + steps) / modulus).
        # For a left move it is floor((steps - previous_position + modulus) / modulus).
        if direction == "R":
            traversed_zeros = (previous_position + steps) // self.modulus
        else:  # direction == "L"
            traversed_zeros = ((self.modulus - previous_position) + steps) // self.modulus

        # edge case handling:
        if previous_position == 0 and traversed_zeros > 0:
            traversed_zeros -= 1

        # If the move ended exactly on zero, use the traversal count only 
        if traversed_zeros > 0:
            zeros_this_move = traversed_zeros
        else:
            # check if we are pointing at zero
            if self.current_position == 0:
                zeros_this_move = 1
        self.zero_count += zeros_this_move
        
        # accumulate traversals
        #self.traverse_zero_count += traversed_zeros

        print(f"Moved {instruction}: zeros  = {zeros_this_move}    ({previous_position} -> {self.current_position})")
        # return the number of times the dial has pointed to zero (previous behavior)
        return self.instruction_count
        
        
    def get_zero_count(self) -> int:
        """Returns the number of times the dial has pointed to zero."""
        return self.zero_count
    
    def get_current_position(self) -> int:
        """Returns the current position of the dial."""
        return self.current_position
    
    def get_instruction_count(self) -> int:
        """Returns the number of instructions processed."""
        return self.instruction_count
    
    def get_traverse_zero_count(self) -> int:
        """Returns the number of times the dial has traversed past zero."""
        return self.traverse_zero_count
        
                
class Safe_Instruction_Handler:
    """
    Helper to load and expose safe instructions from a txt file path.
    The constructor accepts a file path, reads the file, and stores parsed lines as items in a list.
    """
    
    def __init__(self, path: str):
        self.path = path
        self.instruction_list: list[str] = self.load_instructions()
        
        
    def load_instructions(self) -> list[str]:
        """Loads instructions from the file at self.path and returns them as a list of strings."""
        if not os.path.isfile(self.path):
            raise FileNotFoundError(f"File not found: {self.path}")
        with open(self.path, 'r') as file:
            instruction_list = [line.strip() for line in file if line.strip()]
        return instruction_list
    
    def get_next_instruction(self) -> Optional[str]:
        """Returns the next instruction from the list and pop the item."""
        if len(self.instruction_list) == 0:
            return None
        return self.instruction_list.pop(0) if self.instruction_list else None
    
    def has_instructions(self) -> bool:
        """Returns True if there are more instructions to process."""
        return len(self.instruction_list) > 0
