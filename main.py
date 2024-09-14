from idlelib.browser import file_open

from Materials.EnhancementMaterials import EnhancementMaterials
from Materials.Gems import Gems
from Materials.LevelMaterials import LevelMaterials
from Materials.Materials import Materials
from Materials.TalentBooks import TalentBooks
from Materials.TalentMaterial import TalentMaterials
from Character import Character
from laod_characters import read_character_data

#TODO - ADD ALL CHARACTERS MATERIALS AND SAVE IT IN TXT FILES,
# THEN REDO THE CHARACTER CLASS TO SET ALL NAMES FROM FILE, THEN CREATE MATERIALS IN THIS CLASS NOT IN MAIN


# Call the function to read the character data
character_data = read_character_data()

# Example: print the data for a specific character
for name, attributes in character_data.items():
    print(f"Character: {name}")
    for attribute, value in attributes.items():
        print(f"  {attribute}: {value}")
    print()  # Empty line for separation
#
# # Create a Character instance
# materials = Materials(LevelMaterials("Pyro","small lamp grass","everflame seed","Fatui insygnia"), TalentMaterials())
#
# character = Character(name="Diluc", element="Pyro", weapon="Claymore", materials=materials)
#
# # Display the materials needed for ascension and talents
# character.display_character_info()
#
# start_phase = 1
# end_phase = 6
# start_lvl = 1
# end_lvl = 10
# # Example of calculating and displaying the total materials needed
# ascension_phases = list(range(start_phase, end_phase+1))
# talent_levels = list(range(start_lvl, end_lvl+1))
#
# print("\nCalculating total materials needed:")
# character.materials.total_materials_needed(ascension_phases, talent_levels)
