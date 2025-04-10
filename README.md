# Django 서비스 프로젝트

이 프로젝트는 Django를 사용하여 만든 세 가지 서비스를 포함하고 있습니다:

1. **투표 서비스 (Vote Service)**
   - 다양한 주제로 투표를 생성하고 참여할 수 있는 서비스
   - 투표 생성, 투표 참여, 결과 확인 기능

2. **로또 번호 생성기 (Lotto Service)**
   - 1부터 45까지의 숫자 중 6개와 보너스 번호 1개를 무작위로 생성
   - 실제 로또 6/45와 동일한 규칙 적용

3. **가위바위보 게임 (RSP Service)**
   - 컴퓨터와 가위바위보 게임을 즐길 수 있는 서비스
   - 승패 결과 확인 및 다시하기 기능

## 설치 및 실행 방법

1. 저장소 클론
```
git clone [저장소 URL]
cd [프로젝트 폴더]
```

2. 가상환경 생성 및 활성화
```
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. 필요한 패키지 설치
```
pip install -r requirements.txt
```

4. 데이터베이스 마이그레이션
```
python manage.py makemigrations
python manage.py migrate
```

5. 서버 실행
```
python manage.py runserver
```

6. 웹 브라우저에서 접속
```
http://127.0.0.1:8000/
```

## 기술 스택
- Python 3.x
- Django 3.2
- HTML/CSS
- JavaScript 