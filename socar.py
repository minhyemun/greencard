
import streamlit as st
from PIL import Image
import base64
from io import BytesIO
import webbrowser
# 이미지 파일을 Base64로 인코딩하는 함수
def image_to_base64(image_path):
    img = Image.open(image_path)
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return img_str

image_path1 = './icon3.png'
img_base64_1 = image_to_base64(image_path1)
st.markdown(
    """
<style>
    .block-container {
        background-color: rgb(8,190,246);
        padding: 2rem;
        width: 400px;  /* 최대 너비 설정 */
        height: 800px;
        margin: auto;  /* 가운데 정렬 */
        position: relative;
    }
    .bottom-box {
        background-color: rgb(222,248,252); /* 파란색 배경 */
        padding: 1rem;
        width: 400px;  /* 부모 요소에 맞춰 너비 설정 */
        height: 330px;  
        position: absolute;
        bottom: -00px;  
        border-top-left-radius: 20px; /* 왼쪽 하단 모서리 둥글게 */
        border-top-right-radius: 20px; 
        right: -9.5%;
        margin-bottom: -620px;
    }
    .stButton>button {
        width: 100%;
        border-radius: 25px;
        background-color: #2196F3;
        color: white;
        border: none;
        height: 3rem;
        font-size: 1.2rem;
    }
    .title {
        font-size: 24px;
        color: white;
        margin-left: 10px; 
        margin-top: 70px;
        font-weight: bold;
    }
    .title2 {
        font-size: 26px;
        color: black;
        margin-top: -10px;
        margin-left: 10px; 
        font-weight: bold;
    }
    .custom-img {
        width: 400px;
        margin-right: 5px; 
        position: absolute; 
        right: -22%; 
        margin-top: 200px;
        transform: translateY(-50%); /* 세로 중앙 정렬 */
    }
    .card1 {
        width: 100px;
        height: 30px;
        margin-left: 50px;
        margin-top: 240px; 
        background-color: rgb(11,60,121);
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .card1 .text {
        font-size: 17px;
        font-weight: bold;
        color: white;
        margin-left: 24px;
        margin-top: -57px;  
    }
    .card2 {
        width: 130px;
        height: 30px;
        margin-left: 150px;
        margin-top: 20px; 
        background-color: rgb(93,172,67);
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .card2 .text {
        font-size: 17px;
        font-weight: bold;
        color: white;
        margin-left: 22px;
        margin-top: -50px;  
    }
    .title3 {
        font-size: 70px;
        color: black;
        margin-top: 30px;
        margin-left: 30px; 
    }
    .card3 {
        width: 280px;
        height: 45px;
        border-radius: 8px;
        border-color: rgb(168,234,168);
        border: 1.5px solid rgb(168,234,168);
        margin-left: 30px;
        margin-top: 20px; 
        background-color: white;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .card3 .text {
        font-size: 15px;
        color: black;
        margin-left: 25px;
        margin-top: 8px;  
    }
    .card4 {
        width: 280px;
        height: 45px;
        border-radius: 8px;
        border: 1.5px solid rgb(124,247,237);
        margin-left: 30px;
        margin-top: 15px; 
        background-color: white;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .card4 .text {
        font-size: 15px;
        color: black;
        margin-left: 25px;
        margin-top: 8px;  
    }
    .card5 {
        width: 280px;
        height: 45px;
        border-radius: 8px;
        border: 1.5px solid rgb(138,84,201);
        margin-left: 30px;
        margin-top: 15px; 
        background-color: white;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .card5 .text {
        font-size: 15px;
        color: black;
        margin-left: 25px;
        margin-top: 8px;  
    }
    .stButton>button {
    width: 100px;
    border-radius: 5px;
    background-color:rgb(5,172,233);
    color: white;
    border: none;
    height: 30px;
    font-size: 12px;
    margin-top: 20px; 
    margin-left: 115px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.2); 
    transition: background-color 0.3s ease; 
}
    .stButton>button:hover {
    background-color: rgb(4,146,197); /* 마우스 호버 시 배경색 변경 */
}



</style>
""", unsafe_allow_html=True)

# 타이틀 및 정보 텍스트
st.markdown("<div class='title'>친환경 여행<span style='font-size: 20px;'>을 떠나세요!</span></div>", unsafe_allow_html=True)
# 이미지 표시
st.markdown(f'<img src="data:image/png;base64,{img_base64_1}" alt="icon" class="custom-img">', unsafe_allow_html=True)
st.markdown("<div class='bottom-box'></div>", unsafe_allow_html=True)
st.markdown("""

<style>
    .title2 p {
        margin: -4px 0; 
    }
    .title2 span {
        display: block; 
        font-weight: bold; 
        font-size: 20px; 
    }
</style>

<div class='title2'>
    <p><span style='color: rgb(8,57,149);'>쏘카에서 전기차</span></p>
    <p><span style='color: white;'>렌트하면,</span></p>
    <p><span style='color: rgb(81,244,171);'>에코마일리지 적립!</span></p>
</div>
<div class='card1'>
                <p class='card1. text'>SOCAR</p>
</div>
<div class='card2'>
                <p class='card2. text'>에코마일리지</p>
</div>
<div class='title3'>
                <p>💡참여방법</p>
</div>
<div class='card3'>
                <p class='card3. text'>그린카드 앱에서 쏘카 전기차 렌트 예약</p>
            </div>
<div class='card4'>
                <p class='card4. text'>전기차로 여행하고 탄소중립 실천</p>
</div>
<div class='card5'>
                <p class='card5. text'>주행거리만큼 에코마일리지 자동 적립</p>
</div>
<a href='https://www.socar.kr' target='_blank' class='stButton'>
    <button>참여하러 가기</button>
</a>
""", unsafe_allow_html=True)


