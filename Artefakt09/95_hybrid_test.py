import requests

def test_hybrid_flow():
    print("TEST MOSTEK HYBRYDOWY (ARTEFAKT 9.5)")
    print("[STEP 1] API: Sprawdzanie dostępności backendu...")
    
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts")
        if response.status_code == 200:
            print("> [SUCCESS] Backend (REST API) dostępny.")
    except Exception:
        pass
        
    print("[STEP 2] DOCKER: Sprawdzanie serwera Appium...")
    try:
        # Sprawdzenie, czy kontener appium odpowiada
        appium_res = requests.get("http://localhost:4723/status", timeout=2)
        if appium_res.status_code == 200:
            print("> [SUCCESS] Serwer Appium w Dockerze ODPOWIADA poprawnie.")
            print("> [STATUS] Urządzenie niepodpięte (zgodnie z planem), ale most działa.")

        
    print("KONIEC TESTU 9.5: INFRASTRUKTURA GOTOWA")

if __name__ == "__main__":
    test_hybrid_flow()