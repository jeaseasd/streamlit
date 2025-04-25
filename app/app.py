import streamlit as st
import pandas as pd
import numpy as np

# 페이지 설정
st.set_page_config(
    page_title="내 첫 Streamlit 앱",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 제목과 소개
st.title('환영합니다! 👋')
st.markdown('## 첫 번째 Streamlit 애플리케이션')

st.write("""
이 앱은 Streamlit의 기본 기능을 보여줍니다.
아래에서 다양한 요소들을 확인해보세요.
""")

# 사이드바 
st.sidebar.header('사이드바 메뉴')
option = st.sidebar.selectbox(
    '원하는 기능을 선택하세요:',
    ['데이터 보기', '차트 보기', '정보']
)

# 샘플 데이터 생성
if option == '데이터 보기':
    st.header('샘플 데이터')
    
    data = pd.DataFrame({
        '이름': ['김철수', '이영희', '박민수', '최지은'],
        '나이': [24, 22, 25, 23],
        '점수': [85, 92, 78, 96]
    })
    
    st.dataframe(data)
    
elif option == '차트 보기':
    st.header('샘플 차트')
    
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['A', 'B', 'C']
    )
    
    st.line_chart(chart_data)
    
else:
    st.header('앱 정보')
    st.info('이 앱은 Streamlit 기초 강의용으로 제작되었습니다.')
    st.balloons()