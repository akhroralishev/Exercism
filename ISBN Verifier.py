def is_valid(isbn: str) -> bool:
    # Remove all hyphens from the input string
    processed = isbn.replace('-', '')
    
    # Check if the length is exactly 10 characters
    if len(processed) != 10:
        return False
    
    # Validate characters
    for i in range(9):
        if not processed[i].isdigit():
            return False
    
    last_char = processed[9]
    if not (last_char.isdigit() or last_char == 'X'):
        return False
    
    total = 0
    for i in range(10):
        char = processed[i]
        value = 10 if (i == 9 and char == 'X') else int(char)
        total += value * (10 - i)
    
    return total % 11 == 0
    
