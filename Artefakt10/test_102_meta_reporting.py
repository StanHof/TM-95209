import pytest
import allure

@allure.epic("Platforma Edukacyjna Artefakt")
@allure.feature("Moduł Kursy i Lekcje")
@allure.story("Przeglądanie listy lekcji")
def test_hierarchy():
    with allure.step("Otwarcie listy lekcji"):
        allure.attach("Log tekstowy: Załadowano listę", name="Prosty log", attachment_type=allure.attachment_type.TEXT)
        assert True