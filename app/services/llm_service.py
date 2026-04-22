import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

print("API KEY LOADED:", os.getenv("OPENAI_API_KEY"))

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_resume_with_llm(resume_text, job_desc):
    try:
        resume_text = resume_text[:3000]

        prompt = f"""
        You are an expert ATS resume analyzer.

        Analyze this resume:
        {resume_text}

        Job Description:
        {job_desc}

        Provide:
        - ATS Score (0-100)
        - Strengths
        - Weaknesses
        - Missing Skills
        - Improvement Suggestions
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error in LLM processing: {str(e)}"