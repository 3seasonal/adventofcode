from typing import List
import os
import sys
from typing import Iterable, List, Optional
import re

class ValidatePIDs:
    """
    Validate product IDs.
    """


    def __init__(self)):
        """
        Args:
            modulus: number of distinct positions on the dial (must be > 0). Default 10.
            start: initial position (int). The initial position is counted as a visit if it equals zero.
            record: if True, keeps a list of visited positions in ._visits which is exposed via .visits.
        """
        self.invalid_pid_count = 0
        self.invalid_pids: List[int] = []
        

                
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
        """Returns all parsed ranges as a list of lists of integers."""
        return self.parsed_ranges
        
