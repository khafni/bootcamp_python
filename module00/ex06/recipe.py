import sys
import os

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
		print("\nPlease select an option by typing the corresponding number:")
		print("1) Add a recipe")
		print("2) Delete a recipe")
		print("3) print a recipe")
		print("4) print the cookbook")
		print("5) Quite")
		try:
			choice = int(input("select an option: "))
		except:
			sys.stderr.write("non valid choice")
			input("\nPlease Enter a key to continue")
			continue
		if choice < 1 or choice > 5:
			sys.stderr.write("non valid choice")
			input("\nPlease Enter a key to continue")
			continue
		os.system('clear')
		if choice == 1:
			name = input("\nname for recipe: ")
			os.system('clear')
			while True:
				print("Please select an option by typing the corresponding number:")
				print("1) add ingrediant: ")
				print("2) finish adding ingrediants and go on")
				choice = int(input("select an option: "))
				os.system('clear')
				if choice == 1:
					ingrds.append(input("insert ingredient name:"))
					continue
				meal = input("insert type of meal: ")
				prep_time = int(input("insert preparation time in minutes: "))
				add_recipe(cookbook, name, ingrds, meal,prep_time)
				os.system('clear')
				break
		elif choice == 2:
			name = input("\nname for recipe: ")	
			delete_recipe(cookbook, name)
			os.system('clear')
		elif choice == 3:
			name = input("\nrecipe's name: ")
			print_recipe(cookbook, name)
			input("\nPlease Enter a key to continue")
			os.system('clear')
		elif choice == 4:
			print_all_recipes_name(cookbook)
			input("\nPlease Enter a key to continue")
			os.system('clear')
		elif 5:
			print("exiting the prog")
			break


if __name__ == "__main__":
	main()
