import streamlit as st
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# 1. 스트림릿 Secrets에 숨겨둔 API 키를 안전하게 로드합니다!
load_dotenv()

# 2. 사용할 모델명을 정확하게 명시해줍니다 (최신 버전 에러 방지)
chat_model = ChatOpenAI(model="gpt-4o-mini")

# 3. 스트림릿 UI 그리기 (교수님 원본 가이드 100% 반영)
st.title("인공지능 시인")
subject = st.text_input("시의 주제를 입력해주세요.")
st.write("시의 주제 : " + subject)

if st.button("시 작성"):
    if not subject.strip():
        st.warning("시의 주제를 먼저 입력해주세요!")
    else:
        with st.spinner("시 작성중 ..."):
            try:
                result = chat_model.invoke(subject + "에 대한 시를 써줘")
                st.write(result.content)
            except Exception as e:
                st.error(f"시 작성 중 에러가 발생했습니다: {e}")
