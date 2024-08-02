import streamlit as st
import openai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get('OPEN_API_KEY')
client = openai.OpenAI(api_key=api_key)


def main():
    st.set_page_config(page_title="음성 챗봇", page_icon=":스튜디오_마이크:", layout="wide")
   
    st.header("음성 챗봇 프로그램")

    st.markdown("---")
    with st.expander("음성 챗봇 프로그램에 관하여", expanded = True):
        st.write(
            """
            - 음성 번역 챗봇 프로그램의 UI는 스트림릿을 활용합니다.
            - STT(Speech-To-Text)는 OpenAI의 Whisper를 활용합니다.
            - 답변은 OpenAI의 GPT 모델을 활용합니다.
            - TTS(Text-To-Speech)는 OpenAI의 TTS를 활용합니다.
        """)
        st.markdown("")
    with st.sidebar:
        
        model = st.radio(label="GPT 모델 선택", options=["gpt-3.5-turbo", "gpt-4o", "gpt-4-turbo"])
        st.markdown("---")
    
        if st.button(label = "초기화"):
            pass

if __name__ == "__main__":
    print(__name__, "실행")
    main()