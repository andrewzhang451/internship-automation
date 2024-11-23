import csv
from datetime import datetime

def log_application(company_name, job_title, application_url, status="Submitted"):
    log_file = "../applications.csv"
    fields = ["Date", "Company Name", "Job Title", "Application URL", "Status"]

    data = {
        "Date": datetime.now().strftime("%Y-%m-%d"),
        "Company Name": company_name,
        "Job Title": job_title,
        "Application URL": application_url,
        "Status": status
    }

    try:
        with open(log_file, "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writerow(data)
    except FileNotFoundError:
        with open(log_file, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            writer.writerow(data)

    print(f"Application logged for {company_name} - {job_title}")

# Example usage
log_application("Tech Corp", "Software Engineering Intern", "https://example.com/application-form")
