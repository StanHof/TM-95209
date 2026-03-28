import xml.etree.ElementTree as ET
import os

# Ścieżka do zdekodowanego manifestu
manifest_path = "../Artefakt02/decompiled_apk/AndroidManifest.xml"
log_file = "52_inspection.log"

def run_inspection():
    if not os.path.exists(manifest_path):
        print(f"BŁĄD: Nie znaleziono pliku {manifest_path}")
        return

    # Definiujemy przestrzeń nazw Androida
    ns = {'android': 'http://schemas.android.com/apk/res/android'}
    android_name = f"{{{ns['android']}}}name"

    # Wczytujemy XML
    tree = ET.parse(manifest_path)
    root = tree.getroot()

    # 1. Pobieramy nazwę paczki
    package = root.attrib.get('package')

    # 2. Wyciągamy uprawnienia (Permissions)
    permissions = [elem.attrib.get(android_name) for elem in root.findall('uses-permission', ns)]
    # Usuwamy ewentualne wartości None
    permissions = [p for p in permissions if p]

    # 3. Wyciągamy aktywności (Activities)
    activities = [elem.attrib.get(android_name) for elem in root.findall('.//activity', ns)]
    activities = [a for a in activities if a]

    # 4. Przygotowanie raportu do zapisu
    report_lines = [
        "========================================",
        "      RAPORT ANALIZY MANIFESTU APK      ",
        "========================================",
        f"PAKIET GŁÓWNY: {package}",
        f"LICZBA UPRAWNIEŃ: {len(permissions)}",
        f"LICZBA AKTYWNOŚCI: {len(activities)}",
        "\nLISTA UPRAWNIEŃ:",
    ]
    
    for perm in permissions:
        report_lines.append(f" [-] {perm}")

    report_lines.append("\nLISTA AKTYWNOŚCI:")
    for act in activities:
        report_lines.append(f" [!] {act}")

    # 5. Zapis do pliku logu
    with open(log_file, "w", encoding="utf-8") as f:
        f.write("\n".join(report_lines))

    # Wyświetlenie podglądu w konsoli
    print("\n".join(report_lines[:6])) # Wyświetla nagłówek i statystyki
    print(f"\nPEŁNY RAPORT ZAPISANO W: {log_file}")

if __name__ == "__main__":
    run_inspection()