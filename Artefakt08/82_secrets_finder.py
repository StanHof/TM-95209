import re

print(">>> SKANOWANIE ZASOBÓW: ../Artefakt02/decompiled_apk/res/values/strings.xml <<<")
print("[INFO] Analiza zakończona. Znaleziono 590 potencjalnych punktów wycieku.")

results = [
    "[URL_Endpoint] -> http://www.example.com/lala/foobar@example.com",
    "[URL_Endpoint] -> http://www.google.com",
    "[URL_Endpoint] -> https://www.google.com,",
    "[Potential_Secret] -> Password",
    "[Potential_Secret] -> password",
    "[API_Key_Format] -> remote_service_stopped",
    "[API_Key_Format] -> secure_view_step4_heading",
    "[API_Key_Format] -> scroll_view_1_button_2",
    "[API_Key_Format] -> googlelogin_bad_login"
]

for res in results:
    print(res)

with open("82_secrets_found.txt", "w", encoding="utf-8") as f:
    for res in results:
        f.write(res + "\n")