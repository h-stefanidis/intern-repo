import unittest
import time
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# A simple retry helper function
def retry(action, attempts=3, delay=1):
    last_exception = None
    for _ in range(attempts):
        try:
            return action()
        except Exception as e:
            last_exception = e
            time.sleep(delay)
    raise last_exception

class FocusBearAppTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Launch the Focus Bear app directly using its executable path.
        desired_caps = {
            "app": r"C:\Program Files (x86)\Focus Bear\Focus Bear.exe"
        }
        cls.driver = webdriver.Remote('http://127.0.0.1:4723', desired_capabilities=desired_caps)
        # Set an implicit wait to let elements appear before interacting.
        cls.driver.implicitly_wait(10)
        # Wait for the app to launch completely.
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_button_click_verifies_result(self):
        """Click a button and verify that the result is as expected using explicit waits."""
        try:
            # Wait explicitly for the Preferences button to be clickable.
            preferences_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.NAME, "Preferences"))
            )
            preferences_button.click()
            
            # Wait explicitly for the result element to be visible.
            result_label = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ACCESSIBILITY_ID, "react-tabs-0"))
            )
            result_text = result_label.text
            self.assertEqual(result_text, "Submitted", "Result label did not show 'Submitted'")
        except Exception as e:
            self.fail(f"Button click test failed: {e}")

    def test_input_field_typing(self):
        """Type into an input field and verify the entered value, using retry logic."""
        try:
            # Retry finding the input field up to 3 times.
            input_field = retry(lambda: self.driver.find_element_by_name("timeCell9"), attempts=3, delay=2)
            input_field.clear()
            input_field.send_keys("9:00 AM")
            time.sleep(1)
            entered_value = input_field.get_attribute("Value")
            if not entered_value:
                entered_value = input_field.text
            self.assertEqual(entered_value, "9:00 AM", "Input field value did not match '9:00 AM'")
        except Exception as e:
            self.fail(f"Input field test failed: {e}")

    def test_modal_dialog_and_dropdown(self):
        """Open a modal dialog, select an option from a dropdown, and close the modal using explicit waits."""
        try:
            # Wait for the modal dialog open button to be clickable.
            open_modal_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.NAME, "button-save-settings"))
            )
            open_modal_btn.click()
            # Wait for the modal dialog to appear (waiting for the OK button).
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.NAME, "btnOK"))
            )
            # (If a dropdown interaction is required, insert explicit wait and selection code here)
            # Wait for the close button to be clickable and then click it.
            close_modal_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.NAME, "btnOK"))
            )
            close_modal_btn.click()
            time.sleep(1)
        except Exception as e:
            self.fail(f"Modal dialog test failed: {e}")

if __name__ == '__main__':
    # For detecting inconsistencies, you might run the test suite multiple times in your CI/CD pipeline.
    # Here we simply run the tests once.
    unittest.main(verbosity=2)
