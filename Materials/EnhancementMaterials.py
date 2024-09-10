class EnhancementMaterials:
    def __init__(self, star_quality, count):
        """
        Initialize the EnhancementMaterials class with star quality and count.

        :param star_quality: Quality of the enhancement material (e.g., "2 Stars", "3 Stars").
        :param count: Number of materials needed.
        """
        self.star_quality = star_quality
        self.count = count

    def display(self):
        """Displays the enhancement material details."""
        print(f"{self.count} {self.star_quality} Enhancement Materials")

    def __str__(self):
        return f"{self.count} {self.star_quality} Enhancement Materials"
