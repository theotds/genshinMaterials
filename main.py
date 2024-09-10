from Materials.EnhancementMaterials import EnhancementMaterials
from Materials.Gems import Gems
from Materials.LevelMaterials import LevelMaterials
from Materials.Materials import Materials
from Materials.TalentBooks import TalentBooks
from Materials.TalentMaterial import TalentMaterials
from Character import Character

# Define talent materials per level
quantity_per_level = {
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

# Define level materials for ascension phases
quantity_per_phase = {
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

# Create LevelMaterials and TalentMaterials instances
level_materials = LevelMaterials(quantity_per_phase)
talent_materials = TalentMaterials(quantity_per_level)

# Create a Character instance
materials = Materials(level_materials, talent_materials)

diluc = Character(name="Diluc", element="Pyro", weapon="Claymore", materials=materials)

# Display the materials needed for ascension and talents
diluc.display_character_info()

# Example of calculating and displaying the total materials needed
ascension_phases = [1, 2, 3, 4, 5, 6]
talent_levels = [2, 3, 4, 5, 6, 7, 8, 9, 10]

print("\nCalculating total materials needed:")
diluc.materials.total_materials_needed(ascension_phases, talent_levels)
