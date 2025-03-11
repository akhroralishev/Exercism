def get_list_of_wagons(*wagon_ids):
    """
    Accepts an arbitrary number of wagon IDs and returns them as a single list.
    
    :param wagon_ids: Positive integers representing wagon IDs
    :return: List of wagon IDs
    """
    return list(wagon_ids)

# Test
print(get_list_of_wagons(1, 7, 12, 3, 14, 8, 5))

def fix_list_of_wagons(train_wagons, missing_wagons):
    """
    Fix the order of the train wagons by:
    - Moving the first two wagons to the end.
    - Inserting missing wagons immediately after the locomotive (ID = 1).
    
    :param train_wagons: List of wagon IDs where the first element is locomotive (1)
    :param missing_wagons: List of missing wagon IDs
    :return: Fixed list of wagons
    """
    # Locomotive ID (1) ni aniqlaymiz
    loco_index = train_wagons.index(1)
    
    # Lokomotivdan keyingi qism
    correct_order = [1] + missing_wagons + train_wagons[loco_index + 1:]
    
    # Birinchi ikkita vagonni oxiriga ko‘chiramiz
    correct_order.extend(train_wagons[:loco_index])  

    return correct_order

# Test
print(fix_list_of_wagons([2, 5, 1, 7, 4, 12, 6, 3, 13], [3, 17, 6, 15]))
def add_missing_stops(route_info, **stops):
    """
    Updates the routing dictionary with additional stops.

    :param route_info: A dictionary containing 'from' and 'to' locations.
    :param stops: Keyword arguments representing stop_number=city.
    :return: The updated routing dictionary with a new key 'stops'.
    """
    # Stopsni qiymatlarini tartib bilan olish
    sorted_stops = [stops[key] for key in sorted(stops.keys())]
    route_info["stops"] = sorted_stops
    return route_info

# Test
print(add_missing_stops(
    {"from": "New York", "to": "Miami"},
    stop_1="Washington, DC", stop_2="Charlotte",
    stop_3="Atlanta", stop_4="Jacksonville", stop_5="Orlando"
))


def extend_route_information(route_info, additional_info):
    """
    Merge two dictionaries containing train route information.

    :param route_info: Dictionary with the route's origin and destination.
    :param additional_info: Dictionary with extra details about the route.
    :return: A single dictionary containing all the route information.
    """
    # update() metodi orqali ikkinchi lug‘atni birinchi lug‘atga qo‘shamiz
    route_info.update(additional_info)
    return route_info

# Test
print(extend_route_information({"from": "Berlin", "to": "Hamburg"}, {"length": "100", "speed": "50"}))
def fix_wagon_depot(depot):
    """
    Reorders the given list of wagons so that each row has different colors 
    and each column aligns by color.

    :param depot: A list of three sublists, each containing three tuples (wagon ID, wagon color).
    :return: A correctly reordered list of wagon rows.
    """
    # zip(*depot) yordamida ustunlarni bir-biriga almashtiramiz
    fixed_depot = list(map(list, zip(*depot)))
    return fixed_depot

# Test
print(fix_wagon_depot([
    [(2, "red"), (4, "red"), (8, "red")],
    [(5, "blue"), (9, "blue"), (13, "blue")],
    [(3, "orange"), (7, "orange"), (11, "orange")]
]))


