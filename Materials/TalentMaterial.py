class TalentMaterials:
    def __init__(self):
        """
        Materials required for talent level-ups (levels 1-10).

        :param quantity_per_level: Dictionary of required materials per talent level.
        """
        # Define talent materials per level
        self.quantity_per_level = {
            2: {
                'mora': 12500,
                'enhancement_materials': {'2 Stars': 6},
                'talent_books': {'2 Stars': 3},
                'weekly_boss_drops': 0,
                'crown_of_insight': 0
            },
            3: {
                'mora': 17500,
                'enhancement_materials': {'3 Stars': 3},
                'talent_books': {'3 Stars': 2},
                'weekly_boss_drops': 0,
                'crown_of_insight': 0
            },
            4: {
                'mora': 25000,
                'enhancement_materials': {'3 Stars': 4},
                'talent_books': {'3 Stars': 4},
                'weekly_boss_drops': 0,
                'crown_of_insight': 0
            },
            5: {
                'mora': 30000,
                'enhancement_materials': {'3 Stars': 6},
                'talent_books': {'3 Stars': 6},
                'weekly_boss_drops': 0,
                'crown_of_insight': 0
            },
            6: {
                'mora': 37500,
                'enhancement_materials': {'3 Stars': 9},
                'talent_books': {'3 Stars': 9},
                'weekly_boss_drops': 0,
                'crown_of_insight': 0
            },
            7: {
                'mora': 120000,
                'enhancement_materials': {'4 Stars': 4},
                'talent_books': {'4 Stars': 4},
                'weekly_boss_drops': 1,
                'crown_of_insight': 0
            },
            8: {
                'mora': 260000,
                'enhancement_materials': {'4 Stars': 6},
                'talent_books': {'4 Stars': 6},
                'weekly_boss_drops': 1,
                'crown_of_insight': 0
            },
            9: {
                'mora': 450000,
                'enhancement_materials': {'4 Stars': 9},
                'talent_books': {'4 Stars': 12},
                'weekly_boss_drops': 2,
                'crown_of_insight': 0
            },
            10: {
                'mora': 700000,
                'enhancement_materials': {'4 Stars': 12},
                'talent_books': {'4 Stars': 16},
                'weekly_boss_drops': 2,
                'crown_of_insight': 1
            }
        }

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
