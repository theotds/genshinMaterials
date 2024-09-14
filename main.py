from idlelib.browser import file_open

from Materials.EnhancementMaterials import EnhancementMaterials
from Materials.Gems import Gems
from Materials.LevelMaterials import LevelMaterials
from Materials.Materials import Materials
from Materials.TalentBooks import TalentBooks
from Materials.TalentMaterial import TalentMaterials
from Character import Character
from laod_characters import read_character_data

# TODO - ADD ALL CHARACTERS MATERIALS AND SAVE IT IN TXT FILES,
# THEN REDO THE CHARACTER CLASS TO SET ALL NAMES FROM FILE, THEN CREATE MATERIALS IN THIS CLASS NOT IN MAIN

character_data = read_character_data()
user_input = -1


def printAllCharacters():
    for name, attributes in character_data.items():
        print(f"Character: {name}")
        for attribute, value in attributes.items():
            print(f"  {attribute}: {value}")
        print()
    #


def print_all_commands():
    print(
        "0 - exit\n"
        "1 - all characters\n"
        "2 - check specific character materials\n"
        "3 - check how many materials is needed for sepcific character\n")


def searchSpecificCharacter():
    search_name = input("Enter the character name you want to search: ").strip()

    # Normalize case for comparison
    found = False
    for name, attributes in character_data.items():
        if search_name.lower() == name.lower():
            found = True
            print(f"Character: {name}")
            for attribute, value in attributes.items():
                print(f"  {attribute}: {value}")
            print()
            break

    if not found:
        print(f"Character '{search_name}' not found. Please check the name and try again.")


def get_level_and_ascention_limits():
    end_lvl, end_phase, start_lvl, start_phase = 0, 0, 0, 0
    incorrect = True
    # Asking for the phases and levels for calculation
    while incorrect:
        start_phase = int(input("Enter the starting ascension phase (0-6): ").strip())
        end_phase = int(input("Enter the ending ascension phase (0-6): ").strip())
        start_lvl = int(input("Enter the starting talent level (1-10): ").strip())
        end_lvl = int(input("Enter the ending talent level (1-10): ").strip())
        if 0 <= start_phase <= end_phase <= 6 and 1 <= start_lvl <= end_lvl <= 10:
            incorrect = False
    return end_lvl, end_phase, start_lvl, start_phase


def process_character_data(attributes, name):
    print(f"Character: {name}")
    end_lvl, end_phase, start_lvl, start_phase = get_level_and_ascention_limits()
    # Creating LevelMaterials instance with material names
    level_materials = LevelMaterials(
        gem_name=attributes['gems'],
        local_specialties_name=attributes['local_specialties'],
        boss_material_name=attributes['boss_material'],
        common_material_name=attributes['common_material']
    )
    # Creating TalentMaterials instance with material names
    talent_materials_instance = TalentMaterials(
        enhancement_materials_name=attributes['enhancement_material'],
        talent_books_name=attributes['talent_books'],
        weekly_boss_material_name=attributes['weekly_boss']
    )
    # Create Character instance with materials
    character = Character(
        name=name,
        element=attributes['element'],
        weapon=attributes['weapon_type'],
        materials=Materials(
            level_materials=level_materials,
            talent_materials=talent_materials_instance
        )
    )
    # Calculate total materials needed
    ascension_phases = list(range(start_phase, end_phase + 1))
    talent_levels = list(range(start_lvl, end_lvl + 1))
    print(f"\nCalculating total materials needed for {name}:")
    # Use total_needed() for both ascension and talent materials for checking how many I need in future
    total_ascension_materials = character.materials.level_materials.total_needed(ascension_phases)
    total_talent_materials = character.materials.talent_materials.total_needed(talent_levels)


def character_material():
    search_name = input("Enter the character name you want to calculate materials for: ").strip()

    # Normalize case for comparison
    found = False
    for name, attributes in character_data.items():
        if search_name.lower() == name.lower():
            found = True
            process_character_data(attributes, name)
            break

    if not found:
        print(f"Character '{search_name}' not found. Please check the name and try again.")

    if not found:
        print(f"Character '{search_name}' not found. Please check the name and try again.")


while user_input != 0:
    user_input = input("Hi What u want to do? type help for all commands\n")
    try:
        user_input = int(user_input)
        match user_input:
            case 0:
                exit(0)
            case 1:
                printAllCharacters()
            case 2:
                searchSpecificCharacter()
            case 3:
                character_material()
    except ValueError:
        if user_input.lower() == "help":
            print_all_commands()
        else:
            print("Incorrect input try to type Help to get all commands list")
