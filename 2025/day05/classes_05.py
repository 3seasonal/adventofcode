from typing import List
import os
import sys
from typing import Iterable, List, Optional
import re
import numpy as np

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
        self.items: List[int] = []
        self.item_cursor_unique: int = 0
        self.item_cursor: int = 0
        self.fresh_items: List[(int)] = []
        try:
            with open(path, "r", encoding="utf-8") as fh:
                raw = fh.read()
        except OSError as e:
            raise FileNotFoundError(f"Unable to read file {path}: {e}")

        if not raw:
            return

        # read in line by line and remove any blank lines.
        input_lines = [line.strip() for line in raw.splitlines() if line.strip()]

        # iterate through lines.
        print (f"Parsing {len(input_lines)} input lines...")
        for line in input_lines:
            # if the line is not blank or None:
            #print (line)
            if line:
                if len(line) > 0:

                    # if the line contains "-" it is a range.
                    # save range as a list of tuples representing start and end.
                    if line.__contains__("-"):
                        parts = line.split("-")
                        start = int(parts[0])
                        end = int(parts[1])
                        self.fresh_items.append((start, end))
                    
                    # else the line is a single item (not a range)
                    # add the line to the items list as a string.
                    else:
                        self.items.append(int(line))

        # calculate unique items by converting to a set and back to a list.
        self.items_unique = list(set(self.items))
        self.fresh_items_unique = list(set(self.fresh_items))

        # report on the number of items loaded.
        print(f"Loaded {len(self.items)} items - {len(self.items_unique)} unique")
        print(f"noted {len(self.fresh_items)} items in fresh items in range - {len(self.fresh_items_unique)} unique") 


    def more_items(self, unique: bool = False) -> bool:
        """ Checks if there is another item in the input list.
        Args:
            None
        Returns:
            bool: True if there is another thing in the input list, False otherwise.
        """
        if unique:
            if self.item_cursor_unique < len(self.items_unique):
                return True
            return False
        if self.item_cursor < len(self.items):
            return True
        return False

    def item_is_fresh(self, item: int, unique: bool = False) -> bool:
        """ Checks if the given item is in the fresh items list.
        Args:
            item (int): The item to check.
        Returns:
            bool: True if the item is in the fresh items list, False otherwise.
        """
        if unique:
            for fr in self.fresh_items_unique:
                if item >= fr[0] and item <= fr[1]:
                    return True
            return False
        for fr in self.fresh_items:
            if item >= fr[0] and item <= fr[1]:
                return True
        return False


    def consolidate_fresh_items(self):
        """ Consolidates the fresh items list by merging overlapping ranges.
        Args:
            None
        Returns:
            None
        """
        # sort the fresh items by start value
        self.fresh_items.sort(key=lambda x: x[0])
        consolidated = []
        current_start, current_end = self.fresh_items[0]

        for start, end in self.fresh_items[1:]:
            if start <= current_end:  # overlap
                current_end = max(current_end, end)
            else:
                consolidated.append((current_start, current_end))
                current_start, current_end = start, end
                
        consolidated.append((current_start, current_end))
        self.fresh_items = consolidated


    def get_consolidated_fresh_items(self) -> List[(int)]:
        """ Returns the consolidated fresh items list.
        Args:
            None
        Returns:
            List[(int)]: The consolidated fresh items list.
        """
        return self.fresh_items

    
    def get_next_item(self, unique: bool = False) -> Optional[int]:
        """ Returns the next item from the input list.
        Args:
            unique (bool): If True, returns the next unique item. Defaults to False.
        Returns:
            Optional[str]: The next item from the input list, or None if at end of list.
        """
        if unique:
            if self.item_cursor_unique < len(self.items_unique):
                item = self.items_unique[self.item_cursor_unique]
                self.item_cursor_unique += 1
                return item
            return None
        else:
            if self.item_cursor < len(self.items):
                item = self.items[self.item_cursor]
                self.item_cursor += 1
                return item
            return None

    def get_fresh_items(self, unique: bool = False) -> List[int]:
        """ Returns the list of fresh items.
        Args:
            None
        Returns:
            List[int]: The list of fresh items.
        """
        if unique:
            return self.fresh_items_unique
        return self.fresh_items

   