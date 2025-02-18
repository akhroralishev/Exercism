#
"""Functions to manage a users shopping cart items."""

def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """

    for item in items_to_add:
        if item in current_cart:
            current_cart[item] += 1
        else:
            current_cart[item] = 1
    
    return current_cart

def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """

    cart = {}
    for item in notes:
        if item in cart:
            cart[item] += 1
        else:
            cart[item] = 1
    
    return cart

def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: dict - dictionary with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """

    ideas.update(recipe_updates)
    return ideas

def sort_entries(cart):
    """Sort a user's shopping cart in alphabetical order.

    :param cart: dict - a user's shopping cart dictionary.
    :return: dict - user's shopping cart sorted in alphabetical order.
    """

    return dict(sorted(cart.items()))

def send_to_store(cart, aisle_mapping):
    """Combine user's order to aisle and refrigeration information.

    :param cart: dict - user's shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """

    fulfillment = {}
    for item, quantity in cart.items():
        if item in aisle_mapping:
            fulfillment[item] = {
                "quantity": quantity,
                "aisle": aisle_mapping[item]["aisle"],
                "refrigeration": aisle_mapping[item]["refrigeration"]
            }
        else:
            fulfillment[item] = {"quantity": quantity}
    
    return fulfillment

def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment_cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory.
    :return: dict - store inventory updated.
    """

    for item, details in fulfillment_cart.items():
        if item in store_inventory:
            store_inventory[item] -= details["quantity"]
            if store_inventory[item] < 0:
                store_inventory[item] = 0
        else:
            print(f"{item} do'konda mavjud emas.")
    
    return store_inventory
