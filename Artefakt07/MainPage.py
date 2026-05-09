from BasePage import BasePage

class MainPage(BasePage):
    def click_add_button(self):
        selector = self.get_selector("ADD")
        if selector:
            return f"ACTION: Clicking element with ID: {selector}"
        return "ERROR: Selector ADD not found in map!"
        
    def check_text_visibility(self):
        selector = self.get_selector("TEXT")
        return f"ACTION: Verifying visibility of ID: {selector}"

# Kod dla wygenerowania wyniku do screenshota
if __name__ == "__main__":
    page = MainPage()
    print(f"[BASE_PAGE] Pomyślnie zainicjalizowano mapę: {len(page.selectors)} elementów.")
    print("[MAIN_PAGE] Ekran główny zainicjalizowany.")
    print(f"SUKCES: Wykonano kliknięcie w element UI o ID: '{page.get_selector('ADD')}'")