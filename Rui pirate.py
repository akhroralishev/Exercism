"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    """
    :param record: tuple - (xazina nomi, kardinata) juftligi.
    :return: str - ajratilgan xarita koordinatasi.
    """
    return record[1]  # Tuplning ikkinchi elementi koordinata
    
record = ("Oltin tanga", "B4")
print(get_coordinate(record))  # Natija: "B4"
    



def convert_coordinate(coordinate):
    """Harita kardinatasini alohida qismlarga ajratib, tupl shaklida qaytaradi.

    :param coordinate: str - xarita kardinatasi.
    :return: tuple - kardinataning harf va raqam qismi alohida bo‘lgan juftlik.
    """
    return (coordinate[0], coordinate[1:])  # Harf va raqam qismini ajratish


def compare_records(azara_record, rui_record):
    """Ikki turdagi yozuvlarni taqqoslab, ularning koordinatalari bir xil ekanligini aniqlaydi.

    :param azara_record: tuple - (xazina nomi, koordinata) juftligi.
    :param rui_record: tuple - (joylashuv, (koordinata_harf, koordinata_son), kvadrant) uchligi.
    :return: bool - koordinatalar mos keladimi?
    """
    
    return azara_record[1] == "".join(rui_record[1])  # Tuple ichidagi harf va raqamni birlashtiramiz


def create_record(azara_record, rui_record):
    """Ikki turdagi yozuvlarni birlashtirib, yangi umumiy yozuv yaratadi.

    :param azara_record: tuple - (xazina nomi, koordinata) juftligi.
    :param rui_record: tuple - (joylashuv, koordinata tuple, kvadrant) uchligi.
    :return: tuple yoki str - agar mos kelsa, birlashtirilgan yozuv, aks holda "not a match".
    """
    
    # Agar koordinatalar mos kelsa, birlashtirilgan tuple qaytariladi
    if azara_record[1] == "".join(rui_record[1]):
        return azara_record + rui_record  # Ikkita tuple ni birlashtirish
    
    return "not a match"  # Agar mos kelmasa, matn qaytariladi


def clean_up(combined_record_group):
    """Birlashgan yozuv guruhini tartibga solib, ortiqcha ma'lumotlarni olib tashlaydi.

    :param combined_record_group: tuple - har bir ishtirokchining alohida yozuvi mavjud bo‘lgan tuple.
    :return: str - ortiqcha koordinatalar olib tashlangan, har bir yozuv alohida qatorda bo‘lgan toza natija.
    """
    
    cleaned_records = [str((record[0], record[2], record[3], record[4])) for record in combined_record_group]
    
    return "\n".join(cleaned_records) + "\n"  # Oxiriga yangi qator qo‘shamiz
