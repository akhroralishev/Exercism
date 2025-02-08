"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Barcha talabalar ballarini eng yaqin butun songa yaxlitlaydi.

    :param student_scores: list - talabalar imtihon ballari (float yoki int).
    :return: list - talabalar ballarining yaxlitlangan qiymatlari.
    """
    return [round(score) for score in student_scores]  # Har bir ballni yaxlitlash
scores = [89.6, 74.2, 91.9, 67.5]
rounded_scores = round_scores(scores)
print(rounded_scores)  # [90, 74, 92, 68]


def count_failed_students(student_scores):
    """Berilgan guruhdan imtihondan o'ta olmagan talabalar sonini hisoblaydi.

    :param student_scores: list - talabalar imtihon ballari (int qiymatlar).
    :return: int - 40 yoki undan past ball olgan talabalar soni.
    """
    return sum(1 for score in student_scores if score <= 40)  # 40 yoki undan past ballarni sanash
scores = [35, 80, 40, 90, 20, 50, 39]
failed_count = count_failed_students(scores)
print(failed_count)  # 3



def above_threshold(student_scores, threshold):
    """Berilgan chegaradan yuqori yoki unga teng bo‘lgan ballarni aniqlaydi.

    :param student_scores: list - talabalar imtihon ballari (int qiymatlar).
    :param threshold: int - "eng yaxshi" ball bo‘lishi uchun minimal chegara.
    :return: list - threshold dan katta yoki teng bo‘lgan ballar ro‘yxati.
    """
    return [score for score in student_scores if score >= threshold]  # Chegaradan yuqori ballarni tanlash
scores = [50, 80, 40, 90, 20, 60, 39]
best_scores = above_threshold(scores, 60)
print(best_scores)  # [80, 90, 60]



def letter_grades(highest):
    """Berilgan eng yuqori baho asosida harfli baholar chegaralarini yaratadi.

    :param highest: int - eng yuqori imtihon balli.
    :return: list - D, C, B va A baholari uchun quyi chegara ballari ro‘yxati.
    
    Masalan, agar eng yuqori ball 100 bo‘lsa va 40 yoki undan past ball "o‘tish" 
    sharti bo‘lmasa, natija quyidagicha bo‘ladi: [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """
    step = (highest - 40) // 4  # Har bir baho diapazonining oraliq uzunligini hisoblash
    return [41 + step * i for i in range(4)]  # D, C, B va A baholari uchun quyi chegaralarni yaratish
print(letter_grades(100))  # [41, 56, 71, 86]
print(letter_grades(80))   # [41, 51, 61, 71]



def student_ranking(student_scores, student_names):
    """Talabalar reytingini, ismini va ballarini kamayish tartibida tartiblaydi.

    :param student_scores: list - talabalar ballari (kamayish tartibida).
    :param student_names: list - talabalar ismlari (ballar bo‘yicha kamayish tartibida).
    :return: list - ["<reyting>. <talaba ismi>: <ball>"] formatidagi ro‘yxat.
    """
    return [f"{rank + 1}. {name}: {score}" for rank, (name, score) in enumerate(zip(student_names, student_scores))]
names = ["Ali", "Bobur", "Sanjar"]
scores = [95, 85, 75]
ranking = student_ranking(scores, names)
print(ranking)


def perfect_score(student_info):
    """Imtihondan 100 ball olgan birinchi talabani aniqlaydi.

    :param student_info: list - har bir talaba uchun [<ism>, <ball>] ko‘rinishidagi ro‘yxat.
    :return: list - birinchi [<talaba ismi>, 100] yoki agar topilmasa, bo‘sh ro‘yxat [].
    """
    for student in student_info:
        if student[1] == 100:  # Agar talabani balli 100 bo‘lsa
            return student  # Ushbu talabani qaytarish
    return []  # Agar 100 ball olgan talaba bo‘lmasa, bo‘sh ro‘yxat qaytarish
students = [["Ali", 95], ["Bobur", 100], ["Sanjar", 100]]
print(perfect_score(students))  # ['Bobur', 100]

students2 = [["Ali", 95], ["Sanjar", 98]]
print(perfect_score(students2))  # []

