import csv

# Log data
application_data = {
    "Company Name": "Tech Corp",
    "Job Title": "Software Engineering Intern",
    "Application Link": "https://application-form-link.com",
    "Status": "Submitted",
    "Notes": "Follow-up in 2 weeks"
}

# Write to CSV
file_name = "../applications.csv"
fields = ["Company Name", "Job Title", "Application Link", "Status", "Notes"]

try:
    with open(file_name, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writerow(application_data)
except FileNotFoundError:
    # Create a new file if not existing
    with open(file_name, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerow(application_data)

print("Application logged successfully!")
