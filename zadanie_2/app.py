import re
import unicodedata
from datetime import datetime


def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))


def calculate_area(shape, *dimensions):
    if shape == "circle" and len(dimensions) == 1:
        return 3.14 * dimensions[0] ** 2
    elif shape == "rectangle" and len(dimensions) == 2:
        return dimensions[0] * dimensions[1]
    elif shape == "triangle" and len(dimensions) == 2:
        return 0.5 * dimensions[0] * dimensions[1]
    else:
        raise ValueError("Invalid shape or dimensions")


def process_list(data):
    return sorted(set(data))


def convert_date_format(date_str, from_format="%Y-%m-%d", to_format="%d-%m-%Y"):
    try:
        return datetime.strptime(date_str, from_format).strftime(to_format)
    except ValueError:
        return "Invalid date format"


def is_palindrome(text):
    # Normalizacja tekstu (usunięcie znaków diakrytycznych i konwersja na małe litery)
    text = unicodedata.normalize("NFD", text)  # Normalizuje do formy rozłożonej
    text = "".join(c for c in text if unicodedata.category(c) != "Mn")  # Usunięcie znaków diakrytycznych

    # Usunięcie niealfanumerycznych znaków (interpunkcja, spacje)
    cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', text.lower())

    # Porównanie tekstu z jego odwrotnością
    return cleaned_text == cleaned_text[::-1]
