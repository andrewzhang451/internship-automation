import json
from selenium import webdriver
from selenium.webdriver.common.by import By

# Load configurations
with open("../config/site_config.json", "r") as file:
    site_config = json.load(file)
with open("../data/resume_info.json", "r") as file:
    personal_info = json.load(file)

def fill_form(site_key):
    config = site_config[site_key]
    fields = config["fields"]

    driver = webdriver.Chrome(executable_path="/path/to/chromedriver")
    driver.get(config["url"])

    # Fill out the form
    driver.find_element(By.ID, fields["name"]).send_keys(personal_info["name"])
    driver.find_element(By.ID, fields["email"]).send_keys(personal_info["email"])
    driver.find_element(By.ID, fields["phone"]).send_keys(personal_info["phone"])
    driver.find_element(By.ID, fields["linkedin"]).send_keys(personal_info["linkedin"])
    driver.find_element(By.ID, fields["github"]).send_keys(personal_info["github"])
    driver.find_element(By.ID, fields["resume_upload"]).send_keys(personal_info["resume"])
    driver.find_element(By.ID, fields["cover_letter_upload"]).send_keys(personal_info["cover_letter"])

    input("Complete any captchas or manual steps, then press Enter to continue...")

    # Submit the form
    driver.find_element(By.ID, config["submit_button"]).click()
    print("Form submitted successfully!")
    driver.quit()

# Example usage
fill_form("default")
