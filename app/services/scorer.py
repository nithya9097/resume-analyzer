import spacy

nlp = spacy.load("en_core_web_sm")

SKILL_KEYWORDS = [
    "python", "machine learning", "deep learning", "nlp",
    "sql", "data analysis", "pandas", "numpy",
    "tensorflow", "pytorch", "power bi", "excel"
]

# 🔹 1. Extract skills
def extract_skills(text):
    doc = nlp(text.lower())

    found_skills = set()

    for skill in SKILL_KEYWORDS:
        if skill in text.lower():
            found_skills.add(skill)

    for chunk in doc.noun_chunks:
        chunk_text = chunk.text.strip()
        if len(chunk_text.split()) <= 3:
            found_skills.add(chunk_text)

    return list(found_skills)


# 🔹 2. Skill gap analysis (THIS MUST EXIST)
def skill_gap_analysis(resume_text, job_desc):
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_desc)

    matched = list(set(resume_skills) & set(job_skills))
    missing = list(set(job_skills) - set(resume_skills))

    return matched, missing


# 🔹 3. ATS score
def calculate_ats_score(similarity, matched_skills, missing_skills, resume_text):
    total_skills = len(matched_skills) + len(missing_skills)
    skill_score = (len(matched_skills) / total_skills) * 100 if total_skills > 0 else 0

    similarity_score = similarity * 100

    word_count = len(resume_text.split())
    if word_count > 300:
        length_score = 100
    elif word_count > 150:
        length_score = 70
    else:
        length_score = 40

    final_score = (
        0.5 * skill_score +
        0.3 * similarity_score +
        0.2 * length_score
    )

    return round(final_score, 2)

def detect_sections(resume_text):
    text = resume_text.lower()

    sections = {
        "skills": ["skills", "technical skills"],
        "experience": ["experience", "work experience"],
        "education": ["education", "academic"],
        "projects": ["projects", "project"]
    }

    result = {}

    for section, keywords in sections.items():
        found = any(keyword in text for keyword in keywords)
        result[section] = "present" if found else "missing"

    return result

def calculate_section_score(section_result):
    total = len(section_result)
    present = sum(1 for v in section_result.values() if v == "present")

    score = (present / total) * 100
    return round(score, 2)

def generate_suggestions(matched, missing, sections, resume_text):
    suggestions = []

    # 🔹 Missing skills
    if missing:
        suggestions.append(f"Add missing skills: {', '.join(missing)}")

    # 🔹 Section improvements
    for section, status in sections.items():
        if status == "missing":
            suggestions.append(f"Include a {section.capitalize()} section in your resume")

    # 🔹 Resume length check
    word_count = len(resume_text.split())
    if word_count < 150:
        suggestions.append("Increase resume content with more details and achievements")

    # 🔹 Achievements suggestion
    if "project" in resume_text.lower():
        suggestions.append("Add measurable achievements (e.g., improved accuracy by 20%)")

    # 🔹 General improvement
    if len(matched) < 3:
        suggestions.append("Improve keyword alignment with job description")

    return suggestions