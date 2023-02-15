# Question-style data augmentation

Question-style data augmentation은 해당 [논문](https://www.dbpia.co.kr/pdf/pdfView.do?nodeId=NODE11113862)에서 제시된 증강 기법으로 증강을 적용하지 않은 데이터로 학습된 모델 대비 향상된 성능을 불러옴
## Data
- [Naver Sentiment Movie Corpus](https://github.com/e9t/nsmc) (NSMC)
  - 네이버의 영화 리뷰 데이터셋인 NSMC 일부 사용

## Model
- [KoELECTRA](https://github.com/monologg/KoELECTRA)
  - 모델로 한국어로 학습된 Electra 모델인 KoELECTRA를 선택하였으며 원활한 실험을 위해 KoELECTRA-small-v2 사용
