class Recipe:
    def __init__(self, name = '', cooking_level = 1, cooking_time = 0, ingredients = [], decription = '', recipe_type = ''):
        self.name = name


r = Recipe("lol")
print(r.name)