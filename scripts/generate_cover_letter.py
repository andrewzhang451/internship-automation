import json
from jinja2 import Template

# Load resume info
with open("../data/resume_info.json", "r") as file:
    resume_info = json.load(file)

# Load cover letter template
with open("../templates/cover_letter_template.txt", "r") as file:
    template = Template(file.read())

# Fill details dynamically
data = {
    "recruiter_name": "Hiring Manager",
    "job_title": "Software Engineering Intern",
    "company_name": "Tech Corp",
    "key_skills": "React, TypeScript, SQL, and Appwrite",
    "technologies_used": "React, Tailwind CSS, Python, SQL",
    "relevant_skills": "full-stack development, API integration, and database management",
    **resume_info
}

# Generate cover letter
cover_letter = template.render(data)

# Save to a file
output_file = "../data/cover_letter_TechCorp.pdf"
with open(output_file, "w") as file:
    file.write(cover_letter)

print(f"Cover letter saved to {output_file}")
