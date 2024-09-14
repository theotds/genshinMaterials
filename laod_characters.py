# Define the file path
file_path = 'genshin_characters.txt'

# Function to parse the file
def read_character_data():
    characters = {}

    # Open and read the file
    with open(file_path, 'r') as file:
        for line in file:
            # Split the character name from the attributes using ":"
            if ':' in line:
                name, attributes = line.split(':', 1)

                # Split the attributes into a list by commas
                attributes_list = [attr.strip() for attr in attributes.split(',')]

                # Store the parsed attributes into a dictionary
                characters[name.strip()] = {
                    'element': attributes_list[0],
                    'weapon_type': attributes_list[1],
                    'gems': attributes_list[2],
                    'common_material': attributes_list[3],
                    'local_specialties': attributes_list[4],
                    'boss_material': attributes_list[5],
                    'enhancement_material': attributes_list[6],
                    'talent_books': attributes_list[7],
                    'weekly_boss': attributes_list[8]
                }

    return characters
