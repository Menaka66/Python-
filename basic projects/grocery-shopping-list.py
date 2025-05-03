print("\n🛒 Welcome to the Grocery Shopping List Generator! 🛍️")

# List of predefined meals and their ingredients
meals_list = [
    "pasta", "omelette", "salad", "chicken curry", "fried rice","tomato rice"
]

ingredients_list = [
    ["pasta", "tomato sauce", "cheese", "garlic"],  # Pasta
    ["eggs", "milk", "cheese", "onion"],  # Omelette
    ["lettuce", "tomato", "cucumber", "olive oil"],  # Salad
    ["chicken", "onion", "tomato", "garlic", "spices"],  # Chicken Curry
    ["rice", "carrot", "peas", "onion", "soy sauce"] , # Fried Rice
    ["tomato", "onion", "chilly", "salt", "oil", "curry leaf", "gingergarlic paste", "rice"] #tomato rice
]

selected_meals = []
shopping_list = []

# Get user meal selection
print("\nEnter your planned meals for the week (type 'done' to finish):")
while True:
    meal = input("Meal: ").strip().lower()
    if meal == "done":
        break
    if meal in meals_list:
        selected_meals.append(meal)
    else:
        print("⚠ Meal not found. Try another one.")

# Generate shopping list
for meal in selected_meals:
    index = meals_list.index(meal)  # Find the index of the meal
    ingredients = ingredients_list[index]  # Get ingredients
    for item in ingredients:
        if item not in shopping_list:  # Avoid duplicates
            shopping_list.append(item)

# Display the final shopping list
print("\n📝 Your Final Shopping List:")
for i, item in enumerate(shopping_list, 1):
    print(f"{i}. {item.capitalize()}")

print("\n🎯 Happy Shopping!!!!! 🛍️")
