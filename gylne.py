import random
import streamlit as st

# Side­konfigurasjon
st.set_page_config(page_title="Tilfeldig setning", layout="centered")

@st.cache_data
def load_sentences(path="sentences.txt"):
    with open(path, encoding="utf-8") as f:
        return [l.strip() for l in f if l.strip()]

sentences = load_sentences()

if "sentence" not in st.session_state:
    st.session_state.sentence = random.choice(sentences)

if st.button("Ny setning"):
    st.session_state.sentence = random.choice(sentences)

# Sett CSS slik at teksten er mørk (#333) uansett tema og en god kontrast
st.markdown(
    """
    <style>
      /* Knapp øverst til venstre */
      .stButton {
        position: absolute;
        top: 80px;
        left: 20px;
        z-index: 1000;
      }
      .stButton > button {
        background-color: white;
        color: #333 !important;
        border: 2px solid #333;
        padding: 10px 20px;
        font-size: 18px;
        border-radius: 4px;
      }

      /* Container for setningen */
      .container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: calc(100vh - 80px);
        margin-top: 80px;
      }
      .sentence-box {
        border: 2px solid #333;
        background-color: #f9f9f9;
        color: #333 !important;         /* Helt sikkert mørk tekst */
        padding: 20px;
        font-size: 1.5rem;
        text-align: center;
        max-width: 90%;
        border-radius: 8px;
        word-wrap: break-word;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

# Render kun boksen med setningen
st.markdown(
    f"""
    <div class="container">
      <div class="sentence-box">
        {st.session_state.sentence}
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)
