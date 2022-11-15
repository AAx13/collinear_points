from point import Point
from typing import List

class CollinearPointFinder:
    # Takes in a list of points and creates the CollinearPointFinder
    # This method should have O(N^2 log N) runtime.
    # Hint: This method will be the majority of the logic in your code
    # It will include a lot of preprocessing to make the other methods very quick.

    def __init__(self, points: List['Point']):

    # Returns the number of points in CollinearPointFinder
    # The runtime should be O(1)
    def size(self) -> int:

    # Returns the number of collinear segments with at least length k.
    # The runtime should be O(N log N) in the worst case.
    def num_segments(self, k: int) -> int:

    # Returns a list of all collinear segments with at least length k.
    # The runtime should be O(N log N) in the worst case.
    def get_segments(self, k: int) -> List['Point']: