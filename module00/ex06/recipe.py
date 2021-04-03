import sys

def print_recipe(cookbook, recipe_name):
	try:
		print(cookbook[recipe_name])
	except:
		sys.stderr.write("recipe \"{}\" does not exist".format(recipe_name))

def delete_recipe(cookbook, recipe_name):
	try:
		del cookbook[recipe_name]
	except:
		sys.stderr.write("recipe does not exist")

def add_recipe(cookbook, name_of_recipe, ingredients, meal, prep_time):
	cookbook[name_of_recipe] = {'ingrediants':ingredients, 'meal':meal, 'prep_time':prep_time}

def print_all_recipes_name(cookbook):
	for recipe in cookbook:
		print(recipe)



def main():
	ingrds = []
	cookbook = {'sandwich':{'ingredients':['ham','bread','cheese',"tomatoes"], 'meal':'lunch','prep_time':15,}
	,'cake':{'ingredients':['flour','sugar','eggs'], 'meal':'dessert','prep_time':60,}
	,'salad':{'ingredients':['avocado','arugula','tomatoes','spinach'], 'meal':'lunch','prep_time':15,}
	}
	while True:
		print("Please select an option by typing the corresponding number:")
		print("1) Add a recipe")
		print("2) Delete a recipe")
		print("3) print a recipe")
		print("4)print the cookbook")
		print("5) Quite")
		choice = int(input("select an option: "))
		if choice == 1:
			name = input("name for recipe: ")
			while True:
				print("Please select an option by typing the corresponding number:")
				print("1) add ingrediant: ")
				print("2) finish adding ingrediants and go on")
				choice = int(input("select an option: "))
				if choice == 1:
					ingrds.append(input("insert ingredient name:"))
					continue
				meal = input("insert type of meal: ")
				prep_time = int(input("insert preparation time in minutes: "))
				add_recipe(cookbook, name, ingrds, meal,prep_time)
				break
		elif choice == 2:
			name = input("name for recipe: ")	
			delete_recipe(cookbook, name)
		elif choice == 3:
			name = input("recipe's name: ")
			print_recipe(cookbook, name)
			input("\nPlease Enter a key to continue")
		elif choice == 4:
			print_all_recipes_name(cookbook)
			input("\nPlease Enter a key to continue")
		elif 5:
			break


	

if __name__ == "__main__":
	main()
