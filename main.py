load_dotenv()
from langchain.chat_models import ChatOpenAI

chat_model = ChatOpenAI()

st.title('인공지능 시안')




content = st.chat_input("입력해주세요")
# if content:
#     st.write(f"User has sent the following prompt: {prompt}")


if content:
    with st.spinner('잠시만 기다려 주세요...'):
        result = chat_model.predict(content + "에 대한 시를 써줘")
        st.write(result)





