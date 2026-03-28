import xml.etree.ElementTree as ET
import os
import json

# Ścieżka do folderu z layoutami (upewnij się, że ścieżka jest poprawna)
layout_dir = "../Artefakt02/decompiled_apk/res/layout"
output_file = "53_selectors.json"

def create_ui_map():
    if not os.path.exists(layout_dir):
        print(f"BŁĄD: Nie znaleziono folderu {layout_dir}")
        return

    # Inicjalizacja struktury słownika
    ui_map = {
        "app_info": "Mobile UI Map",
        "selectors": {}
    }

    # Definiujemy przestrzeń nazw Androida dla atrybutu ID
    android_id_attr = '{http://schemas.android.com/apk/res/android}id'

    count = 0
    # Iterujemy po plikach layoutów
    for file_name in os.listdir(layout_dir):
        if file_name.endswith(".xml"):
            try:
                file_path = os.path.join(layout_dir, file_name)
                tree = ET.parse(file_path)
                root = tree.getroot()

                # Szukamy wszystkich elementów z atrybutem id
                for element in root.iter():
                    res_id = element.attrib.get(android_id_attr)
                    
                    if res_id:
                        # Oczyszczamy ID (np. @id/button_login -> button_login)
                        clean_id = res_id.split('/')[-1]
                        
                        # Tworzymy nazwę biznesową (np. LOGIN_BTN)
                        # Dodajemy nazwę pliku, jeśli chcesz uniknąć duplikatów
                        business_name = clean_id.upper()
                        
                        # Zapisujemy do mapy
                        ui_map["selectors"][business_name] = clean_id
                        count += 1
            except Exception as e:
                # W razie błędu w jednym pliku, idź dalej
                continue

    # Zapisujemy mapę do pliku JSON
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(ui_map, f, indent=4)

    print("========================================")
    print("      GENEROWANIE MAPY INTERFEJSU       ")
    print("========================================")
    print(f"Przetworzono pliki z: {layout_dir}")
    print(f"Zmapowano unikalnych elementów UI: {len(ui_map['selectors'])}")
    print(f"Wynik zapisano w: {output_file}")

if __name__ == "__main__":
    create_ui_map()