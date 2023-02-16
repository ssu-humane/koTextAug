# Question-style data augmentation

Question-style data augmentation은 해당 [논문](https://www.dbpia.co.kr/pdf/pdfView.do?nodeId=NODE11113862)에서 제시된 증강 기법으로 증강을 적용하지 않은 데이터로 학습시보다 향상된 성능을 불러옴
## Data
- [Naver Sentiment Movie Corpus](https://github.com/e9t/nsmc) (NSMC)
  - 네이버의 영화 리뷰 데이터셋인 NSMC 중 10,000개 사용 (랜덤 샘플링)

## Model
- [KoELECTRA](https://github.com/monologg/KoELECTRA)
  - 모델로 한국어로 학습된 Electra 모델인 KoELECTRA를 선택하였으며 원활한 실험을 위해 KoELECTRA-small-v2 사용

## Experiment
- baseline
  - 질문 형태의 증강을 적용하지 않은 데이터로 파인튜닝 진행 후 모델 평가
- complete question-style augmentation
  - 완전한 질문 형태의 증강을 적용한 데이터로 파인튜닝 진행 후 모델 평가
  - (해당 리뷰는 부정 리뷰입니까?, 해당 리뷰는 긍정 리뷰입니까?)를 complete question으로 사용
- pseudo question-style augmentation
  - pseudo 질문 형태의 증강을 적용한 데이터로 파인튜닝 진행 후 모델 평가
  - (부정적인, 긍정적인)을 pseudo question으로 사용

\*실험은 colab 환경에서 진행됨
