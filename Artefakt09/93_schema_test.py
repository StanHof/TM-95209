import requests
from jsonschema import validate, ValidationError

def test_schema_validation():
    print(">>>> ZADANIE 9.3: WALIDACJA STRUKTURY JSON (KONTRAKT) <<<<")
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    data = response.json()

    # DEFINICJA SCHEMATU 
    expected_schema = {
        "type": "object",
        "properties": {
            "userId": {"type": "number"},
            "id": {"type": "number"},
            "title": {"type": "string"},
            "body": {"type": "string"}
        },
        "required": ["userId", "id", "title"] 
    }

    try:
        validate(instance=data, schema=expected_schema)
        print("[SUCCESS] Kontrakt zachowany. Struktura JSON jest poprawna.")
        print(f"[DEBUG] Zweryfikowano pola dla obiektu ID: {data['id']}")
    except ValidationError as e:
        print(f"[ERROR] Walidacja schematu nie powiodła się: {e.message}")

if __name__ == "__main__":
    test_schema_validation()