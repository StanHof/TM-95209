import pytest
import allure

@allure.feature("10.1: Inicjalizacja Allure")
def test_passed():
    with allure.step("Krok 1: Wykonanie poprawnej akcji"):
        assert True

@allure.feature("10.1: Inicjalizacja Allure")
def test_failed():
    with allure.step("Krok 1: Wykonanie błędnej akcji"):
        assert False, "Wymuszony błąd do raportu"