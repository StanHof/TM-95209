import json

class BasePage:
    def __init__(self, selectors_file="53_selectors.json"):
        with open(selectors_file, "r") as f:
            # Wczytywanie mapy utworzonej w Bloku 5
            self.selectors = json.load(f)["selectors"]
            
    def get_selector(self, business_name):
        return self.selectors.get(business_name, None)

# Kod pozwalający na wygenerowanie wyniku do screenshota
if __name__ == "__main__":
    page = BasePage()
    print(f"[BASE_PAGE] Pomyślnie zainicjalizowano mapę: {len(page.selectors)} elementów.")
    print(f"Weryfikacja klucza 'ADD': {page.get_selector('ADD')}")