class CustomCollection:
    """A custom collection class demonstrating magic methods."""

    def __init__(self, items=None):
        """Initialize the collection with a list of items."""
        self._items = list(items) if items else []

    # Object Representation
    def __str__(self):
        """User-friendly representation (print)."""
        return f"CustomCollection with {len(self)} items: {self._items}"

    def __repr__(self):
        """Developer-friendly representation."""
        return f"CustomCollection({self._items!r})"

    # Comparison Methods
    def __eq__(self, other):
        """Check equality based on items."""
        if isinstance(other, CustomCollection):
            return self._items == other._items
        return False

    def __lt__(self, other):
        """Check if this collection is 'less than' another (by length)."""
        if isinstance(other, CustomCollection):
            return len(self) < len(other)
        return NotImplemented

    def __gt__(self, other):
        """Check if this collection is 'greater than' another (by length)."""
        if isinstance(other, CustomCollection):
            return len(self) > len(other)
        return NotImplemented

    # Length
    def __len__(self):
        """Return number of items."""
        return len(self._items)

    # Indexing and Assignment
    def __getitem__(self, index):
        """Get item at a given index."""
        return self._items[index]

    def __setitem__(self, index, value):
        """Set item at a given index."""
        self._items[index] = value

    # Iteration Support
    def __iter__(self):
        """Return an iterator over the collection."""
        return iter(self._items)

    # Custom Methods
    def add(self, item):
        """Add an item to the collection."""
        self._items.append(item)

    def remove(self, item):
        """Remove an item from the collection."""
        self._items.remove(item)


# Create two collections
col1 = CustomCollection([1, 2, 3])
col2 = CustomCollection([4, 5])

# String representations
print(str(col1))   # User-friendly
print(repr(col1))  # Developer-friendly

# Comparisons
print(col1 == col2)   # False
print(col1 > col2)    # True
print(col1 < col2)    # False

# Length and Indexing
print(len(col1))      # 3
print(col1[0])        # 1

# Setting items
col1[1] = 99
print(col1)

# Iteration
for item in col1:
    print("Item:", item)

# Adding and Removing
col1.add(50)
print(col1)
col1.remove(99)
print(col1)
