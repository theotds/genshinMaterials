class Materials:
    def __init__(self, gems, boss_drop, local_specialty, common_enemy, books=None, boss_material=None):
        """
        Initialize the materials needed for ascension and talents.
        :param gems: Gemstone needed for character ascension (elemental stones).
        :param boss_drop: Material dropped by a boss for ascension.
        :param local_specialty: Region-specific collectible used for ascension.
        :param common_enemy: Material dropped by common enemies used for ascension/talents.
        :param books: Books from domains for talent level-up (optional).
        :param boss_material: Weekly boss drop for talent level-up (optional).
        """
        self.gems = gems
        self.boss_drop = boss_drop
        self.local_specialty = local_specialty
        self.common_enemy = common_enemy
        self.books = books
        self.boss_material = boss_material

    def display_materials(self):
        print(f"Gems: {self.gems}")
        print(f"Boss Drop: {self.boss_drop}")
        print(f"Local Specialty: {self.local_specialty}")
        print(f"Common Enemy Material: {self.common_enemy}")

        # Check if books and boss material are provided (for talents)
        if self.books:
            print(f"Books: {self.books}")
        if self.boss_material:
            print(f"Boss Material: {self.boss_material}")
