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
    def __init__(self0):
        pass
    
        
                
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
        return len(self.instruction_list) > 0
