MOCK_PROFILE = {
    "name": "Alex Morgan",
    "headline": "Senior Software Engineer | Cloud Architecture Specialist",
    "summary": (
        "Passionate software engineer with over 8 years of experience building scalable web applications "
        "and cloud native solutions. Specialized in Python, Go, and AWS cloud architecture. "
        "Enjoys mentoring junior developers and contributing to open-source automation tools."
    ),
    "experience": [
        {
            "role": "Senior Software Engineer",
            "company": "TechCorp Solutions",
            "duration": "2022 - Present",
            "description": "Led a team of 4 engineers to migrate legacy monolith architecture to microservices on AWS, improving system reliability by 35%."
        },
        {
            "role": "Software Engineer",
            "company": "Innovate Web Studio",
            "duration": "2019 - 2022",
            "description": "Developed high-throughput REST APIs using FastAPI and PostgreSQL. Implemented automated CI/CD pipelines."
        }
    ],
    "interests": [
        "Cloud FinOps",
        "Distributed Systems",
        "Technical Writing",
        "Hiking & Landscape Photography"
    ]
}


def get_formatted_profile():
    """Formats the profile dictionary into a clean string for the AI context."""
    exp_strings = []
    for exp in MOCK_PROFILE["experience"]:
        exp_strings.append(f"- {exp['role']} at {exp['company']} ({exp['duration']}): {exp['description']}")

    experience_text = "\n".join(exp_strings)
    interests_text = ", ".join(MOCK_PROFILE["interests"])

    profile_text = f"""
Name: {MOCK_PROFILE['name']}
Headline: {MOCK_PROFILE['headline']}

Summary:
{MOCK_PROFILE['summary']}

Professional Experience:
{experience_text}

Interests:
{interests_text}
"""
    return profile_text.strip()