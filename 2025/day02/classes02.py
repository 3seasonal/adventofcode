from typing import List
import os
import sys
from typing import Iterable, List, Optional
import re

class ValidatePIDs:
    """
    Validate product IDs.
    """


    def __init__(self):
        """
        Args:
            modulus: number of distinct positions on the dial (must be > 0). Default 10.
            start: initial position (int). The initial position is counted as a visit if it equals zero.
            record: if True, keeps a list of visited positions in ._visits which is exposed via .visits.
        """
        self.net_invalid_pid_count = 0
        self.net_invalid_pids: List[int] = []


    def get_invalid_pid(self, pid_list: list[int])-> list[int]:
        """
        Count invalid product IDs from a list.

        Args:
            pid_list (list[int]): The list of invalid product IDs to count.
        """
        invalid_pids = []
        
        # convert the list of int to a list of str
        str_pids = [str(pid) for pid in pid_list]

        # remove all elements in the str_pids list that have an odd number of characters
        str_pids = [pid for pid in str_pids if len(pid) % 2 == 0]

        # for each element in the list, split the string in half and compare the two halves. 
        # If they match, add then to the invalid_pids list
        for pid in str_pids:
            half_len = len(pid) // 2
            first_half = pid[:half_len]
            second_half = pid[half_len:]
            if first_half == second_half:
                invalid_pids.append(int(pid))
        
        count_invalid = len(invalid_pids)
        if count_invalid > 0:
            self.net_invalid_pid_count += count_invalid
            self.net_invalid_pids.extend(invalid_pids)

        return invalid_pids

    def get_regx_invalid_pid(self, pid_list: list[int])-> list[int]:
        """
        Count invalid product IDs from a list usign regular expressions.

        Args:
            pid_list (list[int]): The list of invalid product IDs to count.
        """
        invalid_pids = []
        
        # convert the list of int to a list of str
        str_pids = [str(pid) for pid in pid_list]

        # regex to match any string  made only of some sequence of one or more numerical digits repeated at least twice
        pattern = re.compile(r'^(\d+)\1+$')
        for pid in str_pids:
            if pattern.match(pid):
                invalid_pids.append(int(pid))
        count_invalid = len(invalid_pids)
        if count_invalid > 0:
            self.net_invalid_pid_count += count_invalid
            self.net_invalid_pids.extend(invalid_pids) 
        return invalid_pids




                

class PidParser:
    """
    Helper to load and expose product ID ranges.
    The constructor accepts a file path, reads the file, and creates a list of ranges.
    """
    
    def __init__(self, path: str):
        """ Initializes the parser and loads ranges from the given file path.
        Creates a list of ranges, where each range is a list of integers.

        Args:
            path (str): Path to the input file containing product ID ranges.
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

        # split on commas (allow surrounding whitespace and newlines), drop empties
        self.input_ranges = [part.strip() for part in re.split(r'\s*,\s*', raw.strip()) if part.strip()]

        # ranges are in the format "start-end" convert to list of lists.
        # such that "11-15" -> [11,12,13,14,15]
        self.parsed_ranges: List[List[int]] = []
        for r in self.input_ranges:
            match = re.match(r'^(\d+)-(\d+)$', r)
            if not match:
                raise ValueError(f"Invalid range format: {r}")
            start_str, end_str = match.groups()
            start, end = int(start_str), int(end_str)
            if start > end:
                raise ValueError(f"Invalid range with start > end: {r}")
            self.parsed_ranges.append(list(range(start, end + 1)))

    def get_all_ranges(self) -> List[List[int]]:
        """Returns all parsed ranges as a list of lists of integers.
        
        Args:
            None

        Returns:
            List[List[int]]: List of parsed ranges.
        """
        return self.parsed_ranges
        

    def get_range_count(self) -> int:
        """Returns the number of parsed ranges.

        Returns:
            int: The number of parsed ranges.
        """
        return len(self.parsed_ranges)


    def has_more_ranges(self) -> bool:
        """Returns True if there are more ranges to process.

        Returns:
            bool: True if more ranges are available, False otherwise.
        """
        return self.index < len(self.parsed_ranges)


    def get_next_range(self) -> List[int]:
        """Returns the next parsed range as a list of integers.

        Returns:
            List[int]: The next parsed range.
        """
        if self.index >= len(self.parsed_ranges):
            raise IndexError("No more ranges available.")

        next_range = self.parsed_ranges[self.index]
        self.index += 1
        return next_range