import xml.etree.ElementTree as ET
import json
import os

# Ścieżka do zdekodowanego manifestu (dostosuj jeśli folder nazywa się inaczej)
manifest_path = "../Artefakt02/decompiled_apk/AndroidManifest.xml"

def extract_capabilities():
    if not os.path.exists(manifest_path):
        print(f"BŁĄD: Nie znaleziono pliku {manifest_path}")
        return

    # Definiujemy przestrzenie nazw (często spotykane w Androidzie)
    ns = {'android': 'http://schemas.android.com/apk/res/android'}
    
    # Wczytujemy plik XML
    tree = ET.parse(manifest_path)
    root = tree.getroot()

    # 1. Pobieramy nazwę paczki (appPackage)
    package = root.attrib.get('package')

    # 2. Szukamy głównej aktywności (appActivity)
    main_activity = ""
    for activity in root.findall(".//activity", ns):
        intent = activity.find(".//intent-filter", ns)
        if intent is not None:
            # Szukamy akcji MAIN
            action = intent.find("./action[@android:name='android.intent.action.MAIN']", ns)
            # Szukamy kategorii LAUNCHER
            category = intent.find("./category[@android:name='android.intent.category.LAUNCHER']", ns)
            
            if action is not None and category is not None:
                main_activity = activity.get(f"{{{ns['android']}}}name")
                break

    # 3. Tworzymy słownik capabilities
    capabilities = {
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "appPackage": package,
        "appActivity": main_activity,
        "deviceName": "emulator-5554",
        "noReset": True
    }

    # 4. Zapisujemy do pliku JSON (wymagane w zadaniu)
    with open('51_caps.json', 'w', encoding='utf-8') as f:
        json.dump(capabilities, f, indent=4)

    print("Sukces! Wykryto parametry aplikacji:")
    print(f"Package: {package}")
    print(f"Activity: {main_activity}")
    print("Dane zapisano do pliku 51_caps.json")

if __name__ == "__main__":
    extract_capabilities()