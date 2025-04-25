import streamlit as st
import pandas as pd
import numpy as np

st.title('고급 레이아웃 디자인 🎨')

# 기본 컬럼 레이아웃
st.header('1. 기본 컬럼 레이아웃')

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("컬럼 1")
    st.write("이것은 첫 번째 컬럼입니다.")
    st.metric(label="온도", value="32°C", delta="1.5°C")

with col2:
    st.subheader("컬럼 2")
    st.write("이것은 두 번째 컬럼입니다.")
    st.metric(label="습도", value="68%", delta="-2%")

with col3:
    st.subheader("컬럼 3")
    st.write("이것은 세 번째 컬럼입니다.")
    st.metric(label="기압", value="1013 hPa", delta="+5 hPa")

# 다양한 너비의 컬럼
st.header('2. 가변 너비 컬럼')

col1, col2, col3 = st.columns([1, 2, 1])  # 비율 기반 너비

with col1:
    st.subheader("좁은 컬럼")
    st.write("1 단위 너비")

with col2:
    st.subheader("넓은 컬럼")
    st.write("2 단위 너비")
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['A', 'B', 'C'])
    st.line_chart(chart_data)

with col3:
    st.subheader("좁은 컬럼")
    st.write("1 단위 너비")