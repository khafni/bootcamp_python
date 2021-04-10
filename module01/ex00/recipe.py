class Recipe:
    def __init__(self, name, cooking_level, cooking_time, ingredients, decription, recipe_type):
        if not isinstance(name, str):
            raise TypeError("name is not a string")
        self.name = name
        if not isinstance(cooking_level, int):
            raise TypeError("cooking_level is not an int")
        self.cooking_level = cooking_level
        if not isinstance(cooking_time, int):
            raise TypeError("cooking_time is not an int")
        self.cooking_time = cooking_time
        if not isinstance(ingredients, list):
            raise TypeError("ingredients is not a list")
        self.ingredients = ingredients
        if not isinstance(decription, str):
            raise TypeError("description is not a string")
        self.description = decription
        if not isinstance(recipe_type, str):
            raise TypeError("recipe_type is not a string")
        self.recipe_type = recipe_type

    def __str__(self):
        str = ""
        str += "Recipe name: {}\n".format(self.name)
        str += "cooking level: {}\n".format(self.cooking_level)
        str += "cooking time: {}\n".format(self.cooking_time)
        str  += "ingredients: {}\n".format(" , ".join(self.ingredients))
        str += "description: {}\n".format(self.description)
        str += "recipe type: {}".format(self.recipe_type)
        return str

