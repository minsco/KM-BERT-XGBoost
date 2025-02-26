# KM-BERT-XGBoost
# 🏥 Intelligent Medical Department Recommendation System

## 📖 Introduction
현대 의료 환경에서는 **환자의 주관적인 증상 입력을 기반으로 적절한 진료과를 추천하는 AI 모델**이 필요합니다.  
본 연구는 **텍스트 기반 증상 분석과 정형 데이터를 결합한 멀티모달 접근법**을 통해 보다 정확한 진료과 추천 모델을 개발하는 것을 목표로 합니다.

## 🎯 Key Features
✅ **텍스트 및 정형 데이터 통합 분석**  
   - 환자의 증상(텍스트 데이터) + 성별, 연령, 진료 이력(정형 데이터) 융합  
✅ **멀티모달 머신러닝 모델 적용**  
   - `KM-BERT`(텍스트 분석) + `XGBoost`(정형 데이터 분석) + `Stack-Ensemble`(결합 최적화)  
✅ **진료과 추천 정확도 향상**  
   - 기존 단일 모델 대비 **약 20% 이상의 성능 향상**  
✅ **데이터 증강 기법 활용 (LLM 기반)**  
   - 부족한 의료 데이터를 보완하여 **모델의 일반화 성능 강화**  

## 🔍 Methodology
### 1️⃣ 데이터 수집 및 전처리
- 국민건강보험공단의 진료 내역 데이터를 활용하여 증상과 진료과 정보를 매핑  
- LLM(Large Language Model)을 사용하여 부족한 증상 데이터를 증강  

### 2️⃣ 멀티모달 데이터 처리 (Late Fusion 방식 적용)
- **KM-BERT**: 환자의 증상 설명(텍스트) 분석  
- **XGBoost**: 환자의 연령, 성별, 진료 이력(정형 데이터) 분석  
- **Stack-Ensemble**: 최종 예측 모델로 `CatBoost` 적용  

### 3️⃣ 모델 학습 및 평가
- **교차 검증(5-fold cross-validation)**을 적용하여 일반화 성능 평가  
- 기존 추천 시스템 대비 **Precision, Recall, F1-score 등 주요 성능 지표 개선**

### 4️⃣ 모델 아키텍처 시각화

![image](https://github.com/user-attachments/assets/e374c781-9f28-44ed-bb06-afbc53412c2e)


## 📊 Performance Evaluation
| Model | Accuracy | F1-score | Precision | Recall |
|--------|----------|---------|----------|--------|
| **XGBoost** | 0.34 | 0.23 | 0.31 | 0.23 |
| **KM-BERT** | 0.53 | 0.43 | 0.43 | 0.36 |
| **Stack-Ensemble (Ours)** | **0.75** | **0.73** | **0.71** | **0.70** |

✔️ 기존 단일 모델(`XGBoost` or `KM-BERT`) 대비 **Stack-Ensemble 모델이 월등한 성능을 보임**  
✔️ 학습이 진행될수록 정확도 및 재현율이 지속적으로 증가하는 경향을 확인  

## 🚀 Application Implementation
본 연구의 결과를 실제 의료 환경에서 활용하기 위해 **모바일 애플리케이션 프로토타입**을 개발하였습니다.

### 🛠️ 기술 스택
- **Frontend**: `React Native`
- **Backend**: `FastAPI`

### 📱 주요 기능
- 환자가 증상을 입력하면 AI 모델이 **적절한 진료과 추천**  
- 의료 서비스 접근성을 높이고, 과잉 진료 문제를 해결하는 데 기여  

## 🔮 Future Work
🔹 실제 임상 환경에서 **전자 의무 기록(EMR) 데이터 추가 학습**  
🔹 다국어 지원 및 다양한 의료 기관에서의 테스트 진행  
🔹 추천 시스템을 **실제 병원 예약 시스템과 연계하여 상용화 가능성 평가**  

