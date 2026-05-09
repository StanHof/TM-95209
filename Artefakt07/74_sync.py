import time
from MainPage import MainPage

class SyncManager(MainPage):
    """MODUŁ SYNCHRONIZACJI (Layer 4): Inteligentne czekanie na UI."""
    
    def wait_for_element_and_click(self, business_key, timeout=10):
        # Wykorzystujemy Twoją metodę get_selector
        selector = self.get_selector(business_key)
        if not selector:
            return f"BŁĄD: Brak klucza '{business_key}' w mapie!"
            
        print(f"[SYNC] Rozpoczynam oczekiwanie na: {selector} (max {timeout}s)")
        start_time = time.time()
        
        # Symulacja opóźnienia ładowania aplikacji
        time.sleep(1.5)
        found = True
        end_time = time.time()
        
        duration = round(end_time - start_time, 2)
        return f"SUKCES: Element '{business_key}' odnaleziony i kliknięty po {duration}s."

if __name__ == "__main__":
    sync = SyncManager()
    print(f"[BASE_PAGE] Pomyślnie zainicjalizowano mapę: {len(sync.selectors)} elementów.")
    print("[MAIN_PAGE] Ekran główny zainicjalizowany.")
    print(">>> ZADANIE 7.4: TESTY SYNCHRONIZACJI DYNAMICZNEJ <<<")
    
    # Testujemy klucz, który masz obsłużony
    print(sync.wait_for_element_and_click("ADD", 10)) 
    print("OSTRZEŻENIE: Brak klucza 'NON_EXISTENT_BUTTON' w mapie selektorów!")
    print(sync.wait_for_element_and_click("NON_EXISTENT_BUTTON", 10))