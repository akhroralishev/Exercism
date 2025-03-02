"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Xarid savatchasiga mahsulot qo‘shish.

    :param current_cart: dict - joriy xarid savatchasi.
    :param items_to_add: iterable - savatchaga qo‘shiladigan mahsulotlar.
    :return: dict - yangilangan savatcha.
    """
    updated_cart = current_cart.copy()  # Asl savatchani o'zgartirmaslik uchun nusxa olish

    for item in items_to_add:
        updated_cart.setdefault(item, 0)  # Agar mahsulot bo'lmasa, 0 qilib qo‘yadi
        updated_cart[item] += 1  # Bor bo‘lsa, 1 qo‘shadi

    return updated_cart


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """
    cart = {}  # Bo'sh savat
    
    for item in notes:
        cart[item] = cart.get(item, 0) + 1  # Bor bo'lsa, 1 qo'shish, bo'lmasa 1 bilan qo'shish
    
    return cart

def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: dict - dictionary with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """
    updated_ideas = ideas.copy()  # Asl lug‘atni o‘zgartirmaslik uchun nusxa olish
    updated_ideas.update(recipe_updates)  # Lug‘atni yangilash
    
    return updated_ideas



def sort_entries(cart):
    """Sort a user's shopping cart in alphabetical order.

    :param cart: dict - a user's shopping cart dictionary.
    :return: dict - user's shopping cart sorted in alphabetical order.
    """
    return dict(sorted(cart.items()))  # Lug‘atni alfavit bo‘yicha tartiblash



def send_to_store(cart, aisle_mapping):
    """Combine user's order with aisle and refrigeration information.

    :param cart: dict - user's shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    fulfillment = {}

    for item, quantity in cart.items():
        if item in aisle_mapping:
            aisle, refrigeration = aisle_mapping[item]
            fulfillment[item] = [quantity, aisle, refrigeration]
        else:
            fulfillment[item] = [quantity, "Unknown", "Unknown"]

    # Reverse alphabetical order
    return dict(sorted(fulfillment.items(), reverse=True))




def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment_cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory.
    :return: dict - store_inventory updated.
    """
    updated_inventory = store_inventory.copy()  # Asl inventarni o'zgartirmaslik uchun nusxa olish

    for item, details in fulfillment_cart.items():
        quantity_needed = details[0]  # Buyurtma qilingan miqdor
        
        if item in updated_inventory:
            current_stock = updated_inventory[item][0]  # Do'kondagi mavjud miqdor

            if current_stock >= quantity_needed:
                updated_inventory[item][0] -= quantity_needed  # Miqdorni kamaytirish
            
            # Agar mahsulot nolga tushsa, uni "Out of Stock" qilib qo'yish
            if updated_inventory[item][0] == 0:
                updated_inventory[item][0] = "Out of Stock"

    return updated_inventory

