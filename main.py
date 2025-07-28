
import streamlit as st
from utils.pdf_reader import read_pdf
from utils.summarizer import summarize_text
from utils.translator import translate_text
from utils.qa_engine import ask_question

st.set_page_config(page_title="Basahin Mo Na Lang AI", layout="centered")
st.title("📚 Basahin Mo Na Lang AI")
st.markdown("**AI na magbabasa at sasagot para sa'yo.**")

lang = st.selectbox("🗣️ Piliin ang wika ng output:", ["Tagalog", "English"])
is_tl = lang == "Tagalog"

uploaded_file = st.file_uploader("📤 I-upload ang PDF ng libro mo:", type=["pdf"])

book_text = ""
if uploaded_file:
    book_text = read_pdf(uploaded_file)
    st.success("✅ File loaded successfully.")

    st.subheader("📖 Buod ng Libro")
    summary = summarize_text(book_text)
    if is_tl:
        summary = translate_text(summary, target_lang="tl")
    st.write(summary)

    st.subheader("❓ Magtanong tungkol sa libro")
    user_q = st.text_input("Halimbawa: 'Ano ang aral sa kabanata 5?' o 'Sino si Elias?'")
    if user_q:
        answer = ask_question(book_text, user_q)
        if is_tl:
            answer = translate_text(answer, target_lang="tl")
        st.markdown(f"**Sagot:** {answer}")
