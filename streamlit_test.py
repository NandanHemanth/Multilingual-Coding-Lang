import streamlit as st
import subprocess
import openai

# Set up the app layout
st.set_page_config(page_title="IDE", page_icon=":clipboard:")
st.markdown("<h1 style='text-align: center; font-size: 4em;'>Bit-Fiddler</h1>", unsafe_allow_html=True)
st.header("Your Multilingual Coding Playground :computer:\n")

# Set up OpenAI API key
openai.api_key = "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"
model = "text-davinci-002"


def open_file(url):
    with open(url, "r") as file:
        file_contents = file.read()
    return file_contents

def open_file1(text):
    with open(text, 'r') as file:
        file_contents = file.read()
    return file_contents

# Set up app menu
st.markdown("")
st.markdown("")
st.markdown("")
menu = ["Python IDE", "Julia IDE"]
choice = st.sidebar.selectbox("Select a tool:", menu)

if choice == "Python IDE":
    st.subheader("Visual Learning")
    st.markdown("")
    
    prompt = st.text_area("Enter your prompt here")

    # Make API request
    if st.button("Generate text"):
        model = "text-davinci-002"
        response = openai.Completion.create(
            engine=model,
            prompt=prompt,
            max_tokens=1000,
        )
        generated_text = response.choices[0].text
        st.text(generated_text)

    if st.button("Run Visualization"):
        subprocess.run(["python", "graphviz_main.py"])



if choice == "Julia IDE":
    st.subheader("Visual Learning")
    st.markdown("")
    
    prompt = st.text_area("Enter your prompt here")

    # Make API request
    if st.button("Generate text"):
        model = "text-davinci-002"
        response = openai.Completion.create(
            engine=model,
            prompt=prompt,
            max_tokens=1000,
        )
        generated_text = response.choices[0].text
        st.text(generated_text)

    if st.button("Run Visualization"):
        subprocess.run(["python", "graphviz_main.py"])
