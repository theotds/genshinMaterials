class Materials:
    def __init__(self, level_materials, talent_materials):
        """
        Combines level materials and talent materials for a character.

        :param level_materials: An instance of LevelMaterials class.
        :param talent_materials: An instance of TalentMaterials class.
        """
        self.level_materials = level_materials
        self.talent_materials = talent_materials

    def display_materials(self):
        """Displays all materials needed for both ascension and talents."""
        print("Ascension Materials:")
        self.level_materials.display()
        print("Talent Materials:")
        self.talent_materials.display()

    def total_materials_needed(self, ascension_phases, talent_levels):
        """Calculates total materials needed for both ascension and talents."""
        print(f"Total materials needed for ascension phases: {ascension_phases}")
        total_ascension = self.level_materials.total_needed(ascension_phases)
        print(total_ascension)

        print(f"\nTotal materials needed for talent levels: {talent_levels}")
        total_talent = self.talent_materials.total_needed(talent_levels)
        print(total_talent)
