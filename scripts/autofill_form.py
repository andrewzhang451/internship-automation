from selenium import webdriver
from selenium.webdriver.common.by import By
import json

# Load resume info
with open("../data/resume_info.json", "r") as file:
    resume_info = json.load(file)

# Initialize WebDriver
driver = webdriver.Chrome(executable_path="/path/to/chromedriver")

# Open the application form
driver.get("https://application-form-link.com")

# Fill in the form
driver.find_element(By.ID, "name").send_keys(resume_info["name"])
driver.find_element(By.ID, "email").send_keys(resume_info["email"])
driver.find_element(By.ID, "linkedin").send_keys(resume_info["linkedin"])
driver.find_element(By.ID, "github").send_keys(resume_info["github"])
driver.find_element(By.ID, "resume_upload").send_keys("../data/Andrew_Zhang_Resume.pdf")
driver.find_element(By.ID, "cover_letter_upload").send_keys("../data/cover_letter_TechCorp.pdf")

# Submit the form
driver.find_element(By.ID, "submit").click()

print("Application form submitted successfully!")

driver.quit()
