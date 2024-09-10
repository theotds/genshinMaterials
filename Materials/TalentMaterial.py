# Class for Talent Materials (Weekly Boss Materials)
class TalentMaterial:
    def __init__(self, name, quality):
        """
        Initialize the TalentMaterial class with a name and quality.

        :param name: Name of the talent material (e.g., "Dvalin's Plume").
        :param quality: Quality of the material (1-star, 2-star, 3-star).
        """
        self.name = name
        self.quality = quality

    def display(self):
        """Displays the talent material details."""
        print(f"Talent Material: {self.name}, Quality: {self.quality}-star")
