import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog, messagebox, Listbox
from tkinter import *
import time
from validate_year_module import *
from cov_matrix_module import *


def click_fun(wn, _ml):
    """
    Funkcja powoduje zamknięcie okna wstępnego i otwarcie pierwszego okna programu.
    """
    wn.destroy()
    root = tk.Tk()
    open_first_win(root)

def open_first_win(root):
    """
    Funkcja otwiera pierwsze okno programu. Nadaje mu tytuł 'Krok 1.'.
    Pozwala na wybór pliku, z którego pobierane są dane.
    Zawiera 3 przyciski: 'Przeglądaj', 'Zatwierdź wybór', 'Dalej',
    które prowadzą odpowiednio do wywołania funkcji:
    browse_files(entry_file_path),
    save_file_path(entry_file_path),
    next(root).
    """
    global state
    state = False
    root.geometry("600x100")
    root.title("Krok 1.")

    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    label_file = tk.Label(frame, text="Wybierz plik danych:")
    label_file.grid(row=0, column=0, padx=5, pady=5)

    button_browse = tk.Button(frame, text="Przeglądaj", command=lambda: browse_files(entry_file_path))
    button_browse.grid(row=0, column=2, padx=5, pady=5)

    entry_file_path = tk.Entry(frame, width=50)
    entry_file_path.grid(row=0, column=1, padx=5, pady=5)

    button_save = tk.Button(frame, text="Zatwierdź wybór.", command=lambda: save_file_path(entry_file_path))
    button_save.grid(row=1, column=0, padx=5, pady=5)

    button_next = tk.Button(frame, text="Dalej.", command=lambda: next(root))
    button_next.grid(row=1, column=1, padx=5, pady=5)


def open_sec_win(root):
    """
    Funkcja otwiera drugie okno programu. Nadaje mu tytuł 'Krok 2.'.
    Tworzy również obiekt DataFrame, z którego pobierane są dane w trakcie dalszej pracy programu.
    Pozwala też na wybór opcji (np indeksów giełdowych) z listy wielokrotnego wyboru.
    Zawiera 3 przyciski: 'Wróć do poprzedniego okna', 'Zatwierdź wybór', 'Dalej',
    które prowadzą odpowiednio do wywołania funkcji:
    go_back(root),
    save_index_list(lb),
    next(root).
    """
    global state
    global df
    state = False
    root.title("Krok 2.")
    frame = tk.Frame(root)
    frame.grid(row=0, column=0, padx=5, pady=5)
    label = tk.Label(frame, text='Wybierz z poniższej listy i kliknij: zatwierdź wybór.')
    label.grid(row=0, column=0, padx=5, pady=5)

    #tworzenie DataFrame
    df = pd.read_excel(input_file, skiprows=[0])

    index_names = df.columns[1:].values.tolist()
    lb = Listbox(root, selectmode=MULTIPLE, height=len(index_names), width=50)
    for x in index_names: lb.insert(END, x)
    lb.grid(row=1, column=0, padx=5, pady=5)

    button_save_indexes = tk.Button(root, text="Zatwierdź wybór.", command=lambda: save_index_list(lb))
    button_save_indexes.grid(row=4, column=0, padx=5, pady=5)

    button_back = tk.Button(root, text="Wróć do poprzedniego okna.", command=lambda: go_back(root))
    button_back.grid(row=3, column=0, padx=5, pady=5)

    button_next = tk.Button(frame, text="Dalej.", command=lambda: next(root))
    button_next.grid(row=2, column=0, padx=5, pady=5)


def open_third_win(root):
    """
    Funkcja otwiera trzecie okno programu. Nadaje mu tytuł 'Krok 3.'.
    Pozwala na wybór zakresu lat odpowiadających wierszom wczytanego pliku.
    Zawiera 2 przyciski: 'Wróć do poprzedniego okna', 'Zatwierdź wybór',
    które prowadzą odpowiednio do wywołania funkcji:
    go_back(root),
    save_years(entry_year_from, entry_year_to).
    """
    global state
    state = False
    root.title("Krok 3.")

    frame = tk.Frame(root)
    frame.grid(row=0, column=0, padx=5, pady=5)

    label = tk.Label(frame, text=f'Podaj zakres lat od {df.iat[0, 0]} do {df.iat[-1, 0]}.')
    label.grid(row=0, column=0, padx=5, pady=5)

    label = tk.Label(frame, text='Od:')
    label.grid(row=1, column=0, padx=5, pady=5)

    label = tk.Label(frame, text='Do:')
    label.grid(row=2, column=0, padx=5, pady=5)

    entry_year_from = tk.Entry(frame)
    entry_year_from.grid(row=1, column=1, padx=5, pady=5)

    entry_year_to = tk.Entry(frame)
    entry_year_to.grid(row=2, column=1, padx=5, pady=5)

    button_save_years = tk.Button(root, text="Zatwierdź wybór.", command=lambda: save_years(entry_year_from, entry_year_to))
    button_save_years.grid(row=3, column=0, padx=5, pady=5)

    button_back = tk.Button(root, text="Wróć do poprzedniego okna.", command=lambda: go_back(root))
    button_back.grid(row=4, column=0, padx=5, pady=5)


def browse_files(entry_file_path):
    """
    Funkcja wywoływana w pierwszym oknie programu, odpowiadająca za możliwosć przeglądania plików.
    """
    filename = filedialog.askopenfilename(filetypes=[("Excel", "*.xlsx")])
    entry_file_path.delete(0, tk.END)
    entry_file_path.insert(0, filename)


def save_file_path(entry_file_path):
    """
    Funkcja wywoływana w pierwszym oknie programu,
    odpowiadająca za zapisanie wybranego pliku do zmiennej input_file.
    """
    global state
    global input_file
    input_file = entry_file_path.get()
    if not input_file:
        messagebox.showerror("Błąd", "Proszę wybrać plik danych.")
        return
    else:
        messagebox.showinfo("Komunikat", "Zapisano scieżkę do pliku.")
        state = True


def next(root):
    """
    Funkcja wywoływana w pierwszym i drugim oknie programu,
    odpowiadająca za przechodzenie do następnego okna,
    pod warunkiem wczesniejszego zatwierdzenia wyboru.
    W przypadku niezatwierdzenia wyboru wyswietlany jest odpowiedni komunikat o błędzie.
    """
    global state
    global licznik
    print(state, licznik)
    if state:
        state = False
        root.destroy()
        root = tk.Tk()
        licznik += 1
        time.sleep(0.5)
        if licznik == 2:

            open_sec_win(root)
        if licznik == 3:
            open_third_win(root)
    else:
        messagebox.showerror("Błąd", "Nie zatwierdzono wyboru.")
        return

def go_back(root):
    """
    Funkcja wywoływana w drugim i trzecim oknie programu,
    odpowiadająca za powrót do wczesniejszego okna.
    """
    global licznik
    licznik -= 1
    root.destroy()
    root = tk.Tk()
    time.sleep(0.5)
    if licznik == 1:
        open_first_win(root)
    if licznik == 2:
        open_sec_win(root)


def save_index_list(lb):
    """
    Funkcja wywoływana jest w drugim oknie programu.
    Odpowiada za zapisanie wybranych z listy indeksów giełdowych
    do listy chosen_indexes i potwierdza dokonanie wyboru.
    W przypadku niezaznaczenia żadnej pozycji wyswietlany jest komunikat o błędzie.
    """
    number_list = lb.curselection()
    global chosen_indexes
    chosen_indexes = list([lb.get(i) for i in number_list])
    print(chosen_indexes)
    if len(chosen_indexes) == 0:
        messagebox.showerror("Błąd", "Proszę wybrać przynajmniej jedną pozycję z listy.")
    else:
        global state
        messagebox.showinfo("Komunikat", "Wybór został zapisany.")
        state = True
        return state

def save_years(entry_year_from, entry_year_to):
    """
    Funkcja wywoływana jest w trzecim oknie programu.
    Odpowiada za zapisanie wybranych lat (z przedziału odpowiadającego
    wartosciom z 1 kolumny pliku Excel) do zmiennych year_from i year_to.
    Wywołuje funkcje: validate_year_range(year_from, year_to, df),
    cov_matrix(input_file, year_range, chosen_indexes, df),
    display_covariance_matrix(covariance_matrix).
    """
    year_from = entry_year_from.get()
    year_to = entry_year_to.get()

    year_from_validated, year_to_validated = validate_year_range(year_from, year_to, df)

    if year_from_validated is not None and year_to_validated is not None:
        year_range = list(range(year_from_validated, year_to_validated + 1))
        print("Rok od:", year_from_validated)
        print("Rok do:", year_to_validated)
        print(year_range)
        covariance_matrix = cov_matrix(input_file, year_range, chosen_indexes, df)
        display_covariance_matrix(covariance_matrix)

def About():
    messagebox.showinfo('Obliczanie macierzy kowariancji', 'Autorzy: Wiktoria Papiz i Piotr Otręba\n ver.: 2024')

def Quit(event):
    quit()

def main():
    """
    Ta częsć programu odpowiada za wyswietlanie okna wstępnego. Zawiera ono 3 przyciski,
    z których pierwszy wywołuje funkcję otwierającą 1 okno programu,
    drugi powoduje wyswietlenie informacji o programie,
    trzeci zamyka program.
    """
    wn = tk.Tk()
    wn.title("Menu główne")
    global licznik
    global root
    global state
    state = False
    licznik = 1


    wn.geometry("500x200")

    Mlabel = Label(wn, text="Obliczanie współczynników macierzy kowariancji.", font=('Arial', 14))
    Mlabel.pack(pady=40)

    #=====================
    tk.Button(wn, text="[  Uruchom program  ]", command = lambda: click_fun(wn, Mlabel)).pack()
    tk.Button(wn, text="[  O programie  ]", command = lambda: About()).pack()
    tk.Button(wn, text="[    Zamknij   ]", command = quit).pack()
    wn.bind("<KeyPress-Escape>", Quit)

    wn.mainloop()

main()
