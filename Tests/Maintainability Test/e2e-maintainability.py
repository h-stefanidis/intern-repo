import unittest
import time
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Helper function for retry logic.
def retry(action, attempts=3, delay=1):
    last_exception = None
    for _ in range(attempts):
        try:
            return action()
        except Exception as e:
            last_exception = e
            time.sleep(delay)
    raise last_exception

# ---------------------------
# Page Object Model (POM)
# ---------------------------

class BasePage:
    def __init__(self, driver):
        self.driver = driver

class HomePage(BasePage):
    def click_preferences(self):
        # Wait for the Preferences button to be clickable, then click it.
        preferences_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "Preferences"))
        )
        preferences_button.click()
    
    def get_result_text(self):
        # Wait until the result element is visible, then return its text.
        result_label = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ACCESSIBILITY_ID, "react-tabs-0"))
        )
        return result_label.text

class LoginPage(BasePage):
    def login(self, username, password):
        # Wait for the username field and type the username.
        username_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "Username"))
        )
        username_field.clear()
        username_field.send_keys(username)
        
        # Find and fill the password field.
        password_field = self.driver.find_element_by_name("Password")
        password_field.clear()
        password_field.send_keys(password)
        
        # Click the login button.
        login_button = self.driver.find_element_by_name("Login")
        login_button.click()

class ModalPage(BasePage):
    def open_modal(self):
        open_modal_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "button-save-settings"))
        )
        open_modal_btn.click()
    
    def close_modal(self):
        close_modal_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "btnOK"))
        )
        close_modal_btn.click()

# ---------------------------
# Test Suite
# ---------------------------

class FocusBearE2ETests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        desired_caps = {
            "app": r"C:\Program Files (x86)\Focus Bear\Focus Bear.exe"
        }
        # Launch the app using WinAppDriver.
        cls.driver = webdriver.Remote('http://127.0.0.1:4723', desired_capabilities=desired_caps)
        # Set an implicit wait for all element searches.
        cls.driver.implicitly_wait(10)
        # Allow the app to fully launch.
        time.sleep(5)
        # Initialize Page Objects.
        cls.home_page = HomePage(cls.driver)
        cls.login_page = LoginPage(cls.driver)
        cls.modal_page = ModalPage(cls.driver)
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login_and_preferences(self):
        """Log in and navigate to Preferences, then verify the result."""
        try:
            # If login is required, perform login; adjust credentials as needed.
            self.login_page.login("testuser", "password123")
            time.sleep(2)
        except Exception as e:
            print("Login might not be required:", e)
        # Navigate to Preferences.
        self.home_page.click_preferences()
        time.sleep(2)
        result_text = self.home_page.get_result_text()
        self.assertEqual(result_text, "Submitted", "Preferences result mismatch")
    
    def test_input_field_typing(self):
        """Type into an input field and verify the entered value."""
        try:
            # Use retry logic to overcome transient failures.
            input_field = retry(lambda: self.driver.find_element_by_name("timeCell9"), attempts=3, delay=1)
            input_field.clear()
            input_field.send_keys("9:00 AM")
            time.sleep(1)
            entered_value = input_field.get_attribute("Value")
            if not entered_value:
                entered_value = input_field.text
            self.assertEqual(entered_value, "9:00 AM", "Input field value mismatch")
        except Exception as e:
            self.fail(f"Input field test failed: {e}")
    
    def test_modal_dialog_and_dropdown(self):
        """Open a modal dialog, interact with a dropdown if needed, and close the modal."""
        try:
            self.modal_page.open_modal()
            time.sleep(2)
            # Optionally: Interact with dropdown elements here.
            self.modal_page.close_modal()
            time.sleep(1)
        except Exception as e:
            self.fail(f"Modal dialog test failed: {e}")
    
    def test_repeated_execution(self):
        """Run a test multiple times to detect inconsistencies."""
        for i in range(3):
            with self.subTest(run=i):
                self.home_page.click_preferences()
                result_text = self.home_page.get_result_text()
                self.assertEqual(result_text, "Submitted", "Repeated test: Preferences result mismatch")
                # Optionally, reset state here if necessary.
                time.sleep(2)

if __name__ == '__main__':
    unittest.main(verbosity=2)
