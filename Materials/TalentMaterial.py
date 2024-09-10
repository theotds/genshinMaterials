class TalentMaterials:
    def __init__(self, quantity_per_level):
        """
        Materials required for talent level-ups (levels 1-10).

        :param quantity_per_level: Dictionary of required materials per talent level.
        """
        self.quantity_per_level = quantity_per_level

    def display(self):
        """Displays the required talent materials per level."""
        print("Talent Materials per Level:")
        for level, materials in self.quantity_per_level.items():
            print(f"  Level {level}:")
            print(f"    Mora: {materials['mora']}")
            print(f"    Enhancement Materials:")
            for quality, count in materials['enhancement_materials'].items():
                print(f"      {quality}: {count}")
            print(f"    Talent Books:")
            for quality, count in materials['talent_books'].items():
                print(f"      {quality}: {count}")
            print(f"    Weekly Boss Drops: {materials['weekly_boss_drops']}")
            print(f"    Crown of Insight: {materials['crown_of_insight']}")
            print()

    def total_needed(self, levels):
        """Calculate the total number of talent materials needed for a range of levels."""
        total = {
            'mora': 0,
            'enhancement_materials': {},
            'talent_books': {},
            'weekly_boss_drops': 0,
            'crown_of_insight': 0
        }

        for level in levels:
            if level in self.quantity_per_level:
                level_materials = self.quantity_per_level[level]
                total['mora'] += level_materials.get('mora', 0)

                # Aggregate enhancement materials by quality
                for quality, count in level_materials.get('enhancement_materials', {}).items():
                    if quality in total['enhancement_materials']:
                        total['enhancement_materials'][quality] += count
                    else:
                        total['enhancement_materials'][quality] = count
                # Aggregate talent books by quality
                for quality, count in level_materials.get('talent_books', {}).items():
                    if quality in total['talent_books']:
                        total['talent_books'][quality] += count
                    else:
                        total['talent_books'][quality] = count
                total['weekly_boss_drops'] += level_materials.get('weekly_boss_drops', 0)
                total['crown_of_insight'] += level_materials.get('crown_of_insight', 0)

        return total
