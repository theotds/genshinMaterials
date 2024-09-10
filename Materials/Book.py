class Book:
    def __init__(self, name, quality):
        """
        Initialize the Books class with a name and quality.

        :param name: Name of the book (e.g., "Teachings of Freedom").
        :param quality: Quality of the book (1-star, 2-star, 3-star).
        """
        self.name = name
        self.quality = quality

    def display(self):
        """Displays the book details."""
        print(f"Book: {self.name}, Quality: {self.quality}-star")
