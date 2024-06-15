import streamlit as st
import pandas as pd
from googletrans import Translator

# Bhagavad Gita Chapter Summaries (Sample Dictionary)
bhagavad_gita_data = {
    "Chapter 1": {
        "en": "Arjuna's Despair and the Battlefield Dilemma",
        "hi": "अर्जुन का विषाद और युद्धभूमि की दुविधा",
        "mr": "अर्जुनाचे दुःख आणि युद्धभूमीची दुविधा"
    },
    "Chapter 2": {
        "en": "The Yoga of Knowledge",
        "hi": "ज्ञान का योग",
        "mr": "ज्ञानाचा योग"
    },
    # ... more chapters
}

# Function to translate text
def translate_text(text, target_language):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

# Streamlit App
st.title("Bhagavad Gita Chapter Summaries")

selected_chapter = st.selectbox("Select Chapter", list(bhagavad_gita_data.keys()))
selected_language = st.selectbox("Select Language", ["en", "hi", "mr"])  # Add more as needed

if selected_chapter and selected_language:
    chapter_data = bhagavad_gita_data[selected_chapter]
    if selected_language in chapter_data:
        summary = chapter_data[selected_language]
        st.write(summary)
    else:
        st.warning(f"Summary not available in {selected_language}. Translating...")
        translated_summary = translate_text(chapter_data["en"], selected_language)
        st.write(translated_summary)
