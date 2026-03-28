import xml.etree.ElementTree as ET
import glob
import os

def run_game():
    print("=== INTERAKTYWNY KREATOR SELEKTORÓW (Selector Game) ===")
    
    # 1. Dane wejściowe od studenta (pobierasz je ze swojego pliku miner_report.json)
    target_id = input("1. Podaj wartość 'id' z raportu (np. lunch): ").strip()
    target_tag = input("2. Podaj wartość 'tag' z raportu (np. RadioButton): ").strip()

    matches = 0
    # Przestrzeń nazw Androida w plikach XML
    ns = {'android': 'http://schemas.android.com/apk/res/android'}

    # Ścieżka do layoutów z poprzedniego zadania
    path = "../Artefakt02/decompiled_apk/res/layout/*.xml"
    files = glob.glob(path)

    if not files:
        print("BŁĄD: Nie znaleziono plików XML w ../Artefakt02/decompiled_apk/res/layout/")
        return

    print("Analizowanie plików... proszę czekać.")

    for file in files:
        try:
            tree = ET.parse(file)
            for elem in tree.iter():
                # Pobieramy pełne ID (np. @id/lunch)
                node_id = elem.get('{http://schemas.android.com/apk/res/android}id', "")
                # Pobieramy tag (klasę) elementu
                node_tag = elem.tag

                # Sprawdzamy, czy w ID znajduje się nasz szukany ciąg i czy tag jest identyczny
                # node_tag może zawierać pełną ścieżkę klasy, więc sprawdzamy końcówkę
                if target_id in node_id and node_tag.endswith(target_tag):
                    matches += 1
        except Exception:
            continue

    print(f"\nWynik wyszukiwania: Znaleziono {matches} dopasowań.")

    # 2. Logowanie wyniku i weryfikacja unikalności
    with open('xpath_verification.txt', 'w', encoding='utf-8') as f:
        if matches == 1:
            print(">>>> STATUS: ZALICZONE! Twój selektor jest unikalny.")
            f.write(f"PROJEKT SELEKTORA:\nID: {target_id}\nTAG: {target_tag}\nSTATUS: ZALICZONE\n")
        else:
            print(">>>> STATUS: BŁĄD! Musisz znaleźć unikalną parę ID i TAG. Wynik musi wynosić dokładnie 1.")
            print(f"Obecny wynik: {matches}. Spróbuj z innym ID z raportu.")

if __name__ == "__main__":
    run_game()