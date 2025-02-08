def eat_ghost(power_pellet_active, touching_ghost):
    """Determine if Pac-Man can eat a ghost.

    :param power_pellet_active: bool - is the power pellet active?
    :param touching_ghost: bool - is Pac-Man touching a ghost?
    :return: bool - can Pac-Man eat the ghost?
    """
    return power_pellet_active and touching_ghost

def score(touching_power_pellet, touching_dot):
    """Determine if Pac-Man has scored.

    :param touching_power_pellet: bool - is Pac-Man touching a power pellet?
    :param touching_dot: bool - is Pac-Man touching a dot?
    :return: bool - has Pac-Man scored?
    """
    return touching_power_pellet or touching_dot

def lose(power_pellet_active, touching_ghost):
    """Determine if Pac-Man has lost the game.

    :param power_pellet_active: bool - is the power pellet active?
    :param touching_ghost: bool - is Pac-Man touching a ghost?
    :return: bool - has Pac-Man lost the game?
    """
    return not power_pellet_active and touching_ghost
def win(has_key, opened_door, collected_treasure, touching_ghost=False):
    """
    has_key: O'yinchi kalitga ega bo'lsa True.
    opened_door: Eshik ochilgan bo'lsa True.
    collected_treasure: Agar o'yinchi xazina to'plagan bo'lsa True.
    touching_ghost: Agar o'yinchi ruhga tegsa True (default qiymat False).
    """
    if touching_ghost:
        return False
    if collected_treasure:
        # Agar xazina to'plangan bo'lsa, g'olib bo'lish uchun kalit va eshik ham kerak.
        return has_key and opened_door
    # Agar xazina to'plamagan bo'lsa, demak barcha nuqtalar yeyilgan va o'yinchi yutadi.
    return True

# Test misollari:
print(win(True, False, False))  # True, chunki xazina to'planmagan (barcha dots yeyilgan)
print(win(True, True, True))    # True, agar kalit bor, eshik ochilgan va xazina to'plangan bo'lsa
print(win(False, True, True))   # False, kalit yo'q, shuning uchun g'alaba emas
print(win(True, True, True, touching_ghost=True))  # False, ruhga tegilgan bo'lsa har doim yutqazadi


# Test chaqiruvlari
print(win(True, True, True, False))   # Ehtimol, True (agar ghostga tegilmagan bo'lsa)
print(win(True, False, True))           # Default touching_ghost=True → False
    
    
    

# Test uchun chaqiruv:
#

# Example usage:
if __name__ == "__main__":
    # Test eat_ghost function
    print(eat_ghost(True, True))  # True
    print(eat_ghost(True, False)) # False
    print(eat_ghost(False, True)) # False

    # Test score function
    print(score(True, False))  # True
    print(score(False, True))  # True
    print(score(False, False)) # False

    # Test lose function
    print(lose(False, True))  # True
    print(lose(True, True))   # False
    print(lose(False, False)) # False

    # Test win function
    print(win(10, 10, True, True))  # True
    print(win(9, 10, True, True))   # False
    print(win(10, 10, False, False)) # True
    print(win(10, 10, False, True))  # False
