"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D, A, B, C, D, ...
    """

    seat_letters = ['A', 'B', 'C', 'D']
    for i in range(number):
        yield seat_letters[i % 4]  # Modulus operator helps cycle through letters

# Example usage:
for seat in generate_seat_letters(10):
    print(seat, end=" ")  # Output: A B C D A B C D A B

"""Functions to automate Conda airlines ticketing system."""


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B
    """

    seat_letters = ['A', 'B', 'C', 'D']
    row = 1
    count = 0

    while count < number:
        if row == 13:  # Skip row 13
            row += 1

        for seat in seat_letters:
            if count < number:
                yield f"{row}{seat}"
                count += 1

        row += 1  # Move to the next row

# Example usage:
for seat in generate_seats(10):
    print(seat, end=" ")  # Output: 1A 1B 1C 1D 2A 2B 2C 2D 3A 3B


"""Functions to automate Conda airlines ticketing system."""


def generate_seats(number):
    """Generate a series of identifiers for airline seats."""
    seat_letters = ['A', 'B', 'C', 'D']
    row = 1
    count = 0

    while count < number:
        if row == 13:  # Skip row 13
            row += 1

        for seat in seat_letters:
            if count < number:
                yield f"{row}{seat}"
                count += 1

        row += 1


def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}
    """

    seats = generate_seats(len(passengers))  # Generate required number of seats
    return {passenger: next(seats) for passenger in passengers}  # Assign seats


# Example usage:
passengers_list = ["Adele", "Björk", "Charlie", "David"]
assigned_seats = assign_seats(passengers_list)
print(assigned_seats)  # Output: {'Adele': '1A', 'Björk': '1B', 'Charlie': '1C', 'David': '1D'}

"""Functions to automate Conda airlines ticketing system."""


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.
    """

    for seat in seat_numbers:
        code = f"{seat}{flight_id}"[:12]  # Trim if too long
        yield code.ljust(12, '0')  # 'X' o‘rniga '0' bilan to‘ldirish

# Test
test_data = [
    (["12A", "38B", "69C", "102B"], "KL1022"),
    (["22C", "88B", "33A", "44B"], "DL1002")
]
expected_results = [
    ['12AKL1022000', '38BKL1022000', '69CKL1022000', '102BKL102200'],
    ['22CDL1002000', '88BDL1002000', '33ADL1002000', '44BDL1002000']
]

# Checking the results
for (seats, flight), expected in zip(test_data, expected_results):
    result = list(generate_codes(seats, flight))
    assert result == expected, f"Test failed: expected {expected}, got {result}"

print("All tests passed! ✅")
