
""". Smart Resume Keyword Matcher
Given a resume text and job description:
Extract keywords
Calculate match percentage
Suggest missing skills"""






resume = input("Enter resume text: ").lower()
job_desc = input("Enter job description: ").lower()

keywords = [
    "python", "java", "sql", "machine learning",
    "data analysis", "communication", "teamwork",
    "excel", "power bi", "ai"
]

matched = []
missing = []

for word in keywords:
    if word in job_desc:
        if word in resume:
            matched.append(word)
        else:
            missing.append(word)

if len(matched) + len(missing) > 0:
    match_percent = (len(matched) / (len(matched) + len(missing))) * 100
else:
    match_percent = 0

print("Matched Keywords:", matched)
print("Missing Skills:", missing)
print("Match Percentage:", round(match_percent, 2), "%")
