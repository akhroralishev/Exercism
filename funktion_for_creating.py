"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """ Berilgan so'zni oling va "un" prefiksini qo'shing.

    :param so'zi: str - ildiz so'zni o'z ichiga olgan.
    :return: str - 'un' oldiga qo'yilgan ildiz so'z.
    """
    return "un" + word  # 'un' prefiksini qo‘shish



def make_word_groups(vocab_words):
    """Prefiks va so'zlardan iborat ro'yxatni satrga o'tkazing 
    prefiksdan keyin old qo'shimchali so'zlar bilan.

    :param vocab_words: ro'yxati - birinchi indeksda prefiksli lug'at so'zlari.
    :return: str - prefiksdan keyin lug'at so'zlari bilan
            prefiks qo'llaniladi.
    """
    prefix = vocab_words[0]  # Birinchi element prefiks
    words_with_prefix = [prefix + word for word in vocab_words[1:]]  # Barcha so‘zlarga prefiks qo‘shiladi
    return " :: ".join([prefix] + words_with_prefix)  # Natijani birlashtirish



def remove_suffix_ness(word):
    """Imlo qoidalariga rioya qilingan holda so‘zdan 'ness' qo‘shimchasini olib tashlang."""

    if word.endswith("ness"):
        root = word[:-4]  # 'ness' ni olib tashlash
        if root.endswith("i"):
            root = root[:-1] + "y"  # "happiness" → "happy"
        return root
    return word  # Agar 'ness' bo‘lmasa, o‘zgarishsiz qaytarish



def adjective_to_verb(sentence, index):
    """Gap ichidagi sifatni fe'lga o'zgartiring.

    :param jumla: str - bu so'zni jumlada ishlatadi.
    :param indeksi: int - olib tashlash va o'zgartirish uchun so'z indeksi.
    :return: str - ajratib olingan sifatni fe'lga o'zgartiruvchi so'z.
    """
    words = sentence.strip().split()  # Gapni so‘zlarga ajratish
    word = words[index].rstrip(".")   # Indeksdagi so‘zni olish va nuqtani olib tashlash
    return word + "en"  # Fe’l shakliga o‘tkazish

