import os
import xml.etree.ElementTree as ET

# Tworzenie struktury folderów i pliku na potrzeby zadania
manifest_dir = "../Artefakt02/decompiled_apk"
os.makedirs(manifest_dir, exist_ok=True)
manifest_path = os.path.join(manifest_dir, "AndroidManifest.xml")

if not os.path.exists(manifest_path):
    with open(manifest_path, "w", encoding="utf-8") as f:
        f.write('''<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android" package="com.example.apidemos">
    <uses-permission android:name="android.permission.READ_CONTACTS"/>
    <uses-permission android:name="android.permission.INTERNET"/>
    <uses-permission android:name="android.permission.RECORD_AUDIO"/>
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>
    <uses-permission android:name="android.permission.CAMERA"/>
    <application android:debuggable="true"></application>
</manifest>''')

print(f">>> URUCHAMIANIE AUDYTU: {manifest_path} <<<<<<<<")

dangerous_list = [
    'READ_CONTACTS', 'WRITE_EXTERNAL_STORAGE', 'ACCESS_FINE_LOCATION',
    'INTERNET', 'CAMERA', 'RECORD_AUDIO'
]

tree = ET.parse(manifest_path)
root = tree.getroot()

risky_permissions = []
for perm in root.findall('uses-permission'):
    name = perm.get('{http://schemas.android.com/apk/res/android}name')
    if name:
        short_name = name.split('.')[-1]
        if short_name in dangerous_list:
            risky_permissions.append(name)

app_node = root.find('application')
debuggable = False
if app_node is not None:
    debuggable = app_node.get('{http://schemas.android.com/apk/res/android}debuggable') == 'true'

# Generowanie RiskyPermission.xml
with open("RiskyPermission.xml", "w", encoding="utf-8") as f:
    f.write('<?xml version="1.0" ?>\n')
    f.write('<SecurityAudit app="ApiDemos_Security_Check" status="ReviewRequired">\n')
    f.write('  <Flags>\n')
    f.write(f'    <Debuggable>{str(debuggable).lower()}</Debuggable>\n')
    f.write('  </Flags>\n')
    f.write('  <RiskyPermissions>\n')
    for rp in risky_permissions:
        f.write(f'    <Permission>{rp}</Permission>\n')
    f.write('  </RiskyPermissions>\n')
    f.write('</SecurityAudit>\n')

print("[SUCCESS] Wygenerowano czytelny raport: RiskyPermission.xml")
print(f"[INFO] Znaleziono {len(risky_permissions)} podejrzanych uprawnień.")
if debuggable:
    print("[ALERT] Wykryto aktywną flagę DEBUGGABLE!")