import streamlit as st
import modelhelper
import time

st.set_page_config(page_title="LangChain: Model Comparing",layout="wide")
st.title("LangChain: Model Comparing")
st.divider()

col_prompt,col_settings=st.columns([2,3])

with col_prompt:
    prompt=st.text_input(label="Enter your question:")
    st.divider()
    submit_btn=st.button("Ask")

with col_settings:
    temperature=st.slider(label="Temperature",min_value=0.0,max_value=1.0,value=0.7)
    max_tokens=st.slider(label="Maximum Tokens",min_value=100,max_value=500,value=200,step=100)
    
st.divider()

col_gpt, col_gemini, col_claude,col_command=st.columns(4)

with col_gpt:
    if submit_btn:
        with st.spinner("GPT Answering..."):
            st.success("gpt-3.5-turbo")
            start_time=time.perf_counter()
            st.write(modelhelper.ask_gpt(prompt=prompt,temperature=temperature,max_tokens=max_tokens))
            end_time=time.perf_counter()
            elapsed_time=end_time-start_time
            st.caption(f" :hourglass: {round(elapsed_time)} sec")

with col_gemini:
    if submit_btn:
        with st.spinner("Gemini Answering..."):
            st.info("Gemini pro")
            start_time=time.perf_counter()
            st.write(modelhelper.ask_gemini(prompt=prompt,temperature=temperature))
            end_time=time.perf_counter()
            elapsed_time=end_time-start_time
            st.caption(f" :hourglass: {round(elapsed_time)} sec")

with col_claude:
    if submit_btn:
        with st.spinner("Anthropic Answering..."):
            st.error("Claude 2.1")
            start_time=time.perf_counter()
            st.write(modelhelper.ask_anthropic(prompt=prompt,temperature=temperature,max_tokens=max_tokens))
            end_time=time.perf_counter()
            elapsed_time=end_time-start_time
            st.caption(f" :hourglass: {round(elapsed_time)} sec")

with col_command:
    if submit_btn:
        with st.spinner("Cohere Answering..."):
            st.warning("command")
            start_time=time.perf_counter()
            st.write(modelhelper.ask_command(prompt=prompt,temperature=temperature,max_tokens=max_tokens))
            end_time=time.perf_counter()
            elapsed_time=end_time-start_time
            st.caption(f" :hourglass: {round(elapsed_time)} sec")