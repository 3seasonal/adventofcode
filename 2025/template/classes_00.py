from typing import List
import os
import sys
from typing import Iterable, List, Optional
import re

class DoTheThing:
    """
    A class to store the functional code.
    """


    def __init__(self):
        """ A constructor for the functional code class.
        Args:
            None
        Returns:
            None #has to always return None
        """
        self.net_count = 0
        self.net_list= []

    

class InputParser:
    """
    Helper to load and expose input .
    The constructor accepts a file path, and a type, reads the file, and creates a list of ranges.
    """
    
    def __init__(self, path: str):
        """ Initializes the parser and loads ranges from the given file path.
        Creates a list of ranges, where each range is a list of integers.

        Args:
            path (str): Path to the input file containing input.
        """
        self.path = path
        self.index = 0
        self.input_ranges: List[str] = []
        try:
            with open(path, "r", encoding="utf-8") as fh:
                raw = fh.read()
        except OSError as e:
            raise FileNotFoundError(f"Unable to read file {path}: {e}")

        if not raw:
            return

        # check what type of input we have and proces accordingly
        # - lines
        #self.input_lines = [line.strip() for line in raw.splitlines() if line.strip()]
        # - comma-separated values
        #self.input_csv = [item.strip() for item in raw.split(",") if item.strip()]
        
        # save handlers.
        self.current_index = 0


    # def has_next(self) -> bool:
    #   """ Checks if there is another thing in the input list.
    #   Args:
    #       None
    #   Returns:
    #       bool: True if there is another thing in the input list, False otherwise.
    #   """
    

    # def get_next(self) -> str:
    #   """ Returns the next thing from the input list.
    #   Args:
    #       None
    #   Returns:
    #       str: The next thing from the input list, or None if at end of list.
    #   """
     