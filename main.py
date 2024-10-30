import streamlit as st
from scrape import scrape_website, split_dom_content, clean_body_content, extract_body_content
from parse import parse_with_ollama


st.title("My first web scrapper")
url = st.text_input("Enter website url")
html_string = "<h3>this is an html string</h3>"
st.html(html_string)
if st.button("Scrape Site"):
    st.write("website scrapping is running now")
    result = scrape_website(url)
    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)
    st.session_state.dom_content = cleaned_content

    with st.expander("view more content"):
        st.text_area("Dom Content", cleaned_content, height=300)

if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse?")

    if st.button("Parse Content"):
        st.write("Parsing the content")
        dom_chunks = split_dom_content(st.session_state.dom_content)
        result = parse_with_ollama(dom_chunks, parse_description)
        st.write(result)

