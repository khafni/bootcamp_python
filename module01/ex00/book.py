from recipe import Recipe
from datetime import datetime

class Book:
    def __init__(self, name, last_update, creation_date, recipe_list):
        self.name = name 
        self.last_update = last_update
        self.creation_date = creation_date
        self.recipe_list = recipe_list
    def get_recipe_by_name(self, name):
        for rec in self.recipe_list.values():
            if rec.name == name:
                print(rec.name)
                return rec
    def get_recipe_by_types(self, recipe_type):
        r_arr = []
        for elem in self.recipe_list:
            if (elem.recipe_type == recipe_type):
                print(elem.name)
                r_arr.append(elem.name)
    def add_recipe(self, recipe):
        if not isinstance(recipe, Recipe):
            raise TypeError("arg passed in add_recipe is not a recipe")
        self.recipe_list.append(recipe)
        self.last_update = datetime.now()


r = Recipe("pizza", 1, 90, ["dough", "tomatoes sauce", "cheese"],"wow tasty", "italian food")
b = Book(r.name, 1, 1, [r])
b.get_recipe_by_types("italian food")
r = Recipe("pasta", 1, 90, ["pasta", "tomatoes sauce", "cheese"],"wow tasty", "italian food")       
b.add_recipe(r)
b.get_recipe_by_types("italian food")