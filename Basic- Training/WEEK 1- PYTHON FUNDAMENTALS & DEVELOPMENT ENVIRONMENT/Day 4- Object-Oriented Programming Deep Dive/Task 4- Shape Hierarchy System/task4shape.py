from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for geometric shapes."""

    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        pass

    def __lt__(self, other):
        """Compare shapes by area for sorting."""
        if isinstance(other, Shape):
            return self.area() < other.area()
        return NotImplemented

    def __eq__(self, other):
        """Check if two shapes have the same area."""
        if isinstance(other, Shape):
            return math.isclose(self.area(), other.area(), rel_tol=1e-9)
        return False


class Rectangle(Shape):
    """Rectangle shape class."""

    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive numbers.")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Circle(Shape):
    """Circle shape class."""

    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be a positive number.")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def __repr__(self):
        return f"Circle(radius={self.radius})"


class Triangle(Shape):
    """Triangle shape class using 3 side lengths."""

    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("All sides must be positive numbers.")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Invalid triangle sides.")
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        # Heron's formula
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c

    def __repr__(self):
        return f"Triangle(a={self.a}, b={self.b}, c={self.c})"


if __name__ == "__main__":
    shapes = [
        Rectangle(4, 5),
        Circle(3),
        Triangle(3, 4, 5),
        Rectangle(2, 7)
    ]

    # Display each shape's area and perimeter
    for shape in shapes:
        print(f"{shape} -> Area: {shape.area():.2f}, Perimeter: {shape.perimeter():.2f}")

    # Compare shapes
    print("\nComparisons:")
    print(shapes[0] == Rectangle(4, 5))  # True
    print(shapes[0] < Circle(4))         # Depends on area

    # Sort shapes by area
    sorted_shapes = sorted(shapes)
    print("\nSorted by area:")
    for s in sorted_shapes:
        print(f"{s} (Area: {s.area():.2f})")
