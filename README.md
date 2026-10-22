# Selenium Web Automation – Website Screenshot

## Project Description
This project uses **Python and Selenium WebDriver** to automate opening a website in the Chrome browser and capturing a screenshot. It demonstrates basic browser automation and automated website testing.

## Technologies Used
- Python
- Selenium WebDriver
- Google Chrome
- ChromeDriver (managed automatically by Selenium when supported)

## Features
- Opens `https://example.com` in Chrome.
- Displays a success message when the website opens.
- Captures a screenshot of the webpage.
- Saves the screenshot as `example.png`.
- Handles errors using exception handling.
- Closes the browser after execution.

## Prerequisites
- Python installed on your system.
- Google Chrome browser installed.
- Selenium Python package.

## Installation
Install Selenium using the following command:

```bash
pip install selenium
```

## How to Run
1. Save the Python code in a file named `selenium_test.py`.
2. Open a terminal in the folder containing the file.
3. Run the following command:

```bash
python selenium_test.py
```

## Expected Output
```text
Website opened successfully
Screenshot saved as example.png
```

After successful execution, the screenshot will be saved as `example.png` in the current working directory.

## Error Handling
If an error occurs during execution, the script displays a failure message. The `finally` block ensures that the Chrome browser is closed after the test.

## Conclusion
This project demonstrates basic Selenium automation by opening a website, capturing a screenshot, and closing the browser automatically. It provides a simple introduction to browser automation using Python.
