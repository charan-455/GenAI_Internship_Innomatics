import streamlit as st
from google_ai import review_code

# Streamlit UI
st.title(":blue[Code Review with Gen AI] 🧑‍💻")

st.subheader("Select the programming language :")

language_option = st.selectbox(
    "-",
    ("Python", "C", "C++","Java"),
    placeholder="Choose a language",
    index=None,
)

# Input Code
st.subheader("Enter your code here :memo:")
code_input = st.text_area("-",placeholder="Type you code here", height=200)

if st.button("Submit for Review"):
    if code_input and language_option:
        with st.spinner("Reviewing your code..."):
            review_feedback = review_code(code_input,language_option)

        # Display Results
        st.subheader(":green[Code Review Feedback]")
        st.write(review_feedback)
    else:
        st.error("Please select both language and enter code.")
