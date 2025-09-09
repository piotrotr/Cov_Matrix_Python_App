import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *
import time

def cov_matrix(input_file, year_range, index_names, df):
    """
    Funkcja wywoływana jest w 3 oknie programu przez funkcję save_years(entry_year_from, entry_year_to).
    Na podstawie danych z pliku Excel tworzy obiekt DataFrame
    zawierający rekordy i kolumny wybrane przez użytkownika.
    Następnie oblicza współczynniki macierzy kowariancji dla utworzonego DataFrame.
    Odpowiada za wyswietlenie macierzy kowariancji w formie mapy ciepła.
    """
    global covariance_matrix
    mask_rows = df.iloc[:, 0].isin(year_range)
    mask_cols = index_names
    df = df[mask_rows]
    df = df[mask_cols]
    print(df)
    covariance_matrix = df.cov()
    print(covariance_matrix)
    sn.heatmap(data = df.cov())
    plt.title("Wizualizacja macierzy kowariancji")
    plt.show()
    return covariance_matrix


def display_covariance_matrix(matrix):
    """
    Funkcja wywoływana jest w 3 oknie programu przez funkcję save_years(entry_year_from, entry_year_to).
    Odpowiada za wyswietlenie macierzy kowariancji w formie tabeli.
    """
    root = tk.Tk()
    root.title("Macierz Kowariancji")

    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    label = tk.Label(frame, text="Współczynniki macierzy kowariancji:")
    label.grid(row=0, column=0, padx=5, pady=5)

    text_area = tk.Text(frame, height=100, width=100)
    text_area.grid(row=1, column=0, padx=5, pady=5)

    text_area.insert(tk.END, str(matrix))

    button_close = tk.Button(frame, text="Zamknij", command=root.destroy)
    button_close.grid(row=2, column=0, padx=5, pady=5)

if __name__ == "__main__":
    # testujemy dla pliku indeksy_projekt.xlsx
    input_file = 'indeksy_projekt.xlsx'
    df = pd.read_excel(input_file, skiprows=[0])
    cov_matrix(input_file, [2017, 2018, 2019, 2020, 2021, 2022, 2023], ['S&P 500', 'Dow Jones', 'DAX', 'Nikkei', 'FTSE 100', 'WIG20'], df)
    display_covariance_matrix(covariance_matrix)

    time.sleep(2)
    cov_matrix(input_file, [2017, 2018, 2019, 2020], ['S&P 500', 'FTSE 100', 'WIG20'], df)
    time.sleep(2)
    display_covariance_matrix(covariance_matrix)

    # testujemy dla pliku plik_testowy.xlsx
    input_file = 'plik_testowy.xlsx'
    df = pd.read_excel(input_file, skiprows=[0])
    time.sleep(2)
    cov_matrix(input_file, [1800, 1801, 1802, 1803, 1804], ['Opcja 1', 'Opcja 2', 'Opcja 3'], df)
    display_covariance_matrix(covariance_matrix)