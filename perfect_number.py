import math

def classify(number):
    if type(number) is not int or number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    
    if number == 1:
        return 'deficient'
    
    sum_divisors = 1  # 1 is a proper divisor for numbers > 1
    sqrt_n = int(math.sqrt(number))
    
    for i in range(2, sqrt_n + 1):
        if number % i == 0:
            sum_divisors += i
            counterpart = number // i
            if counterpart != i and counterpart != number:
                sum_divisors += counterpart
    
    if sum_divisors == number:
        return 'perfect'
    elif sum_divisors > number:
        return 'abundant'
    else:
        return 'deficient'
