from typing import List
import os
import sys
from typing import Iterable, List, Optional
import re

class JoltageCalculator:
    """
    Functions to help calculate the maximum battery capacity from a list of battery bank configurations.

    Args:
        None
    Returns:
        None
    """
    #
    def __init__(self):
        self.total_joltage = 0
        
    
    def accumulate_joltage(self, joltage:int) -> int:
        """Accumulates the given joltage to the total and returns the new total."""
        self.total_joltage += joltage
        return self.total_joltage
    
    def get_total_joltage(self) -> int:
        """Returns the current total joltage."""
        return self.total_joltage

    def get_max_joltage_from_subbank(self, length:int, subbank:str) -> tuple[str, int] :
        """Recursively finds the maximum joltage from a subbank string of given length.
        Args:
            length (int): The length of the subbank to consider.
            subbank (str): The string representation of the battery bank.
        Returns:
            tuple[str, int]: A tuple containing the maximum joltage string and the character position.
        """
        if length > 1:
            returned_joltage, char_position = self.get_max_joltage_from_subbank(length-1, str(subbank[:-1]))
        else:
            char_position = -1
            returned_joltage = ""
        
        bank = [int(char) for char in subbank[char_position+1:]]
        max_value = max(bank)
        pos = bank.index(max_value)+char_position+1
        returned_joltage =  returned_joltage + str(max_value)
        
        return (returned_joltage, pos)
        
    
class BatteryBank:
    """
    A parser to handle the battery bank configuration instructions from a file.
    """
    
    def __init__(self, path: str):
        self.path = path
        self.bank_list: list[str] = self.load_banks()
        
        
    def load_banks(self) -> list[str]:
        """Loads battery bank configurations from the file at self.path and returns them as a list of strings."""
        if not os.path.isfile(self.path):
            raise FileNotFoundError(f"File not found: {self.path}")
        with open(self.path, 'r') as file:
            bank_list = [line.strip() for line in file if line.strip()]
        return bank_list
    
    def get_next_bank(self) -> Optional[str]:
        """Returns the next bank configuration from the list and pop the item."""
        if len(self.bank_list) == 0:
            return None
        return self.bank_list.pop(0) if self.bank_list else None
    
    def has_banks(self) -> bool:
        """Returns True if there are more banks to process."""
        return len(self.bank_list) > 0
