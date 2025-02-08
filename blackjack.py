"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.

    1. 'J', 'Q', 'K' = 10
    2. 'A' = 1
    3. '2' - '10' = numerical value.
    """
    
    if card in ['J', 'Q', 'K']:
        return 10
    elif card == 'A':
        return 1
    else:
        return int(card)

# Test cases
print(value_of_card('J'))  # 10
print(value_of_card('A'))  # 1
print(value_of_card('5'))  # 5
print(value_of_card('10')) # 10


def card_value(card):
    """Return the numeric value of a card."""
    if card in ['J', 'Q', 'K']:
        return 10
    elif card == 'A':
        return 1
    else:
        return int(card)  # '2' - '10' ni son sifatida qaytaradi

def higher_card(card_one, card_two):
    """Determine which card has a higher value."""
    value_one = card_value(card_one)
    value_two = card_value(card_two)

    if value_one > value_two:
        return card_one
    elif value_two > value_one:
        return card_two
    else:
        return (card_one, card_two)  # Ikkalasi teng bo‘lsa, tuple qaytariladi


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    def card_value(card):
        """Helper function to get numerical value of a card."""
        if card in ('J', 'Q', 'K'):
            return 10
        elif card == 'A':
            return 11
        else:
            return int(card)

    # Hisoblash
    first_value = card_value(card_one)
    second_value = card_value(card_two)
    
    total = first_value + second_value
    
    # Ace uchun eng yaxshi qiymatni aniqlash
    return 1 if total + 11 > 21 else 11



def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt.
    :return: bool - is the hand a blackjack (two cards worth 21).
    """

    def card_value(card):
        """Helper function to get numerical value of a card."""
        if card in ('J', 'Q', 'K'):
            return 10
        elif card == 'A':
            return 11
        else:
            return int(card)

    # Kartalar qiymatini hisoblash
    total = card_value(card_one) + card_value(card_two)

    # Blackjack bo‘lishi uchun faqat 2 ta karta va ular yig‘indisi 21 bo‘lishi kerak
    return total == 21



def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    def card_value(card):
        """Helper function to get numerical value of a card."""
        if card in ('J', 'Q', 'K'):
            return 10
        elif card == 'A':
            return 11  # Split qilsa, ikkita "A" bo‘lib qoladi
        else:
            return int(card)

    # Kartalar qiymatini tekshiramiz
    return card_value(card_one) == card_value(card_two)


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand be doubled down? (i.e. totals 9, 10 or 11 points).
    """

  

    # Kartalar qiymatini hisoblash
    total = card_value(card_one) + card_value(card_two)

    # Double Down shartini tekshiramiz (faqat 9, 10 yoki 11 bo‘lsa)
    return total in (9, 10, 11)
