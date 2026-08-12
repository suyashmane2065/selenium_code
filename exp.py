from selenium import webdriver
import time

driver = webdriver.Chrome()

try:
    driver.get("https://example.com")
    print("Website opened successfully")

    # Take screenshot
    driver.save_screenshot("example.png")
    print("Screenshot saved as example.png")

    time.sleep(5)

except Exception as e:
    print("Test Failed:", e)

finally:
    driver.quit()
