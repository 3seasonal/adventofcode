from typing import List
import os
import sys
from typing import Iterable, List, Optional
import re

from pyparsing import col

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
            


    def start_calc_values(self, map: List[List[str]]) -> None:
        """ Calculates values on the map.
        Args:
            map (List[List[str]]): 2d grid of characters.  
        """
        self.vals_map = map
        for col in range (len(self.vals_map[0])):
            # expect only one
            if self.vals_map[0][col] == "S":
                self.calc_value(0, col, 1)

        #summ last line
        last_array = self.vals_map[len(self.vals_map)-1]
        self.print_map(self.vals_map)
        return sum(int(v) for v in last_array if v.isdigit())



    def row_scan(self, map: List[List[str]] ) -> int:
        self.scanned_map = map
        for i in range(len(self.scanned_map)):
            if i % 2 == 1:
                # even row

                print (self.scanned_map[i-2])
                print (self.scanned_map[i-1])
                #print (self.scanned_map[i])


                # scan the row
                for col in range (len(self.scanned_map[i])):
                                          
                    # check for beam
                    if self.scanned_map[i][col] == "|":
                        value = 0
                        
                        # base case
                        if self.scanned_map[i-1][col]=="S":
                            value = 1

                        # check above
                        if self.scanned_map[i-1][col]=="|":
                            value += int(self.scanned_map[i-2][col])

                        # check left
                        if col-1 >= 0: #valid col
                            if self.scanned_map[i-1][col-1]=="^":
                                if self.scanned_map[i-2][col-1].isdigit():
                                    value += int(self.scanned_map[i-2][col-1])
                                # else is an unused splitter

                        # check right
                        if col+1 < len(self.scanned_map[i]): #valid col
                            if self.scanned_map[i-1][col+1]=="^":
                            
                                if self.scanned_map[i-2][col+1].isdigit():
                                    value += int(self.scanned_map[i-2][col+1])
                                # else is an unused splitter    
                            
                        self.scanned_map[i][col] = str(value)

        return sum(int(v) for v in self.scanned_map[len(self.scanned_map)-1] if v.isdigit())



    def calc_value(self, row, col, increment_value):
        print((f"calc_value({row}, {col}, {increment_value})"))

        # exit contition
        if row > len(self.vals_map)-1:
            return
        
        if self.vals_map[row][col] == "S":
            # set the number
            self.vals_map[row+1][col] = str(increment_value)
            self.calc_value(row+2, col, increment_value)
            
        # value is a beam
        if self.vals_map[row][col] == "|":
            down_increment_value = increment_value
            if self.vals_map[row+1][col].isdigit():
                down_increment_value = down_increment_value + int(self.vals_map[row+1][col])
            self.vals_map[row+1][col] = str(down_increment_value)
            self.calc_value(row+2, col, down_increment_value)

        # value is a splitter
        if self.vals_map[row][col] == "^":
            #left side
            left_increment_value = increment_value
            if self.vals_map[row+1][col-1].isdigit():
                left_increment_value = left_increment_value + int(self.vals_map[row+1][col-1])
            self.vals_map[row+1][col-1] = str(left_increment_value)
            self.calc_value(row+2, col-1, left_increment_value)

            # right branch
            right_increment_value = increment_value
            if self.vals_map[row+1][col+1].isdigit():
                right_increment_value = right_increment_value + int(self.vals_map[row+1][col+1])
            self.vals_map[row+1][col+1] = str(right_increment_value)
            self.calc_value(row+2, col+1, right_increment_value)

  

        

    def start_traverse_sum_branches(self, newmapt: List[List[str]]) -> int:

        """ Starts the new traversal from the starting point 'S'.
        Args:
            newmapt (List[List[str]]): 2d grid of characters.  
        """
        self.newmap = newmapt
        for col in range(len(self.newmap[0])):
            # expect only one
            if self.newmap[0][col] == "S":
                traversal_count =  self.sum_branches (2, col, 0)
                print (r"\n")
                return traversal_count


    def sum_branches(self, row, col, count):

        # if we are beyond the last row, we have a complete traversal
        if (row == len(self.newmap)):
            return 1

        x = self.newmap[row][col]

        # if there is no splitter:  
        if x == "|":
            return self.sum_branches(row+2, col, count)

        # if there is a splitter:
        if x == "^":
            return self.sum_branches(row+2, col-1, count) + self.sum_branches(row+2, col+1, count)
            count = self.sum_branches(row+2, col+1, count) # right branch



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
            if count % 1000000 == 0:
                #print(f"({row},{col}), ", end="")
                print (".", end="")
                #flush output
                sys.stdout.flush()

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
        self.map_calcs = map.copy()
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