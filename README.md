# AI Resume Analyzer & ATS Scoring System

An advanced **GenAI-powered Resume Analyzer** that evaluates resumes against job descriptions using **NLP, Machine Learning, and LLMs**.
It provides ATS scores, skill gap analysis, section evaluation, suggestions, and an interactive chatbot.

---

## 🌟 Features

* 📄 Resume Upload & Parsing (PDF)
* 🤖 AI-based Resume Analysis (LLM)
* 📊 ATS Score Calculation (Custom Logic)
* 🔍 Semantic Similarity (Embeddings)
* 🧠 Smart Skill Extraction (NLP)
* ❌ Missing Skills Detection
* 📂 Resume Section Detection
* 💡 Actionable Suggestions Engine
* 💬 Chatbot for Resume Q&A
* 🌐 Streamlit UI for user interaction

---

## 🛠️ Tech Stack

### Backend

* FastAPI
* Python
* Uvicorn

### AI / ML

* OpenAI API
* Sentence Transformers
* FAISS
* spaCy (NLP)

### Frontend

* Streamlit

### Tools

* Git & GitHub

---

## 📂 Project Structure

```
resume-analyzer-ai/
│
├── app/
│   ├── main.py
│   ├── routes/
│   │   └── analyze.py
│   ├── services/
│   │   ├── parser.py
│   │   ├── embedding.py
│   │   ├── llm_service.py
│   │   └── scorer.py
│   └── models/
│       └── schema.py
│
├── app_ui.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```
git clone https://github.com/your-username/resume-analyzer.git
cd resume-analyzer
```

---

### 2️⃣ Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Add Environment Variables

Create `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

---

### 5️⃣ Run Backend Server

```
uvicorn app.main:app --reload
```

👉 Open:

```
http://127.0.0.1:8000/docs
```

---

### 6️⃣ Run Frontend (Streamlit)

```
streamlit run app_ui.py
```

👉 Open:

```
http://localhost:8501
```

---

## 📊 API Endpoints

### 🔹 Analyze Resume

```
POST /analyze-resume
```

**Input:**

* Resume file (PDF)
* Job description

**Output:**

* ATS Score
* Similarity Score
* Matched Skills
* Missing Skills
* Sections
* Suggestions

---

### 🔹 Chat with Resume

```
POST /chat
```

**Input:**

* Question
* Resume Text
* Job Description

**Output:**

* AI-generated answer

---

## 📸 Screenshots

*(Add screenshots here after deployment)*

---

## 🚀 Deployment

* Backend: Render
* Frontend: Streamlit Cloud

---

## 📌 Future Improvements

* Resume Rewriting (LLM)
* PDF Export of Improved Resume
* User Authentication
* Database Integration
* Advanced Skill Ontology

---

## 👨‍💻 Author

**Nithya Nandeep Kumar**
B.Tech CSE (Data Science)

---

## ⭐ Acknowledgements

* OpenAI
* Hugging Face
* Streamlit
* FastAPI

---

## 📢 Note

⚠️ Do NOT upload `.env` file to GitHub
⚠️ Keep API keys secure

---

## 💯 Project Highlights

✔ Real-world ATS simulation
✔ Hybrid AI system (LLM + ML)
✔ Explainable AI outputs
✔ Full-stack deployment ready

---

# 🔥 This project demonstrates strong skills in:

* Generative AI
* NLP
* Backend Development
* API Design
* ML Integration

---
*
