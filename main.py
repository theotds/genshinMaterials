from Character import Character
from Materials.Book import Book
from Materials.Materials import Materials
from Materials.TalentMaterial import TalentMaterial

# Create a Books object
resistance_book = Book(name="Teachings of Resistance", quality=2)

# Create a Materials object for Diluc using the new Books and TalentMaterial classes
diluc_materials = Materials(
    gems="Agnidus Agate",
    boss_drop="Everflame Seed",
    local_specialty="Small Lamp Grass",
    common_enemy=TalentMaterial(name="Recruit's Insignia", quality=2),
    books=resistance_book,      # Using Books object
    boss_material=TalentMaterial(name="dvalin_plume", quality=5)
)

# Create a Character object for Diluc
diluc = Character(
    name="Diluc",
    element="Pyro",
    weapon="Claymore",
    materials=diluc_materials
)

# Display Diluc's details and required materials
diluc.display_character_info()
