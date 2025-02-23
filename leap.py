def leap_year(year):  # Funksiya nomini testga moslashtirdik
    """Kabisa yil ekanligini aniqlovchi funksiya"""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False

def main():
    try:
        year = int(input("Yilni kiriting: "))  # Foydalanuvchidan butun son sifatida kiritish talab qilinadi
        if year < 0:
            print("Musbat yil kiriting.")
            return

        if leap_year(year):  # Yangilangan funksiya nomi
            print(f"{year} kabisa yil!")
        else:
            print(f"{year} kabisa yil emas.")

    except ValueError:
        print("Noto‘g‘ri kiritish! Butun son kiriting.")

if __name__ == "__main__":
    main()
