from Materials.Gems import Gems


class LevelMaterials:
    def __init__(self):
        """
        Materials required for character ascension (phases 1-6).

        :param quantity_per_phase: Dictionary of required materials per ascension phase.
        """
        # Define level materials for ascension phases
        self.quantity_per_phase = {
            1: {
                'gems': Gems("Pyro", {"2 Stars": 1}),
                'local_specialties': 3,
                'common_materials': {"2 Stars": 3},
                'boss_material': 0,
                'mora_cost': 20000
            },
            2: {
                'gems': Gems("Pyro", {"3 Stars": 3}),
                'local_specialties': 10,
                'common_materials': {"2 Stars": 15},
                'boss_material': 2,
                'mora_cost': 40000
            },
            3: {
                'gems': Gems("Pyro", {"3 Stars": 6}),
                'local_specialties': 20,
                'common_materials': {"3 Stars": 12},
                'boss_material': 4,
                'mora_cost': 60000
            },
            4: {
                'gems': Gems("Pyro", {"4 Stars": 3}),
                'local_specialties': 30,
                'common_materials': {"3 Stars": 18},
                'boss_material': 8,
                'mora_cost': 80000
            },
            5: {
                'gems': Gems("Pyro", {"4 Stars": 6}),
                'local_specialties': 45,
                'common_materials': {"4 Stars": 12},
                'boss_material': 12,
                'mora_cost': 100000
            },
            6: {
                'gems': Gems("Pyro", {"5 Stars": 6}),
                'local_specialties': 60,
                'common_materials': {"4 Stars": 24},
                'boss_material': 20,
                'mora_cost': 120000
            }
        }

    def display(self):
        """Displays the required materials per ascension phase."""
        for phase, materials in self.quantity_per_phase.items():
            print(f"Ascension Phase {phase}:")
            print(f"  Gems:")
            materials['gems'].display()
            print(f"  Local Specialties: {materials['local_specialties']}")
            print(f"  Common Materials:")
            for quality, count in materials['common_materials'].items():
                print(f"    {quality}: {count}")
            print(f"  Boss Material: {materials['boss_material']}")
            print(f"  Mora Cost: {materials['mora_cost']}")
            print()

    def total_needed(self, phases):
        """Calculate the total number of materials needed for a range of ascension phases."""
        total = {
            'gems': {},
            'local_specialties': 0,
            'common_materials': {},
            'boss_material': 0,
            'mora_cost': 0
        }
        for phase in phases:
            if phase in self.quantity_per_phase:
                phase_materials = self.quantity_per_phase[phase]
                # Aggregate gem counts by quality
                for quality, count in phase_materials['gems'].quality_counts.items():
                    if quality in total['gems']:
                        total['gems'][quality] += count
                    else:
                        total['gems'][quality] = count

                # Aggregate common materials by quality
                for quality, count in phase_materials.get('common_materials', {}).items():
                    if quality in total['common_materials']:
                        total['common_materials'][quality] += count
                    else:
                        total['common_materials'][quality] = count

                total['local_specialties'] += phase_materials.get('local_specialties', 0)
                total['boss_material'] += phase_materials.get('boss_material', 0)
                total['mora_cost'] += phase_materials.get('mora_cost', 0)
        return total
