#!/usr/bin/env python3
#Den src Pfad hier hinzufügen
import sys #Standardmodul um die Pfade von Modulen nachfragen
sys.path.append('..')#relativ path zu vorherigen Ordner also src

import unittest
from planet import Direction, Planet


class ExampleTestPlanet(unittest.TestCase):
    def setUp(self):
        """
        Instantiates the planet data structure and fills it with paths

        +--+
        |  |
        +-0,3------+
           |       |
          0,2-----2,2 (target)
           |      /
        +-0,1    /
        |  |    /
        +-0,0-1,0
           |
        (start)

        """
        # Initialize your data structure here
        self.planet = Planet()
        self.planet.add_path(((0, 0), Direction.NORTH), ((0, 1), Direction.SOUTH), 1)
        self.planet.add_path(((0, 1), Direction.WEST), ((0, 0), Direction.WEST), 1)

    @unittest.skip('Example test, should not count in final test results')
    def test_target_not_reachable_with_loop(self):
        """
        This test should check that the shortest-path algorithm does not get stuck in a loop between two points while
        searching for a target not reachable nearby

        Result: Target is not reachable
        """
        self.assertIsNone(self.planet.shortest_path((0, 0), (1, 2)))


class TestRoboLabPlanet(unittest.TestCase):
    maxDiff = None
    def setUp(self):
        """
        Instantiates the planet data structure and fills it with paths

        MODEL YOUR TEST PLANET HERE (if you'd like):

        """
        # Initialize your data structure here
        self.planet = Planet()
        # self.planet.add_path(...)
        self.planet.add_path(((0, 0), Direction.NORTH), ((0, 1), Direction.SOUTH), 50)
        self.planet.add_path(((0, 1), Direction.EAST), ((1, 1), Direction.WEST), 50)
        self.planet.add_path(((1, 1), Direction.SOUTH), ((1, 0), Direction.NORTH), 50)
        print("--- Inhalt der Karte nach add_path-Aufrufen ---")
        print(self.planet.get_paths())
        print("-------------------------------------------------")

    def test_integrity(self):
        """
        This test should check that the dictionary returned by "planet.get_paths()" matches the expected structure
        """
        expected_paths = {
            (0, 0): {Direction.NORTH: ((0, 1), Direction.SOUTH, 50)},
            (0, 1): {Direction.SOUTH: ((0, 0), Direction.NORTH, 50), Direction.EAST: ((1, 1), Direction.WEST, 50)},
            (1, 1): {Direction.WEST: ((0, 1), Direction.EAST, 50), Direction.SOUTH: ((1, 0), Direction.NORTH, 50)},
            (1, 0): {Direction.NORTH: ((1, 1), Direction.SOUTH, 50)}
        }
        #self.fail('implement me!')
        # Überprüfen das erwartete Ergebnis:
        self.assertDictEqual(self.planet.get_paths(), expected_paths)

    def test_empty_planet(self):
        """
        This test should check that an empty planet really is empty
        """
        #self.fail('implement me!')
        empty_planet = Planet()
        # Überprüfen, ob ein leeres Planet wirklich leer ist 
        self.assertDictEqual(empty_planet.get_paths(), {})

    def test_target(self):
        """
        This test should check that the shortest-path algorithm implemented works.

        Requirement: Minimum distance is three nodes (two paths in list returned)
        """
        #self.fail('implement me!')
        #Die Mehthode gibt den Pfad als Liste von Tupeln zurück.
        expected_path = [
            ((0, 0), Direction.NORTH),
            ((0, 1), Direction.EAST),
            ((1, 1), Direction.SOUTH)
        ]
        actual_path = self.planet.shortest_path((0, 0), (1, 0))
        #Überprüfen, ob die Ergebnisse gleich sind.
        self.assertEqual(actual_path, expected_path)

    def test_target_not_reachable(self):
        """
        This test should check that a target outside the map or at an unexplored node is not reachable
        """
        #self.fail('implement me!')

    def test_same_length(self):
        """
        This test should check that the shortest-path algorithm implemented returns a shortest path even if there
        are multiple shortest paths with the same length.

        Requirement: Minimum of two paths with same cost exists, only one is returned by the logic implemented
        """
        #self.fail('implement me!')

    def test_target_with_loop(self):
        """
        This test should check that the shortest-path algorithm does not get stuck in a loop between two points while
        searching for a target nearby

        Result: Target is reachable
        """
        #self.fail('implement me!')

    def test_target_not_reachable_with_loop(self):
        """
        This test should check that the shortest-path algorithm does not get stuck in a loop between two points while
        searching for a target not reachable nearby

        Result: Target is not reachable
        """
        #self.fail('implement me!')


if __name__ == "__main__":
    unittest.main()
