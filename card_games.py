"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Berilgan raqamni va undan keyingi ikki raqamni o‘z ichiga olgan ro‘yxat yaratadi.

    :param number: int - Hozirgi raund raqami.
    :return: list - Hozirgi raund va undan keyingi ikkita raund raqamlari.
    """
    return [number, number + 1, number + 2]  # Hozirgi va keyingi ikkita raundni ro‘yxatga qo‘shish


def concatenate_rounds(rounds_1, rounds_2):
    """Ikki raund ro‘yxatini birlashtirib, umumiy ro‘yxat hosil qiladi.

    :param rounds_1: list - Birinchi o‘ynalgan raundlar.
    :param rounds_2: list - Ikkinchi o‘ynalgan raundlar.
    :return: list - Ikkala ro‘yxatni birlashtirib, barcha raundlarni qaytaradi.
    """
    return rounds_1 + rounds_2  # Ikki ro‘yxatni birlashtirish



def list_contains_round(rounds, number):
    """Berilgan raundlar ro‘yxati ichida ma’lum bir raund mavjudligini tekshiradi.

    :param rounds: list - O‘ynalgan raundlar ro‘yxati.
    :param number: int - Tekshirilayotgan raund raqami.
    :return: bool - Agar raund o‘ynalgan bo‘lsa, True; aks holda, False qaytaradi.
    """
    return number in rounds  # 'in' operatori bilan mavjudligini tekshirish



def card_average(hand):
    """Ro‘yxatdagi kartalar qiymatining o‘rtacha qiymatini hisoblaydi.

    :param hand: list - Qo‘ldagi kartalar ro‘yxati.
    :return: float - Qo‘ldagi kartalar o‘rtacha qiymati.
    """
    return sum(hand) / len(hand)  # Kartalar yig‘indisini ularning soniga bo‘lish



def approx_average_is_average(hand):
    """Qo‘ldagi kartalar uchun hisoblangan haqiqiy o‘rtacha qiymat, 
    birinchi va oxirgi kartalar o‘rtachasiga yoki markaziy kartaning qiymatiga tengligini tekshiradi.

    :param hand: list - Qo‘ldagi kartalar ro‘yxati.
    :return: bool - Agar taxminiy o‘rtacha haqiqiy o‘rtachaga teng bo‘lsa, True qaytaradi, aks holda False.
    """
    true_average = sum(hand) / len(hand)  # Haqiqiy o‘rtacha qiymat
    approx1 = (hand[0] + hand[-1]) / 2   # Birinchi va oxirgi kartalar o‘rtachasi
    approx2 = hand[len(hand) // 2]       # Ro‘yxatning o‘rtasidagi kartaning qiymati
    
    return true_average in (approx1, approx2)  # Agar haqiqiy o‘rtacha approx1 yoki approx2 ga teng bo‘lsa, True


def average_even_is_average_odd(hand):
    """Juft indeksli kartalar o‘rtacha qiymati toq indeksli kartalar o‘rtacha qiymatiga tengligini tekshiradi.

    :param hand: list - Qo‘ldagi kartalar ro‘yxati.
    :return: bool - Agar juft indeksli va toq indeksli kartalar o‘rtacha qiymati teng bo‘lsa, True qaytaradi.
    """
    even_cards = hand[0::2]  # Juft indeksli kartalar (0, 2, 4, ...)
    odd_cards = hand[1::2]   # Toq indeksli kartalar (1, 3, 5, ...)
    
    even_avg = sum(even_cards) / len(even_cards) if even_cards else 0  # Juft indeksli o‘rtacha
    odd_avg = sum(odd_cards) / len(odd_cards) if odd_cards else 0  # Toq indeksli o‘rtacha
    
    return even_avg == odd_avg  # Agar ikkala o‘rtacha teng bo‘lsa, True



def maybe_double_last(hand):
    """Agar oxirgi karta 'J' (Jack) bo‘lsa, uning qiymatini 2 ga ko‘paytiradi.

    :param hand: list - Qo‘ldagi kartalar ro‘yxati.
    :return: list - Agar oxirgi karta J bo‘lsa, uning qiymati ikki barobar oshirilgan yangi ro‘yxat qaytariladi.
    """
    if hand and hand[-1] == 11:  # Agar ro‘yxat bo‘sh bo‘lmasa va oxirgi karta 'J' bo‘lsa
        hand[-1] *= 2  # Oxirgi kartaning qiymatini 2 ga ko‘paytirish
    
    return hand  # O‘zgartirilgan ro‘yxatni qaytarish

