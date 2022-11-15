class Point:
    # Initializes 2D point with x,y coordinate
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        
    def __repr__(self) -> str:

    def __str__(self) -> str:

    # Calculates the slope between this point and other point.
    # Computed as (y1 - y0) / (x1 - x0)
    # Horizontal lines have 0 slope.
    # Veritcal lines have infinity slope.
    # If self == other, then return negative infinity.
    def slope_to(self, other: 'Point') -> float:

    # Built in comparators for sorting Points by y-coordinate first and using x-coordinate for ties.
    # Here greater than or less than refer to y-coordinate.
    
    # Returns True if self has the same (x,y) coordinates as other.
    def __eq__(self, other: 'Point') -> bool:

    # Returns True if self is "less than" the point as other 
    def __lt__(self, other: 'Point') -> bool:

    # Returns True if self is "greater than" the point as other 
    def __gt__(self, other: 'Point') -> bool:

    # Hash function for Points.
    # Hint: You can use the hash function for tuples.
    def __hash__(self):