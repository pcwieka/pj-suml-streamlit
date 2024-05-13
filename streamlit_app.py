import streamlit as st
from transformers import pipeline

st.title('Polyglot')
st.divider()
st.image('sprechen_sie_deutsch.jpg')

st.write('''
Polyglot is designed to bridge language barriers and uncover the underlying emotions in texts.

- **Text Translation**: Instantly convert English sentences into German with state-of-the-art accuracy.
- **Sentiment Analysis**: Uncover the emotional tone of English texts, from joyful to sorrowful, with a single click.
''')

st.divider()

option = st.selectbox(
    "Options",
    [
        "Text translation from English to German",
        "Sentiment analysis of text (eng)",
    ]
)

# Translating text from English to German
if option == "Text translation from English to German":
    text = st.text_area("Enter the text in English", max_chars=500)
    if text:
        with st.spinner("Translating..."):
            try:
                translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-de")
                translation = translator(text)
                st.write('Translation to German:')
                st.text(translation[0]['translation_text'])
                st.balloons()
            except Exception as e:
                st.error(f"An error occurred during translation: {e}")

# Sentiment analysis of the text
if option == "Sentiment analysis of text (eng)":
    text = st.text_area("Enter the text")
    if text:
        with st.spinner("Analyzing sentiment..."):
            try:
                classifier = pipeline("sentiment-analysis")
                answer = classifier(text)
                st.write("Sentiment analysis result:", answer)
            except Exception as e:
                st.error(f"An error occurred during sentiment analysis: {e}")

st.divider()
st.write('Created by s22000')
