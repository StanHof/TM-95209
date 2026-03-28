import xml.etree.ElementTree as ET
import glob
import json
import os

def stability_audit(layout_path):
    audit_results = []
    search_pattern = os.path.join(layout_path, "**/*.xml")
    files = glob.glob(search_pattern, recursive=True)
 
    if not files:
        print(f"Błąd: Nie znaleziono plików XML w lokalizacji: {layout_path}")
        return

    for file_path in files:
        try:
            tree = ET.parse(file_path)
            root = tree.getroot()
            class_counts = {}
            total_elements = 0
            
            for elem in tree.iter():
                tag = elem.tag.split('}')[-1] 
                class_counts[tag] = class_counts.get(tag, 0) + 1
                total_elements += 1
            file_report = {
                "file": os.path.basename(file_path),
                "total_elements": total_elements,
                "classes": []
            }
            
            for tag, count in class_counts.items():

                cdi = (count / total_elements) * 100 if total_elements > 0 else 0
                stability = "STABLE" if count == 1 else "UNSTABLE (Index-required)"
                
                file_report["classes"].append({
                    "class_name": tag,
                    "count": count,
                    "cdi_index": f"{round(cdi, 2)}%",
                    "status": stability
                })
            
            audit_results.append(file_report)
            print(f"Zaudytowano: {os.path.basename(file_path)} (Elementów: {total_elements})")
            
        except Exception as e:
            print(f"Błąd podczas analizy {file_path}: {e}")
    with open("stability_report.json", "w", encoding="utf-8") as f:
        json.dump(audit_results, f, indent=4)
    
    print("\n" + "="*40)
    print("[OK] Audyt stabilności zakończony.")
    print("Raport zapisano w pliku: stability_report.json")
    print("="*40)
path_to_layout = "../Artefakt02/decompiled_apk/res/layout"
stability_audit(path_to_layout)