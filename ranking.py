import streamlit as st
import base64

# HTML 및 CSS를 사용하여 경계선 및 박스 스타일 정의
st.markdown(
    """
    <style>
    .custom-div {
        background-color: rgb(250, 254, 255);
        padding: 50px;
    }
    h2 {
        text-align: center;
        margin-bottom: -80px; /* 제목과 이미지 사이의 간격을 줄이기 */
    }
    .green-text {
        color: #65B741;
    }
    .yellow-text {
        color: #FFD23F;
    }
    p {
        margin-bottom: 30 px;
    }
    table {
        width: 100%;
        border-collapse: collapse;
        background-color: #E0FBE2;
        margin: 0 auto;
        border: 1.5px solid white;
    }
    tr, td {
        text-align: center;
        border: 1.5px solid white;
    }
    th {
        background-color: #BFF6C3;
        border: 1.5px solid white;
    }
    .image-container {
        text-align: center;
        position: relative;
        width: 100%; /* 이미지 컨테이너의 너비를 정의 */
        height: auto; /* 자동으로 높이 조절 */
    }
    .image-container img {
        width: 100%;
        height: auto;
        opacity: 0.5;
    }
    .overlay-box {
        position: absolute;
        width: 400px; /* 박스 크기 */
        height: 60px;
        border: 3px solid #65B741; /* 박스 경계선 색상과 두께 */
        border-radius:50px;
        background-color:white;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .box-top {
        top: 50%; /* 상단 박스의 상단 위치 */
        left: 15%; /* 상단 박스의 왼쪽 위치 */
    }
    .box-bottom {
        top: 70%; /* 하단 박스의 상단 위치 */
        left: 15%; /* 하단 박스의 왼쪽 위치 */
        background-color: #D3D3D3; /* 회색 배경색 */
        border: 3px solid #A9A9A9; /* 회색 경계선 색상 */
}
    .text1{
        color: #65B741;
        margin-left: 10px;
        font-size:18px;
        font-weight: bold;
    }
    .text2{
        color: #65B741;
        margin-left: 30%;
        font-size:18px;
        font-weight: bold;
    }
    .text3{
        color: white;
        margin-left: 10px;
        font-size:18px;
        font-weight: bold;
    }
    .text4{
        color: white;
        margin-left: 30%;
        font-size:18px;
        font-weight: bold;
    }
    .overlay-box img {
        width: auto;
        height: 25px; /* 텍스트 크기에 맞추기 */
        vertical-align: middle; /* 텍스트와 수평 정렬 */
        opacity: 1;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# HTML 컨텐츠
content = """
<div class="custom-div">
    <h2>이달의 <span class="green-text">탄소</span> 절감왕!</h2>
    <div class="image-container">
        <img src="data:image/png;base64,{image_data}" alt="따릉이 자전거 이미지">
        <div class="overlay-box box-top"><img src="data:image/png;base64,{image_data2}" alt="자전거 이미지"><span class="text1">하루 탄소배출량</span><span class="text2">ZERO</span></div>
        <div class="overlay-box box-bottom"><img src="data:image/png;base64,{image_data3}" alt="자동차 이미지"><span class="text3">하루 탄소배출량</span><span class="text4">8.53kg</span></div>
    </div>
    <h3><span class="yellow-text">당첨</span> 축하드려요!</h3>
    <p>매월 15일, 따릉이 최다 이용자 5명에게 에코마일리지가 지급됩니다!</p>
    <table>
        <thead>
            <tr>
                <th>이름</th>
                <th>휴대폰 번호</th>
                <th>이용 횟수</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>김*리</td>
                <td>01-84**-**92</td>
                <td>82회</td>
            </tr>
            <tr>
                <td>박*환</td>
                <td>010-26**-**35</td>
                <td>75회</td>
            </tr>
            <tr>
                <td>강*민</td>
                <td>010-47**-**02</td>
                <td>52회</td>
            </tr>
            <tr>
                <td>신*호</td>
                <td>010-11**-**55</td>
                <td>49회</td>
            </tr>
            <tr>
                <td>민*설</td>
                <td>010-92**-**54</td>
                <td>35회</td>
            </tr>
        </tbody>
    </table>
</div>
"""

# 이미지 파일을 읽어서 base64로 인코딩
def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

image_data = get_base64_image("./따릉이 자전거 이미지.png")
image_data2 = get_base64_image("./따릉이 아이콘.png")
image_data3 = get_base64_image("./승용차 아이콘.png")

# HTML 컨텐츠 삽입 (이미지 포함)
st.markdown(content.format(image_data=image_data, image_data2=image_data2, image_data3=image_data3), unsafe_allow_html=True)

# 페이지 하단에 여백 추가 (선택 사항)
st.write("\n" * 10)
