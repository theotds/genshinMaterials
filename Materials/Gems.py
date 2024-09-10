class Gems:
    def __init__(self, element, quality_counts):
        """
        Initialize the Gems class with element and quality counts.

        :param element: Element of the gem (e.g., "Pyro", "Electro").
        :param quality_counts: Dictionary of gem qualities and their counts.
        """
        self.element = element
        self.quality_counts = quality_counts  # {'2 Stars': 1, '3 Stars': 3, ...}

    def display(self):
        """Displays the gem details."""
        for quality, count in self.quality_counts.items():
            print(f"Element: {self.element}, Quality: {quality}, Count: {count}")

    def __str__(self):
        return ", ".join(f"{count} x {quality} {self.element} Gems" for quality, count in self.quality_counts.items())
