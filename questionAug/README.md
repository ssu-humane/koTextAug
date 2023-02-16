# Question-style data augmentation
Question-style data augmentation은 해당 [논문](https://www.dbpia.co.kr/pdf/pdfView.do?nodeId=NODE11113862)에서 제시된 증강 기법으로, 질문 형태의 텍스트를 기존 텍스트에 추가하고 질문에 따른 새로운 라벨을 할당함으로써 데이터 증강을 가능케 함.
<br>
<p align="center"><img src="https://user-images.githubusercontent.com/80903024/219297928-70c46c21-3cb9-4088-97e2-53dfedb7838c.PNG" width="50%" height="50%"></p>

## Data
- [Naver Sentiment Movie Corpus](https://github.com/e9t/nsmc) (NSMC)
  - 네이버의 영화 리뷰 데이터셋인 NSMC 중 10,000개 사용 (랜덤 샘플링)

## Model
- [KoELECTRA](https://github.com/monologg/KoELECTRA)
  - 모델로 한국어로 학습된 Electra 모델인 KoELECTRA를 선택하였으며 원활한 실험을 위해 KoELECTRA-small-v2 사용

## Experiment
- baseline ([nsmc_koelectra_base.ipynb](https://github.com/ssu-humane/koTextAug/blob/main/questionAug/nsmc_koelectra_base.ipynb))
  - 질문 형태의 증강을 적용하지 않은 데이터로 파인튜닝 진행 후 모델 평가
- complete question-style augmentation ([nsmc_koelectra_pseudo_question.ipynb](https://github.com/ssu-humane/koTextAug/blob/main/questionAug/nsmc_koelectra_pseudo_question.ipynb))
  - 완전한 질문 형태의 증강을 적용한 데이터로 파인튜닝 진행 후 모델 평가
  - (해당 리뷰는 부정 리뷰입니까?, 해당 리뷰는 긍정 리뷰입니까?)를 complete question으로 사용
- pseudo question-style augmentation ([nsmc_koelectra_complete_question.ipynb](https://github.com/ssu-humane/koTextAug/blob/main/questionAug/nsmc_koelectra_complete_question.ipynb))
  - pseudo 질문 형태의 증강을 적용한 데이터로 파인튜닝 진행 후 모델 평가
  - (부정적인, 긍정적인)을 pseudo question으로 사용

\*실험은 colab 환경에서 진행됨

## Result
<img src="https://user-images.githubusercontent.com/80903024/219298086-581844ad-cb07-4684-b16d-37bab1c51dec.PNG" width="50%" height="50%">
