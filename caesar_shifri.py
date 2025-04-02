def rotate(text, key):
    key %= 26
    result = []
    for char in text:
        if char.islower():
            base = ord('a')
            shifted = (ord(char) - base + key) % 26 + base
            result.append(chr(shifted))
        elif char.isupper():
            base = ord('A')
            shifted = (ord(char) - base + key) % 26 + base
            result.append(chr(shifted))
        else:
            result.append(char)
    return ''.join(result)
