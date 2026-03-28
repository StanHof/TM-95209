import json
import os
from datetime import datetime
# Importujemy Appium Options (jeśli masz zainstalowaną bibliotekę)
# from appium.options.android import UiAutomator2Options

caps_file = "51_caps.json"
selectors_file = "53_selectors.json"
log_file = "54_session.log"

def start_session_manager():
    log_entries = []
    
    def log_event(message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"[{timestamp}] {message}"
        print(entry)
        log_entries.append(entry)

    log_event("=== INICJALIZACJA APPIUM SESSION MANAGER ===")

    # 1. Ładowanie Capabilities
    try:
        with open(caps_file, 'r') as f:
            caps = json.load(f)
        log_event(f"Załadowano Capabilities dla: {caps.get('appPackage')}")
    except FileNotFoundError:
        log_event("BŁĄD: Nie znaleziono pliku 51_caps.json!")
        return

    # 2. Tworzenie obiektu opcji (to jest kluczowe dla Appium)
    # W kodzie produkcyjnym byłoby to: options = UiAutomator2Options().load_capabilities(caps)
    appium_options_dict = {
        "appium:options": caps,
        "appium:automationName": "UiAutomator2",
        "appium:platformName": "Android"
    }
    log_event("Obiekt AppiumOptions został skonfigurowany.")

    # 3. Weryfikacja mapy selektorów
    if os.path.exists(selectors_file):
        with open(selectors_file, 'r') as f:
            ui_map = json.load(f)
        log_event(f"Mapa selektorów aktywna: {len(ui_map['selectors'])} elementów.")

    log_event("STATUS: READY TO CONNECT")
    log_event(f"Endpoint: http://localhost:4723")

    # Zapis logów
    with open(log_file, "w", encoding="utf-8") as f:
        f.write("\n".join(log_entries))

if __name__ == "__main__":
    start_session_manager()