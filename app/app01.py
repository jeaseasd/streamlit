import streamlit as st

# 텍스트 요소 활용 예시
st.title('다양한 텍스트 요소 👨‍💻')

st.header('1. 헤더와 서브헤더')
st.subheader('이것은 서브헤더입니다')

st.markdown('## 마크다운 지원')
st.markdown('*이탤릭* 또는 **볼드** 텍스트를 사용할 수 있습니다.')
st.markdown('- 불릿 포인트 1\n- 불릿 포인트 2')

st.text('단순한 텍스트는 st.text()로 표시합니다.')

st.write('st.write()는 다양한 형식을 자동으로 처리합니다.')
st.write({'a': 1, 'b': 2})  # 딕셔너리도 표시

st.caption('이것은 작은 캡션 텍스트입니다')

code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')

st.latex(r'''
    a + ar + ar^2 + ar^3 + \cdots + ar^{n-1} = \frac{a(1-r^n)}{1-r}
''')