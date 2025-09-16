import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PyPDF2 import PdfReader
from docx import Document
import io

# 🎯 App Title
st.title("📄 Word Cloud from PDF or Word Document")

# 📤 File Upload
uploaded_file = st.file_uploader("Upload a PDF or Word (.docx) file", type=["pdf", "docx"])

# 🎨 Customize WordCloud
max_words = st.slider("Max number of words", 10, 200, 100)
background_color = st.selectbox("Background color", ["white", "black", "skyblue", "pink", "yellow"])

def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def extract_text_from_docx(file):
    doc = Document(file)
    return "\n".join([para.text for para in doc.paragraphs])

# 📊 Generate WordCloud
if uploaded_file is not None:
    file_type = uploaded_file.name.split('.')[-1].lower()
    
    if file_type == "pdf":
        text = extract_text_from_pdf(uploaded_file)
    elif file_type == "docx":
        text = extract_text_from_docx(uploaded_file)
    else:
        st.error("Unsupported file type.")
        text = ""

    if text.strip():
        wordcloud = WordCloud(
            width=800,
            height=400,
            max_words=max_words,
            background_color=background_color
        ).generate(text)

        # 📷 Display WordCloud
        fig, ax = plt.subplots()
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis("off")
        st.pyplot(fig)
    else:
        st.warning("No text found in the document.")
