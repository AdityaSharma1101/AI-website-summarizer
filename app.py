# app.py
import streamlit as st
from scraper import extract_text_from_url
from summarizer import summarize_text

st.set_page_config(page_title="Website Summarizer", layout="centered")
st.title("🌐 Website Summarizer (Local LLM)")
st.write("Paste a website URL (like a Wikipedia article) and get a friendly, readable summary.")

url = st.text_input("🔗 Enter the website URL:")

if st.button("Summarize") and url:
    with st.spinner("📄 Extracting content..."):
        content = extract_text_from_url(url)

    if not content or len(content) < 100:
        st.error("Couldn't extract meaningful content. Try a different URL.")
    else:
        with st.spinner("🧠 Summarizing using local model..."):
            summary = summarize_text(content[:4000])  # Trim large text to stay under model limit
            st.success("✅ Summary Ready!")
            st.markdown("### 📝 Summary")
            st.markdown(summary)
