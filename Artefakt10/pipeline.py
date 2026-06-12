import os

def run_pipeline():
    print(">>>> ROZPOCZĘCIE PIPELINE <<<<")

    print("KROK 1: Uruchamianie infrastruktury...")
    # Zakładamy, że masz plik docker-compose.yml z Bloku 9
    os.system("docker compose up -d")

    print("KROK 2: Wykonywanie testów (pytest)...")
    # Wywołujemy wszystkie dzisiejsze testy
    os.system("python -m pytest test_101_allure_init.py test_102_meta_reporting.py test_103_attachments.py --alluredir=allure-results")

    print("KROK 3: Generowanie raportu Allure...")
    # Generujemy raport statyczny do folderu allure-report
    os.system("allure generate allure-results --clean -o allure-report")
    print("Report successfully generated to allure-report")

    print("KROK 4: Sprzątanie środowiska...")
    os.system("docker compose down")

    print(">>>> PIPELINE UKOŃCZONY Z SUKCESEM! <<<<")

if __name__ == "__main__":
    run_pipeline()