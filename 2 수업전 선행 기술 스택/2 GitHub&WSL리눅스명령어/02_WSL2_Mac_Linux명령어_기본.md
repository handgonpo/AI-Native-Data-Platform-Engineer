
> 대상: Windows WSL2 사용자와 Mac 터미널 사용자  
> 목적: 수업 실습을 시작하기 전에 터미널 기본 명령어, VSCode 실행, Python 첫 실행, 가상환경, pip/uv 패키지 관리 흐름을 이해한다.  
> 사용 위치: `0 커리큘럼/2 수업전 선행 기술 스택/2 GitHub&WSL리눅스명령어/`

---

AI 네이티브 데이터 플랫폼 수업에서는 터미널을 자주 사용한다.
```text
프로젝트 폴더 이동
파일과 폴더 생성
VSCode로 프로젝트 열기
Python 파일 만들기
Python 코드 실행
가상환경 생성
패키지 설치
requirements.txt 설치
uv 기반 패키지 관리
Git 명령어 실행
서버 실행
로그 확인
```

처음에는 터미널이 낯설 수 있지만, 자주 쓰는 명령어는 많지 않다.  
이 문서는 수업 시작 전 꼭 필요한 명령어와 첫 실행 테스트, pip에서 uv로 넘어가는 기본 흐름을 한 곳에 정리한다.

---

# PART A. WSL2 / Mac 기본 이해

---

## 3. WSL2 사용자와 Mac 사용자의 차이

| 구분 | WSL2 사용자 | Mac 사용자 |
|---|---|---|
| 기본 터미널 | Ubuntu on Windows / Windows Terminal | Terminal / iTerm2 |
| 홈 경로 예시 | `/home/youjung` | `/Users/youjung` |
| 현재 폴더 열기 | `explorer.exe .` | `open .` |
| VSCode 열기 | `code .`, `code -r .` | `code .`, `code -r .` |
| 패키지 설치 | `sudo apt install 패키지명` | `brew install 패키지명` |
| Python 명령어 | `python3`, `pip3` 또는 가상환경 후 `python` | `python3`, `pip3` 또는 가상환경 후 `python` |
| 권장 프로젝트 위치 | `/home/사용자명/projects` | `/Users/사용자명/projects` |

수업에서는 가능한 한 WSL2와 Mac에서 모두 동작하는 명령어를 사용한다.

---

## 4. WSL2 사용자가 주의할 점

### 4.1 프로젝트는 WSL 홈 안에 두는 것이 좋다

권장 위치:
```bash
/home/youjung/projects
```

비권장 위치:
```bash
/mnt/c/Users/...
```

`/mnt/c`는 Windows 파일 시스템이다.  
여기에 프로젝트를 두면 속도, 권한, 파일 감시 문제로 개발 중 불편이 생길 수 있다.

---

### 4.2 Windows 경로와 Linux 경로를 혼동하지 않기

Windows 경로:
```text
C:\Users\youjung\Documents
```

WSL 경로:
```text
/home/youjung/projects
```

Windows C드라이브를 WSL에서 보면 다음처럼 보인다.
```text
/mnt/c/Users/youjung
```

---

## 5. Mac 사용자가 주의할 점

Mac은 기본적으로 Unix 계열이라 Linux 명령어 대부분이 동작한다.  
다만 패키지 설치는 `apt`가 아니라 `brew`를 많이 사용한다.

Homebrew 설치 여부 확인:
```bash
brew --version
```

패키지 설치 예시:
```bash
brew install git
brew install tree
```

---

# PART B. 기본 Linux 명령어

---

## 6. 현재 위치 확인
```bash
pwd
```

예시:

WSL2:
```bash
/home/youjung
```

Mac:
```bash
/Users/youjung
```

`pwd`는 “내가 지금 어느 폴더에 있는지” 확인하는 명령어이다.

---

## 7. 파일 목록 보기

```bash
ls
```

상세 보기:
```bash
ls -l
```

숨김 파일 포함:
```bash
ls -a
```

상세 정보와 숨김 파일 함께 보기:
```bash
ls -la
```

---

## 8. 폴더 이동

홈 폴더로 이동:
```bash
cd ~
```

특정 폴더로 이동:
```bash
cd 폴더명
```

상위 폴더로 이동:
```bash
cd ..
```

예시:
```bash
cd ~
cd projects
cd ..
```

주의할 점:
```bash
cd ..
```

이 명령은 현재 폴더의 한 단계 위, 즉 부모 폴더로 이동한다.

예시:
```text
/home/youjung/project
→ cd ..
→ /home/youjung
```

---

## 9. 폴더 만들기

```bash
mkdir 폴더명
```

예시:
```bash
mkdir ai-platform-class
```

중간 폴더까지 한 번에 만들기:
```bash
mkdir -p data_lake/raw/gas_events
```

`-p`는 중간 폴더가 없어도 함께 만들어주는 옵션이다.  
이미 폴더가 있어도 오류 없이 넘어간다.

---

## 10. 파일 만들기

빈 파일 만들기:
```bash
touch README.md
```

`touch`는 새 파일을 만들거나, 기존 파일의 수정 시간을 갱신한다.

간단한 내용이 있는 파일 만들기:
```bash
echo "# My Project" > README.md
```

여러 줄 파일 만들기:
```bash
cat > README.md <<'EOF'
# My Project

이 문서는 프로젝트 설명서입니다.
EOF
```

---

## 11. 파일 내용 확인

전체 내용 출력:
```bash
cat README.md
```

긴 파일을 페이지 단위로 보기:
```bash
less README.md
```

처음 몇 줄 보기:
```bash
head README.md
```

마지막 몇 줄 보기:
```bash
tail README.md
```

로그 파일을 실시간으로 보기:
```bash
tail -f app.log
```

---

## 12. 파일과 폴더 복사

파일 복사:
```bash
cp 원본파일 대상파일
```

예시:
```bash
cp README.md README_backup.md
```

폴더 복사:
```bash
cp -r 원본폴더 대상폴더
```

---

## 13. 파일과 폴더 이동 / 이름 변경

```bash
mv 원본 대상
```

이름 변경:
```bash
mv old_name.md new_name.md
```

폴더 이동:
```bash
mv README.md docs/README.md
```

---

## 14. 파일과 폴더 삭제

파일 삭제:
```bash
rm 파일명
```

폴더 삭제:
```bash
rm -r 폴더명
```

강제 삭제:
```bash
rm -rf 폴더명
```

주의:
```text
rm -rf는 매우 위험하다.
삭제한 파일은 휴지통으로 가지 않고 바로 사라질 수 있다.
수업 중에는 경로를 반드시 확인하고 사용한다.
```

삭제 전 현재 위치와 파일 목록을 확인한다.
```bash
pwd
ls
```

---

## 15. 폴더 구조 보기

`tree`가 설치되어 있다면 다음 명령어를 사용할 수 있다.
```bash
tree
```

2단계까지만 보기:
```bash
tree -L 2
```

WSL2에서 tree 설치:
```bash
sudo apt update
sudo apt install tree -y
```

Mac에서 tree 설치:
```bash
brew install tree
```

---

## 16. 텍스트 검색

파일 안에서 특정 단어 찾기:
```bash
grep "검색어" 파일명
```

예시:
```bash
grep "error" app.log
```

폴더 전체에서 검색:
```bash
grep -R "FastAPI" .
```

---

## 17. 파일 찾기

현재 폴더 아래에서 파일 찾기:
```bash
find . -name "README.md"
```

확장자로 찾기:
```bash
find . -name "*.md"
```

Python 파일 찾기:
```bash
find . -name "*.py"
```

---

# PART C. VSCode로 프로젝트 열기

---

## 18. VSCode로 현재 폴더 열기

현재 폴더를 VSCode로 열기:
```bash
code .
```

이미 열려 있는 VSCode 창을 재사용해서 현재 폴더 열기:
```bash
code -r .
```

정리하면 다음과 같다.
```text
code .      = 현재 폴더를 VSCode로 연다. 새 창으로 열릴 수 있다.
code -r .   = 이미 열려 있는 VSCode 창을 재사용해서 현재 폴더를 연다.
```

파일 하나만 열 수도 있다.
```bash
code README.md
```

특정 폴더를 열 수도 있다.
```bash
code docs
```

WSL2 사용자는 VSCode의 WSL 확장이 필요하다.  
Mac 사용자는 VSCode의 Shell Command 설정이 되어 있어야 `code .` 또는 `code -r .` 명령어를 사용할 수 있다.

---

## 19. code 명령어가 안 될 때

### WSL2 사용자

오류 예시:
```text
code: command not found
```

확인할 것:
```text
VSCode 설치 여부
VSCode WSL 확장 설치 여부
Ubuntu 터미널에서 실행했는지 여부
```

VSCode 확장 메뉴에서 다음 확장을 설치한다.
```text
WSL
Python
Pylance
GitLens
```

---

### Mac 사용자

Mac에서 `code` 명령어가 안 되면 다음을 설정한다.
```text
VSCode 실행
→ Command Palette 열기
→ Cmd + Shift + P
→ Shell Command: Install 'code' command in PATH
```

그 다음 터미널을 새로 열고 다시 실행한다.
```bash
code .
```

---

## 20. 현재 폴더를 파일 탐색기로 열기

WSL2:
```bash
explorer.exe .
```

Mac:
```bash
open .
```

---

# PART D. 첫 Python 실행 테스트

---

## 21. 왜 첫 실행 테스트가 필요한가?

수업을 시작하기 전에 반드시 확인해야 할 것이 있다.
```text
터미널이 정상적으로 실행되는가?
프로젝트 폴더를 만들 수 있는가?
VSCode로 폴더를 열 수 있는가?
Python 파일을 만들 수 있는가?
Python 코드를 실행할 수 있는가?
```

이 과정을 확인하지 않으면 이후 Django, FastAPI, Airflow, RAG 실습에서 계속 문제가 생길 수 있다.

---

## 22. WSL2 버전: 첫 실행 테스트

### 22.1 폴더 만들기

Ubuntu 또는 WSL 터미널을 열고 실행한다.
```bash
cd ~
mkdir -p ~/day1_console
cd ~/day1_console
```

현재 위치 확인:
```bash
pwd
```

예시:
```bash
/home/youjung/day1_console
```

---

### 22.2 VSCode로 폴더 열기

```bash
code .
```

또는 이미 열려 있는 VSCode 창을 재사용하려면 다음을 사용한다.
```bash
code -r .
```

---

### 22.3 hello.py 파일 만들기

방법 1. VSCode 좌측 탐색기에서 새 파일 만들기
```text
New File
→ hello.py
```

방법 2. 터미널에서 만들기
```bash
touch hello.py
```

---

### 22.4 VSCode 터미널 열기

VSCode 상단 메뉴에서 다음을 선택한다.
```text
Terminal
→ New Terminal
```

터미널 프롬프트가 이런 형태면 WSL 터미널이다.
```bash
username@컴퓨터이름:~/day1_console$
```

---

### 22.5 Python 버전 확인

```bash
python3 --version
```

예시:
```bash
Python 3.12.3
```

WSL에서는 보통 `python` 대신 `python3`를 사용해도 된다.  
가상환경을 활성화한 뒤에는 `python` 명령어를 사용해도 된다.

---

### 22.6 첫 Python 코드 작성

`hello.py` 파일에 다음 코드를 작성한다.
```python
print("안녕하세요! 파이썬 첫날입니다.")
print("오늘 목표는 입력-처리-출력 흐름 익히기!")
```

---

### 22.7 Python 코드 실행

터미널에서 실행한다.
```bash
python3 hello.py
```

또는 환경에 따라 다음도 가능하다.
```bash
python hello.py
```

출력 예시:
```text
안녕하세요! 파이썬 첫날입니다.
오늘 목표는 입력-처리-출력 흐름 익히기!
```

---

## 23. Mac 버전: 첫 실행 테스트

### 23.1 폴더 만들기

Mac 터미널을 열고 실행한다.
```bash
mkdir -p ~/day1_console
cd ~/day1_console
```

현재 위치 확인:
```bash
pwd
```

예시:
```bash
/Users/yourname/day1_console
```

---

### 23.2 VSCode로 폴더 열기
```bash
code .
```

또는 현재 VSCode 창을 재사용하려면 다음을 실행한다.
```bash
code -r .
```

`code: command not found`가 나오면 VSCode에서 Shell Command 설정을 먼저 한다.
```text
Command Palette
→ Shell Command: Install 'code' command in PATH
```

---

### 23.3 hello.py 파일 만들기

```bash
touch hello.py
```

또는 VSCode 좌측 탐색기에서 직접 `hello.py` 파일을 만든다.

---

### 23.4 Python 버전 확인

```bash
python3 --version
```

예시:
```bash
Python 3.12.3
```

---

### 23.5 첫 Python 코드 작성

`hello.py` 파일에 다음 코드를 작성한다.
```python
print("안녕하세요! 파이썬 첫날입니다.")
print("오늘 목표는 입력-처리-출력 흐름 익히기!")
```

---

### 23.6 Python 코드 실행
```bash
python3 hello.py
```

또는 환경에 따라 다음도 가능하다.
```bash
python hello.py
```

출력 예시:
```text
안녕하세요! 파이썬 첫날입니다.
오늘 목표는 입력-처리-출력 흐름 익히기!
```

---

## 24. 첫 실행 테스트 체크리스트

```text
day1_console 폴더를 만들었다.
pwd로 현재 위치를 확인했다.
code . 또는 code -r . 으로 VSCode를 열었다.
hello.py 파일을 만들었다.
python3 --version을 확인했다.
hello.py에 print 코드를 작성했다.
python3 hello.py로 실행했다.
터미널에 출력 결과가 보였다.
```

---

# PART E. Python 가상환경과 pip 기본

---

## 25. Python 가상환경이란?

Python 가상환경은 프로젝트별로 패키지를 분리하는 공간이다.

예를 들어 A 프로젝트는 Django 5.1을 쓰고, B 프로젝트는 Django 4.2를 쓸 수 있다.  
이때 가상환경을 사용하지 않으면 패키지 버전이 서로 충돌할 수 있다.

```text
Python 가상환경 = 프로젝트별 Python 패키지 격리 공간
```

---

## 26. venv, Docker, Kubernetes 차이

| 구분 | 한 줄 설명 | 해결하는 문제 | 수업에서의 사용 시점 |
|---|---|---|---|
| Python 가상환경 venv | Python 패키지를 프로젝트별로 분리 | Django, FastAPI, pandas 같은 패키지 버전 충돌 방지 | 가장 먼저 실습 |
| Docker | 애플리케이션과 실행환경을 컨테이너로 포장 | 내 컴퓨터와 다른 사람 컴퓨터의 실행환경 차이 해결 | DB/Redis부터 사용 후 앱까지 확장 |
| Docker Compose | 여러 컨테이너를 한 번에 실행 | Django, FastAPI, PostgreSQL, Redis를 한 번에 실행 | 중반부터 본격 사용 |
| Kubernetes | 여러 컨테이너를 운영환경에서 배포·관리 | 장애 복구, 확장, 무중단 배포, 운영 자동화 | 후반부 맛보기/운영형 실습 |

---

## 27. venv 가상환경 만들기

프로젝트 폴더 안에서 실행한다.
```bash
python3 -m venv .venv
```

가상환경 활성화:
```bash
source .venv/bin/activate
```

활성화되면 터미널 앞에 보통 다음처럼 표시된다.
```bash
(.venv) user@computer:~/project$
```

비활성화:
```bash
deactivate
```

---

## 28. pip 패키지 설치

가상환경을 활성화한 뒤 실행한다.
```bash
pip install 패키지명
```

예시:
```bash
pip install fastapi uvicorn
```

설치된 패키지 확인:
```bash
pip list
```

설치 목록 저장:
```bash
pip freeze > requirements.txt
```

requirements.txt 기반 설치:
```bash
pip install -r requirements.txt
```

---

# PART F. uv 패키지 관리 기본

---

## 29. uv란 무엇인가?

uv는 Python 패키지 설치, 의존성 관리, 가상환경 관리까지 도와주는 빠른 패키지 관리자이다.

쉽게 말하면 다음 도구들의 역할 일부를 하나로 묶은 도구라고 볼 수 있다.
```text
pip
venv
virtualenv
pip-tools
poetry 일부 기능
```

한 문장으로 정리하면 다음과 같다.
```text
uv = Python 프로젝트의 가상환경과 패키지 설치를 빠르고 재현 가능하게 관리하는 도구
```

---

## 30. pip와 uv 비교

| 항목 | pip | uv |
|---|---|---|
| 기본 목적 | 패키지 설치 | 패키지 설치 + 버전 고정 + 가상환경 관리 |
| 속도 | 보통 | 매우 빠름 |
| 가상환경 관리 | 별도 venv 필요 | `uv venv` 제공 |
| 의존성 충돌 확인 | 제한적 | 더 강함 |
| 고정 파일 | `requirements.txt` 중심 | `uv.lock` 사용 가능 |
| 재현성 | 낮거나 보통 | 높음 |
| 팀 협업 | 설정을 잘 맞춰야 함 | lock 파일로 재현성 높임 |

---

## 31. pip 방식 예시

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install django==5.1
pip install djangorestframework==3.15
pip freeze > requirements.txt
```

---

## 32. uv 방식 예시

```bash
uv venv .venv
source .venv/bin/activate
uv add django djangorestframework
```

또는 기존 `requirements.txt`가 있다면 다음처럼 설치할 수 있다.
```bash
uv pip install -r requirements.txt
```

---

## 33. uv 설치

uv가 설치되어 있는지 확인한다.
```bash
uv --version
```

없다면 설치한다.

### 방법 1. 공식 설치 스크립트

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

설치 후 터미널을 다시 열거나 안내된 PATH 설정을 반영한다.

### 방법 2. pip로 설치

```bash
pip install uv
```

수업 환경에서는 강사가 정한 방식으로 통일하는 것이 좋다.

---

## 34. uv 기본 명령어

| 명령어 | 의미 |
|---|---|
| `uv --version` | uv 설치 확인 |
| `uv venv .venv` | `.venv` 가상환경 생성 |
| `source .venv/bin/activate` | 가상환경 활성화 |
| `uv add 패키지명` | 패키지 추가 |
| `uv remove 패키지명` | 패키지 제거 |
| `uv pip install 패키지명` | pip 호환 방식으로 패키지 설치 |
| `uv pip install -r requirements.txt` | requirements.txt 기반 설치 |
| `uv pip list` | 설치된 패키지 확인 |
| `uv run 파일명.py` | uv 환경에서 Python 파일 실행 |

---

## 35. uv로 새 프로젝트를 시작하는 기본 흐름

```bash
# 1. 프로젝트 폴더 생성
mkdir -p ~/uv-practice
cd ~/uv-practice

# 2. 가상환경 생성
uv venv .venv

# 3. 가상환경 활성화
source .venv/bin/activate

# 4. 패키지 설치
uv add fastapi uvicorn python-dotenv

# 5. 설치 확인
uv pip list
```

---

## 36. uv run으로 Python 파일 실행

예제 파일 만들기:
```bash
echo 'print("Hello uv")' > hello_uv.py
```

실행:
```bash
uv run hello_uv.py
```

출력:
```text
Hello uv
```

`uv run`은 uv가 관리하는 환경에서 명령을 실행하는 방식이다.

---

# PART G. pip → uv 방식 전환 가이드

---

## 37. 언제 uv로 전환하면 좋은가?

| 상황 | 추천 |
|---|---|
| 개인 학습용 아주 작은 프로젝트 | pip 유지 가능 |
| 팀 협업 프로젝트 | uv 추천 |
| Docker 기반 배포 | uv 추천 |
| 패키지 설치가 잦은 프로젝트 | uv 추천 |
| 실행 환경을 똑같이 맞춰야 하는 프로젝트 | uv 추천 |

---

## 38. pip 방식 프로젝트 예시

기존 프로젝트 구조가 다음과 같다고 가정한다.
```text
myproject/
├── venv/
├── requirements.txt
└── manage.py
```

또는 다음처럼 되어 있을 수 있다.
```text
myproject/
├── .venv/
├── requirements.txt
└── main.py
```

---

## 39. 전환 전 주의사항

한 프로젝트 안에서는 패키지 관리 방식을 섞지 않는 것이 좋다.

비권장:
```bash
pip install django
uv add djangorestframework
pip uninstall django
```

권장:
```bash
uv add django
uv add djangorestframework
uv remove django
```

한 문장으로 정리하면 다음과 같다.
```text
이 프로젝트는 uv로 관리한다고 정했으면 설치와 삭제는 되도록 uv 명령어로 통일한다.
```

---

## 40. pip → uv 전환 순서

### 40.1 기존 가상환경 비활성화

가상환경이 켜져 있다면 먼저 끈다.
```bash
deactivate
```

---

### 40.2 기존 가상환경 삭제

기존 가상환경 이름이 `venv`라면:
```bash
rm -rf venv
```

기존 가상환경 이름이 `.venv`라면:
```bash
rm -rf .venv
```

주의:
```text
rm -rf는 위험한 명령어이다.
반드시 프로젝트 폴더 안에서 실행하고, 삭제할 폴더명을 확인한다.
```

---

### 40.3 uv 설치 확인

```bash
uv --version
```

없다면 설치한다.
```bash
pip install uv
```

또는 공식 설치 방식을 사용한다.
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

---

### 40.4 uv 기반 새 가상환경 생성

```bash
uv venv .venv
```

---

### 40.5 가상환경 활성화

WSL2 / Mac:
```bash
source .venv/bin/activate
```

Windows PowerShell 참고:
```powershell
.\.venv\Scripts\Activate.ps1
```

---

### 40.6 기존 패키지 다시 설치

`requirements.txt`가 있다면:
```bash
uv pip install -r requirements.txt
```

설치 확인:
```bash
uv pip list
```

---

## 41. requirements.txt와 uv.lock 차이

| 구분 | requirements.txt | uv.lock |
|---|---|---|
| 역할 | 설치할 패키지 목록 | 정확히 재현 가능한 의존성 스냅샷 |
| 생성 방식 | `pip freeze > requirements.txt` | uv가 계산하여 생성 |
| 특징 | 상위/하위 패키지가 섞일 수 있음 | 버전과 하위 의존성까지 고정 |
| 수업 초반 | 사용 가능 | 필수는 아님 |
| 팀/배포 단계 | 부족할 수 있음 | 권장 |

초반에는 `requirements.txt`만 사용해도 된다.  
하지만 팀 협업, Docker, CI/CD까지 가면 `uv.lock`을 함께 관리하는 것이 좋다.

---

## 42. VSCode에서 uv 가상환경 선택

uv로 가상환경을 만들어도 VSCode 입장에서는 일반 Python 가상환경이다.

설정 순서:
```text
Ctrl + Shift + P
→ Python: Select Interpreter
→ .venv/bin/python 선택
```

Mac도 동일하게 `.venv/bin/python`을 선택하면 된다.

Windows PowerShell 환경에서는 다음 경로일 수 있다.
```text
.venv\Scripts\python.exe
```

---

## 43. uv 사용 시 자주 하는 실수

### 43.1 가상환경 활성화를 안 하고 설치함

문제:
```bash
uv add django
```

했는데 VSCode가 다른 Python을 보고 있을 수 있다.

확인:
```bash
which python
python --version
```

---

### 43.2 pip와 uv를 섞어서 사용함

문제:
```bash
pip install pandas
uv remove pandas
```

패키지 상태가 헷갈릴 수 있다.

권장:
```bash
uv add pandas
uv remove pandas
```

---

### 43.3 requirements.txt가 오래됨

문제:
```text
실제 설치된 패키지와 requirements.txt가 다름
```

해결:
```bash
pip freeze > requirements.txt
```

또는 uv 기반으로 정리한다.
```bash
uv pip list
```

---

## 44. 수업에서 권장하는 패키지 관리 기준

초반 수업:
```text
venv + pip 방식 이해
requirements.txt 이해
```

중반 이후:
```text
uv venv
uv add
uv pip install -r requirements.txt
uv.lock 개념 이해
```

팀 프로젝트:
```text
팀에서 pip 방식 또는 uv 방식 중 하나로 통일
섞어 쓰지 않기
README에 설치 방법 명확히 작성
```

---

## 45. README에 적을 설치 방법 예시

pip 방식
```markdown
## 설치 방법

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
```

### uv 방식

```markdown
## 설치 방법

```bash
uv venv .venv
source .venv/bin/activate
uv pip install -r requirements.txt
```
```

또는 uv 프로젝트 방식:

```markdown
## 설치 방법

```bash
uv venv .venv
source .venv/bin/activate
uv add fastapi uvicorn
```
```

---

# PART H. 서버 실행 예시

---

## 46. FastAPI 실행 예시

파일 구조 예시:

```text
project/
└── main.py
```

실행:
```bash
uvicorn main:app --reload
```

브라우저 확인:
```text
http://127.0.0.1:8000
```

Swagger UI:
```text
http://127.0.0.1:8000/docs
```

---

## 47. Django 실행 예시

```bash
python manage.py runserver
```

브라우저 확인:
```text
http://127.0.0.1:8000
```

---

# PART I. 최종 체크리스트

---

## 48. 수업 시작 전 최소 체크리스트

```text
터미널 실행 가능
pwd로 현재 위치 확인 가능
ls로 파일 목록 확인 가능
cd로 폴더 이동 가능
mkdir로 폴더 생성 가능
touch 또는 echo로 파일 생성 가능
cat으로 파일 내용 확인 가능
rm 삭제 명령어의 위험성 이해
code . 으로 VSCode 열기 가능
code -r . 으로 현재 VSCode 창 재사용 가능
python3 --version 확인 가능
hello.py 파일 생성 가능
python3 hello.py 실행 가능
python3 -m venv .venv 실행 가능
source .venv/bin/activate 실행 가능
pip install 실행 가능
requirements.txt 의미 이해
uv --version 확인 가능
uv venv .venv 실행 가능
uv pip install -r requirements.txt 실행 가능
pip 방식과 uv 방식 차이 이해
git --version 확인 가능
```

---

## 49. 이 문서에서 반드시 기억할 것

```text
1. pwd로 현재 위치를 확인한다.
2. cd로 폴더를 이동한다.
3. mkdir -p로 폴더를 만든다.
4. touch로 파일을 만든다.
5. code . 또는 code -r . 으로 VSCode를 연다.
6. python3 hello.py로 Python 파일을 실행한다.
7. 가상환경은 프로젝트별 패키지를 분리하기 위해 사용한다.
8. pip는 기본 패키지 설치 도구이다.
9. uv는 더 빠르고 재현성 높은 패키지 관리 도구이다.
10. 한 프로젝트에서는 pip 방식과 uv 방식을 섞지 않는 것이 좋다.
```

---

## 50. 한 문장 정리

```text
WSL2와 Mac 터미널 명령어는 프로젝트 폴더를 만들고, VSCode로 열고, Python을 실행하고, 가상환경과 패키지를 관리하기 위한 기본 작업 도구이다.
```
