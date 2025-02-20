class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate."""

    total_aliens_created = 0  # Class-level attribute to track total aliens

    def __init__(self, x_coordinate, y_coordinate):
        """Initialize Alien with given coordinates and default health of 3."""
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3

        Alien.total_aliens_created += 1  # Increment total aliens count

    def hit(self):
        """Decrement Alien health by one point."""
        if self.health > 0:
            self.health -= 1

    def is_alive(self):
        """Check if the Alien is still alive."""
        return self.health > 0

    def teleport(self, new_x_coordinate, new_y_coordinate):
        """Move Alien object to new coordinates."""
        self.x_coordinate = new_x_coordinate
        self.y_coordinate = new_y_coordinate

    def collision_detection(self, other):
        """Placeholder for collision detection implementation."""
        pass  # Implementation TBD

def new_aliens_collection(coordinates):
    """Create a list of Alien objects from a list of (x, y) coordinates."""
    return [Alien(x, y) for x, y in coordinates]
