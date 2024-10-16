## **🎙음성 챗봇 프로그램**


STT (Speech-to-Text), GPT 모델 답변 생성, 그리고 TTS (Text-to-Speech) 기능을 갖춘 음성 기반 챗봇입니다.
이 프로젝트는 스트림릿(Streamlit)으로 UI를 구축하여 간단하게 음성 챗봇을 활용할 수 있도록 설계되었습니다.

------
📋 기능 소개
STT (Speech-to-Text):
사용자가 녹음한 음성을 텍스트로 변환 (OpenAI Whisper 사용).
GPT 답변 생성:
사용자의 질문에 대한 답변 생성 (GPT-3.5-turbo, GPT-4 등 지원).
TTS (Text-to-Speech):
텍스트 답변을 음성 파일로 변환하여 재생.
UI 구축:
Streamlit을 사용한 직관적인 사용자 인터페이스 제공.

------
🚀 실행 방법
1. 환경설정
   - .env 파일 생성 후 아래와 같이 OpenAI API 키 추가:
     
         OPEN_API_KEY=your_openai_api_key

2. 필요한 패키지 설치
   
       pip install -r requirements.txt

4. 애플리케이션 실행
   
       streamlit run app.py

------
🗂 파일 구조

    .
    ├── app.py              # 메인 앱 파일
    
    ├── requirements.txt    # 필요한 패키지 목록
    
    └── .env                # 환경 변수 파일 (API 키 저장)

------
🛠 사용된 기술 스택
-프레임워크: Streamlit
-AI 모델: OpenAI Whisper, GPT-3.5, GPT-4, TTS
-언어: Python




