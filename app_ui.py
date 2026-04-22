import streamlit as st
import requests

st.title("📄 AI Resume Analyzer")

# Upload resume
uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

# Job description
job_desc = st.text_area("Enter Job Description")

if st.button("Analyze Resume"):
    if uploaded_file and job_desc:
        files = {"file": uploaded_file}
        data = {"job_desc": job_desc}

        response = requests.post(
            "http://127.0.0.1:8000/analyze-resume",
            files=files,
            data=data
        )

        result = response.json()

        st.subheader("📊 ATS Score")
        st.write(result.get("ats_score"))

        st.subheader("📈 Similarity Score")
        st.write(result.get("similarity_score"))

        st.subheader("✅ Matched Skills")
        st.write(result.get("matched_skills"))

        st.subheader("❌ Missing Skills")
        st.write(result.get("missing_skills"))

        st.subheader("📂 Sections")
        st.write(result.get("sections"))

        st.subheader("💡 Suggestions")
        for s in result.get("suggestions", []):
            st.write("- " + s)

    else:
        st.warning("Please upload resume and enter job description")

# Chat section
st.subheader("💬 Chat with Resume")

question = st.text_input("Ask a question")
resume_text = st.text_area("Paste Resume Text for Chat")

if st.button("Ask"):
    if question and resume_text and job_desc:
        response = requests.post(
            "http://127.0.0.1:8000/chat",
            data={
                "question": question,
                "resume_text": resume_text,
                "job_desc": job_desc
            }
        )

        st.write("🤖:", response.json().get("answer"))