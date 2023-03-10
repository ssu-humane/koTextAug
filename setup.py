from setuptools import setup, find_packages

setup(name='koTextAug', # 패키지 명

version='1.0.0.4',

description='Korean Text data Augmentation package',

author='Humane Lab',

author_email='parkchaewon8566@gmail.com',

url='https://ssu-humane.github.io/',

license='MIT', # MIT에서 정한 표준 라이센스 따른다

py_modules=['textAugmentation','tokenizer','utils'], # 패키지에 포함되는 모듈

python_requires='>=3',

install_requires=[], # 패키지 사용을 위해 필요한 추가 설치 패키지

packages=['koTextAug'] # 패키지가 들어있는 폴더들

)