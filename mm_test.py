import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys


class MMCreatAccontWrongMail(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://mediamarkt.pl/")

    def testWrongEmail(self):
        driver = self.driver
        # 1. Kliknij "Zaloguj się"
        zaloguj_btn = WebDriverWait(driver, 30)\
        .until(EC.element_to_be_clickable((By.XPATH, '//*[@class="js-header_login"]'))) # noqa
        zaloguj_btn.click()
        # 2. Kliknij "Załóż_Konto"
        załóż_konto_btn = WebDriverWait(driver, 30)\
        .until(EC.element_to_be_clickable((By.XPATH, '//*[@class="m-btn m-btn_primary is-submitBtn"]'))) # noqa
        załóż_konto_btn.click()
        # 3. Wybierz zwrot grzecznościowy "Pan"
        # 3a) musimy przescrolować stronę
        sleep(5)
        body = driver.find_element_by_xpath('//*[@data-page-name="Rejestracja w serwisie"]') # noqa
        body.click()
        body.send_keys(Keys.PAGE_DOWN)
        # 3b) zaznaczamy "Pan"
        pan_btn = driver.find_element_by_id("js-salutation_mister")
        driver.execute_script("arguments[0].click();", pan_btn)
        # 4. Wprowadź imię
        firstName = driver.find_element_by_id("enp_customer_registration_form_type_address_firstName") # noqa
        firstName.send_keys("Tomasz")
        # 5. Wprowadź nazwisko
        lastName = driver.find_element_by_id("enp_customer_registration_form_type_address_lastName") # noqa
        lastName.send_keys("Kowalski")
        # 6. Wrowadź błędny email
        email = driver.find_element_by_id("enp_customer_registration_form_type_email") # noqa
        email.send_keys("kowalskipoczta.pl")
        # 7. Wprowadź hasło
        password = driver.find_element_by_id("enp_customer_registration_form_type_plainPassword") # noqa
        password.send_keys("Asdfg1!")
        # 8 Wprowadź numer telefonu
        phone = driver.find_element_by_id("enp_customer_registration_form_type_mobileNumber_number") # noqa
        phone.send_keys("500100200")
        # 9 Wprowadź kod pocztowy
        postcode = driver.find_element_by_id("enp_customer_registration_form_type_address_postcode") # noqa
        postcode.send_keys("50001")
        # 10 Zaakceptuj regulaminy
        # 10a) Strona wymaga przescrolowania
        body.click()
        body.send_keys(Keys.PAGE_DOWN)
        # Zaznacz akceptację regulaminów
        rules = driver.find_element_by_xpath('//label[@for="enp_customer_registration_form_type_consentForm_consent_686_0"]') # noqa
        driver.execute_script("arguments[0].click();", rules)
        # 11 Kliknij "Zarejestruj się"
        zarejestruj_btn = driver.find_element_by_xpath('//*[@class="m-btn m-btn_primary js-register_submit"]') # noqa
        zarejestruj_btn.click()
        # 12 Szukamy błędu
        error = driver.find_element_by_xpath('//*[@class="invalid"]') # noqa
        print(error.text)
        assert error.text == "Podaj prawidłowy adres email"

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
