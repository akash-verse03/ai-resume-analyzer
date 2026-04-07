import streamlit as st
from utils import extract_text_from_pdf, analyze_resume

st.set_page_config(page_title="AI Resume Analyzer")

st.title("📄 AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")
job_role = st.text_input("Enter Job Role")

if uploaded_file and job_role:
    with st.spinner("Analyzing..."):
        text = extract_text_from_pdf(uploaded_file)
        result = analyze_resume(text, job_role)

        st.subheader("🔍 Result")
        st.write(result)