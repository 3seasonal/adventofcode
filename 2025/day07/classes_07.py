from typing import List
import os
import sys
from typing import Iterable, List, Optional
import re

class DoTheThing:
    """
    A class to store the functional code.
    """


    def print_map(self, map: List[List[str]]) -> None:
        """ Prints the map to the console.

        Args:
            map (List[List[str]]): 2d grid of characters.
        """
        for row in map:
            print("".join(row)) 
            




    def start_traverse(self, mapt: List[List[str]]) -> int:
        """ Starts the traversal from the starting point 'S'.
        Args:
            mapt (List[List[str]]): 2d grid of characters.  
        """
        self.mapt = mapt
        for col in range(len(self.mapt[0])):
            # expect only one
            if self.mapt[0][col] == "S":
                traversal_count =  self.traverse (2, col, 0)
                print (r"\n")
                return traversal_count
            

    def traverse(self, row, col, count):
        """ Traverses the map recursively.
        Left depth-first search.

        Args:
            row (int): current row
            col (int): current column
            count (int): current count of traversals
        Returns:   
            int : total count of traversals    
        """

        #print ((row, col), count)
        #print (len(self.mapt), len(self.mapt[0]))

        # complete traversal
        if (row == len(self.mapt)):
            # show progress
            if count % 1000 == 0:
                print(".", end="")

            return (count + 1)

        tree_char = self.mapt[row][col]

        # if there is no splitter:  
        if tree_char == "|":
            count = self.traverse(row+2, col, count)

        # if there is a splitter:
        if tree_char == "^":
            count = self.traverse(row+2, col-1, count) # left branch
            count = self.traverse(row+2, col+1, count) # right branch
        
        return count






    def simulate_tacheon_beams(self, map: List[List[str]]) -> int:
        """ Simulates the tacheon beams on the map.
        Looks in the first row for the 'S' character, and shoots beams downwards.
        Args:
            map (List[List[str]]): 2d grid of characters.

        Returns:
            int: The number of tacheon beams that hit a target.
        """
        self.net_beam_count: int = 0
        self.net_split_count: int = 0
        self.map = map
        # before
        self.print_map(self.map)
        for col in range(len(self.map[0])):
            if self.map[0][col] == 'S':
                
                # shoot beam to the next row
                self._shoot_beam( 1, int(col))
        
        # after
        self.print_map(self.map)
        print (f"total splits: {self.net_split_count}")
        return self.net_beam_count

    def _shoot_beam(self, row: int, col: int):
        """ Shoots a beam downwards from the given position.

        Args:
            map (List[List[str]]): 2d grid of characters.
            row (int): The starting row.
            col (int): The starting column.

        Returns:
            int: the number of beams fired
        """
        # handle exit cases 
        if row >= len(self.map):
            # we have reached the end
            return
        
        char = self.map[row][col]
        
        if char == '|':
            # beam is already here, stop
            return
        
        if char == '.':
            # empty space, continue beam
            self.map[row][col] = '|'
            self.net_beam_count += 1
            self._shoot_beam(row + 1, col)
                    
        if char == '^':
            # splitter, shoot both ways
            self.net_split_count += 1
            if col - 1 >= 0:
                self._shoot_beam(row + 1, col - 1)
            if col + 1 < len(self.map[0]):
                self._shoot_beam(row + 1, col + 1)
        
        return 

class InputParser:
    """
    Helper to load and expose input .
    The constructor accepts a file path, and a type, reads the file, and creates a list of ranges.
    """
    
    def __init__(self, path: str):
        """ Initializes the parser and loads a 2d grid of characters.

        Args:
            path (str): Path to the input file containing input.
        """
        self.path: str = path
        self.map: List[List[str]] = []
        try:
            with open(self.path, "r", encoding="utf-8") as fh:
                raw = fh.read()
        except OSError as e:
            raise FileNotFoundError(f"Unable to read file {self.path}: {e}")

        if not raw:
            return
        self.map = [list(line) for line in raw.splitlines()]
    

    def get_map(self) -> List[List[str]]:
        """ Returns the 2d grid of characters.

        Returns:
            List[List[str]]: 2d grid of characters.
        """
        return self.map