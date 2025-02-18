"""Functions for compiling dishes and ingredients for a catering company."""


from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(dish_name, dish_ingredients):
    """Remove duplicates from `dish_ingredients`.

    :param dish_name: str - containing the dish name.
    :param dish_ingredients: list - dish ingredients.
    :return: tuple - containing (dish_name, ingredient set).
    """
    
    return (dish_name, set(dish_ingredients))


def check_drinks(drink_name, drink_ingredients):
    """Append "Cocktail" (alcohol) or "Mocktail" (no alcohol) to `drink_name`, based on `drink_ingredients`.

    :param drink_name: str - name of the drink.
    :param drink_ingredients: list - ingredients in the drink.
    :return: str - drink_name appended with "Mocktail" or "Cocktail".
    """
    
    if any(ingredient in ALCOHOLS for ingredient in drink_ingredients):
        return f"{drink_name} Cocktail"
    return f"{drink_name} Mocktail"

# Misol uchun:
print(check_drinks("Mojito", ["mint", "sugar", "lime", "rum"]))
# Natija: "Mojito Cocktail"

print(check_drinks("Virgin Mojito", ["mint", "sugar", "lime", "soda"]))
# Natija: "Virgin Mojito Mocktail"


def categorize_dish(dish_name, dish_ingredients):
    """Categorize `dish_name` based on `dish_ingredients`.

    :param dish_name: str - dish to be categorized.
    :param dish_ingredients: set - ingredients for the dish.
    :return: str - the dish name appended with ": <CATEGORY>".
    """
    
    categories = {
        "VEGAN": VEGAN,
        "VEGETARIAN": VEGETARIAN,
        "PALEO": PALEO,
        "KETO": KETO,
        "OMNIVORE": OMNIVORE
    }

    for category, ingredients in categories.items():
        if dish_ingredients.issubset(ingredients):
            return f"{dish_name}: {category}"

    return f"{dish_name}: OMNIVORE"

# Misol uchun:
print(categorize_dish("Avocado Salad", {"avocado", "olive oil", "lettuce"}))
# Agar barcha ingredientlar `VEGAN` to‘plamida bo‘lsa, chiqishi: "Avocado Salad: VEGAN"

print(categorize_dish("Chicken Stir Fry", {"chicken", "soy sauce", "garlic"}))
# Agar hech qaysi kategoriya to‘liq mos kelmasa, chiqishi: "Chicken Stir Fry: OMNIVORE"


def tag_special_ingredients(dish):
    """Compare `dish` ingredients to `SPECIAL_INGREDIENTS`.

    :param dish: tuple - of (dish name, list of dish ingredients).
    :return: tuple - containing (dish name, dish special ingredients).
    """
    
    dish_name, dish_ingredients = dish
    special_ingredients = set(dish_ingredients) & SPECIAL_INGREDIENTS
    
    return (dish_name, special_ingredients)

# Misol uchun:
print(tag_special_ingredients(("Peanut Butter Sandwich", ["bread", "peanut butter", "jelly"])))
# Agar "peanut butter" `SPECIAL_INGREDIENTS` to‘plamida bo‘lsa, chiqishi: ('Peanut Butter Sandwich', {'peanut butter'})

print(tag_special_ingredients(("Fruit Salad", ["apple", "banana", "grapes"])))
# Agar hech qanday maxsus ingredient bo‘lmasa, chiqishi: ('Fruit Salad', set())


def compile_ingredients(dishes):
    """Create a master list of ingredients.

    :param dishes: list - of dish ingredient sets.
    :return: set - of ingredients compiled from `dishes`.
    """
    
    return set().union(*dishes)

# Misol uchun:
dishes = [
    {"tomato", "cheese", "basil"},
    {"chicken", "garlic", "pepper"},
    {"cheese", "bread", "butter"}
]

print(compile_ingredients(dishes))
# Natija: {'tomato', 'cheese', 'basil', 'chicken', 'garlic', 'pepper', 'bread', 'butter'}



def separate_appetizers(dishes, appetizers):
    """Determine which `dishes` are designated `appetizers` and remove them.

    :param dishes: list - of dish names.
    :param appetizers: list - of appetizer names.
    :return: list - of dish names that do not appear on appetizer list.
    """
    
    return list(set(dishes) - set(appetizers))

# Misol uchun:
dishes = ["Caesar Salad", "Garlic Bread", "Steak", "Pasta", "Garlic Bread"]
appetizers = ["Garlic Bread", "Caesar Salad"]

print(separate_appetizers(dishes, appetizers))
# Natija: ['Pasta', 'Steak']


def singleton_ingredients(dishes, intersection):
    """Determine which `dishes` have a singleton ingredient (an ingredient that only appears once across dishes).

    :param dishes: list - of ingredient sets.
    :param intersection: constant - can be one of `<CATEGORY>_INTERSECTIONS` constants imported from `sets_categories_data.py`.
    :return: set - containing singleton ingredients.
    """
    
    # Barcha ingredientlarni birlashtirish
    all_ingredients = set().union(*dishes)
    
    # Ingredientlarning qanchalik ko‘p takrorlanishini hisoblash
    ingredient_count = {ingredient: sum(ingredient in dish for dish in dishes) for ingredient in all_ingredients}
    
    # Faqat bir marta takrorlangan ingredientlarni olish
    singleton_ingredients = {ingredient for ingredient, count in ingredient_count.items() if count == 1}
    
    return singleton_ingredients

# Misol uchun:
dishes = [
    {"tomato", "cheese", "basil"},
    {"chicken", "garlic", "tomato"},
    {"cheese", "bread", "butter"}
]
intersection = None  # Bu misolda ishlatilmaydi, lekin kerak bo‘lsa, qo‘shimcha ishlatilishi mumkin.

print(singleton_ingredients(dishes, intersection))
# Natija: {'basil', 'garlic', 'bread', 'butter'}
