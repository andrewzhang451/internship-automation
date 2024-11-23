import json
from jinja2 import Template

# Load personal information
with open("../data/resume_info.json", "r") as file:
    resume_info = json.load(file)

# Cover letter template
template_text = """
Dear {{ recruiter_name }},

I am thrilled to apply for the {{ job_title }} position at {{ company_name }}. With a strong foundation in {{ key_skills }} and hands-on experience in {{ projects }}, I am confident in my ability to excel in this role.

As an Event Manager at Illinois Institute of Technology, I led teams and ensured seamless event execution. My technical expertise, showcased in projects like {{ notable_project }}, demonstrates my ability to deliver impactful solutions.

I would be delighted to bring my skills in {{ relevant_skills }} to your team. Please feel free to contact me at {{ email }} or {{ phone }}.

Thank you for considering my application.

Sincerely,
{{ name }}
"""

template = Template(template_text)

# Fill in placeholders
data = {
    "recruiter_name": "Hiring Manager",
    "job_title": "Software Engineering Intern",
    "company_name": "Tech Corp",
    "key_skills": "React, Python, SQL, and Vue.js",
    "projects": "social media app development and inventory management systems",
    "notable_project": "Social Media App",
    "relevant_skills": "full-stack development and API integration",
    **resume_info
}

# Generate the cover letter
cover_letter = template.render(data)

# Save the cover letter
output_file = "../data/cover_letter.pdf"
with open(output_file, "w") as file:
    file.write(cover_letter)

print(f"Cover letter saved at {output_file}")
