from fastapi import APIRouter, UploadFile, File, Form
from app.services.parser import extract_text
from app.services.llm_service import analyze_resume_with_llm
from app.services.embedding import calculate_similarity
from app.services.scorer import generate_suggestions
from app.services.scorer import (
    skill_gap_analysis,
    calculate_ats_score,
    detect_sections,
    calculate_section_score
)

router = APIRouter()

# =========================
# 🔹 Resume Analysis API
# =========================
@router.post("/analyze-resume")
async def analyze_resume(file: UploadFile = File(...), job_desc: str = Form(...)):
    
    # 🔹 Step 1: Extract text
    text = extract_text(file)

    # 🔹 Step 2: LLM (may fail if billing not enabled)
    llm_result = analyze_resume_with_llm(text, job_desc)

    # 🔹 Step 3: Semantic similarity
    similarity = calculate_similarity(text, job_desc)

    # 🔹 Step 4: Skill gap
    matched, missing = skill_gap_analysis(text, job_desc)

    # 🔹 Step 5: ATS score
    ats_score = calculate_ats_score(similarity, matched, missing, text)

    # 🔹 Step 6: Section detection
    sections = detect_sections(text)
    section_score = calculate_section_score(sections)

    # 🔹 Step 7: Suggestions
    suggestions = generate_suggestions(matched, missing, sections, text)

    # 🔹 Final response
    return {
        "message": "Analysis Complete",
        "ats_score": ats_score,
        "similarity_score": round(similarity * 100, 2),
        "matched_skills": matched,
        "missing_skills": missing,
        "sections": sections,
        "section_score": section_score,
        "suggestions": suggestions,
        "analysis": llm_result
    }


# =========================
# 🔥 Chatbot API (NEW)
# =========================
@router.post("/chat")
async def chat_with_resume(
    question: str = Form(...),
    resume_text: str = Form(...),
    job_desc: str = Form(...)
):
    question = question.lower()

    # 🔹 Reuse your logic
    matched, missing = skill_gap_analysis(resume_text, job_desc)
    sections = detect_sections(resume_text)

    # 🔹 Smart responses
    if "missing skill" in question:
        return {"answer": f"You are missing these skills: {', '.join(missing)}"}

    elif "improve" in question:
        return {
            "answer": "To improve your resume: add missing skills, include projects, and add measurable achievements."
        }

    elif "section" in question:
        missing_sections = [k for k, v in sections.items() if v == "missing"]
        return {
            "answer": f"Your resume is missing these sections: {', '.join(missing_sections)}"
        }

    elif "ats score" in question:
        return {
            "answer": "Improve ATS score by increasing skill match, adding projects, and improving resume structure."
        }

    else:
        return {
            "answer": "Your resume is good, but improving skills and structure will increase your chances."
        }