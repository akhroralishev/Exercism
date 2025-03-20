def is_isogram(string):
    string = string.lower()  # Katta-kichik harflarni bir xil ko'rib chiqish
    seen_letters = set()
    
    for char in string:
        if char.isalpha():  # Faqat harflarni tekshiramiz, bo'sh joy va chiziqchalarni hisobga olmaymiz
            if char in seen_letters:
                return False
            seen_letters.add(char)
    
    return True

# Test misollar
print(is_isogram("lumberjacks"))  # True
print(is_isogram("background"))   # True
print(is_isogram("six-year-old")) # True
print(is_isogram("isograms"))     # False
