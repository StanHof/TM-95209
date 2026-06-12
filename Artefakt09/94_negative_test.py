import requests

def test_api_errors():
    print(">>>> ZADANIE 9.4: TESTY NEGATYWNE (OBSŁUGA BŁĘDÓW) <<<<")
    
    url_404 = "https://jsonplaceholder.typicode.com/posts/999999"
    print(f"[INFO] Próba pobrania nieistniejącego zasobu: {url_404}")
    response_404 = requests.get(url_404)
    
    if response_404.status_code == 404:
        print("[SUCCESS] API poprawnie zwróciło kod 404 Not Found.")
    else:
        print(f"[FAIL] Otrzymano kod: {response_404.status_code}")
        
    url_post = "https://jsonplaceholder.typicode.com/posts"
    print(f"[INFO] Próba wysłania błędnego body (nie-JSON) do: {url_post}")
    
    bad_data = "To nie jest JSON, to zwykly tekst"
    response_bad = requests.post(url_post, data=bad_data)
    
    print(f"[DEBUG] Status dla błędnych danych: {response_bad.status_code}")

if __name__ == "__main__":
    test_api_errors()