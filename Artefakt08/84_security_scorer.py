import os
import json
import xml.etree.ElementTree as ET

score = 100
deductions = []

# 1. ANALIZA FLAG Z XML (Zadanie 8.1)
xml_path = "RiskyPermission.xml"
if os.path.exists(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    debuggable_elem = root.find(".//Debuggable")
    
    if debuggable_elem is not None and debuggable_elem.text == "true":
        score -= 30
        deductions.append("[-30] Flaga Debuggable jest AKTYWNA (High Risk)")

# 2. ANALIZA PODATNOŚCI Z JSON (Zadanie 8.3)
json_path = "83_vulnerabilities.json"
if os.path.exists(json_path):
    with open(json_path, "r", encoding="utf-8") as f:
        vulnerabilities = json.load(f)
        for v in vulnerabilities:
            if v['severity'] == "CRITICAL":
                score -= 50
                deductions.append(f"[-50] Krytyczna luka w {v['library']} (Critical)")
            elif v['severity'] == "HIGH":
                score -= 20
                deductions.append(f"[-20] Poważna luka w {v['library']} (High)")
            elif v['severity'] == "MEDIUM":
                score -= 10
                deductions.append(f"[-10] Średnia luka w {v['library']} (Medium)")

print(">>> ZADANIE 8.4: OBLICZANIE SECURITY SCORE (ALGORITHM V1) <<<")
print("\nSzczegóły dedukcji:")
for d in deductions:
    print(d)

# Zabezpieczenie, by wynik nie spadł poniżej 0
score = max(0, score)

print(f"\nWYNIK KOŃCOWY: {score}/100")
status = "REJECTED (Aplikacja niebezpieczna)" if score < 50 else "APPROVED"
print(f"STATUS: {status}")

with open("84_risk_score.txt", "w", encoding="utf-8") as f:
    f.write(f"SCORE: {score}\nSTATUS: {status}\n")