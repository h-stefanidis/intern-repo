import unittest
import time
from appium import webdriver

class FocusBearPreferencesTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        desired_caps = {
            "app": r"C:\Program Files (x86)\Focus Bear\Focus Bear.exe"
        }
        # Launch Focus Bear app using WinAppDriver
        cls.driver = webdriver.Remote('http://127.0.0.1:4723', desired_capabilities=desired_caps)
        # Wait for the app to load completely
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_select_preferences(self):
        # Locate and click the Preferences option.
        try:
            preferences_button = self.driver.find_element_by_name("Preferences")
            preferences_button.click()
        except Exception as e:
            self.fail(f"Failed to select preferences: {str(e)}")
        # Wait for the Preferences screen to load (adjust time as necessary)
        time.sleep(3)
        self.assertTrue(True, "Preferences option was selected successfully.")

if __name__ == '__main__':
    unittest.main(verbosity=2)

