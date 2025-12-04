from typing import List
import os
import sys
from typing import Iterable, List, Optional
import re
import pandas as pd

    

class ParseAndProcess:
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
        self.rows: int = 0
        self.cols: int = 0
        self.df_paper_grid = None
        self.df_proximity_grid = None
        self.input_ranges: List[str] = []
        self.dict_proximity_count = {i: 0 for i in range(9)}
        
        
        try:
            with open(path, "r", encoding="utf-8") as fh:
                raw = fh.read()
        except OSError as e:
            raise FileNotFoundError(f"Unable to read file {path}: {e}")

        if not raw:
            return

        # the imput are equal length lines of chars eg: 
        '''
        ..@@.@@@@.
        @@@.@.@.@@
        '''
        # read in the lines and store each charecter in a pandas dataframe
        lines = raw.splitlines()
        self.rows = len(lines)
        self.cols = len(lines[0])
        grid_data = []
        for line in lines:
            grid_data.append(list(line))
        self.df_paper_grid = pd.DataFrame(grid_data)

        # create a proximity grid to count adjacent paper rolls, each cell starts at None
        proximity_data = [[None for _ in range(self.cols)] for _ in range(self.rows)]
        self.df_proximity_grid = pd.DataFrame(proximity_data)

    def get_rows(self) -> int:
        """ returns the number of rows in the paper grid.
        Args:
            None
        Returns:
            int: number of rows
        """
        return self.rows
    
    def get_cols(self) -> int:
        """ returns the number of columns in the paper grid.
        Args:
            None
        Returns:
            int: number of columns
        """
        return self.cols
    

    def get_df_paper_grid(self, row:int=None, col:int=None):
        """ returns the paper grid.
        Args:
            None
        Returns:
            pandas.DataFrame: The paper grid as a pandas DataFrame.
        """
        if row==None and col==None:
            return self.df_paper_grid
        
        if row!=None and col!=None:        
            return self.df_paper_grid.iat[row, col]
        else:
            raise ValueError("Both row and col must be provided to get a specific cell value.")


    def set_df_paper_grid(self, row:int, col:int, value=None) -> bool:
        """ set a specific cell in the paper grid.
        Args:
            row (int): row index
            col (int): column index
            value: value to set          
        Returns:
            bool: True if the value was set successfully, False otherwise.
        """
        if row!=None and col!=None:
            self.df_paper_grid.iat[row, col] = value
            return True
        else:
            return False


    def get_df_proximity_grid(self, row:int=None, col:int=None) :
        """ returns the proximity grid.
        Args:
            row (int, optional): row index
            col (int, optional): column index
        Returns:
            pandas.DataFrame: The proximity grid as a pandas DataFrame.
            or if row and col are provided, returns the value at that cell.
        """
        if row==None and col==None:
            return self.df_proximity_grid
        
        if row!=None and col!=None:        
            return self.df_proximity_grid.iat[row, col]
        else:
            raise ValueError("Both row and col must be provided to get a specific cell value.")

    

    def set_df_proximity_grid(self, row:int=None, col:int=None, value=None) -> bool:
        """ set a specific cell in the proximity grid.
        Args:
            row (int): row index
            col (int): column index
            value: value to set          
        Returns:
            bool: True if the value was set successfully, False otherwise.
        """
        if row!=None and col!=None:
            self.df_proximity_grid.iat[row, col] = value
            if value in ('0','1','2','3','4','5','6','7','8'):
                self.dict_proximity_count[int(value)] += 1
            return True
        else:
            return False
        

     
    def get_count_adjacent_paper_rolls(self, row:int, col:int) -> str:
        """ counts the number of adjacent paper rolls to the cell at (row, col).
        Args:
            row (int): row index
            col (int): column index
        Returns:
            int: number of adjacent paper rolls
        """
        adjacent_positions = [
            (row-1, col-1), (row-1, col), (row-1, col+1),
            (row, col-1),                 (row, col+1),
            (row+1, col-1), (row+1, col), (row+1, col+1)
        ]
        
        if self.df_paper_grid.iat[row, col] != '@':
            return '_'

        count = 0
        for r, c in adjacent_positions:
            if 0 <= r < self.rows and 0 <= c < self.cols:
                if self.df_paper_grid.iat[r, c] == '@':
                    count += 1
        return str(count)
    

    
    def get_count_of_cells_with_min_adjacent_rolls(self, min_rolls:int) -> int:
        """ counts the number of cells with at least min_rolls adjacent paper rolls.
        Args:
            min_rolls (int): minimum number of adjacent rolls to count
        Returns:
            int: number of cells with at least min_rolls adjacent paper rolls
        """
        total_count = 0
        for k in self.dict_proximity_count.keys():
            if k <= min_rolls:
                total_count += self.dict_proximity_count[k]
        return total_count
     

    def get_dict_proximity_count(self) -> dict:
        """ returns the dictionary of proximity counts.
        Args:
            None
        Returns:
            dict: dictionary with counts of cells by number of adjacent paper rolls
        """
        return self.dict_proximity_count