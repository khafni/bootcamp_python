from recipe import Recipe

class Book:
    def __init__(self, name, last_update, creation_date, recipe_list):
        self.name = name 
        self.last_update = last_update
        self.creation_date = creation_date
        self.recipe_list = recipe_list
    def get_recipe_by_name(self, name):
        for rec in self.recipe_list.values():
            print(rec)

r = Recipe("pizza", 1, 90, ["dough", "tomatoes sauce", "cheese"],"wow tasty", "italian food")
b = Book(r.name, 1, 1, [].append(r))
print(r)


        