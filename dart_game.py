def score(x, y):
    distance = (x**2 + y**2) ** 0.5  # Dartning markazdan uzoqligi (Pifagor teoremasi)
    
    if distance > 10:
        return 0
    elif distance > 5:
        return 1
    elif distance > 1:
        return 5
    else:
        return 10

# Test qilish
print(score(0, 0))   # 10 (bullseye)
print(score(2, 3))   # 5 (middle circle)
print(score(6, 8))   # 1 (outer circle)
print(score(10, 10)) # 0 (outside)
