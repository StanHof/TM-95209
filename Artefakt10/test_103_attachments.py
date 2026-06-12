import pytest
import allure

@allure.epic("Platforma Edukacyjna Artefakt")
@allure.feature("10.3: Dowody wizualne (Załączniki)")
@allure.story("Test ze zrzutem ekranu (Symulacja)")
def test_failure_with_screenshot():
    with allure.step("Krok 1: Próba kliknięcia w przycisk 'Zapisz'"):
        try:
            raise Exception("ElementNotVisibleException")
        except Exception as e:
            # Symulacja zrzutu ekranu (puste dane binarne) i pliku tekstowego
            allure.attach(b"Fake PNG data", name="Screenshot_Error_01", attachment_type=allure.attachment_type.PNG)
            allure.attach("Fake API Response: 500 Internal Server Error", name="API_Response", attachment_type=allure.attachment_type.TEXT)
            assert False, f"Test padł, ale mamy dowody! Log: {e}"