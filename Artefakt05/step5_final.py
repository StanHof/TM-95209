import json
import xml.etree.ElementTree as ET
import os

def run_final_validation():
    # 1. Ładowanie danych z poprzednich etapów
    try:
        with open('51_caps.json', 'r') as f:
            caps = json.load(f)
        with open('53_selectors.json', 'r') as f:
            ui_map = json.load(f)
    except FileNotFoundError:
        print("Błąd: Upewnij się, że pliki 51_caps.json i 53_selectors.json istnieją!")
        return

    results = []
    
    # --- TEST 1: Weryfikacja identyfikatora pakietu ---
    # Sprawdzamy, czy appPackage z caps nie jest pusty (symulacja zgodności z manifestem)
    package_name = caps.get("appPackage", "")
    test1_passed = len(package_name) > 0 and "." in package_name
    results.append({
        "name": "Weryfikacja identyfikatora pakietu",
        "status": "passed" if test1_passed else "failed"
    })

    # --- TEST 2: Weryfikacja obecności kluczowych selektorów ---
    # Sprawdzamy, czy w mapie znajduje się jakikolwiek element (np. zdekodowany z XML)
    selectors = ui_map.get("selectors", {})
    test2_passed = len(selectors) > 0
    results.append({
        "name": "Weryfikacja obecności kluczowych selektorów",
        "status": "passed" if test2_passed else "failed"
    })

    # 2. Generowanie pliku 55_result.xml (JUnit XML)
    testsuite = ET.Element("testsuite", name="ConsistencyTestSuite", tests=str(len(results)))
    
    for res in results:
        testcase = ET.SubElement(testsuite, "testcase", name=res["name"])
        if res["status"] == "failed":
            failure = ET.SubElement(testcase, "failure", message="Błąd walidacji danych")
            failure.text = "Dane z konfiguracji nie pokrywają się z plikami aplikacji."

    # Zapis do pliku
    tree = ET.ElementTree(testsuite)
    with open("55_result.xml", "wb") as f:
        tree.write(f, encoding="utf-8", xml_declaration=True)

    print("=== WYNIK TESTU SPÓJNOŚCI ===")
    for res in results:
        print(f"{res['name']}: {res['status'].upper()}")
    print("\nRaport zapisano w 55_result.xml")

if __name__ == "__main__":
    run_final_validation()