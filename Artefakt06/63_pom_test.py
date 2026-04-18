from MainPage import MainPage

def run_pom_test():
    print(">>> ZADANIE 6.3: URUCHAMIANIE TESTU W ARCHITEKTURZE POM <<<")
    
    # Inicjalizacja strony
    page = MainPage()
    print(f"[BASE_PAGE] Pomyślnie zainicjalizowano mapę: {len(page.selectors)} elementów.")
    print("[MAIN_PAGE] Ekran główny zainicjalizowany.")
    print("PRZEBIEG SCENARIUSZA TESTOWEGO")
    
    # Symulacja kroków testowych
    step1 = page.click_add_button()
    step2 = page.check_text_visibility()
    
    print(f"KROK 1: {step1}")
    print(f"KROK 2: {step2}")
    
    # Zapisujemy feedback inżynierski
    with open("64_pom_audit.log", "w") as f:
        f.write(f"Test Execution Log:\n{step1}\n{step2}")
        
    print("[OK] Scenariusz wykonany. Log audytu zapisany w 64_pom_audit.log")

if __name__ == "__main__":
    run_pom_test()