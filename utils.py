import PyPDF2
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def analyze_resume(resume_text, job_role):
    prompt = f"""
    You are an expert resume reviewer.

    Analyze this resume for: {job_role}

    Return:
    Skills:
    - ...

    Suggestions:
    - ...

    Match Score:
    (number out of 100)

    Resume:
    {resume_text}
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content