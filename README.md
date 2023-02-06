# koTextAug
한국어 텍스트 데이터 증강을 위한 PyPI 패키지

## Installation
- S/W 다운로드 기반 설치 및 사용
  - 해당 디렉토리 zip 다운로드 해 압축 해제 후 koTextAug 디렉토리 내에서 사용 
- pip 기반 설치 및 사용
  ```
  pip install koTextAug
  ```
  - 위 명령어로 koTextAug 패키지 설치

## requirements
- konlpy
- requests
- beautifulsoup4
- googletrans==3.1.0a0
- pandas
- numpy

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
aug.synonymReplacement(comment, n=1)

# 역번역
aug.backTranslation(comment, lang='en')

# 질문 형태의 증강 기법
aug.question([comment,0], sent=['일반','혐오'], domain='댓글')
```
- **Augmention** 클래스는 *mode*와 *tokenizer*를 인자로 받는다. 여기서 mode는 총 4가지로 "whole", "trans", "token", "no-package" 어떤 증강 기법을 사용할 것이냐에 따라 선택될 수 있다. trans는 역번역 사용시(googletrans package 필요), token은 EDA 증강 기법 사용시(konlpy 필요), no-package는 question 증강 기법만 사용하려 할 때, whole은 모든 증강 기법 사용시 설정한다. <br>tokenizer는 whole, token 모드에서 필요로 되며, konlpy에서 제공하는 토크나이저로 지정 가능하다.

### 증강 기법 설명
- randomSwap(comment, n): 문장(comment)과 swap 횟수(n)를 입력으로 받는다.
  - 문장을 토크나이징 한 후 랜덤하게 토큰을 선택해 n번의 swap을 진행해 새로운 문장을 만든다. *konlpy 필요
  ```
  지금는 입니다 텍스트 증강 패키지 작성중나.
  ```
  <br>
- randomDeletion(comment, p): 문장(comment)과 삭제 확률(p)를 입력으로 받는다.<br>
  - 문장을 토크나이징 한 후 p의 확률로 토큰을 삭제해 새로운 문장을 만든다. *konlpy 필요
  - return: "나는 지금 텍스트 패키지 작성중" <br>
- randomInsertion(comment, n): 문장(comment)과 삽입될 단어 개수(n)을 입력으로 받는다.<br>
  - 문장을 토크나이징 한 후 n개의 토큰을 랜덤하게 선택해 해당 토큰의 유의어를 랜덤한 위치에 삽입해 새로운 문장을 만든다. *konlpy 필요
  - return: "이제 나는 지금 텍스트 증강 패키지 현재 작성중입니다."<br>
- synonymReplacement(comment, n): 문장(comment)과 대체될 단어 개수(n)을 입력으로 받는다.<br>
  - 문장을 토크나이징 한 후 랜덤하게 n개의 토큰을 선택해 유의어로 치환해 새로운 문장을 만든다. *konlpy 필요
  - return: "나는 지금 텍스트 증강 패키지 작어입니다." 
- backTranslation(comment, lang): 문장(comment)과 번역될 중간 언어(lang)를 입력으로 받는다.
  - 문장을 kor -> lang -> kor 순으로 번역해 새로운 문장을 만든다. *googletrans 필요
  - return: "현재 텍스트 확대 패키지를 작성 중입니다."<br>
- question([comment,label], sent, domain): 문장(comment)과 라벨(label)의 리스트와 클래스(sent), 도메인(domain)을 입력으로 받는다. *[논문 참고](https://www.dbpia.co.kr/pdf/pdfView.do?nodeId=NODE11113862)
  - 문장을 입력받은 클래스로 질문을 만들고, 라벨로 답변 라벨을 재구성해 새로운 형태로 증강한다.
  - return: [['나는 지금 텍스트 증강 패키지 작성중입니다.', '해당 댓글은 일반 댓글입니까?', 1], ['나는 지금 텍스
트 증강 패키지 작성중입니다.', '해당 댓글은 혐오 댓글입니까?', 0]]<br> 
<br>

  *입력 문장과 증강 후 문장이 동일할 경우 반환값이 없습니다.*
