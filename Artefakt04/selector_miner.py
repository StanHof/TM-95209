import xml.etree.ElementTree as ET
import glob
import json
import os

def mine_selectors(path):
    found_ids = []
    search_path = os.path.join(path, "**/*.xml")
    for file_path in glob.glob(search_path, recursive=True):
        try:
            tree = ET.parse(file_path)
            for elem in tree.iter():
          
                res_id = elem.get('{http://schemas.android.com/apk/res/android}id')
                if res_id:
                    clean_id = res_id.split('/')[-1]

                    tag_name = elem.tag.split('}')[-1] 
        
                    found_ids.append({
                        "file": os.path.basename(file_path),
                        "id": clean_id,
                        "tag": tag_name
                    })
                    print(f"File: {os.path.basename(file_path)} | Found ID: {clean_id}")
        except Exception as e:
            print(f"Błąd podczas parsowania {file_path}: {e}")
    with open("miner_report.json", "w", encoding="utf-8") as f:
        json.dump(found_ids, f, indent=4)
    
    print(f"\n[OK] Wydobyto {len(found_ids)} identyfikatorów. Raport zapisano w miner_report.json.")
mine_selectors("../Artefakt02/decompiled_apk/res/layout")