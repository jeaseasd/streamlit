import streamlit as st

st.title('컨테이너와 확장기 📦')

# 기본 컨테이너
st.header('1. 기본 컨테이너')

with st.container():
    st.write("이것은 컨테이너 내부입니다.")
    st.bar_chart({"데이터": [1, 5, 2, 6, 2, 1]})

# 확장기 (Expander)
st.header('2. 확장기 (Expander)')

with st.expander("클릭하여 세부 정보 보기"):
    st.write("이것은 확장기 내부에 있는 내용입니다.")
    st.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=200)
    
    with st.container():
        st.write("확장기 내부에 컨테이너를 중첩할 수 있습니다.")
        st.code("""
        with st.expander("확장기 제목"):
            st.write("확장기 내용")
        """)

# 여러 확장기 사용
st.header('3. 여러 확장기 사용')

with st.expander("섹션 1: 프로젝트 개요", expanded=True):
    st.write("프로젝트의 목적과 주요 기능에 대한 설명입니다.")
    st.info("이 프로젝트는 데이터 시각화를 위해 만들어졌습니다.")

with st.expander("섹션 2: 데이터 소스"):
    st.write("이 앱에서 사용하는 데이터 소스에 대한 정보입니다.")
    st.warning("데이터는 매일 업데이트됩니다.")

with st.expander("섹션 3: 사용 방법"):
    st.write("앱 사용 방법에 대한 지침입니다.")
    st.success("왼쪽 사이드바에서 옵션을 선택하세요.")