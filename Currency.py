"""Functions for calculating steps in exchanging currency.

Python numbers documentation: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Overview of exchanging currency when travelling: https://www.compareremit.com/money-transfer-tips/guide-to-exchanging-currency-for-overseas-travel/
"""



#
def exchange_money(budget, exchange_rate):
    """
    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """
    return budget / exchange_rate


def get_change(budget, exchanging_value):
    """
    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """
    return budget - exchanging_value

# Test misollari:
print(get_change(463000, 5000))   # 458000
print(get_change(1250, 120))      # 1130
print(get_change(15000, 1380))    # 13620



def get_value_of_bills(denomination, number_of_bills):
    """
    :param denomination: int - the value of a bill.
    :param number_of_bills: int - total number of bills.
    :return: int - calculated value of the bills.
    """
    return denomination * number_of_bills

# Test misollari:
print(get_value_of_bills(10000, 128))  # 1280000
print(get_value_of_bills(50, 360))     # 18000
print(get_value_of_bills(200, 200))    # 40000



def get_number_of_bills(amount, denomination):
    """
    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills that can be obtained from the amount.
    """
    return amount // denomination

# Test misollari:
print(get_number_of_bills(163270, 50000))  # 3
print(get_number_of_bills(54361, 1000))     # 54



def get_leftover_of_bills(amount, denomination):
    """
    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: float - the amount that is "leftover", given the current denomination.
    """
    return amount % denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    # 1. Spreadni hisoblash
    spread_fee = exchange_rate * (spread / 100)
    total_exchange_rate = exchange_rate + spread_fee

    # 2. Valyuta almashinuvi
    total_value = budget / total_exchange_rate

    # 3. Denominatsiya bo'yicha qisqartirish
    max_value = (total_value // denomination) * denomination

    return int(max_value)


