"""Functions to manage and organize queues at Chaitana's roller coaster."""


def add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name):
    """Kishini 'express' yoki 'normal' navbatga qo‘shadi."""
    if ticket_type == 1:
        express_queue.append(person_name)
        return express_queue
    else:
        normal_queue.append(person_name)
        return normal_queue

# Navbatlar ro‘yxati
express = ["Azamat", "Fazliddin"]
normal = ["Abdulloh", "Aliyor"]

# Natijani ekranga chiqarish uchun print() tashqarida
print(add_me_to_the_queue(express, normal, 1, "Doniyor"))  # Express navbatga qo‘shiladi
print(add_me_to_the_queue(express, normal, 0, "Otabek"))   # Normal navbatga qo‘shiladi




def find_my_friend(queue, friend_name):
    """Navbatdan do‘stingizni qidirib, uning indeksini qaytaradi."""
    if friend_name in queue:
        return queue.index(friend_name)  # Indeksni qaytarish
    else:
        return -1  # Topilmasa -1 qaytarish

queue_list = ["Azamat", "Fazliddin", "Abdulloh", "Aliyor", "Doniyor"]

# print() funksiyani chaqirgandan keyin yoziladi
print(find_my_friend(queue_list, "Abdulloh"))  # 2
print(find_my_friend(queue_list, "Doniyor"))  # 4
print(find_my_friend(queue_list, "Otabek"))  # -1


def add_me_with_my_friends(queue, index, person_name):
    """Kech qolgan odamni navbatning muayyan indeksiga qo‘shish.

    :param queue: list - Navbatdagi ismlar ro‘yxati.
    :param index: int - Yangi ismni qo‘shish kerak bo‘lgan indeks.
    :param person_name: str - Qo‘shiladigan shaxsning ismi.
    :return: list - Yangilangan navbat.
    """
    queue.insert(index, person_name)  # Kiritilgan indeksga ism qo‘shish
    return queue  # Yangilangan navbatni qaytarish
queue_list = ["Azamat", "Fazliddin", "Abdulloh", "Aliyor"]

print(add_me_with_my_friends(queue_list, 2, "Doniyor"))  
# ['Azamat', 'Fazliddin', 'Doniyor', 'Abdulloh', 'Aliyor'] (Doniyor 2-joyga qo‘shildi)



def remove_the_mean_person(queue, person_name):
    """Navbatdan betoqat odamni olib tashlash.

    :param queue: list - Navbatdagi ismlar ro‘yxati.
    :param person_name: str - Olib tashlanishi kerak bo‘lgan shaxsning ismi.
    :return: list - Yangilangan navbat.
    """
    if person_name in queue:  # Agar odam navbatda bo‘lsa
        queue.remove(person_name)  # Uni olib tashlash
    return queue  # Yangilangan navbatni qaytarish



def how_many_namefellows(queue, person_name):
    """Navbatda berilgan ism necha marta uchraganini hisoblash.

    :param queue: list - Navbatdagi ismlar ro‘yxati.
    :param person_name: str - Qidirilayotgan ism.
    :return: int - Ushbu ism navbatda necha marta borligi.
    """
    return queue.count(person_name)  # Ismning necha marta uchraganini sanash



def remove_the_last_person(queue):
    """Navbatdagi oxirgi odamni olib tashlaydi va uning ismini qaytaradi.

    :param queue: list - navbatdagi odamlarning ro‘yxati.
    :return: str - oxirgi bo‘lib olib tashlangan odamning ismi.
    """
    return queue.pop() if queue else None  # Agar ro‘yxat bo‘sh bo‘lsa, None qaytaradi



def sorted_names(queue):
    """Navbatdagi ismlarni alifbo tartibida saralaydi va natijani qaytaradi.

    :param queue: list - navbatdagi odamlarning ro‘yxati.
    :return: list - alifbo tartibida saralangan ro‘yxatning nusxasi.
    """
    return sorted(queue)  # Ro‘yxatning asl nusxasini o‘zgartirmasdan saralaydi
queue = ["Akhror", "Bobur", "Muslim"]
sorted_queue = sorted_names(queue)
print(sorted_queue)  # ["Muslim", "Bobur", "Akhror"]
print(queue)  # ["Akhror", "Bobur", "Muslim"] (Asl ro‘yxat o‘zgarmaydi)
