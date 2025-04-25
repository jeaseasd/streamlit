import streamlit as st
import datetime

st.title('입력 위젯 마스터하기 🎛️')

# 기본 입력 위젯
st.header('기본 입력 위젯')

col1, col2 = st.columns(2)

with col1:
    name = st.text_input('이름을 입력하세요', '홍길동')
    age = st.number_input('나이를 입력하세요', min_value=0, max_value=120, value=30)
    height = st.slider('키(cm)', min_value=100, max_value=200, value=170)
    
with col2:
    is_member = st.checkbox('회원입니까?')
    membership = st.radio('멤버십 단계', ['기본', '프리미엄', 'VIP'], 
                          disabled=not is_member)
    join_date = st.date_input('가입일', datetime.date.fromisoformat('2002-06-10'))

# 선택 위젯
st.header('선택 위젯')

col3, col4 = st.columns(2)

with col3:
    option = st.selectbox('좋아하는 프로그래밍 언어', 
                         ['Python', 'JavaScript', 'Java', 'C++', 'Go'])
    st.write(f'선택: {option}')
    
with col4:
    options = st.multiselect('사용해본 프레임워크',
                            ['Django', 'Flask', 'React', 'Vue', 'Angular'],
                            ['Django'])
    st.write(f'선택 항목: {", ".join(options)}')

# 파일 업로드
st.header('파일 업로드')
uploaded_file = st.file_uploader("데이터 파일을 업로드하세요", 
                                type=['csv', 'xlsx', 'txt'])

if uploaded_file is not None:
    st.success('파일이 업로드되었습니다!')
    st.write(f'파일명: {uploaded_file.name}')
    
# 색상 선택기
color = st.color_picker('색상을 선택하세요', '#00f900')
st.write(f'선택한 색상: {color}')

# 시간 입력
time_value = st.time_input('약속 시간', datetime.time(12, 0), step=60*60)
st.write(f'선택한 시간: {time_value}')