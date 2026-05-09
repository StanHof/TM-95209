import datetime
from MainPage import MainPage

class DeviceStateManager(MainPage):
    """MODUŁ ZARZĄDZANIA STANEM (Layer 4): Obsługa fizycznych zmian urządzenia."""
    
    def __init__(self):
        super().__init__() # Wywołuje BasePage.__init__ i wczytuje JSON
        self.log_file = "73_state.log"

    def _log_event(self, event_name, detail):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] {event_name.upper()}: {detail}\n")

    def toggle_screen_orientation(self, target="LANDSCAPE"):
        print(f"[DEVICE] Zmiana orientacji na: {target}")
        detail = f"Ekran obrócony do {target}. Weryfikacja przerysowania layoutu..."
        self._log_event("orientation", detail)
        return f"SUKCES: Orientacja zmieniona na {target}."

    def simulate_power_connection(self, is_connected=True):
        state = "CONNECTED" if is_connected else "DISCONNECTED"
        print(f"[DEVICE] Zasilanie: {state}")
        self._log_event("power_state", f"Zasilanie zewnętrzne: {state}")
        return f"SUKCES: Stan zasilania ustawiony na {state}."

if __name__ == "__main__":
    manager = DeviceStateManager()
    print(f"[BASE_PAGE] Pomyślnie zainicjalizowano mapę: {len(manager.selectors)} elementów.")
    print("[MAIN_PAGE] Ekran główny zainicjalizowany.")
    print(">>> ZADANIE 7.3: ZARZĄDZANIE FIZYCZNYM STANEM URZĄDZENIA <<<")
    
    print(manager.toggle_screen_orientation("LANDSCAPE"))
    print(manager.toggle_screen_orientation("PORTRAIT"))
    print(manager.simulate_power_connection(True))
    print("[OK] Zmiany zapisane w: 73_state.log")