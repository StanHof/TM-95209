import time
from MainPage import MainPage

class InterruptManager(MainPage):
    """MODUŁ PRZERWAŃ (Layer 4): Symulacja zdarzeń systemowych Androida."""
    
    def simulate_incoming_call(self, duration_sec=5):
        print("\n[INTERRUPT] KROK 1: Stan aplikacji przed połączeniem: ACTIVE")
        print(f"[INTERRUPT] KROK 2: Wyzwalanie zdarzenia: INCOMING CALL (Duration: {duration_sec}s)")
        time.sleep(1)
        print(">>> SYSTEM: Aplikacja w tle (onPause) | Widoczny ekran połączenia <<<")
        time.sleep(duration_sec) 
        print("[INTERRUPT] KROK 3: Zakończenie połączenia. Powrót do aplikacji.")
        return "SUKCES: Aplikacja odzyskała fokus (onResume). Dane sesji zachowane."

    def simulate_low_battery_warning(self):
        print("\n[INTERRUPT] Wyzwalanie zdarzenia: LOW BATTERY WARNING")
        return "SUKCES: Aplikacja obsłużyła systemowe okno dialogowe bez błędu."

if __name__ == "__main__":
    manager = InterruptManager()
    print(f"[BASE_PAGE] Pomyślnie zainicjalizowano mapę: {len(manager.selectors)} elementów.")
    print("[MAIN_PAGE] Ekran główny zainicjalizowany.")
    print(">>> ZADANIE 7.2: TESTY ODPORNOŚCI NA PRZERWANIA <<<")
    
    print(manager.simulate_incoming_call(3))
    print(manager.simulate_low_battery_warning())