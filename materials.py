class Materials:
    def __init__(self, gems, boss_drop, local_specialty, common_enemy, books=None, boss_material=None):
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
