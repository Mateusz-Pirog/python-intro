import math  # Importujemy moduł math, aby wykorzystać jedną z jego funkcji

# Tworzenie dwóch list
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

# Łączenie dwóch list za pomocą funkcji zip()
# https://docs.python.org/3/library/functions.html#zip
zipped_lists = list(zip(list1, list2))
print("Połączone listy:", zipped_lists)

# Próba wykonania operacji z obsługą wyjątku
try:
    number = -9  # Przykładowa liczba ujemna
    result = math.sqrt(number)  # Próba obliczenia pierwiastka kwadratowego z liczby ujemnej
except ValueError as e:
    print("Błąd!", e)  # Obsługa wyjątku dla liczb ujemnych w funkcji sqrt()
    # https://docs.python.org/3/library/exceptions.html#ValueError
