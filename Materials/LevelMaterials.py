class LevelMaterials:
    def __init__(self, quantity_per_phase):
        """
        Materials required for character ascension (phases 1-6).

        :param quantity_per_phase: Dictionary of required materials per ascension phase.
        """
        self.quantity_per_phase = quantity_per_phase  # {1: {...}, 2: {...}, ...}

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
