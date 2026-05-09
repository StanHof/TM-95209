from MainPage import MainPage

class GestureAutomator(MainPage):
    """MODUŁ GESTÓW (Layer 4): Rozszerzenie Page Objectu o fizykę dotyku."""
    
    def scroll_down_logic(self, start_y=0.8, end_y=0.2, duration_ms=1000):
        print(f"[GESTURE] Start Swipe: Y={start_y} -> End Y={end_y} (t={duration_ms}ms)")
        if duration_ms < 200:
            return "BŁĄD: Gest zbyt szybki - grozi brakiem reakcji UI (Flick)."
        return f"SUKCES: Przewinięto listę o {int((start_y - end_y) * 100)}% wysokości ekranu."

    def long_press_element(self, element_key):
        # Wykorzystujemy Twoją metodę get_selector
        selector = self.get_selector(element_key)
        if selector:
            return f"SUKCES: Wykonano LONG PRESS (2s) na elemencie: {selector}"
        return f"BŁĄD: Nie odnaleziono elementu '{element_key}' w mapie selektorów."

if __name__ == "__main__":
    automator = GestureAutomator()
    print(f"[BASE_PAGE] Pomyślnie zainicjalizowano mapę: {len(automator.selectors)} elementów.")
    print("[MAIN_PAGE] Ekran główny zainicjalizowany.")
    print(">>> ZADANIE 7.1: TESTY FIZYKI DOTYKU <<<")
    
    print(automator.scroll_down_logic(0.8, 0.2, 800))
    # Wpisz tu klucz, który na pewno istnieje w Twoim JSONie, np. "ADD"
    print(automator.long_press_element("LIST_ITEM"))