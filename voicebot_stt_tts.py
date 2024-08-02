import streamlit as st
import openai
import os
from dotenv import load_dotenv

load_dotenv()
from audiorecorder import audiorecorder
from datetime import datetime
api_key = os.environ.get('OPEN_API_KEY')
client = openai.OpenAI(api_key=api_key)

def STT(speech):
    filename = 'input.mp3'
    speech.export(filename,format='mp3')

    with open(filename,"rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model ="whisper-1",
            file = audio_file
        )
    os.remove(filename)
    return transcription.text    


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

    system_content = "You are a thoughtful assistant. Respond to all input in 25 words and answer in korea"

    if "chat" not in st.session_state:
        st.session_state["chat"] = []
    if "message" not in st.session_state:
        st.session_state["messages"] = [{"role":"system", "content": system_content}]
    if "check_reset" not in st.session_state:
        st.session_state["check_reset"] = False


    with st.sidebar:
        
        model = st.radio(label="GPT 모델 선택", options=["gpt-3.5-turbo", "gpt-4o", "gpt-4-turbo"])
        st.markdown("---")
    
        if st.button(label = "초기화"):
            st.session_state["chat"] = []
            st.session_state["messages"] = [{"role": "system", "content": system_content}]
            st.session_state["check_reset"] = True

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("질문하기")

        audio = audiorecorder()
        if (audio.duration_seconds > 0) and (st.session_state["check_reset"]==False):
            st.audio(audio.export().read())

            question = STT(audio)

            now = datetime.now().strftime("$H:%M")
            st.session_state["chat"] = st.session_state["chat"] + [("user", now, question)]
            st.session_state["messages"] = st.session_state["messages"] + [{"role": "user", "content": question}]



    with col2:
        st.subheader("질문/답변")



if __name__ == "__main__":
    main()