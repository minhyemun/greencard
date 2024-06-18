import streamlit as st
import base64

# 이미지 파일을 Base64로 인코딩하는 함수
def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

image_data = get_base64_image("seal.png")

#퀴즈
quiz = {
"question": "다음 중 탄소중립을 위해 개인이 할 수 있는 노력으로 적절하지 않은 것은 무엇일까요?",
"options": ["대중교통 이용하기", "에너지 효율이 높은 가전제품 사용하기", "일회용 플라스틱 사용 늘리기", "자전거 이용하기"],
"answer": "일회용 플라스틱 사용 늘리기"
}

# HTML 및 CSS를 사용하여 스타일 정의
st.markdown(
    """
    <style>
    .custom-div {
        background-color: rgb(250, 254, 255);
        padding: 50px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column; /* 세로 정렬 변경 */
    }
    .row {
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: row;
        margin-bottom: 50px;
    }
    .text-container {
        margin-left: 20px;
        text-align: left;
    }
    .green-text {
        color: #65B741;
    }
    .quiz-container {
        text-align: left;
        margin-top: 20px;
    }
    .quiz-button {
        display: block;
        width: 100%;
        margin: 10px 0;
        padding: 10px;
        background-color: #FFFFFF; /* 배경색 흰색 */
        border: 2px solid #A9A9A9; /* 테두리 회색 */
        border-radius: 5px;
        font-size: 16px;
        color: #A9A9A9; /* 글씨 회색 */
        cursor: pointer;
    }
    .quiz-button.selected {
        border-color: #65B741 !important; /* 클릭 시 테두리 초록색으로 변경 */
    }
    .submit-button {
        display: block;
        width: 100%;
        margin: 20px 0;
        padding: 10px;
        background-color: #65B741; /* 배경색 초록색 */
        border: 2px solid #65B741; /* 테두리 초록색 */
        border-radius: 5px;
        font-size: 16px;
        color: #FFFFFF; /* 글씨 흰색 */
        cursor: pointer;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 퀴즈 페이지 컨텐츠
st.markdown(
    f"""
    <div class="custom-div">
        <div class="row">
            <img src="data:image/png;base64,{image_data}" alt="seal img" style="width: 200px; height: auto;">
            <div class="text-container">
                <h4 style="margin-bottom: -20px;">
                    <span class="green-text">매일</span> 새로운 <span class="green-text">환경퀴즈</span>에 도전하고
                </h4>
                <h4> 
                    <span class="green-text">환경에 도움이 되는 선택</span>을 함께해요!
                </h4>
            </div>
        </div>
        <div class="quiz-container">
            <h6>{quiz['question']}</h6>
            {"".join(f'<button class="quiz-button" onclick="handleClick(this)">{option}</button>' for option in quiz['options'])}
            <button class="submit-button" onclick="submitQuiz()">답변 제출</button>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# JavaScript 코드 추가
st.markdown(
    f"""
    <script>
        function handleClick(button) {{
            const buttons = document.querySelectorAll('.quiz-button');
            buttons.forEach(btn => {{
                btn.classList.remove('selected');
                btn.style.borderColor = '#A9A9A9'; /* 기본 테두리 색상 */
            }});
            button.classList.add('selected');
            button.style.borderColor = '#65B741'; /* 클릭한 버튼 테두리 초록색으로 변경 */
        }}

        function submitQuiz() {{
            const selectedButton = document.querySelector('.quiz-button.selected');
            if (selectedButton) {{
                const imageSrc = "data:image/png;base64,{popup_image_data}";
                const popup = window.open("", "popup", "width=400,height=400");
                popup.document.write('<html><head><title>결과</title></head><body>');
                popup.document.write('<img src="' + imageSrc + '" style="width:100%; height:auto;">');
                popup.document.write('</body></html>');
            }} else {{
                alert('옵션을 선택해주세요.');
            }}
        }}
    </script>
    """,
    unsafe_allow_html=True
)
