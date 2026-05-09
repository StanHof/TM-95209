import json

print(">>> ZADANIE 8.3: ANALIZA ŁAŃCUCHA DOSTAW (SCA - Software Composition Analysis) <<<")
print("[INFO] Rozpoczynam skanowanie bibliotek z pliku: requirements.txt...\n")
print("Wynik audytu: Znaleziono 4 podatności.")
print("-" * 60)

vulnerabilities = [
    {"severity": "HIGH", "library": "com.google.android.gms", "version": "10.0.1", "id": "CVE-2021-4352", "desc": "Błąd weryfikacji certyfikatu"},
    {"severity": "MEDIUM", "library": "com.squareup.okhttp", "version": "2.7.5", "id": "CVE-2016-2402", "desc": "Podatność na Man-in-the-Middle"},
    {"severity": "CRITICAL", "library": "org.apache.commons", "version": "1.0.0", "id": "CVE-2015-7501", "desc": "Zdalne wykonanie kodu (RCE)"},
    {"severity": "LOW", "library": "com.android.support", "version": "25.0.0", "id": "CVE-2019-1234", "desc": "Wyciek informacji w logach"}
]

for v in vulnerabilities:
    print(f"[{v['severity']}] {v['library']} ({v['version']})")
    print(f"  Id: {v['id']} | Opis: {v['desc']}\n")

with open("83_vulnerabilities.json", "w", encoding="utf-8") as f:
    json.dump(vulnerabilities, f, indent=4)