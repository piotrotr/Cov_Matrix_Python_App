from tkinter import messagebox
import time
import pandas as pd


def validate_year_range(year_from, year_to, df):
    """
    Funkcja wywoływana jest w 3 oknie programu przez funkcję save_years(entry_year_from, entry_year_to).
    Odpowiada za sprawdzenie poprawnosci wpisanych danych
    (czy lata są liczbami całkowitymi z zakresu odpowiadającego wartosciom z 1 kolumny pliku Excel
    oraz czy rok początkowy jest nie większy od końcowego).
    """
    try:
        year_from = int(year_from)
        year_to = int(year_to)
        if year_from < df.iat[0, 0] or year_to > df.iat[-1 , 0]:
            raise ValueError(f"Rok musi być w zakresie od {df.iat[0, 0]} do {df.iat[-1, 0]}")
        if year_from > year_to:
            raise ValueError("Rok początkowy nie może być większy niż rok końcowy.")
        return year_from, year_to
    except ValueError:
        messagebox.showerror("Błąd", f"Wpisz liczby całkowite z zakresu {df.iat[0, 0]}  do {df.iat[-1, 0]}")
        return None, None

# Sekcja testowa
if __name__ == "__main__":
    print("Definiujemy testowy DataFrame: zawiera liczby całkowite z przedziału [1000; 1200)")
    df = pd.DataFrame(list(range(1000, 1200))) #definiujemy testowy DataFrame
    # Test dla prawidłowego zakresu
    year_from, year_to = validate_year_range("1000", "1100", df)
    time.sleep(1)
    print("Lata 1000 i 1100 należą do wymaganego zakresu, więc brak informacji o błędzie")
    # Test dla nieprawidłowego zakresu (zbyt duży rok)
    time.sleep(3)
    year_from, year_to = validate_year_range("1123", "1800", df)
    print("Rok 1800 nie należy do wymaganego zakresu, więc pojawia się informacja o błędzie")
    time.sleep(1)

    print("Zmieniamy testowy DataFrame: zawiera liczby całkowite z przedziału [1991;2024)")
    df = pd.DataFrame(list(range(1991, 2024)))
    # Test dla nieprawidłowego zakresu (zbyt mały rok)
    year_from, year_to = validate_year_range("900", "2020", df)
    print("Rok 900 nie należy do wymaganego zakresu, więc pojawia się informacja o błędzie")
    time.sleep(1)
    # Test dla nieprawidłowego zakresu (rok początkowy większy niż końcowy)
    year_from, year_to = validate_year_range("2000", "1995", df)
    print("Rok końcowy jest mniejszy od początkowego, więc pojawia się informacja o błędzie")

