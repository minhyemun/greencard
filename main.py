import streamlit as st

# 사이드바 옵션
tab = st.sidebar.radio("APP_Design:", ['Ranking', 'Quiz', 'Map', 'Socar'])

# 페이지 실행
if tab == 'Ranking':
    # `ranking.py` 스크립트 실행
    exec(open("ranking.py").read())
elif tab == 'Quiz':
    # `quiz.py` 스크립트 실행
    exec(open("quiz.py").read())
elif tab == 'Map':
    # `map.py` 스크립트 실행
    exec(open("map.py").read())
elif tab == 'Socar':
    # `socar.py` 스크립트 실행
    exec(open("socar.py").read())
