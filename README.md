# koTextAug
Korean text Augmentation PyPI package for NLP

# Installation
- S/W 다운로드 기반 설치 및 사용
해당 디렉토리 zip 다운로드 해 압축 해제 후 koTextAug 디렉토리 내에서 모듈 import 하여 사용
- pip 기반 설치 및 사용
'''
pip install koTextAug
'''
위 명령어로 koTextAug 패키지 설치 후 사용

# Usage
- expample <br>
'''
from KoTextAug import Augmentation
<br>
aug = Augmentation(mode='whole', tokenizer='okt')<br>
comment = "나는 지금 텍스트 증강 패키지 작성 중입니다."
<br>
\# Easy Data Augmention 기법<br>
aug.randomSwap(comment, n=2)<br>
aug.randomDeletion(comment, p=0.2)<br>
aug.randomInsertion(comment, n=2)<br>
aug.synonymReplacement(comment, n=2)<br>
<br>
\# 역번역<br>
aug.backTranslation(comment, lang='en')<br>
<br>
\# 질문 형태의 증강 기법<br>
aug.question(comment, sent=['일반','혐오'], domain='댓글')
'''
