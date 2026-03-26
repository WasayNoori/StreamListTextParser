## Description 
A simple script where a text (in English, French or other latin languages) is dropped in a region. The text is always a list of numbered sentences, each on a new line. The script should simply REMOVE the sentence numbers. Results can be displayed in the same window (overwriting the original)OR a tab labeled "output". It is required that this is something that is avaialble online and preferably, free. Security is NOT an issue. 

## Suggestion
Streamlit Community Cloud 
If you prefer writing Python, Streamlit is likely your best bet. It allows you to turn a script into a web app in minutes.

How it works: You write a simple Python script using st.file_uploader or st.text_area.

Hosting: You push your code to a GitHub repo and link it to Streamlit Community Cloud for free hosting.

UI: It automatically generates a clean, modern interface for uploading files and displaying the "cleaned" text.