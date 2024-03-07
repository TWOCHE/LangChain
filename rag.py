import streamlit as st
import raghelper

st.set_page_config(page_title="RAG via LangChain", layout="wide")
st.title("RAG via :chains: LangChain - URL")
st.divider()

col_input, col_rag,col_normal=st.columns([1,2,2])

with col_input:
    target_url=st.text_input(label="Enter the web address to be processed:")
    st.divider()
    prompt=st.text_input(label="Enter your question:",key="url_prompt")
    st.divider()
    submit_btn=st.button(label="Ask",key="url_button")
    st.divider()

    if submit_btn:
        with col_rag:
            with st.spinner("answer is getting ready..."):
                st.success("ANSWER- RAG is enabled")
                st.markdown(raghelper.rag_with_url(target_url=target_url,prompt=prompt))
                st.divider()

        with col_normal:
            with st.spinner("answer is getting ready..."):
                st.info("ANSWER- RAG is disabled")
                st.markdown(raghelper.ask_gemini(prompt=prompt))
                st.divider()


st.title("RAG via :chains: LangChain - PDF")
st.divider()

col_input, col_rag,col_normal=st.columns([1,2,2])

with col_input:
    selected_file=st.file_uploader(label="Select the file to be processed:",type=["pdf"])
    if selected_file is not None:
        with open("temp.pdf", "wb") as f:
            f.write(selected_file.read())
    st.divider()
    prompt=st.text_input(label="Enter your question:",key="pdf_prompt")
    st.divider()
    submit_btn=st.button(label="Ask",key="pdf_button")
    st.divider()

    if submit_btn:
        with col_rag:
            with st.spinner("answer is getting ready..."):
                st.success("ANSWER- RAG is enabled")
                AI_Response,relevant_documents=raghelper.rag_with_pdf(filepath="temp.pdf", prompt=prompt)
                st.markdown(AI_Response)
                st.divider()
                for doc in relevant_documents:
                    st.caption(doc.page_content)
                    st.markdown(f"Source: {doc.metadata}")
                    st.divider()

        with col_normal:
            with st.spinner("answer is getting ready..."):
                st.info("ANSWER- RAG is disabled")
                st.markdown(raghelper.ask_gemini(prompt=prompt))
                st.divider()



