import re
import streamlit as st

st.set_page_config(page_title="List Number Remover", layout="centered")
st.title("List Number Remover")
st.write("Paste a numbered list below. Each line should start with a number (e.g. `1. sentence` or `1) sentence`).")

input_text = st.text_area("Input", height=300, placeholder="1. First sentence\n2. Deuxième phrase\n3. Third sentence")

def remove_numbers(text: str) -> str:
    lines = text.splitlines()
    cleaned = []
    for line in lines:
        # Remove leading number followed by . ) : or space variants, then optional whitespace
        cleaned_line = re.sub(r"^\s*\d+[\.\)\:\-]?\s*", "", line)
        cleaned.append(cleaned_line)
    return "\n".join(cleaned)

tab_input, tab_output = st.tabs(["Input", "Output"])

with tab_input:
    if st.button("Clean numbers"):
        if input_text.strip():
            st.session_state["output"] = remove_numbers(input_text)
        else:
            st.warning("Please paste some text first.")

with tab_output:
    output = st.session_state.get("output", "")
    if output:
        st.text_area("Cleaned text", value=output, height=300)
        st.download_button("Download as .txt", data=output, file_name="cleaned.txt", mime="text/plain")
    else:
        st.info("Click 'Clean numbers' on the Input tab to see results here.")
