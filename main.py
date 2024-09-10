from Materials.EnhancementMaterials import EnhancementMaterials
from Materials.Gems import Gems
from Materials.LevelMaterials import LevelMaterials
from Materials.Materials import Materials
from Materials.TalentBooks import TalentBooks
from Materials.TalentMaterial import TalentMaterials
from Character import Character

# Create a Character instance
materials = Materials(LevelMaterials(), TalentMaterials())

diluc = Character(name="Diluc", element="Pyro", weapon="Claymore", materials=materials)

# Display the materials needed for ascension and talents
diluc.display_character_info()

# Example of calculating and displaying the total materials needed
ascension_phases = [1, 2, 3, 4, 5, 6]
talent_levels = [2, 3, 4, 5, 6, 7, 8, 9, 10]

print("\nCalculating total materials needed:")
diluc.materials.total_materials_needed(ascension_phases, talent_levels)
