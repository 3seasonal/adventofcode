from typing import List
import os
import sys
from typing import Iterable, List, Optional
import re
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

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

    def visualise_coords(self, input_matrix: List[list[int]]) -> None:
        """ Visualizes the input matrix as a grid.
        Args:
            input_matrix (List[list[int]]): A list of lists representing the input matrix.
        Returns:
            None
        """ 
        #print (input_matrix)
        print (f"Visualising {len(input_matrix)} coordinates...")
        if not input_matrix:
            return

        # Extract x, y, z coordinates
        coords = np.array(input_matrix)
        x, y, z = coords[:, 0], coords[:, 1], coords[:, 2]

        # Create 3D scatter plot
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(x, y, z)

        # Crop to content by setting limits to data ranges
        ax.set_xlim(x.min(), x.max())
        ax.set_ylim(y.min(), y.max())
        ax.set_zlim(z.min(), z.max())

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        plt.savefig('/tmp/coordinates_plot.png')
        print("Plot saved to /tmp/coordinates_plot.png")
        plt.close()



class calcs:
    """
    A helper class for calculations.
    """
    def __init__(self, matrix:  List[list[int]]):
        """ A constructor for the calculations helper class.
        Args:
            None
        Returns:
            None #has to always return None
        """
        self.matrix = matrix
        self.matrix_dict = {i: point for i, point in enumerate(matrix)}
        self.eucalidean_dict= {}
        self.circuit_list = []

    


    def calculate_euclidean_distance(self, point1: int, point2: int) -> float:
        """ Calculates the Euclidean distance between two points in 3D space.
        takes the indexes of the points in the matrix_dict.
        returns the distance as a float, 0, or None.

        Args:
            point1 (List[int]): The first point as a list of three integers [x1, y1, z1].
            point2 (List[int]): The second point as a list of three integers [x2, y2, z2].
        Returns:

            float: The Euclidean distance between the two points.
        """

        # check if the the points are either the same
        if point1 == point2:
            return 0.0
         
        # check if we have already calculated this distance
        if (point1, point2) in self.eucalidean_dict or (point2, point1) in self.eucalidean_dict:
            return None
        
        # calcualte and store the distance
        p1 = self.matrix_dict[point1]
        p2 = self.matrix_dict[point2]
        eculidean_distance = ((p1[0] - p2[0]) ** 2 + 
                (p1[1] - p2[1]) ** 2 + 
                (p1[2] - p2[2]) ** 2) ** 0.5 
        
        self.eucalidean_dict[point1, point2] = eculidean_distance
        return eculidean_distance



    def build_euclidean_dict(self) -> dict:
        """ Builds the Euclidean distance dictionary for all points in the matrix.
        calls the calculate_euclidean_distance method for each unique point pair.
        saves the results in the eucalidean_dict usign the point indices as keys.
        sorts the dictionary by distance descending, such that the closest points are first.

        Args:
            None
        Returns:
            None
        """

        # iterate over all unique point pairs and calculate distances
        num_points = len(self.matrix_dict)
        print (f"Building Euclidean distance dictionary for {num_points} points...")
        count = 0
        calcuated = 0
        for i in range(num_points):
            for j in range(i + 1, num_points):
                count += 1
                ed = self.calculate_euclidean_distance(i, j)
                if ed is not None:
                    if ed != 0.0:
                        self.eucalidean_dict[i, j] = ed
                        calcuated += 1

        print (f"Calculated {calcuated} distances out of {count} point pairs.")
        # sort the distance dictionary by distance descending
        self.eucalidean_dict = dict(sorted(self.eucalidean_dict.items(), key=lambda item: item[1], reverse=False))
        return self.eucalidean_dict


    def build_cuircuit_list(self, sorted_distance_matrix, max_connections:int):
        """ takes the sorted dictionary of distances and builds a list of circuits by connecting closest poitns
        Args:
            sorted_distance_matrix (np.ndarray): A 2D numpy array representing the sorted Euclidean distance matrix.
            max_connections (int): max no of connections considerd
        Returns:
            List[tuple[int, int]]: A list of tuples representing the circuits.
        """
        connections = 0
        while (connections < max_connections):

            # pop the first item in the dictionary (with smallest distance)
            last_key = list(sorted_distance_matrix)[-1]
            print (f"distance: {sorted_distance_matrix.pop(last_key)}")
            point1, point2 = last_key

            # Both points already connected?
            if any(point1 in circuit and point2 in circuit for circuit in self.circuit_list):
                print ("Both points already connected?")

            # One point already connected?
            elif any(point1 in circuit or point2 in circuit for circuit in self.circuit_list):
                print ("One point already connected?")
                # add the other point to the circuit list containing the other point
                for circuit in self.circuit_list:
                    if point1 in circuit:
                        for circuit2 in self.circuit_list:
                            if point2 in circuit2:
                                # both points already in different circuits, merge them
                                print ("Both points already in different circuits")
                            else:

'''

Need to review this logic
write the algorith first

'''

                        circuit.append(point2)
                    elif point2 in circuit:
                        circuit.append(point1)
                    else:
                        #print ("Error: point not found in any circuit?")
                        pass
                connections += 1
                    
            else:
            # Neither point connected?
                # add both points to a new circuit list
                self.circuit_list.append([point1, point2])
                connections += 1

            # add all remainning points as individual circuits
            for point in self.matrix_dict.keys():
                if not any(point in circuit for circuit in self.circuit_list):
                    self.circuit_list.append([point])


    def print_cuircuit_list(self):
        """ prints the circuit list to stdout.
        Args:
            None
        Returns:
            None
        """
        print ("Circuit List:")
        lengths = []
        for i, circuit in enumerate(self.circuit_list):
            print (f"Circuit {i}: length: {len(circuit)}. Points: {circuit}")
            lengths.append(len(circuit))

        # multiply the top three lengths together
        lengths.sort(reverse=True)
        if len(lengths) >= 3:
            result = lengths[0] * lengths[1] * lengths[2]
            print (f"Top three lengths multiplied together: {lengths[0]} * {lengths[1]} * {lengths[2]} = {result}")
        


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
        print (f"Loading input from {path}...")
        self.path = path
        self.index = 0
        self.input_matrix: List[list[int]] = []
        try:
            with open(path, "r", encoding="utf-8") as fh:
                raw = fh.read()
        except OSError as e:
            raise FileNotFoundError(f"Unable to read file {path}: {e}")

        # parse input into list of ranges
        self.input_matrix = [list(map(int, line.split(','))) for line in raw.strip().split('\n')]
        
        # calculate the max and min values for each axis
        self.max_values = [max(col) for col in zip(*self.input_matrix)]
        self.min_values = [min(col) for col in zip(*self.input_matrix)]

        # save handler state
        self.current_index = 0
        print (f"Loaded {len(self.input_matrix)} input coordinates.")


    def has_next(self) -> bool:
      """ Checks if there is another thing in the input list.
      Args:
          None
      Returns:
          bool: True if there is another thing in the input list, False otherwise.
      """
      while self.current_index < len(self.input_matrix):
          return True
    
    def get_min_max(self) -> tuple[list[int], list[int]]:
        """ Returns the min and max values for each axis.
        Args:
            None
        Returns:
            tuple[list[int], list[int]]: A tuple containing two lists - the minimum values and maximum values for each axis.
        """
        return self.min_values, self.max_values

    def get_next(self) -> str:
        """ Returns the next thing from the input list.
        Args:
            None
        Returns:
            str: The next thing from the input list, or None if at end of list.
        """
        if self.has_next():
            coords = self.input_matrix[self.current_index]
            self.current_index += 1
            return coords
        return None
    
    def get_matrix(self) -> List[list[int]]:
        """ Returns the entire input matrix.
        Args:
            None
        Returns:
            List[list[int]]: The entire input matrix.
        """
        return self.input_matrix