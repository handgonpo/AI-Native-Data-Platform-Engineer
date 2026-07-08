
> 대상: AI 네이티브 데이터 플랫폼 엔지니어 과정을 처음 시작하는 주니어  
> 목적: 로컬 프로젝트를 Git으로 관리하고 GitHub에 올릴 수 있도록 기본 흐름을 익힌다.

---

## 1. 이 문서를 배우는 이유

이 과정에서는 모든 실습 산출물을 GitHub에 저장한다.  
따라서 주니어는 최소한 다음 흐름을 이해해야 한다.

```text
파일 작성
→ git add
→ git commit
→ git push
→ GitHub에서 확인
```

Git을 잘해야 모든 개발을 잘하는 것은 아니다.  
하지만 Git을 모르면 수업 산출물을 저장하거나 제출하거나 되돌리기 어렵다.

---

## 2. Git과 GitHub의 차이

| 구분 | Git | GitHub |
|---|---|---|
| 역할 | 변경 이력을 관리하는 도구 | Git 저장소를 인터넷에 보관하는 서비스 |
| 위치 | 내 컴퓨터 | 인터넷 / 클라우드 |
| 핵심 | add, commit, branch | repository, push, pull, PR |
| 비유 | 내 컴퓨터의 변경 기록장 | 팀이 함께 보는 공유 저장소 |

한 문장으로 정리하면 다음과 같다.

```text
Git은 변경 이력을 기록하는 도구이고,
GitHub는 그 Git 저장소를 온라인에서 공유하는 공간이다.
```

---

## 3. Git 설치 확인

WSL 또는 Mac 터미널에서 다음 명령어를 입력한다.
```bash
git --version
```

정상 예시:
```bash
git version 2.43.0
```

Git이 없다면 WSL에서는 다음 명령어로 설치한다.
```bash
sudo apt update
sudo apt install git -y
```

Mac에서는 보통 Xcode Command Line Tools 또는 Homebrew를 통해 설치한다.

```bash
git --version
```

위 명령을 입력했을 때 설치 안내가 나오면 안내에 따라 설치하면 된다.

---

## 4. Git 최초 설정

Git은 커밋을 남길 때 작성자 정보를 함께 저장한다.  
처음 한 번은 이름과 이메일을 설정해야 한다.
```bash
git config --global user.name "홍길동"
git config --global user.email "youremail@example.com"
```

설정 확인:
```bash
git config --global --list
```

확인 결과 예시:
```bash
user.name=홍길동
user.email=youremail@example.com
```

가능하면 GitHub 계정에 등록된 이메일과 같은 이메일을 사용하는 것이 좋다.

---

## 5. 새 프로젝트를 Git으로 관리하기

### 5.1 프로젝트 폴더 만들기
```bash
cd ~
mkdir git-practice
cd git-practice
```

현재 위치 확인:
```bash
pwd
```

---

### 5.2 Git 저장소 초기화
```bash
git init
```

이 명령어를 실행하면 현재 폴더에 숨김 폴더인 `.git`이 생긴다.  
이제 이 폴더는 Git이 변경 이력을 관리하는 프로젝트가 된다.

숨김 파일까지 확인:
```bash
ls -a
```

---

### 5.3 첫 파일 만들기
```bash
echo "print('Hello Git')" > app.py
```

상태 확인:
```bash
git status
```

처음에는 `app.py`가 아직 Git에 등록되지 않은 파일로 보인다.

---

## 6. add → commit 흐름

Git은 파일을 바로 저장하지 않는다.  
먼저 이번 커밋에 포함할 파일을 고르고, 그 다음 저장한다.

```text
Working Directory
   ↓ git add
Staging Area
   ↓ git commit
Repository
```

| 단계 | 의미 | 명령어 |
|---|---|---|
| Working Directory | 내가 파일을 수정하는 공간 | VSCode에서 파일 수정 |
| Staging Area | 이번 커밋에 포함할 파일을 고르는 공간 | `git add 파일명` |
| Repository | 변경 이력이 저장되는 공간 | `git commit -m "메시지"` |

---

### 6.1 파일을 스테이징하기
```bash
git add app.py
```

또는 현재 폴더의 모든 변경 파일을 추가할 수 있다.
```bash
git add .
```

---

### 6.2 커밋하기
```bash
git commit -m "Add app.py"
```

커밋 메시지는 “무엇을 했는지” 짧고 구체적으로 작성한다.

좋은 예:
```text
Add README
Create initial project structure
Update data source map
Fix typo in README
```

나쁜 예:
```text
수정
작업
최종
진짜최종
```

---

## 7. GitHub 원격 저장소 만들기

GitHub에서 새 저장소를 만든다.
```text
GitHub 접속
→ New repository
→ 저장소 이름 입력
→ Public 또는 Private 선택
→ README, .gitignore 자동 생성은 체크하지 않기
→ Create repository
```

이미 로컬에 프로젝트가 있으므로 GitHub에서 README를 자동으로 만들지 않는 것이 안전하다.

---

## 8. 로컬 프로젝트와 GitHub 연결

GitHub 저장소 주소를 복사한 뒤 다음 명령어를 입력한다.
```bash
git remote add origin https://github.com/username/repository.git
```

연결 확인:
```bash
git remote -v
```

기본 브랜치 이름을 `main`으로 맞춘다.
```bash
git branch -M main
```

첫 push:
```bash
git push -u origin main
```

이후부터는 보통 다음 명령어만 사용해도 된다.
```bash
git push
```

---

## 9. README.md 작성

README는 프로젝트의 첫 설명서이다.  
GitHub 저장소에 들어가면 가장 먼저 보이는 파일이므로 반드시 작성한다.
```bash
echo "# Git Practice" > README.md
```

커밋하고 GitHub에 올린다.
```bash
git add README.md
git commit -m "Add README"
git push
```

---

## 10. .gitignore 작성

`.gitignore`는 Git에 올리지 않을 파일을 정하는 문서이다.  
가상환경, 캐시, 비밀키 파일은 GitHub에 올리면 안 된다.
```bash
cat > .gitignore <<'EOF'
# Python
__pycache__/
*.pyc

# Virtual Environment
.venv/
venv/

# Environment Variables
.env

# OS
.DS_Store
EOF
```

커밋:
```bash
git add .gitignore
git commit -m "Add gitignore"
git push
```

---

## 11. 자주 쓰는 Git 명령어

| 명령어 | 의미 |
|---|---|
| `git status` | 현재 변경 상태 확인 |
| `git add .` | 모든 변경 파일 스테이징 |
| `git commit -m "메시지"` | 변경 이력 저장 |
| `git log --oneline` | 커밋 기록 간단히 보기 |
| `git push` | GitHub에 올리기 |
| `git pull` | GitHub의 최신 내용을 가져와 반영 |
| `git clone URL` | GitHub 저장소를 내 컴퓨터로 복사 |
| `git branch` | 브랜치 목록 확인 |
| `git checkout 브랜치명` | 브랜치 이동 |
| `git checkout -b 브랜치명` | 브랜치 생성 후 이동 |

---

## 12. clone / pull / fetch 차이

| 명령어 | 언제 쓰는가 | 의미 |
|---|---|---|
| `git clone URL` | 처음 저장소를 받을 때 | 원격 저장소 전체 복사 |
| `git pull` | 최신 내용을 바로 반영할 때 | 원격 변경을 가져와 내 파일에 반영 |
| `git fetch` | 원격 변경을 먼저 확인하고 싶을 때 | 가져오기만 하고 내 파일은 아직 변경하지 않음 |

주니어는 보통 다음 기준으로 사용한다.
```text
처음 받을 때: git clone
최신으로 맞출 때: git pull
원격 변경을 미리 보고 싶을 때: git fetch
```

---

## 13. GitHub에서 파일 삭제하기

Git에서 파일을 삭제할 때는 다음 명령어를 사용한다.
```bash
git rm 파일명
git commit -m "Delete 파일명"
git push
```

폴더 삭제:
```bash
git rm -r 폴더명
git commit -m "Delete folder"
git push
```

주의:
```bash
rm 파일명
```

위 명령어는 파일만 삭제한다.  
Git 이력에 삭제를 반영하려면 결국 `git add` 또는 `git rm` 후 commit이 필요하다.

---

## 14. 수업 시작 전 최소 체크리스트
```text
Git 설치 확인 완료
Git user.name 설정 완료
Git user.email 설정 완료
GitHub 계정 준비 완료
로컬 프로젝트 생성 가능
git init 가능
git add / commit 가능
GitHub 저장소 생성 가능
git remote add origin 가능
git push 가능
README.md 작성 가능
.gitignore 작성 가능
```

---

## 15. 한 문장 정리
```text
Git은 내 컴퓨터에서 변경 이력을 남기는 도구이고,
GitHub는 그 이력을 온라인에 올려 수업 산출물과 협업 결과를 관리하는 공간이다.
```
