# koTextAug
Korean text Augmentation PyPI package for NLP

## Installation
- S/W 다운로드 기반 설치 및 사용
  - 해당 디렉토리 zip 다운로드 해 압축 해제 후 koTextAug 디렉토리 내에서 사용 
- pip 기반 설치 및 사용
  ```
  pip install koTextAug
  ```
  - 위 명령어로 koTextAug 패키지 설치

## Usage
- expample <br>
```
from KoTextAug import Augmentation

aug = Augmentation(mode='whole', tokenizer='okt')
comment = "나는 지금 텍스트 증강 패키지 작성 중입니다."

# Easy Data Augmention 기법
aug.randomSwap(comment, n=2)
aug.randomDeletion(comment, p=0.2)
aug.randomInsertion(comment, n=2)
aug.synonymReplacement(comment, n=2)

# 역번역
aug.backTranslation(comment, lang='en')

# 질문 형태의 증강 기법
aug.question(comment, sent=['일반','혐오'], domain='댓글')
```
*Augmention은 mode와 tokenizer를 입력으로 받는다. 여기서 mode는 총 4가지로 "whole", "trans", "token", "no-package" 어떤 증강 기법을 사용할 것이냐에 따라 선택될 수 있다. trans는 역번역 사용시(googletrans package 필요), token은 EDA 증강 기법 사용시(konlpy 필요), no-package는 question 증강 기법만 사용하려 할 때, whole은 모든 증강 기법 사용시 설정한다. tokenizer는 whole, token 모드에서 필요로 되며, konlpy에서 제공하는 토크나이저로 지정 가능하다.

### 증강 기법 설명
- randomSwap(comment, n): 문장(comment)과 swap 횟수(n)를 입력으로 받는다.<br>
- randomDeletion(comment, p): 문장(comment)과 삭제 확률(p)를 입력으로 받는다.<br>
- randomInsertion(comment, n): 문장(comment)과 삽입될 단어 개수(n)을 입력으로 받는다.<br>
- synonymReplacement(comment, n): 문장(comment)과 대체될 단어 개수(n)을 입력으로 받는다.<br>

- backTranslation(comment, lang): 문장(comment)과 번역될 중간 언어(lang)를 입력으로 받는다.<br>
- question(comment, sent, domain): 문장(comment)과 클래스(sent), 도메인(domain)을 입력으로 받는다.<br>
