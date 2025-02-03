import streamlit as st
from func import *

st.header('정확한 정보를 입력해주세요')
pains = st.multiselect("통증부위를 선택해주세요", pain_list)

col1, col2 = st.columns(2)
with col1:
    check = True if st.radio("동일증상으로 입내원하신 적이 있으신가요?", ("있어요", "없어요"), index = 1) == "있어요" else False
    age = st.text_input("나이 입력")
    department = st.selectbox("동일증상으로 방문하신 진료과를 기입해주세요", options=mapping.values(), disabled=not check, index = None)
    key = next((key for key, value in mapping.items() if value == department), None)
    
with col2:
    gender = st.radio("성별 선택", ("남성", "여성"))
    gender_xgb = 1 if gender == "남성" else 2
    nursing = st.text_input("동일증상으로 요양하신 일수를 기입해주세요", disabled=not check, index = 0)
    median = st.text_input("동일증상으로 복약하신 일수를 기입해주세요", disabled=not check, index = 0)
    
# 버튼 클릭 시 결과 출력
if st.button("완료"):
    if not pains or not gender or not age:
        st.markdown("<h3>입력을 다시 확인해주세요.</h3>", unsafe_allow_html = True)
    elif check and (not department or not nursing or not median):
        st.markdown("<h3>입력을 다시 확인해주세요.</h3>", unsafe_allow_html = True)   
    else:
        if check:
            text = "저는 " + gender + "이고 " + age + "살 입니다." + " 동일 증상으로 " +\
            department + "에 방문한 적이 있고 " + "약은 총" + median + "일 만큼 먹었습니다." \
            + " 추가적으로 요양한 일수는 " + nursing + "일 입니다." 
        else:
            text = "저는" + gender + "이고 " + age + " 살 입니다. 동일 증상으로 방문한적은 없어요"
        st.write(f"xgb에 들어갈 테이블 데이터: 성별코드 {gender_xgb}, 나이코드 {get_age_group(age)}, 요양일수 {nursing}, 복약 일수 {median}, 방문했던 진료과와 코드 {department, key}")
        st.write("bert에 들어갈 텍스트 데이터: ", text)
        inputs = tokenizer(text, return_tensors = "pt", padding = True, truncation = True, max_length = 512)
        
        with torch.no_grad():
            outputs = model(**inputs)
            pred = torch.argmax(outputs.logits, dim=1).item()
        
        st.markdown("<h3>진단 결과</h3>", unsafe_allow_html = True)
        st.markdown(f'{mapping[pred]}')
        

        

