# Django_study
## M(Model) V(View) T(template)

## 환경 설정
1. 가상환경 설치
  - pip3 install virtualenv 
2. 가상 프로젝트 생성
  - 경로로 이동하여 > virtualenv [project_name]
3. 가상 환경 실행
  - Window : [project_name]/Scripts/activate
  - Mac : soruce [project_name]/Scripts/activate
4. Django 설치
  - pip3 install django
5. Django project 설치
  - django-admin startproject [project_name]
6. project > app 생성 (기능 단위 ex> member, board, payment..)
  - django-admin startapp [app_name]
7. template 생성 
  - app 폴더로 이동 후 templates 폴더 생성 (Template 인식 > app MTV 세팅)
8. Project에 등록
  - [Project_name] > [Project_name] 폴더로 이동 후 settings.py 파일의 installed_apps에 생성한 app 추가

- vscode sqlite3 실행 안되는 경우 sqlite3 다운로드 후 프로젝트에 복사하여 확인 .\sqlite3 db.sqlite3
  - https://www.sqlite.org/download.html