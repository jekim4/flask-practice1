# Flask 실습 진행 노트

## 지금까지 한 것
- 파이썬 확인, `flask-practice1` 폴더 생성
- 가상환경 생성 및 활성화 (`venv`)
- `pip install flask` → Flask 3.1.3 설치 확인 완료
- `app.py` 생성 (기본 Hello World 서버)
- `flask run` 으로 서버 정상 기동 확인 (`http://127.0.0.1:5000`)

## 현재 app.py 내용
```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
```

## VS Code에서 이어서 할 일

1. **폴더 열기**: [파일] → [폴더 열기] → `flask-practice1` (폴더째로 열어야 venv가 자동 인식됨)
2. **터미널 열기**: `Ctrl + ` ` `
3. **가상환경 활성화**:
   ```powershell
   venv\Scripts\Activate.ps1
   ```
   프롬프트 앞에 `(venv)`가 붙는지 확인. 안 되면:
   ```powershell
   Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
   ```
   묻는 말에 `Y` 입력 후 재시도.
4. **서버 실행**:
   ```powershell
   flask run
   ```
   또는 디버그 모드(코드 저장 시 자동 재시작):
   ```powershell
   flask --debug run
   ```
5. **브라우저 확인**: `127.0.0.1:5000` → "Hello, World!" 뜨면 성공

## [실습 4] 라우팅 여러 개 만들기 — 완료

`app.py`에 `/about`, `/test/<text>` 라우트 추가 완료. 서버 실행해서 아래 주소 전부 정상 확인함:
- `127.0.0.1:5000/` → 메인 페이지
- `127.0.0.1:5000/about` → 소개 페이지
- `127.0.0.1:5000/test/안녕` → 안녕
- `127.0.0.1:5000/hello` → 404 Not Found (등록 안 한 주소)

## [실습 5] URL 타입 지정 — 완료
`/age/<num>` (타입 없음, str), `/age2/<int:num>` (int, 숫자 아니면 404) 추가하고 확인 완료.

## [실습 6] 템플릿 렌더링 — 완료
`templates/hi.html` 생성, `/hi/<name>` 라우트에서 `render_template()` 사용해 확인 완료.

## 다음 — 실제 과제 HW1 (강의자료 CE-WebSystem-L4.pdf 77~79쪽)
마감: 9월 23일(수) 23:59. `flask-practice1/HW1/` 폴더에 새로 작성 (기존 실습 코드는 그대로 둠).

만들 페이지 3개 (모두 templates 사용, 문자열 return 금지):
- `/` — 이름과 학번
- `/profile` — 취미 3가지 (파이썬 리스트 → `{% for %}`로 출력)
- `/greet/<name>` — "안녕하세요, OOO님"
- 세 페이지가 서로 링크로 연결되어 있을 것

폴더 구조:
```
flask-practice1/
├─ venv/            (저장소 안 올림)
├─ .gitignore
├─ requirements.txt  (맨 위에 하나만)
├─ app.py            (수업 실습, 그대로 둠)
├─ templates/
└─ HW1/
   ├─ app.py
   ├─ templates/
   └─ README.md      (실행 화면 캡처 3장)
```

제출: Git 저장소(public)를 GitHub에 올리고 주소 한 줄만 게시판 제출. 커밋 3개 이상(페이지 만들 때마다 커밋).

※ 아직 Git 저장소 초기화 전 상태 — HW1 작업 전에 `.gitignore`, `git init`, GitHub 업로드부터 필요.

---
막히는 부분 있으면 이 파일 열어둔 채로 Claude Code한테 "여기서부터 이어서 도와줘"라고 하면 됩니다.
