import xml.etree.ElementTree as ET
import glob
import json
import os

def run_a11y_check(layout_path):
    print("=== ANALIZA LUK DOSTĘPNOŚCI (A11y Gap Analysis) ===")
    gaps = []
    
    # Przestrzeń nazw Androida
    ns = '{http://schemas.android.com/apk/res/android}'
    
    # Szukamy plików XML w layoutach
    search_path = os.path.join(layout_path, "**/*.xml")
    files = glob.glob(search_path, recursive=True)

    if not files:
        print(f"BŁĄD: Nie znaleziono plików w {layout_path}")
        return

    for file_path in files:
        try:
            tree = ET.parse(file_path)
            for elem in tree.iter():
                # Pobieramy tekst, opis i ID
                node_text = elem.get(f'{ns}text')
                node_desc = elem.get(f'{ns}contentDescription')
                node_id = elem.get(f'{ns}id', 'no-id')

                # Luka: Element posiada tekst (widoczny), ale brak mu opisu dla czytnika (contentDescription)
                # Sprawdzamy, czy node_text nie jest pusty
                if node_text and not node_desc:
                    gaps.append({
                        "file": os.path.basename(file_path),
                        "id": node_id.split('/')[-1],
                        "text": node_text,
                        "issue": "Brak atrybutu contentDescription przy istniejącym tekście"
                    })
        except Exception as e:
            continue

    # Zapisywanie raportu do pliku JSON
    with open("a11y_report.json", "w", encoding="utf-8") as f:
        json.dump(gaps, f, indent=4, ensure_ascii=False)

    print(f"\n[OK] Analiza zakończona. Znaleziono {len(gaps)} potencjalnych luk.")
    print("Raport zapisano w: a11y_report.json")

# Uruchomienie (upewnij się, że ścieżka jest poprawna)
path = "../Artefakt02/decompiled_apk/res/layout"
run_a11y_check(path)