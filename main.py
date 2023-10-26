import streamlit as st
from langchain.llms import CTransformers


llm = CTransformers(
    model = "llama-2-7b-chat.ggmlv3.q6_K.bin",
    model_type="llama"
)

st.title('인공지능 테스트')

content = st.chat_input("입력해주세요")

if content:
    with st.spinner('잠시만 기다려 주세요...'):
        result = llm.predict("write a poem about" + content + ": ")
        st.write(result)





