"""Shaxmat donasida birinchi katagida 1ta dona bug`doy ikkinchi katagida esa 2 dona , 3-katagida esa 4 dona , hullas har bitta keyingi katak o`zidan oldingisidan ikki barovar ko`p, Shaxmat donasida 64ta katak mavjud, Savol shaxmat donasida jami necha bug`doy donalari mavjud?"""
def grains_on_square(square: int) -> int:
    if square < 1 or square > 64:
        raise ValueError("Square number must be between 1 and 64.")
    return 2 ** (square - 1)

def total_grains_on_chessboard() -> int:
    return sum(grains_on_square(i) for i in range(1, 65))

# Example usage:
try:
    square = 5  # Change this number to test different squares
    print(f"Grains on square {square}: {grains_on_square(square)}")
    print(f"Total grains on chessboard: {total_grains_on_chessboard()}")
except ValueError as e:
    print(e)
