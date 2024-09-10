class TalentBooks:
    def __init__(self, star_quality, count):
        """
        Initialize the TalentBooks class with star quality and count.

        :param star_quality: Quality of the talent book (e.g., "1 Star", "2 Stars").
        :param count: Number of books needed.
        """
        self.star_quality = star_quality
        self.count = count

    def display(self):
        """Displays the talent book details."""
        print(f"{self.count} {self.star_quality} Talent Books")

    def __str__(self):
        return f"{self.count} {self.star_quality} Talent Books"
