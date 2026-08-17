from datetime import datetime

def calculate_tax(TL, CC, date1, date2):

    d1 = datetime.strptime(date1, "%d/%m/%Y")
    d2 = datetime.strptime(date2, "%d/%m/%Y")

    dif = abs((d2 - d1).days)
    months_old = dif // 30

    tax_brackets = [
        (0, 360, 0),
        (361, 730, 14),
        (731, 1095, 21),
        (1096, 1460, 25),
        (1461, 1825, 32),
        (1826, 2190, 35),
        (2191, 2555, 39),
        (2556, 2920, 42),
        (2921, 1500000, 46)
    ]

    cc_tax_brackets = [
        (0, 125, 0),
        (126, 249, 2),
        (250, 900, 7),
        (901, 1400, 12),
        (1401, 1600, 14),
        (1601, 1800, 17),
        (1801, 300000, 25),
    ]

    tax_amount = 0
    registration_tax = 0
    age_rate = 0
    cc_rate = 0

    for lower, upper, rate in tax_brackets:
        if lower <= dif <= upper:
            age_rate = rate
            tax_amount = TL - (TL * age_rate / 100)
            break

    tax_amount += 100

    for lower, upper, rate in cc_tax_brackets:
        if lower <= CC <= upper:
            cc_rate = rate
            registration_tax = tax_amount * cc_rate / 100
            break

    return tax_amount, cc_rate, age_rate, months_old, registration_tax
