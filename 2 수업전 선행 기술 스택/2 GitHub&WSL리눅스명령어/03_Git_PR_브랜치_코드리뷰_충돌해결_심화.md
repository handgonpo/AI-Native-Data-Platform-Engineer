
> 대상: Git add / commit / push를 한 번 이상 해본 주니어  
> 목적: 팀 프로젝트처럼 main, dev, feature 브랜치를 나누고 Pull Request로 협업하는 흐름을 익힌다.

---

## 1. 이 문서를 배우는 이유

혼자 작업할 때는 `main` 브랜치에 바로 commit하고 push해도 큰 문제가 없을 수 있다.  
하지만 팀 프로젝트에서는 그렇게 하면 위험하다.
```text
main에서 바로 작업
→ 코드가 깨짐
→ 팀 전체가 같은 문제를 겪음
→ 누가 무엇을 바꿨는지 추적하기 어려움
```

그래서 팀 프로젝트에서는 보통 브랜치를 나누고 Pull Request로 병합한다.

---

## 2. 수업 표준 브랜치 전략

```text
main
dev
feature/*
```

| 브랜치 | 역할 |
|---|---|
| `main` | 발표 / 배포 / 최종 결과물 |
| `dev` | 여러 기능을 합치는 통합 개발 브랜치 |
| `feature/*` | 개인 또는 기능 단위 작업 브랜치 |

한 줄로 기억한다.

```text
main = 완성본
dev = 합치는 곳
feature/* = 내 작업실
```

---

## 3. 기본 협업 흐름
```text
main
 ↓
dev 생성
 ↓
feature 브랜치 생성
 ↓
개인 작업
 ↓
commit
 ↓
push
 ↓
Pull Request 생성
 ↓
코드리뷰
 ↓
feature → dev 병합
 ↓
dev 최신화
 ↓
dev → main 릴리즈 PR
```

---

## 4. dev 브랜치 만들기

dev는 팀의 공용 기준선이다.  
원칙적으로 팀에서 한 명, 보통 PM 또는 리더가 만든다.
```bash
git checkout main
git pull origin main
git checkout -b dev
git push -u origin dev
```

확인:
```bash
git branch
```

예상:
```text
* dev
  main
```

---

## 5. feature 브랜치 만들기

feature 브랜치는 반드시 dev에서 만든다.
```bash
git checkout dev
git pull origin dev
git checkout -b feature/youjung-login
```

브랜치 이름 예시:
```text
feature/youjung-login
feature/minsu-dashboard
feature/jihye-ingest-api
feature/team2-data-contract
```

좋은 브랜치 이름은 누가 어떤 작업을 하는지 알 수 있어야 한다.

---

## 6. feature에서 작업 후 commit / push

예시 파일 생성:
```bash
mkdir -p backend
echo "def login(username, password):" > backend/login.py
echo "    return 'login ok'" >> backend/login.py
```

상태 확인:
```bash
git status
```

커밋:
```bash
git add backend/login.py
git commit -m "Add dummy login function"
```

원격에 feature 브랜치 push:
```bash
git push -u origin feature/youjung-login
```

---

## 7. Pull Request 만들기

GitHub에서 다음 순서로 진행한다.
```text
Pull requests
→ New pull request
→ base: dev
→ compare: feature/youjung-login
→ Create pull request
```

중요:
```text
feature → dev
```

실수하면 안 되는 것:
```text
feature → main  ❌
```

초보자가 가장 많이 하는 실수는 PR의 base 브랜치를 main으로 두는 것이다.

---

## 8. PR 설명 작성법

PR은 “내가 무엇을 바꿨는지 리뷰어가 이해하도록 설명하는 문서”이다.

간단한 템플릿:
```markdown
### 변경 내용
- 로그인 더미 함수 추가
- README 실행 방법 보완

### 테스트 방법
- 로컬에서 파일 생성 확인
- Python 문법 오류 없음 확인

### 영향 범위 / TODO
- 실제 인증 로직은 아직 없음
- 다음 단계에서 JWT 또는 세션 인증 연결 예정
```

나쁜 PR 설명:
```text
수정함
확인 부탁
```

좋은 PR 설명:
```text
무엇을 바꿨는지, 어떻게 확인했는지, 남은 일이 무엇인지 적혀 있음
```

---

## 9. 코드리뷰 기본

코드리뷰는 혼내는 시간이 아니다.  
코드를 팀 기준에 맞추고, 실수를 줄이고, 서로 이해하는 과정이다.

리뷰 코멘트 예시:
```text
변수명이 조금 더 구체적이면 좋겠습니다.
README에 실행 명령어도 추가하면 좋겠습니다.
이 함수가 실패할 경우를 TODO로 남기면 좋겠습니다.
이 파일은 feature 브랜치에서만 수정하는 것이 좋겠습니다.
```

수업에서는 자기 PR에 직접 코멘트를 남겨보는 방식으로 연습해도 된다.

---

## 10. 병합 방식

GitHub PR에서 자주 보는 병합 방식은 다음과 같다.

| 방식 | 의미 | 수업 추천 |
|---|---|---|
| Merge commit | 커밋 이력을 그대로 합침 | 팀 정책에 따라 사용 |
| Squash and merge | 여러 커밋을 하나로 합쳐 병합 | 초보자 수업 추천 |
| Rebase and merge | 이력을 재정렬하여 병합 | 심화 과정에서 사용 |

수업에서는 보통 `Squash and merge`를 추천한다.

이유:
```text
feature 브랜치에서 커밋을 여러 번 해도
dev에는 기능 단위 커밋 1개로 깔끔하게 남길 수 있다.
```

---

## 11. 병합 후 로컬 dev 최신화

GitHub에서 PR을 병합해도 내 컴퓨터의 dev가 자동으로 바뀌지는 않는다.  
따라서 병합 후 반드시 로컬 dev를 최신화해야 한다.
```bash
git checkout dev
git pull origin dev
```

상태 확인:
```bash
git status
```

정상 예시:
```text
On branch dev
Your branch is up to date with 'origin/dev'.

nothing to commit, working tree clean
```

이 상태에서 다음 feature 브랜치를 만들어야 안전하다.

---

## 12. dev → main 릴리즈 PR

기능들이 dev에 모이면 최종 발표 또는 배포 전에 dev를 main으로 병합한다.
```text
base: main
compare: dev
```

PR 제목 예시:
```text
Release: merge dev into main
```

PR 설명 예시:
```markdown
### 포함된 변경 사항
- 로그인 더미 함수 추가
- README 실행 방법 보완
- Git 브랜치 전략 문서 추가

### 테스트
- dev 브랜치 기준으로 파일 존재 확인
- README 렌더링 확인
```

병합 후 로컬 main 최신화:
```bash
git checkout main
git pull origin main
```

---

## 13. pull과 fetch의 차이

| 명령어 | 의미 | 내 파일 변경 여부 |
|---|---|---|
| `git fetch` | 원격 변경 이력을 가져오기만 함 | 바로 바뀌지 않음 |
| `git pull` | 원격 변경을 가져와 현재 브랜치에 반영 | 바뀜 |

원격과 로컬 차이 확인:
```bash
git fetch
git log --oneline --decorate --all --graph --max-count=10
```

차이 보기:
```bash
git diff main..origin/main
```

주니어 기준:
```text
그냥 최신으로 맞추고 싶다 → git pull
원격 변경을 먼저 보고 싶다 → git fetch
```

---

## 14. 충돌(conflict)이란?

충돌은 Git이 자동으로 합칠 수 없는 상태이다.

주로 다음 상황에서 발생한다.
```text
같은 파일의 같은 줄을
로컬과 원격에서 서로 다르게 수정했을 때
```

충돌은 실패가 아니다.  
Git이 “둘 중 무엇을 최종 버전으로 할지 사람이 결정해달라”고 요청하는 상황이다.

---

## 15. 충돌 만들기 실습

### 15.1 원격에서 README 수정

GitHub 웹에서 `README.md`의 같은 줄을 수정하고 commit한다.

예시:
```markdown
이 줄은 원격에서 수정했습니다.
```

---

### 15.2 로컬에서 같은 줄 수정

로컬에서 같은 줄을 다르게 수정한다.
```bash
code README.md
```

예시:
```markdown
이 줄은 로컬에서 수정했습니다.
```

커밋:
```bash
git add README.md
git commit -m "Update README locally"
```

---

### 15.3 pull 실행

```bash
git pull
```

예상 메시지:
```text
CONFLICT (content): Merge conflict in README.md
Automatic merge failed; fix conflicts and then commit the result.
```

---

## 16. 충돌 표시 읽기

충돌이 난 파일을 열면 다음과 같은 표시가 보인다.
```text
<<<<<<< HEAD
이 줄은 로컬에서 수정했습니다.
=======
이 줄은 원격에서 수정했습니다.
>>>>>>> origin/main
```

의미:

| 표시 | 의미 |
|---|---|
| `<<<<<<< HEAD` 아래 | 내 로컬 버전 |
| `=======` 아래 | 원격에서 가져온 버전 |
| `>>>>>>> origin/main` | 원격 브랜치 표시 |

---

## 17. 충돌 해결 방법

세 가지 중 하나를 선택한다.

### 선택 A. 로컬 버전만 남기기
```markdown
이 줄은 로컬에서 수정했습니다.
```

### 선택 B. 원격 버전만 남기기
```markdown
이 줄은 원격에서 수정했습니다.
```

### 선택 C. 둘을 합쳐 새 문장으로 정리하기
```markdown
이 줄은 로컬과 원격 수정을 합쳐 최종 버전으로 정리했습니다.
```

중요한 규칙:

```text
<<<<<<< HEAD
=======
>>>>>>> origin/main
```

이 표시는 최종 파일에 남으면 안 된다. 반드시 삭제한다.

---

## 18. 충돌 해결 후 commit / push

```bash
git add README.md
git commit -m "Resolve README merge conflict"
git push
```

GitHub에서 최종 README가 정상인지 확인한다.

---

## 19. 팀 협업 전 체크리스트

```text
브랜치 이동 전 git status 확인
작업 전 dev 최신화
feature 브랜치는 dev에서 생성
main에 직접 push하지 않기
feature → dev PR 생성
PR 설명 작성
리뷰 코멘트 확인
Squash and merge로 병합
병합 후 로컬 dev 최신화
릴리즈 시 dev → main PR 생성
충돌 발생 시 표시를 읽고 최종 버전 결정
```

---

## 20. 한 문장 정리

```text
팀 프로젝트에서 Git은 코드를 저장하는 도구를 넘어,
브랜치 전략, PR, 리뷰, 충돌 해결을 통해 협업 흐름을 관리하는 도구이다.
```
