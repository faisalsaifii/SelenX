from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import string
import random
from dotenv import load_dotenv
import os

load_dotenv()

url = os.environ.get("URL")
signUpButtonID = os.environ.get("SIGNUP_BUTTON_ID")
inputsClassName = os.environ.get("INPUTS_CLASSNAME")
nameField_xpath = "//input[@type='text']"
emailField_xpath = "//input[@type='email']"
passwordField_xpath = "//input[@type='password']"
submitButton_xpath = os.environ.get("SUBMIT_BUTTON_XPATH")
signOutButton_xpath = os.environ.get("SIGNOUT_BUTTON_XPATH")
driver = webdriver.Firefox()

try:
    for _ in range(1000):
        driver.get(url)
        name = "".join(random.choices(string.ascii_lowercase + string.digits, k=20))
        email = (
            "".join(random.choices(string.ascii_lowercase + string.digits, k=10))
            + "@gmail.com"
        )
        password = "".join(random.choices(string.ascii_uppercase + string.digits, k=20))

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, signUpButtonID))
        )

        signUpButton = driver.find_element(By.ID, signUpButtonID)
        signUpButton.click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, inputsClassName))
        )

        nameField = driver.find_element(By.XPATH, nameField_xpath)
        nameField.send_keys(name)

        emailField = driver.find_element(By.XPATH, emailField_xpath)
        emailField.send_keys(email)

        passwordField = driver.find_element(By.XPATH, passwordField_xpath)
        passwordField.send_keys("12345678")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, submitButton_xpath))
        )

        submitButton = driver.find_element(By.XPATH, submitButton_xpath)

        driver.execute_script("arguments[0].click();", submitButton)

        WebDriverWait(driver, 10000).until(
            EC.presence_of_element_located((By.XPATH, "//textarea"))
        )

        signOutButton = driver.find_element(By.XPATH, signOutButton_xpath)
        driver.execute_script("arguments[0].click();", signOutButton)

finally:
    driver.quit()
