#!/usr/bin/env python3

# Attention: Do not import the ev3dev.ev3 module in this file
from enum import IntEnum, unique
from typing import Optional, List, Tuple, Dict


@unique
class Direction(IntEnum):
    """ Directions in shortcut """
    NORTH = 0
    EAST = 90
    SOUTH = 180
    WEST = 270


Weight = int
"""
Weight of a given path (received from the server)

Value:  -1 if blocked path
        >0 for all other paths
        never 0
"""

Node = Tuple[int, int]
"""
Node represented by a tuple of two integers

First integer: x-coordinate
Second integer: y-coordinate
"""

OutgoingPaths = Dict[Direction, Tuple[Node, Direction, Weight]]
"""
Dictionary with all paths starting at a Node

Key: Direction of the path
Value: Tuple with (End-)Node, (End-)Direction and Weight of the path
"""

ShortestPath = List[Tuple[Node, Direction]]
"""
Path represented by a list of tuples, each with a Node and a Direction
"""

class Planet:
    """
    Contains the representation of the map and provides certain functions to manipulate or extend
    it according to the specifications
    """

    # DO NOT EDIT THE METHOD SIGNATURE
    def __init__(self):
        """ Initializes the data structure """
        self.paths = {} #In diesem Dic speichern wir alle Knoten und die von ihnen ausgehenden Wege.

    # DO NOT EDIT THE METHOD SIGNATURE
    def add_path(self, start: Tuple[Node, Direction], target: Tuple[Node, Direction],
                 weight: Weight):
        """
         Adds a bidirectional path defined between the start and end coordinates to the map and assigns the weight to it

        Example:
            add_path(((0, 3), Direction.NORTH), ((0, 3), Direction.WEST), 1)
        :param start: 2-Tuple
        :param target:  2-Tuple
        :param weight: Integer
        :return: void
        """
        # YOUR CODE FOLLOWS (remove pass, please!)
        
        #start_node ist die Position und start_direction ist die Direction dafür
        start_node , start_direction = start
        #Ziel Informationen:
        target_node , target_direction = target
        #Überprüfen des Existenz des Startknotens im paths:
        if start_node not in self.paths:
            self.paths[start_node]={}
        #Target Node mit bestimmten Distanz im Path hinzufügen
        self.paths[start_node][start_direction] = (target_node, target_direction, weight)    
        #Wir schreiben jetzt den Weg in andere Richtung:
        if target_node not in self.paths:
            self.paths[target_node] = {}
        #update reverse value
        reverse_direction_value = (start_direction.value + 180) % 360
        reverse_direction = Direction(reverse_direction_value)
        #Den Rückweg im Path hinzufügen:
        self.paths[target_node][reverse_direction] = (start_node, start_direction, weight)    



    # DO NOT EDIT THE METHOD SIGNATURE
    def get_paths(self) -> Dict[Node, OutgoingPaths]:
        """
        Returns all paths

        Example:
            {
                (0, 3): {
                    Direction.NORTH: ((0, 3), Direction.WEST, 1),
                    Direction.EAST: ((1, 3), Direction.WEST, 2),
                    Direction.WEST: ((0, 3), Direction.NORTH, 1)
                },
                (1, 3): {
                    Direction.WEST: ((0, 3), Direction.EAST, 2),
                    ...
                },
                ...
            }
        :return: Dict
        """

        # YOUR CODE FOLLOWS (remove pass, please!)
        return self.paths

    # DO NOT EDIT THE METHOD SIGNATURE
    def shortest_path(self, start: Node, target: Node) -> Optional[ShortestPath]:
        """
        Returns a shortest path between two nodes

        Examples:
            shortest_path((0,0), (2,2)) returns: [((0, 0), Direction.EAST), ((1, 0), Direction.NORTH)]
            shortest_path((0,0), (1,2)) returns: None
        :param start: 2-Tuple
        :param target: 2-Tuple
        :return: None, List[] or List[Tuple[Tuple[int, int], Direction]]
        """

        # YOUR CODE FOLLOWS (remove pass, please!)
        pass
