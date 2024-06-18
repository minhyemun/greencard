
import streamlit as st
from PIL import Image
import base64
from io import BytesIO

# 이미지 파일을 Base64로 인코딩하는 함수
def image_to_base64(image_path):
    img = Image.open(image_path)
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return img_str

# 이미지 파일 경로
# image_path1 = 'static/icon1.png'
# image_path2 = 'static/icon2.png'
# img_base64_1 = image_to_base64(image_path1)
# img_base64_2 = image_to_base64(image_path2)

# HTML 및 CSS를 사용하여 스타일 정의 및 출력
st.markdown(
    f"""
    <style>

    .card3 {{
        width: 360px;
        height: 70px;
        margin-left: 150px;
        margin-top: 30px; /* 조정 필요한 위치에 따라 margin-top 값을 조정하세요 */
        background-color: rgb(181,223,169);
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }}
    .icon3 {{
        font-size: 2.7rem;
        margin-left: 25px;
    }}
    .card3 .text {{
        font-size: 14px;
        color: #666;
        margin-left: 100px;
        margin-top: -57px;
    }}
    .card3 .text2 {{
        font-size: 14px;
        font-weight: bold;
        color: #666;
        margin-left: 100px;
        margin-top: -15px;
    }}
    .card4 {{
        width: 360px;
        height: 70px;
        margin-left: 150px;
        margin-top: 12px;
        background-color: rgb(203,232,195);
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }}
    .card4 .text {{
        font-size: 14px;
        color: #666;
        margin-left: 100px;
        margin-top: -57px;
    }}
    .card4 .text2 {{
        font-size: 14px;
        font-weight: bold;
        color: #666;
        margin-left: 100px;
        margin-top: -15px;
    }}
    .icon4 {{
        font-size: 2.7rem;
        margin-left: 25px;
    }}
    .card5 {{
        width: 360px;
        height: 70px;
        margin-left: 150px;
        margin-top: 12px;
        background-color: rgb(252,232,252);
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }}
    .card5 .text {{
        font-size: 14px;
        color: #666;
        margin-left: 100px;
        margin-top: -57px;
    }}
    .card5 .text2 {{
        font-size: 14px;
        font-weight: bold;
        color: #666;
        margin-left: 100px;
        margin-top: -15px;
    }}   
    .icon5 {{
        font-size: 2.7rem;
        margin-left: 25px;
    }}
    .card6 {{
        width: 360px;
        height: 70px;
        margin-left: 150px;
        margin-top: 12px;
        background-color: rgb(228,217,252);
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }}
    .card6 .text {{
        font-size: 14px;
        color: #666;
        margin-left: 100px;
        margin-top: -57px;
    }}
    .card6 .text2 {{
        font-size: 14px;
        font-weight: bold;
        color: #666;
        margin-left: 100px;
        margin-top: -15px;
    }} 
    .icon6 {{
        font-size: 2.7rem;
        margin-left: 25px;
    }}
    .card7 {{
        width: 360px;
        height: 70px;
        margin-left: 150px;
        margin-top: 12px;
        background-color: rgb(214,228,234);
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }}
    .card7 .text {{
        font-size: 14px;
        color: #666;
        margin-left: 100px;
        margin-top: -57px;
    }}
    .card7 .text2 {{
        font-size: 14px;
        font-weight: bold;
        color: #666;
        margin-left: 100px;
        margin-top: -15px;
    }} 
    .icon7 {{
        font-size: 2.7rem;
        margin-left: 25px;
    }}
    .title {{
        font-size: 24px;
        color: #000;
        padding-bottom: px;
        margin-left: 170px; 
        margin-bottom: 2px;
        font-weight: bold;
    }}
    .info-text1 {{
        font-size: 16px;
        color: #666;
        margin-top: 5px;
        margin-left: 170px;
    }}
    .info-text2 {{
        font-size: 16px;
        color: #666;
        margin-top: -15px;
        margin-left: 170px;
    }}

    .stButton {{
        margin-top: 30px; /* 상단 여백 설정 */
        margin-left: 300px; /* 왼쪽 여백 설정 */
        margin-top: 15px;
    }}

        /* 출발지 입력 필드의 너비 조정 */
    .stTextInput {{
            width: 300px !important;
            margin-left:170px;
            margin-bottom: -10px;
        }}
        /* 도착지 입력 필드의 너비 조정 */
    .stTextInput {{
            width: 300px !important;
            margin-left:170px;
        }}

    </style>
    """,
    unsafe_allow_html=True
)

# 타이틀 및 정보 텍스트
st.markdown("<div class='title'>탄소배출절감 지도</div>", unsafe_allow_html=True)
st.markdown("<p class='info-text1'>내가 이동하는 거리의 교통수단별</p>", unsafe_allow_html=True)
st.markdown("<p class='info-text2'>탄소배출량을 조회해보아요!</p>", unsafe_allow_html=True)
# 출발지 및 도착지 입력 필드
departure = st.text_input("출발지:",key="departure_input")
destination = st.text_input("도착지:", key="destination_input")

# 조회 버튼 및 결과 출력
button_clicked = st.button("조회")
st.markdown(
    """
    <style>
        /* 출발지 입력 필드의 너비 조정 */
        div[data-testid="stTextInput"][data-baseweb="input"] {
            width: 300px !important;
        }
        /* 도착지 입력 필드의 너비 조정 */
        div[data-testid="stTextInput"][data-baseweb="input"] {
            width: 300px !important;
        }
    </style>
    """,
    unsafe_allow_html=True  # unsafe_allow_html=True 옵션을 통해 HTML을 안전하게 허용
)

if button_clicked:
    if departure and destination:
        st.markdown(
            f"""
            
            <div class='card3'>
                <span class='icon3'>🚴‍♂️</span>
                <p class='card3. text'>소요시간: 3분</p>
                <p class='card3. text2'>탄소배출량: 0</p>
            </div>
            <div class='card4'>
                <span class='icon4'>🏃‍♂️</span>
                <p class='card4. text'>소요시간: 13분</p>
                <p class='card4. text2'>탄소배출량: 0</p>
            </div>
            <div class='card5'>
                <span class='icon5'>🚗</span>
                <p class='card5. text'>소요시간: 7분</p>
                <p class='card5. text2'>탄소배출량: 0.36kg = A4용지 72장</p>
            </div>
            <div class='card6'>
                <span class='icon6'>🚌</span>
                <p class='card6. text'>소요시간: 7분</p>
                <p class='card6. text2'>탄소배출량: 0.01335kg = 커피 한잔</p>
            </div>
            <div class='card7'>
                <span class='icon7'>🚆</span>
                <p class='card7. text'>소요시간: 7분</p>
                <p class='card7. text2'>탄소배출량: 0.0615kg = 플라스틱 물병 한 개</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown("<style>.stButton { display: none; }</style>", unsafe_allow_html=True)
