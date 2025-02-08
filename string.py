"""Functions to help edit essay homework using string manipulation."""


def capitalize_title(title):
    """Berilgan matndagi har bir so‘zning birinchi harfini katta qilish.

    :param title: str - Katta harflar bilan boshlanishi kerak bo‘lgan matn.
    :return: str - Har bir so‘zning birinchi harfi katta qilingan matn.
    """
    return title.title()  # Har bir so‘zning birinchi harfini katta harfga o‘zgartirish


def check_sentence_ending(sentence):
    """Jumlani tekshirib, oxirida nuqta (.) borligini aniqlaydi.

    :param sentence: str - Tekshirilishi kerak bo‘lgan jumla.
    :return: bool - Agar jumla nuqta bilan tugasa True, aks holda False qaytariladi.
    """
    return sentence.endswith(".")  # Agar oxiri "." bo‘lsa, True qaytaradi, aks holda False


def clean_up_spacing(sentence):
    """Jumlani boshida va oxirida bo‘sh joy (whitespace) yo‘qligini tekshirib, uni tozalaydi.

    :param sentence: str - Jumlani boshidagi va oxiridagi bo‘sh joylarni olib tashlash kerak.
    :return: str - Boshidagi va oxiridagi bo‘sh joylar olib tashlangan toza jumla.
    """
    return sentence.strip()  # Bosh va oxiridagi bo‘sh joylarni olib tashlaydi



def replace_word_choice(sentence, old_word, new_word):
    """Berilgan jumladagi eski so‘zni yangi so‘z bilan almashtiradi.

    :param sentence: str - So‘zlarni almashtirish kerak bo‘lgan jumla.
    :param old_word: str - Almashtirilishi kerak bo‘lgan so‘z.
    :param new_word: str - Yangi so‘z bilan almashtirish uchun.
    :return: str - Eski so‘z yangi so‘z bilan almashtirilgan jumla.
    """
    return sentence.replace(old_word, new_word)  # Eski so‘zni yangi so‘z bilan almashtirish

