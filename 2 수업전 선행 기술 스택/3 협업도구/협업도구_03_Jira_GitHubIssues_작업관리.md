
> 역할: 프로젝트 작업 카드와 진행 상태 관리  
> 사용 시점: 팀 프로젝트 시작 이후  
> 핵심 목적: 큰 요구사항을 작은 작업으로 나누고 담당자와 진행 상태를 관리한다.

---

## 1. Jira와 GitHub Issues는 무엇인가?

Jira와 GitHub Issues는 프로젝트의 작업을 카드처럼 등록하고 관리하는 도구이다.

수업에서는 다음 흐름을 경험하는 것이 중요하다.
```text
프로젝트 요구사항 이해
→ 기능을 작은 작업으로 분해
→ Issue로 등록
→ 담당자 지정
→ To Do / In Progress / Review / Done 상태 이동
→ GitHub 작업과 연결
→ 진행 상황 공유
```

도구 사용법 자체보다 중요한 것은 **업무를 작업 단위로 쪼개는 능력**이다.

---

## 2. Jira와 GitHub Issues의 차이

| 구분 | Jira | GitHub Issues |
|---|---|---|
| 장점 | 프로젝트 관리 기능이 강함 | GitHub 코드 작업과 연결이 쉬움 |
| 난이도 | 조금 높음 | 비교적 쉬움 |
| 수업 추천 | 최종 프로젝트나 팀 프로젝트 | 초반 실습 또는 간단한 프로젝트 |
| 사용 단위 | Project, Board, Issue | Issue, Label, Milestone, Project |

처음에는 GitHub Issues로 시작하고, 팀 프로젝트가 본격화되면 Jira를 맛보기로 적용해도 좋다.

---

## 3. 가장 중요한 개념
```text
Issue = 하나의 작업 카드
```

예를 들어 다음은 모두 Issue가 될 수 있다.
```text
센서 데이터 수집 API 만들기
Raw JSONL 저장 기능 구현
위험도 계산 함수 작성
대시보드 알람 목록 화면 만들기
데이터 저장 오류 수정
README 실행 방법 보완
```

---

## 4. Issue Type 이해

| 유형 | 의미 | 프로젝트 예시 |
|---|---|---|
| Epic | 큰 기능 묶음 | 위험 알람 시스템 |
| Story | 사용자 관점 요구사항 | 관리자는 위험 알람을 확인할 수 있다 |
| Task | 실제 개발 작업 | 알람 API 구현 |
| Bug | 오류 수정 | 알람 시간이 잘못 표시됨 |
| Sub-task | 작업 안의 세부 작업 | 모델 필드 추가 |

한 줄로 정리하면 다음과 같다.
```text
Epic = 큰 기능
Story = 사용자 요구
Task = 개발 작업
Bug = 오류 수정
```

---

## 5. 산업안전 관제 플랫폼 예시

큰 요구사항:
```text
실시간으로 수집된 센서 데이터를 저장하고,
위험도를 계산한 뒤,
관리자 대시보드에서 알람을 확인할 수 있어야 한다.
```

이 요구사항을 다음처럼 나눌 수 있다.
```text
Epic: 실시간 위험 알람 시스템 구축

Story 1: 센서 데이터를 수집할 수 있다
- Task: FastAPI 수집 API 구현
- Task: Raw JSONL 저장 기능 구현
- Task: 데이터 유효성 검증 로직 작성

Story 2: 위험도를 계산할 수 있다
- Task: 위험도 기준 정의
- Task: Risk Score 계산 함수 구현
- Task: 위험 이벤트 Mart 테이블 생성

Story 3: 대시보드에서 알람을 확인할 수 있다
- Task: 알람 목록 API 구현
- Task: Django 화면 구현
- Task: 알람 상태 변경 기능 구현

Bug:
- event_time 컬럼이 잘못 변환되는 문제 수정
```

---

## 6. Kanban Board 기본

주니어에게는 Scrum보다 Kanban이 먼저 적합하다.

기본 상태는 다음 정도면 충분하다.
```text
To Do
→ In Progress
→ Review
→ Done
```

각 상태의 의미는 다음과 같다.

| 상태 | 의미 |
|---|---|
| To Do | 해야 할 작업 |
| In Progress | 진행 중인 작업 |
| Review | 검토 중인 작업 |
| Done | 완료된 작업 |

---

## 7. Issue 작성 템플릿
```markdown
# 제목
Raw JSONL 저장 기능 구현

## 설명
센서 API로 수집한 원본 데이터를 날짜별 JSONL 파일로 저장한다.

## 완료 기준
- data_lake/raw/ 경로에 저장된다.
- 한 줄에 하나의 JSON이 저장된다.
- event_id가 포함된다.

## 담당자
주니어 A

## 우선순위
High

## 관련 브랜치
feature/AIP-12-raw-jsonl-save
```

---

## 8. GitHub 작업과 Issue 연결

Issue 번호가 다음과 같다고 가정한다.
```text
AIP-12 Raw JSONL 저장 기능 구현
```

브랜치 이름:
```text
feature/AIP-12-raw-jsonl-save
```

커밋 메시지:
```text
AIP-12 Raw JSONL 저장 기능 구현
```

PR 제목:
```text
AIP-12 Raw JSONL 저장 기능 구현
```

이렇게 하면 작업 카드, 코드, PR이 서로 연결된다.

---

## 9. 수업에서 깊게 하지 않아도 되는 것

주니어 수업에서는 아래 내용은 맛보기만 해도 충분하다.
```text
복잡한 JQL
Workflow 커스터마이징
권한 설정
자동화 설정
고급 Dashboard 구성
Jira 관리자 설정
Scrum 상세 이론
Story Point 깊은 설명
```

---

## 10. 최종 프로젝트 적용 기준

팀 프로젝트에서는 최소한 다음 정도만 운영해도 충분하다.
```text
Epic 2~3개
Story 5~7개
Task 15~25개
Bug 등록 방식 정의
팀원별 담당 Issue 배정
매일 또는 매주 Board 업데이트
```

---

## 11. 한 문장 정리
```text
Jira와 GitHub Issues는 프로젝트 요구사항을 작은 작업 카드로 나누고, 담당자와 진행 상태를 추적하기 위한 작업 관리 도구이다.
```
