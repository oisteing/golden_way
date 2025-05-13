import random
import streamlit as st

# Sidesetting
st.set_page_config(page_title="Tilfeldig setning", layout="wide")

@st.cache_data
def load_sentences(path="sentences.txt"):
    with open(path, "r", encoding="utf-8") as f:
        return [linje.strip() for linje in f if linje.strip()]

sentences = load_sentences()

if "sentence" not in st.session_state:
    st.session_state.sentence = random.choice(sentences)

if st.button("Ny setning"):
    st.session_state.sentence = random.choice(sentences)

# Kun CSS for knapp og setningscontainer
st.markdown(
    """
    <style>
      /* Hvit knapp med mørk kant, posisjonert under header */
      .stButton {
        position: absolute;
        top: 70px;    /* ned fra toppen av viewport */
        left: 20px;
        z-index: 1000;
      }
      .stButton > button {
        background-color: white;
        color: #333;
        border: 2px solid #333;
        padding: 10px 20px;
        font-size: 18px;
        cursor: pointer;
        border-radius: 4px;
      }

      /* Sentral beholder ligger også under header */
      .container {
        position: absolute;
        top: 70px;    /* sørger for at vi er under header */
        left: 0; right: 0; bottom: 0;
        display: flex;
        justify-content: center;
        align-items: center;
      }
      .sentence-box {
        border: 2px solid #333;
        padding: 20px;
        font-family: Arial, sans-serif;
        font-size: 24px;
        text-align: center;
        max-width: 80%;
        background-color: #f9f9f9;
        border-radius: 8px;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

# Vi legger kun ut setningsboksen – knappen er levert av st.button
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
