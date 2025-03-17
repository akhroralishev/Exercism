def is_armstrong_number(number):
    num_str = str(number)  # bu f/ya sonni stringga o'girdi
    num_digits = len(num_str)  # bu f/ya raqamlar sonini aniqlaydi
    total = sum(int(digit) ** num_digits for digit in num_str)  # bu f/ya har bir raqamni darajaga oshirib, yig'indini topadi
    return total == number  # bu f/ya natijani tekshiradi


