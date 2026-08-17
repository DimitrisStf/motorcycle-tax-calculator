from motorcycle import calculate_tax

TL = float(input("Τιμή λιανικής; "))
CC = int(input("Κυβικά; "))

date1 = input("Ημερομηνία κυκλοφορίας: ")
date2 = input("Ημερομηνία ΔΕΦΚ: ")

tax_amount, cc_rate, age_rate, months_old, registration_tax = calculate_tax(
    TL, CC, date1, date2
)

print("Φορολογητέο ποσό:", tax_amount, "€")
print(f"Φορολογικός συντελεστής κυβισμού {cc_rate}%")
print(f"Ποσοστό έκπτωσης παλαιότητας {age_rate}%")
print(f"Μήνες παλαιότητας {months_old}")
print(f"Τέλος ταξινόμησης: {registration_tax:.2f} €")
