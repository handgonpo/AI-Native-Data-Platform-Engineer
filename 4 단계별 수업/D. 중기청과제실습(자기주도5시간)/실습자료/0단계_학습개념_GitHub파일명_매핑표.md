## 1. 목적

이 문서는 `0단계_프로젝트_기준선_정리`에서 배운 개념을 GitHub의 `lesson/00_project_baseline` 브랜치에서 어떤 파일로 작성해야 하는지 연결하기 위한 안내 문서이다.
```text
학습 개념
→ GitHub 작성 파일
→ 작성해야 할 내용
→ 완료 기준
```

0단계는 코드를 많이 작성하는 단계가 아니라, 이후 개발이 흔들리지 않도록 기준 문서와 샘플 데이터를 남기는 단계이다.

---

## 2. 0단계 GitHub 산출물 구조

| 위치 | 역할 |
|---|---|
| `README.md` | 프로젝트 전체 소개와 0단계 기준 요약 |
| `docs/` | 프로젝트 목적, 범위, 데이터 흐름, 브랜치 전략 등 기준 문서 |
| `sample_events/` | 0단계에서 사용할 샘플 이벤트 JSON |
| `seed/` | 임계치, 기준값, 초기 설정 데이터 |
| `data_lake/` | 이후 Raw, Staging, Mart 데이터가 저장될 기준 폴더 |

---

## 3. 학습 개념과 GitHub 파일명 매핑표

| 학습 개념                                                       | GitHub 작성 파일                                                  | 작성해야 할 내용                                     | 완료 기준                                   |
| ----------------------------------------------------------- | ------------------------------------------------------------- | --------------------------------------------- | --------------------------------------- |
| 프로젝트 목적                                                   . | `README.md`, `docs/project-overview.md`                       | 프로젝트가 무엇을 만들고 왜 필요한지 작성                       | 목적, 대상, 핵심 흐름이 한눈에 보인다                  |
| 현재 상태                                                       | `docs/current-state.md`                                       | 0단계에서 아직 구현하지 않은 기능과 현재 가능한 범위 작성             | 현재 없는 기능과 가능한 확인 방법이 구분된다               |
| 문제 정의                                                       | `docs/project-overview.md`                                    | 산업안전 관제에서 해결하려는 문제 작성                         | 위험 데이터 수집, 판단, 알람, AI 활용 필요성이 설명된다      |
| 도메인 <br>정의                                                  | `docs/project-overview.md`                                    | 산업안전 관제플랫폼의 업무 영역과 핵심 대상 작성                   | 센서, 전력, 작업자, 위험구역, 알람이 등장한다             |
| 사용자 <br>역할                                                  | `docs/project-overview.md`                                    | 운영자, 관리자, AI 시스템, RAG 시스템 등 역할 작성             | 누가 어떤 데이터를 보고 어떤 판단을 하는지 보인다            |
| 데이터 <br>소스                                                  | `docs/data-source-map.md`                                     | 데이터가 어디서 발생하는지 작성                             | 센서, 전력 장비, 작업자 위치, RAG 로그, 피드백 출처가 정리된다 |
| 데이터 <br>유형                                                  | `docs/ai-service-data-map.md`                                 | 데이터가 AI, RAG, 대시보드, 피드백 중 어디에 쓰이는지 작성         | 학습 데이터, 추론 데이터, RAG 로그, 피드백 데이터가 구분된다   |
| 도메인 <br>이벤트                                                 | `sample_events/*.sample.json`, 필요 시 `docs/data-source-map.md` | 주요 사건을 이벤트명과 샘플 JSON으로 표현                     | 이벤트명이 데이터 파일과 연결된다                      |
| 데이터 <br>흐름                                                  | `docs/baseline-data-flow.md`                                  | 수집 → Raw → Staging → Mart → AI/RAG/대시보드 흐름 작성 | 데이터가 어디서 들어와 어디로 가는지 설명된다               |
| 시스템 <br>경계                                                  | `docs/platform-scope.md`                                      | 만들 것과 만들지 않을 것을 구분                            | 실제 하드웨어, 실제 신고 연동 등 제외 범위가 명확하다         |
| 위험도 <br>판단 기준                                               | `docs/threshold-definition.md`, `seed/thresholds.seed.json`   | 가스, 전력, 위치 위험 기준과 seed 데이터 작성                 | 기준값 문서와 JSON seed가 서로 연결된다              |
| 샘플 <br>이벤트                                                  | `sample_events/gas_sensor_event.sample.json` 등                | 0단계에서 사용할 정상 샘플 JSON 작성                       | 각 이벤트가 어떤 구조로 들어오는지 보인다                 |
| AI서비스 로그                                                    | `sample_events/ai_service_log.sample.json`                    | AI 추론 또는 서비스 호출 로그 예시 작성                      | AI 판단 결과를 추적할 수 있다                      |
| RAG질의 로그                                                    | `sample_events/rag_query_log.sample.json`                     | 질문, 검색 문서, 답변 로그 예시 작성                        | RAG 사용 이력이 데이터로 남는다                     |
| 피드백 <br>데이터                                                 | `sample_events/feedback_event.sample.json`                    | 운영자 피드백, 오탐/정탐/미탐 판단 예시 작성                    | AI 개선에 사용할 수 있는 피드백 구조가 보인다             |
| 브랜치 <br>전략                                                  | `docs/branch-roadmap.md`                                      | 단계별 브랜치 이름과 개발 순서 작성                          | 0단계 이후 어떤 브랜치로 이어지는지 보인다                |
| 최종 <br>시연 기준                                                | `docs/final-demo-scenario.md`                                 | 마지막에 어떤 흐름을 보여줄지 작성                           | 시연 순서와 확인 포인트가 정리된다                     |
| 완료 체크리스트                                                    | `docs/baseline-completion-checklist.md`                       | 0단계가 끝났는지 확인할 항목 작성                           | 문서, 샘플, seed, README가 모두 확인된다           |
| 산출물 <br>기준                                                  | `README.md`, `docs/baseline-completion-checklist.md`          | 0단계에서 남겨야 할 결과물 목록 작성                         | 어떤 파일을 제출해야 하는지 명확하다                    |

---

## 4. 파일별 작성 가이드

### 4.1 `README.md`

작성 내용:
```text
프로젝트명
현재 단계
0단계 목표
앞으로 구현할 단계
현재 없는 기능
실행 방법
0단계 산출물 목록
```

완료 기준:
```text
이 저장소가 어떤 프로젝트인지 설명되어 있다.
현재 브랜치가 0단계 기준선임을 알 수 있다.
0단계에서 구현하지 않는 기능이 명확하다.
docs, sample_events, seed 폴더가 어떤 역할인지 설명되어 있다.
```

---

### 4.2 `docs/project-overview.md`

작성 내용:
```text
프로젝트 목적
해결하려는 문제
주요 사용자
핵심 도메인 요소
0단계에서 바라보는 전체 방향
```

작성 예시:
```text
이 프로젝트는 산업안전 현장에서 발생하는 센서, 전력, 작업자 위치 데이터를 수집하고,
위험도를 판단하여 알람과 대시보드, AI 학습 데이터셋으로 연결하는
AI 네이티브 데이터 플랫폼 실습 프로젝트이다.
```

완료 기준:
```text
프로젝트 목적이 한 문단으로 설명된다.
산업안전 도메인의 핵심 대상이 정리되어 있다.
데이터가 왜 필요한지 설명되어 있다.
```

---

### 4.3 `docs/data-source-map.md`

작성 내용:
```text
데이터 이름
데이터 소스
발생 주체
발생 방식
데이터 형식
사용 목적
품질 위험
```

작성 예시:

| 데이터 이름 | 데이터 소스 | 발생 방식 | 사용 목적 |
|---|---|---|---|
| 가스 센서 데이터 | 가스 센서 또는 시뮬레이터 | 주기적 JSON 전송 | 위험도 판단, AI 이상탐지 |
| 전력 데이터 | 전력 장비 또는 시뮬레이터 | 주기적 JSON 전송 | 과부하 판단 |
| 작업자 위치 데이터 | 위치 장비 또는 앱 | 좌표 전송 | 위험구역 진입 판단 |
| RAG 질의 로그 | 운영자 검색 화면 | 질문 입력 | 대응 매뉴얼 검색 분석 |
| 피드백 데이터 | 운영자 피드백 화면 | 조치 결과 입력 | 재학습 후보 데이터 |

완료 기준:
```text
데이터가 어디서 발생하는지 설명되어 있다.
각 데이터가 AI, RAG, 대시보드, 피드백 중 어디에 쓰이는지 보인다.
데이터 품질 위험이 함께 정리되어 있다.
```

---

### 4.4 `docs/ai-service-data-map.md`

작성 내용:
```text
AI 학습 데이터
AI 추론 데이터
AI 서비스 로그
RAG 로그
피드백 데이터
재학습 후보 데이터
```

완료 기준:
```text
AI 모델이 학습할 데이터와 실제 서비스에서 발생하는 로그가 구분되어 있다.
RAG 검색 로그와 운영자 피드백 데이터가 따로 정리되어 있다.
```

---

### 4.5 `docs/baseline-data-flow.md`

작성 내용:
```text
데이터 발생
→ 수집
→ Raw
→ Staging
→ Mart
→ AI/RAG/대시보드
→ 피드백
→ 데이터 품질 개선
```

작성 예시:
```text
gas_sensor_event.sample.json
→ Raw 가스 이벤트
→ Staging 가스 측정 데이터
→ 위험도 Mart
→ 알람 / 대시보드 / AI 학습 데이터셋
→ 운영자 피드백
```

완료 기준:
```text
Raw, Staging, Mart가 구분되어 있다.
AI, RAG, 대시보드, 피드백으로 연결되는 흐름이 보인다.
Mermaid 다이어그램 또는 표로 설명되어 있다.
```

---

### 4.6 `docs/platform-scope.md`

작성 내용:
```text
만드는 것
만들지 않는 것
대체 방식
이후 단계에서 구현할 것
```

작성 예시:

| 구분 | 내용 |
|---|---|
| 만드는 것 | 샘플 이벤트, 데이터 흐름, 임계치 기준, 시연 시나리오 |
| 만들지 않는 것 | 실제 센서 하드웨어, 실제 문자 발송, 실제 119 신고 연동 |
| 대체 방식 | 샘플 JSON과 seed 데이터로 대체 |
| 이후 구현 | Collector API, Staging 검증, Mart 생성, 대시보드 |

완료 기준:
```text
프로젝트가 어디까지 만들고 어디부터 제외하는지 명확하다.
수업 시간 안에 가능한 범위로 제한되어 있다.
```

---

### 4.7 `docs/threshold-definition.md` / `seed/thresholds.seed.json`

작성 내용:
```text
가스 종류별 임계치
전력 사용량 기준
작업자 위치 위험 기준
normal / warning / danger 구분
문서 기준과 JSON seed의 연결
```

완료 기준:
```text
위험도 판단 기준이 문서로 설명되어 있다.
같은 기준이 seed JSON으로도 표현되어 있다.
나중에 DB seed 또는 기준정보 테이블로 확장할 수 있다.
```

---

### 4.8 `sample_events/*.sample.json`

현재 0단계에서 사용할 수 있는 샘플 이벤트:
```text
sample_events/gas_sensor_event.sample.json
sample_events/power_sensor_event.sample.json
sample_events/worker_location_event.sample.json
sample_events/ai_service_log.sample.json
sample_events/rag_query_log.sample.json
sample_events/feedback_event.sample.json
```

각 파일에 포함할 기본 항목:
```text
event_id
event_type
schema_version
source_system
event_time
payload
```

완료 기준:
```text
각 샘플 JSON이 어떤 이벤트를 표현하는지 명확하다.
데이터 계약과 연결할 수 있는 필드 구조를 가지고 있다.
Raw 저장과 Staging 검증의 기준으로 사용할 수 있다.
```

---

### 4.9 `docs/branch-roadmap.md`

작성 내용:
```text
0단계부터 최종 단계까지 브랜치명
각 브랜치의 목표
각 브랜치에서 만드는 산출물
다음 브랜치와의 연결
```

작성 예시:

| 단계 | 브랜치명 | 목표 |
|---|---|---|
| 0단계 | `lesson/00_project_baseline` | 프로젝트 기준선 정리 |
| 1단계 | `lesson/01_architecture_domain_events` | 아키텍처와 이벤트 설계 |
| 2단계 | `lesson/02_data_collection_lakehouse` | 데이터 수집과 Raw 저장 |
| 3단계 | `lesson/03_pipeline_automation` | Staging, Mart, 자동화 |

완료 기준:
```text
학생이 다음 단계 브랜치를 어떤 기준으로 만들지 알 수 있다.
각 브랜치의 역할이 중복되지 않는다.
```

---

### 4.10 `docs/final-demo-scenario.md`

작성 내용:
```text
시연 목적
시연 순서
입력 데이터
확인 화면 또는 결과
성공 기준
```

작성 예시:
```text
1. 가스 센서 샘플 이벤트를 확인한다.
2. Raw, Staging, Mart로 이어질 데이터 흐름을 설명한다.
3. 임계치 기준으로 위험도 판단이 어떻게 이루어질지 설명한다.
4. 대시보드와 AI 학습 데이터셋으로 연결되는 흐름을 설명한다.
5. 운영자 피드백이 다시 품질 개선과 재학습 후보로 연결되는 구조를 설명한다.
```

완료 기준:
```text
시연 순서가 있다.
어떤 데이터를 보여줄지 정해져 있다.
성공 기준이 명확하다.
```

---

### 4.11 `docs/baseline-completion-checklist.md`

작성 내용:
```text
README 작성 여부
docs 문서 작성 여부
sample_events 작성 여부
seed 작성 여부
데이터 흐름 작성 여부
시스템 경계 작성 여부
최종 시연 시나리오 작성 여부
```

작성 예시:
```md
# 0단계 완료 체크리스트

- [ ] README.md에 현재 단계와 목표가 작성되어 있다.
- [ ] docs/project-overview.md가 작성되어 있다.
- [ ] docs/data-source-map.md가 작성되어 있다.
- [ ] docs/baseline-data-flow.md가 작성되어 있다.
- [ ] docs/platform-scope.md가 작성되어 있다.
- [ ] docs/branch-roadmap.md가 작성되어 있다.
- [ ] docs/final-demo-scenario.md가 작성되어 있다.
- [ ] sample_events/에 샘플 JSON이 있다.
- [ ] seed/thresholds.seed.json이 있다.
```

완료 기준:
```text
학생이 0단계가 끝났는지 스스로 확인할 수 있다.
강사나 리뷰어가 동일 기준으로 검토할 수 있다.
```

---

## 5. 학습 개념별 최소 작성 기준

| 학습 개념 | 최소 작성 기준 |
|---|---|
| 프로젝트 목적 | 한 문단으로 설명할 수 있다 |
| 데이터 소스 | 최소 5개 이상 정리한다 |
| 이벤트 | 최소 5개 이상 이벤트명으로 표현한다 |
| 데이터 흐름 | Raw, Staging, Mart가 보이게 작성한다 |
| 시스템 경계 | 만드는 것과 만들지 않는 것을 구분한다 |
| 샘플 JSON | 최소 3개 이상 작성한다 |
| 임계치 seed | 위험도 판단 기준을 JSON으로 표현한다 |
| 시연 시나리오 | 5단계 이내 흐름으로 설명한다 |
| 체크리스트 | 완료 여부를 체크박스로 확인한다 |

---

## 6. 현업 스타일 검토 기준

| 기준 | 확인 질문 |
|---|---|
| 목적성 | 이 파일이 왜 필요한지 설명되는가? |
| 연결성 | README, docs, sample_events, seed가 서로 연결되는가? |
| 추적성 | 어떤 데이터가 어디서 와서 어디로 가는지 추적되는가? |
| 일관성 | 파일명, 이벤트명, 브랜치명이 같은 규칙을 따르는가? |
| 검증 가능성 | 완료 체크리스트로 작성 여부를 확인할 수 있는가? |
| 확장성 | 이후 단계에서 API, DB, AI, RAG로 확장할 수 있는가? |

---

## 7. 최종 정리

```text
0단계 학습자료는 개념을 배우는 문서이고,
GitHub의 lesson/00_project_baseline은 그 개념을 실제 산출물로 작성하는 공간이다.
```

다음 순서로 작업하면 된다.
```text
1. 0단계 학습자료에서 개념을 이해한다.
2. GitHub의 README.md에서 현재 브랜치 목표를 확인한다.
3. docs/에 기준선 문서를 작성한다.
4. sample_events/에 샘플 이벤트 JSON을 작성한다.
5. seed/에 임계치 기준 데이터를 작성한다.
6. baseline-completion-checklist.md로 완료 여부를 확인한다.
```

한 문장으로 정리하면 다음과 같다.
```text
0단계는 코드를 많이 작성하는 단계가 아니라, 이후 모든 개발이 흔들리지 않도록 기준 문서와 샘플 데이터를 GitHub에 남기는 단계이다.
```
