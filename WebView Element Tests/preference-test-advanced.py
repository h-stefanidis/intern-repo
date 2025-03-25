# Please note that this isn't finalised due to lack of automation IDs for the elements in the app.

import unittest
import time
from appium import webdriver

class FocusBearAppTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Specify the app executable path so WinAppDriver launches it directly.
        desired_caps = {
            "app": r"C:\Program Files (x86)\Focus Bear\Focus Bear.exe"
        }
        cls.driver = webdriver.Remote('http://127.0.0.1:4723', desired_capabilities=desired_caps)
        # Wait for the app to launch completely.
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_button_click_verifies_result(self):
        """Click a button and verify that the result is as expected."""
        try:
            # Locate the Preferences button and click it
            preferences_button = self.driver.find_element_by_name("Preferences")
            preferences_button.click()
            time.sleep(2)
            # Locate the result element using its accessibility id
            result_label = self.driver.find_element_by_accessibility_id("react-tabs-0")
            result_text = result_label.text
            self.assertEqual(result_text, "Submitted", "Result label did not show 'Submitted'")
        except Exception as e:
            self.fail(f"Button click test failed: {e}")

    def test_input_field_typing(self):
        """Type into an input field and verify the entered value."""
        try:
            input_field = self.driver.find_element_by_name("timeCell9")
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
        """Open a modal dialog, select an option from a dropdown, and close the modal."""
        try:
            open_modal_btn = self.driver.find_element_by_name("button-save-settings")
            open_modal_btn.click()
            time.sleep(2)
            # (Add dropdown interaction here if needed)
            close_modal_btn = self.driver.find_element_by_name("btnOK")
            close_modal_btn.click()
            time.sleep(1)
        except Exception as e:
            self.fail(f"Modal dialog test failed: {e}")

if __name__ == '__main__':
    unittest.main(verbosity=2)


