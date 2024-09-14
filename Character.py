class Character:
    def __init__(self, name, element, weapon, materials):
        """
        Initialize a Character with its basic details and materials.

        :param name: Name of the character.
        :param element: Element (e.g., Pyro, Hydro).
        :param weapon: Weapon type (e.g., Sword, Claymore).
        :param materials: An instance of the Materials class.
        """
        self.name = name
        self.element = element
        self.weapon = weapon
        #materials = Materials(LevelMaterials(), TalentMaterials())
        self.materials = materials

    def display_character_info(self):
        """Displays the character's details and materials."""
        print(f"Character: {self.name}")
        print(f"Element: {self.element}")
        print(f"Weapon: {self.weapon}")
        print("\nMaterials for Ascension and Talents:")
        self.materials.display_materials()
