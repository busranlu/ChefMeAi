from YesChefGPT import YesChefGPT

def run():
    chef = YesChefGPT()
   


if __name__ == "__main__":
    run()




chef = YesChefGPT()

def suggest_dish(ingredients):
    # Logic to suggest a dish based on the ingredients
    # For simplicity, let's just echo back the ingredients as the suggested dish
    return f"A dish you can make with these ingredients: {', '.join(ingredients)}"

def get_recipe(dish):
    # Logic to get the recipe for the provided dish
    # For simplicity, let's just echo back the dish name as the recipe
    return f"Recipe for: {dish}"

def get_feedback(recipe):
    # Logic to provide feedback on the given recipe
    # For simplicity, let's just echo back the recipe as the feedback
    return f"Feedback for the recipe: {recipe}"

options = {
    "1": suggest_dish,
    "2": get_recipe,
    "3": get_feedback
}

while True:
    print("Options:")
    print("1. Get dish from ingredients")
    print("2. Get recipe for a dish")
    print("3. Get feedback on a recipe")
    option = input("Choose an option (1/2/3): ")

    if option not in options:
        print("Invalid option. Please choose a valid option.")
        continue

    if option == "1":
        ingredients_input = input("Enter a list of ingredients separated by commas:\n").split(",")
        dish_name=chef.query(ingredients_input)
    elif option == "2":
        dish_input = input("Enter the name of the dish for which you want the recipe:\n")
        recipe=chef.query(dish_input)
    elif option == "3":
        recipe_input = input("Enter the recipe for which you want to provide feedback:\n")
        feedback=chef.query(recipe_input)



