
**AI 네이티브 데이터 플랫폼 엔지니어는 단순 코딩 직무라기보다 “데이터 중심의 기술 기획 + 설계 + 구현 연결”에 가까운 역할**입니다.

다만 일반 기획자처럼 화면이나 기능만 기획하는 것이 아니라, **AI 서비스가 사용할 데이터 흐름을 기술적으로 설계하는 사람**에 가깝습니다.

정리하면 이렇게 볼 수 있습니다.
```
일반 기획자:
사용자 기능, 화면, 서비스 흐름을 기획한다.

백엔드 개발자:
API, DB, 인증, 서버 로직을 구현한다.

AI 네이티브 데이터 플랫폼 엔지니어:
업무에서 어떤 데이터가 발생하는지 파악하고,
그 데이터를 어떻게 수집·검증·저장·가공·AI/RAG/피드백으로 연결할지 설계한다.
```

즉, 이 직무는 코딩만 잘한다고 되는 역할은 아닙니다.  
먼저 다음을 설계해야 합니다.
```
어떤 이벤트가 발생하는가?
어떤 데이터 소스가 있는가?
Raw에는 무엇을 남길 것인가?
Staging에서는 무엇을 검증할 것인가?
Mart는 어떤 목적별 데이터셋으로 만들 것인가?
AI 학습 데이터는 어디서 만들어지는가?
RAG 문서 데이터는 어떻게 관리할 것인가?
피드백은 어떻게 재학습 후보가 되는가?
운영 중 데이터 품질과 지연은 어떻게 볼 것인가?
```

그리고 백엔드는 그 기준에 맞춰 다음을 구현합니다.
```
API 연결
DB 테이블 생성
이벤트 저장
Schema 검증
Raw 저장
Staging 변환
Mart 생성
대시보드 API 제공
피드백 저장
로그 저장
```

그래서 역할을 나누면 이렇게 이해하면 됩니다.

| 역할                        | 하는 일                                                 |
| ------------------------- | ---------------------------------------------------- |
| 데이터 설계자 / AI 데이터 플랫폼 엔지니어 | 어떤 데이터가 필요하고 어떻게 흘러야 하는지 기준을 만든다                     |
| 백엔드 개발자                   | 그 기준에 맞게 API, DB, 서버 로직을 구현한다                        |
| 데이터 엔지니어                  | 수집, 저장, 파이프라인, 품질, 재처리 구조를 만든다                       |
| AI 엔지니어                   | 만들어진 Feature Dataset이나 Vector Data를 사용해 모델/RAG를 연결한다 |
하지만 실제 실무나 작은 팀에서는 이 역할이 완전히 분리되지 않을 수 있습니다.  
그래서 AI 네이티브 데이터 플랫폼 엔지니어는 **기획만 하는 사람도 아니고, 코딩만 하는 사람도 아닙니다.**
```
AI 네이티브 데이터 플랫폼 엔지니어는  
업무 요구사항을 데이터 구조와 데이터 흐름으로 번역하고,  
그 구조가 실제 시스템에서 구현될 수 있도록 설계와 구현을 연결하는 역할이다.
```

그래서 이제 배우게될 `업무 흐름 → 기능 흐름 → 시스템 처리 흐름 → 데이터 흐름 → 이벤트 → Raw/Staging/Mart` 정리는 매우 중요합니다.

이걸 할 수 있어야 백엔드 개발자에게도 이렇게 정확히 말할 수 있습니다.
```
이 기능은 단순히 DB에 저장하는 기능이 아니라,
order_created 이벤트로 남겨야 합니다.

이 이벤트는 Raw에 원본 저장하고,
Staging에서 필수값과 타입을 검증하고,
Mart에서는 고객별 주문 요약 데이터셋으로 만들어야 합니다.

나중에 추천 모델 학습 데이터와 대시보드 매출 지표에도 사용됩니다.
```
이 정도로 말할 수 있으면 단순 기능 구현자가 아니라 **데이터 플랫폼 설계 관점으로 프로젝트를 리딩할 수 있는 사람**이 됩니다.

### 배워야할 기술 스택
| 구분            | 배워야 하는 <br>기술스택                       | 수업 내 역할                              | 중기청 R&D 과제 <br>적용 예시                                       | 중요도             . |
| ------------- | ------------------------------------- | ------------------------------------ | ---------------------------------------------------------- | ----------------- |
| Backend API   | FastAPI                               | 센서 데이터 수집 API, AI 추론 API, RAG API 구현 | 가스·전력·작업자 위치 데이터를 수신하고 Pydantic으로 검증                       | 필수                |
| Backend API   | Django REST Framework                 | 관리자 API, 백오피스, 인증/권한, 도메인 데이터 관리     | 센서 등록, 임계치 관리, 알람 이력, 사용자/조직 관리                            | 필수                |
| Realtime Web  | Django Channels / WebSocket           | 실시간 대시보드 데이터 전송                      | 위험 알람, 센서 상태, 작업자 위치를 화면에 즉시 반영                            | 필수                |
| Async Task    | Celery                                | 무거운 작업 비동기 처리, 주기 작업 실행              | 알람 발송, 데이터 정리, 위험구역 갱신, 백업 작업                              | 필수                |
| Cache / Queue | Redis                                 | 캐시, 상태 저장, 큐, 채널 레이어                 | 실시간 알람 큐, WebSocket 채널 레이어, 중복 알람 방지                       | 필수                |
| Database      | PostgreSQL                            | 운영 데이터 저장, 시계열 이력 관리                 | GasData, PowerData, AlarmRecord, Event, MLAnomalyResult 저장 | 필수                |
| Data Modeling | Raw / Staging / Mart 설계               | 원천 데이터와 분석용 데이터를 분리                  | 센서 원본값은 Raw, 정제 데이터는 Staging, 대시보드 집계는 Mart                | 필수                |
| Data Contract | Pydantic / Serializer / DB Constraint | 데이터 타입·단위·범위 검증                      | CO, H2S, CO2, O2, 전류, 전압, 전력값 검증                           | 필수                |
| Workflow      | Airflow                               | 배치 파이프라인 자동화                         | 일별 센서 집계, 알람 통계, AI 학습 데이터 생성                              | 필수                |
| Workflow      | DAG / Schedule / Retry / Backfill     | 실패 재처리와 과거 데이터 재계산                   | 누락된 센서 데이터 재처리, 과거 7일 알람 통계 재생성                            | 필수                |
| Streaming     | Kafka                                 | 실시간 이벤트 스트리밍                         | gas-sensor, power-sensor, alarm-event topic 구성             | 필수                |
| Streaming     | Spark Structured Streaming            | 실시간 window 집계, 대용량 로그 처리             | 1분 단위 평균 가스 농도, 5분 단위 전력 이상 패턴 집계                          | 필수                |
| Data Quality  | dbt Test                              | 데이터 품질 테스트 자동화                       | null, 중복, 범위 초과, 임계치 불일치 검증                                | 필수                |
| Data Quality  | Data Lineage                          | 데이터 흐름 추적                            | Raw → Staging → Mart → AI 결과 → Dashboard 흐름 문서화            | 필수                |
| Governance    | PII / 권한 관리                           | 개인정보·민감정보 보호                         | 작업자 위치 데이터 접근 권한 분리, 관리자/운영자 권한 설계                         | 필수                |
| AI Model      | IsolationForest                       | 이상치 탐지                               | 전력 사용량, 가스 농도 패턴 이상탐지                                      | 필수                |
| AI Model      | ARIMA / 시계열 예측                        | 추세 예측                                | 전력 사용량 증가 추세 예측, 임계치 도달 전 조기경고                             | 권장                |
| AI Service    | AI 추론 API                             | 모델 결과를 서비스에 연결                       | FastAPI에서 AI 결과를 생성하고 DRF/DB/알람에 연결                        | 필수                |
| RAG           | Chunking                              | 문서를 검색 가능한 단위로 분할                    | 센서 정의서, 장비 카탈로그, 안전 매뉴얼 분할                                 | 필수                |
| RAG           | Embedding                             | 문서를 벡터로 변환                           | H2S, CO, 전력 과부하 대응 문서를 벡터화                                 | 필수                |
| RAG           | Vector DB                             | 문서 검색 저장소                            | 위험 알람 발생 시 관련 안전 매뉴얼 검색                                    | 필수                |
| RAG           | Metadata 설계                           | 검색 품질 개선                             | 가스명, 위험등급, 장비명, 문서 출처 태깅                                   | 필수                |
| RAG           | Hybrid Search                         | 키워드 검색 + 벡터 검색 결합                    | “CO 위험 기준”처럼 정확한 용어 검색과 의미 검색 동시 처리                        | 권장                |
| Monitoring    | Prometheus                            | 시스템 메트릭 수집                           | API 요청 수, 알람 수, DB 저장 실패, Kafka consumer lag 수집            | 필수                |
| Monitoring    | Grafana                               | 운영 대시보드 시각화                          | 센서 수집량, 알람 발생량, AI 탐지 수, 장애 지표 시각화                         | 필수                |
| Infra         | Docker / Docker Compose               | 개발·실습 환경 표준화                         | DRF, FastAPI, PostgreSQL, Redis, Airflow, Kafka를 컨테이너로 실행  | 필수                |
| Infra         | Kubernetes / kind                     | 운영형 배포 구조 학습                         | DRF/FastAPI 다중 replica, HPA, Ingress 구성                    | 권장~필수             |
| CI/CD         | GitHub Actions                        | 테스트·빌드 자동화                           | PR 시 테스트 실행, Docker image build, 배포 준비                     | 필수                |
| Collaboration | Git / GitHub                          | 협업, 이력관리, 포트폴리오 관리                   | branch, PR, issue, code review, README 작성                  | 필수                |
| Collaboration | Jira / Notion / Slack                 | 팀 프로젝트 관리                            | 요구사항 관리, 일정 관리, 회의록, 기능 매핑표 관리                             | 권장                |
| AI Tool       | ChatGPT / Claude / Cursor             | 코드 작성 보조, 문서화, 리뷰                    | 테스트 코드 생성, README 작성, 오류 분석, 리팩토링 보조                       | 필수                |
| Documentation | Markdown / README / 기술문서              | 포트폴리오와 평가 자료 작성                      | 아키텍처, 데이터 흐름, API 명세, 증빙자료 정리                              | 필수                |

#### AI 네이티브 데이터 플랫폼 과정 기술스택 구성안
| 분류            | 함께 가르칠 기술스택                                                          | 수업 내 위치             |
| ------------- | -------------------------------------------------------------------- | ------------------- |
| 기본 개발 환경      | Python, Git, GitHub, Markdown, README, Docker 기초                     | 전 단계 공통             |
| 수집 API        | FastAPI, Pydantic                                                    | 2단계 중심              |
| 운영 API / 백오피스 | Django, Django REST Framework, Serializer, DB Constraint             | 1~2단계 기초, 후반 실습 재사용 |
| 데이터 저장        | PostgreSQL, Raw / Staging / Mart, Parquet, SQL                       | 2~5단계 핵심            |
| 파이프라인 자동화     | Airflow, DAG, Schedule, Retry, Backfill                              | 3단계 핵심              |
| 비동기 처리        | Celery, Redis                                                        | 3~4단계 보조            |
| 실시간 처리        | Kafka, Spark Structured Streaming, WebSocket, Django Channels        | 4단계 핵심              |
| 데이터 품질 / 거버넌스 | dbt Test, Data Quality, Data Lineage, PII, 권한 관리                     | 5단계 핵심              |
| AI 이상탐지       | IsolationForest, ARIMA, AI 추론 API                                    | 5단계 또는 프로젝트 연계      |
| RAG           | Chunking, Embedding, Vector DB, Metadata, Hybrid Search              | 6단계 핵심              |
| 운영 / DataOps  | Prometheus, Grafana, Docker Compose, Kubernetes kind, GitHub Actions | 7단계 핵심              |
| 협업 / AI 도구    | Jira, Notion, Slack 또는 Discord, ChatGPT, Claude, Cursor              | 전 단계 보조             |

---
# 1단계. AI 서비스와 데이터 플랫폼 아키텍처

## 핵심 목표

AI 서비스가 모델만으로 동작하지 않고, 데이터 수집·저장·처리·운영 구조가 필요하다는 것을 이해하는 단계입니다.

## 함께 가르칠 기술스택

|기술스택|수업 내 역할|깊이|
|---|---|---|
|Git / GitHub|브랜치, 커밋, 실습 단계 관리|필수|
|Markdown / README|아키텍처 문서, 데이터 흐름 문서 작성|필수|
|Python 기초|이후 모든 실습 코드 기반|필수|
|Docker 개념|후반부 컨테이너 실행을 위한 사전 이해|개념 중심|
|Django 기본 구조|화면 서버와 프로젝트 골격 이해|얕게|
|FastAPI 개념|수집 API가 무엇인지 이해|얕게|
|PostgreSQL 개념|운영 DB와 분석용 데이터 저장소 차이 이해|개념 중심|
|Raw / Staging / Mart 개념|전체 데이터 플랫폼 흐름의 핵심 구조|필수|
1단계는 기술을 많이 쓰는 단계가 아니라, **전체 구조를 이해하는 단계**입니다.

---
# 2단계. AI 데이터 수집과 레이크하우스 설계

## 핵심 목표

외부 데이터가 들어와서 Raw에 저장되고, 검증된 뒤 Staging으로 정리되는 구조를 만드는 단계입니다.
```
Sensor / Log / Feedback
        ↓
FastAPI Collector
        ↓
Pydantic Validation
        ↓
Raw JSONL
        ↓
Staging Parquet
        ↓
DuckDB / SQL 조회
```

##### 함께 가르칠 기술스택
|기술스택|수업 내 역할|깊이|
|---|---|---|
|FastAPI|센서·로그·피드백 수집 API|실습 필수|
|Pydantic|데이터 계약, 필수 필드, 타입 검증|실습 필수|
|JSON / JSONL|Raw 데이터 저장 형식|필수|
|Parquet|Staging 데이터 저장 형식|필수|
|Raw / Staging / Mart 설계|데이터 레이크하우스 핵심 구조|필수|
|PostgreSQL|기준정보, 임계치, 운영 데이터 저장|기본|
|DuckDB 또는 SQL|Parquet 조회 검증|기본|
|`.env`, `.gitignore`, `.gitkeep`|실습 프로젝트 관리|기본|
|Markdown 기술문서|데이터 계약서, API 설명서 작성|필수|
Django/DRF는 2단계의 중심이 아닙니다.  
다만 센서, 임계치, 알람 같은 기준정보를 나중에 관리해야 하므로 다음 정도만 설명
```
Django는 화면과 백오피스 역할
DRF는 운영 데이터 관리 API 역할
FastAPI는 외부 데이터 수집 API 역할
```

---

# 3단계. AI 워크로드를 위한 데이터 파이프라인 자동화

## 핵심 목표
2단계에서 수동으로 처리하던 데이터 변환 작업을 Airflow로 자동화하는 단계
```
Raw JSONL
        ↓
Airflow DAG
        ↓
Validation Task
        ↓
Staging Parquet
        ↓
Mart 생성
        ↓
AI Training Dataset 생성
        ↓
Quality Report / Metadata 저장
```

##### 함께 가르칠 기술스택
|기술스택|수업 내 역할|깊이|
|---|---|---|
|Airflow|데이터 파이프라인 자동 실행|필수|
|DAG|작업 순서 정의|필수|
|Task|하나의 처리 단위 이해|필수|
|Schedule|정해진 시간에 자동 실행|필수|
|Retry|실패 시 재시도|필수|
|Backfill|과거 데이터 재처리|필수|
|Python Pipeline Package|`pipeline/` 구조로 로직 분리|필수|
|pandas / pyarrow|Raw → Staging → Mart 변환|기본|
|Mart 설계|위험도, 알람, 학습 데이터셋 생성|필수|
|Metadata / Marker|실행 이력과 마지막 처리 상태 관리|필수|
|Celery / Redis|비동기 작업 개념과 비교 설명|개념 또는 보조|
이 단계에서는 Airflow 문법보다 다음을 더 중요하게 알아야 함
```
왜 수동 스크립트만으로는 부족한가?
왜 DAG가 필요한가?
왜 작업을 Task 단위로 나누는가?
왜 Backfill이 필요한가?
왜 실행 이력을 Metadata에 남겨야 하는가?
왜 같은 작업을 여러 번 실행해도 결과가 깨지지 않아야 하는가?
```
즉, 3단계의 핵심은 **Airflow 사용법**이 아니라 **운영 가능한 데이터 파이프라인 사고방식**입니다.

---
# 4단계. 대용량 로그와 실시간 이벤트 스트리밍

## 핵심 목표
배치 처리만으로는 부족한 실시간 센서·알람·로그 데이터를 Kafka와 Spark로 처리하는 단계
```
Sensor Event
        ↓
Kafka Topic
        ↓
Consumer / Spark Streaming
        ↓
Window Aggregation
        ↓
Realtime Mart
        ↓
WebSocket Dashboard
```

##### 함께 가르칠 기술스택
|기술스택|수업 내 역할|깊이|
|---|---|---|
|Kafka|실시간 이벤트 스트리밍 통로|필수|
|Kafka Topic|이벤트 종류별 흐름 분리|필수|
|Producer / Consumer|이벤트 발행과 구독 구조|필수|
|Spark Structured Streaming|대용량 실시간 집계|필수 또는 경량 실습|
|Window Aggregation|1분/5분 단위 집계|필수|
|Partition|대용량 처리 분산 개념|개념 중심|
|Consumer Lag|처리 지연 모니터링|필수|
|Django Channels / WebSocket|실시간 대시보드 반영|실습 필수|
|Redis|WebSocket Channel Layer, 실시간 상태 저장|필수|
|Celery|알람 발송, 후처리 비동기 작업|필수|
Kafka와 Spark
```
Kafka
→ Topic, Producer, Consumer, Consumer Group 이해

Spark Structured Streaming
→ 실시간 데이터를 window 단위로 집계하는 구조 이해

WebSocket
→ 처리 결과를 대시보드에 실시간 표시
```

---
# 5단계. AI 데이터 품질, 계보, 거버넌스

## 핵심 목표
AI 모델과 서비스 신뢰도에 영향을 주는 데이터 품질을 관리하는 단계
```
Raw
 ↓
Staging Validation
 ↓
dbt Test
 ↓
Quality Report
 ↓
Lineage
 ↓
Governance / 권한 관리
```

##### 함께 가르칠 기술스택
|기술스택|수업 내 역할|깊이|
|---|---|---|
|dbt|데이터 변환과 품질 테스트 관리|필수|
|dbt Test|null, unique, accepted values, relationship 검증|필수|
|Data Quality Rule|누락, 중복, 범위 초과, 지연 데이터 검증|필수|
|Data Lineage|Raw → Staging → Mart → AI → Dashboard 흐름 추적|필수|
|Data Contract|데이터 형식과 품질 기준 문서화|필수|
|PII|작업자 위치, 사용자 피드백 등 민감정보 보호|필수|
|권한 관리|관리자/운영자/분석가 권한 분리|필수|
|PostgreSQL Constraint|DB 레벨 품질 제한|기본|
|Serializer / Pydantic|API 레벨 품질 검증|복습|
|IsolationForest|이상탐지 데이터 품질/위험탐지 연결|실습 가능|
|ARIMA|시계열 예측 개념|권장|
5단계에서 AI 모델을 깊게 학습시키는 것이 목적은 아니며 AI 모델은 아래 수준으로 학습
```
IsolationForest
→ 센서값이나 전력 사용량의 이상치를 탐지하는 예제

ARIMA
→ 전력 사용량이나 가스 농도 추세를 예측하는 예제

AI 추론 API
→ 모델 결과를 서비스와 데이터 파이프라인에 연결하는 예제
```

핵심은 모델 성능 튜닝이 아니라 아래 내용입니다
```
모델 입력 데이터는 어디서 오는가?
모델 결과는 어디에 저장되는가?
오탐/정탐 피드백은 어떻게 남기는가?
재학습 후보 데이터셋은 어떻게 만드는가?
```

---
# 6단계. RAG와 벡터 데이터 파이프라인

## 핵심 목표
문서 데이터를 AI 서비스에서 검색 가능한 구조로 만드는 단계
```
PDF / Markdown / Manual
        ↓
Document Loader
        ↓
Chunking
        ↓
Embedding
        ↓
Vector DB
        ↓
Hybrid Search
        ↓
RAG Answer
        ↓
Feedback
```

##### 함께 가르칠 기술스택
|기술스택|수업 내 역할|깊이|
|---|---|---|
|Document Loader|PDF, Markdown, 매뉴얼 문서 수집|필수|
|Chunking|문서를 검색 가능한 단위로 분리|필수|
|Embedding|텍스트를 벡터로 변환|필수|
|Vector DB|벡터 검색 저장소|필수|
|Chroma / FAISS / Qdrant|실습용 Vector DB 선택|하나만 필수|
|Metadata 설계|문서 출처, 장비명, 가스명, 위험등급 태깅|필수|
|Hybrid Search|키워드 검색 + 벡터 검색 결합|권장|
|RAG API|검색 결과 기반 답변 API|필수|
|FastAPI|RAG API 제공|도구로 사용|
|Feedback Log|답변 품질 평가 데이터 수집|필수|
|Data Lineage|문서 출처와 답변 출처 연결|필수|
RAG는 단순히 “챗봇 만들기”가 아니고 
```
RAG는 문서 데이터를 AI 서비스가 사용할 수 있는 데이터 파이프라인으로 바꾸는 구조이다.
```

그래서 6단계의 핵심은 이것
```
문서를 어떻게 수집하는가?
어떻게 쪼개는가?
어떤 메타데이터를 붙이는가?
어떻게 검색 품질을 검증하는가?
답변 출처를 어떻게 남기는가?
사용자 피드백을 어떻게 다시 데이터로 저장하는가?
```

---
# 7단계. AI 서비스 피드백 데이터와 DataOps 운영

## 핵심 목표
AI 서비스 운영 중 발생하는 로그, 피드백, 장애, 품질 지표를 수집하고 개선 사이클로 연결하는 단계
```
AI Service
        ↓
Inference Log
        ↓
User Feedback
        ↓
Quality Monitoring
        ↓
Prometheus / Grafana
        ↓
DataOps Report
        ↓
Retraining Candidate Dataset
```

##### 함께 가르칠 기술스택
|기술스택|수업 내 역할|깊이|
|---|---|---|
|Prometheus|API, DB, Kafka, Celery 지표 수집|필수|
|Grafana|운영 대시보드 시각화|필수|
|Docker / Docker Compose|전체 실습 환경 통합 실행|필수|
|Kubernetes / kind|운영형 배포 구조 경험|권장~필수|
|GitHub Actions|테스트, 빌드, 배포 자동화|필수|
|CI/CD|변경사항 검증과 자동 배포 흐름|필수|
|DataOps|데이터 파이프라인 운영·장애·재처리 관리|필수|
|Feedback Data|사용자 피드백을 개선 데이터로 전환|필수|
|Monitoring Metrics|수집량, 지연, 실패율, 품질 실패율 관리|필수|
|Alerting|장애와 품질 이상 알림|권장|
|ChatGPT / Claude / Cursor|운영 문서, 장애 분석, 코드 리뷰 보조|보조 도구|
7단계는 “배포 수업”이 아니라 **운영 가능한 AI 데이터 플랫폼으로 마무리하는 단계**

따라서 중심 질문은 다음이어야 합니다.
```
데이터 수집이 멈추면 어떻게 알 수 있는가?
Airflow DAG가 실패하면 어떻게 추적하는가?
Kafka Consumer Lag가 쌓이면 무엇을 의미하는가?
AI 추론 결과가 이상하게 나오면 어떤 로그를 봐야 하는가?
RAG 답변 품질이 낮으면 어떤 피드백 데이터를 봐야 하는가?
운영자는 Grafana에서 무엇을 확인해야 하는가?
```


### 단계별 기술스택 최종 정리표
|단계|교과목|반드시 가르칠 기술스택|보조로 다룰 기술스택|
|--:|---|---|---|
|1|AI 서비스와 데이터 플랫폼 아키텍처|Git, GitHub, Markdown, Python, Raw/Staging/Mart 개념, Data Platform Architecture|Docker 개념, Django/FastAPI 역할 구분|
|2|AI 데이터 수집과 레이크하우스 설계|FastAPI, Pydantic, JSON/JSONL, Parquet, PostgreSQL, Raw/Staging/Mart, Data Contract|Django/DRF 역할, DuckDB, `.env`, `.gitignore`|
|3|AI 워크로드 데이터 파이프라인 자동화|Airflow, DAG, Schedule, Retry, Backfill, Mart, Metadata, Pipeline Package|Celery/Redis 개념 비교, pandas/pyarrow|
|4|대용량 로그와 실시간 이벤트 스트리밍|Kafka, Producer/Consumer, Spark Structured Streaming, Window, WebSocket, Django Channels, Redis|Celery, Consumer Lag Monitoring|
|5|AI 데이터 품질, 계보, 거버넌스|dbt Test, Data Quality, Data Lineage, Data Contract, PII, 권한 관리, DB Constraint|IsolationForest, ARIMA, AI 추론 API|
|6|RAG와 벡터 데이터 파이프라인|Chunking, Embedding, Vector DB, Metadata, Hybrid Search, RAG API, Feedback Log|LangChain/LlamaIndex 중 하나, FastAPI|
|7|AI 서비스 피드백 데이터와 DataOps 운영|Prometheus, Grafana, Docker Compose, Kubernetes kind, GitHub Actions, CI/CD, DataOps|ChatGPT/Claude/Cursor, Slack/Notion/Jira|

---

### 필수 기술
|분류|기술|
|---|---|
|데이터 플랫폼 핵심|Raw / Staging / Mart, Data Contract, Data Quality, Data Lineage|
|수집|FastAPI, Pydantic|
|저장|PostgreSQL, JSONL, Parquet|
|자동화|Airflow, DAG, Schedule, Retry, Backfill|
|실시간|Kafka, WebSocket, Redis|
|품질|dbt Test, DB Constraint, PII / 권한 관리|
|RAG|Chunking, Embedding, Vector DB, Metadata|
|운영|Docker Compose, Prometheus, Grafana, GitHub Actions|
|협업|Git, GitHub, Markdown, README|

### 깊게보다는 적용 중심으로 가르칠 기술
|기술|수업에서의 적정 깊이|
|---|---|
|Django REST Framework|백오피스/운영 API 구현에 필요한 만큼|
|Django Channels|실시간 알람 화면 구현에 필요한 만큼|
|Celery|비동기 알람 처리와 주기 작업 이해 중심|
|Spark Structured Streaming|Window 집계와 스트리밍 처리 구조 중심|
|IsolationForest|이상탐지 예제로 사용|
|ARIMA|시계열 예측 개념과 간단한 실습|
|Kubernetes kind|운영형 배포 구조 맛보기|
|Hybrid Search|RAG 검색 품질 개선 개념 중심|
|Jira / Notion / Slack|팀 프로젝트 관리 도구로 사용|

### 이후 적용되는 고급 기술
|기술|이유|
|---|---|
|Django 전체 문법|과정이 웹 백엔드 과정으로 흐를 수 있음|
|DRF 인증/권한 고급 커스터마이징|데이터 플랫폼 핵심에서 벗어남|
|FastAPI 고급 의존성 주입 구조|수집 API 구현 수준이면 충분|
|Spark 분산 클러스터 튜닝|초보자 과정 난이도 초과|
|Kubernetes 운영 고급 설정|DevOps 전문 과정으로 흐를 수 있음|
|ML 모델 튜닝|AI 모델링 과정이 아니라 AI 데이터 플랫폼 과정임|
|LangChain 고급 Agent 구조|RAG 데이터 파이프라인보다 챗봇 구현으로 흐를 수 있음|
### 연습 프로젝트: 중기청 R&D 산업안전 데이터 플랫폼
프로젝트명 : AI 기반 산업안전 통합 관제 데이터 플랫폼
목적 : 전체 기술을 연결하는 대표 포트폴리오입니다.

구현범위
```
가스·전력·작업자 위치 데이터 수집  
FastAPI 센서 생성기  
DRF 백오피스  
PostgreSQL Raw/Staging/Mart 저장  
WebSocket 실시간 대시보드  
Redis/Celery 알람 처리  
Airflow 일별 집계  
dbt 품질 테스트  
Kafka/Spark 스트리밍 일부 적용  
AI 이상탐지  
RAG 안전 매뉴얼 검색  
Prometheus/Grafana 모니터링  
Docker/Kubernetes 배포
```


사용 기술

Backend / API
```
Python  
Django  
Django REST Framework  
FastAPI  
Pydantic  
Django ORM  
Django Admin  
JWT / Session Auth  
httpx
```

Frontend / Dashboard
```
Django Template  
HTML  
CSS  
Vanilla JavaScript  
Chart.js  
WebSocket  
Django Channels
```

Database / Data Modeling
```
PostgreSQL  
SQL  
Django ORM  
Raw / Staging / Mart 설계  
Index 설계  
Data Contract  
DB Constraint
```

Async / Realtime
```
Redis  
Celery  
Celery Beat  
Django Channels  
Redis Channel Layer  
WebSocket
```

Data Pipeline / Data Engineering
```
Apache Airflow  
DAG  
Schedule  
Retry  
Backfill  
dbt  
dbt model  
dbt test  
Data Lineage  
Data Quality
```

Streaming
```
Kafka  
Kafka Producer  
Kafka Consumer  
Spark Structured Streaming  
PySpark  
Window Aggregation  
Consumer Lag Monitoring
```

AI / ML
```
scikit-learn  
IsolationForest  
ARIMA  
statsmodels  
pandas  
numpy  
AI Inference API  
Model Result Logging
```

RAG / Vector Search
```
Chunking  
Embedding  
Vector DB  
Chroma  
Qdrant  
FAISS  
LangChain  
Metadata Filtering  
Hybrid Search  
RAG API
```

Monitoring / Observability
```
Prometheus  
Grafana  
django-prometheus  
FastAPI metrics  
Redis Exporter  
Postgres Exporter  
Celery Monitoring
```

Infra / DevOps
```
Docker  
Docker Compose  
Kubernetes  
kind  
Ingress  
Deployment  
Service  
HPA  
GitHub Actions  
Linux
```

Collaboration / Documentation
```
Git  
GitHub  
Issue  
Pull Request  
Code Review  
Markdown  
README  
API 명세서  
ERD  
아키텍처 문서  
기술문서  
시연 영상
```

### 역할 구분
|기술|한 줄 역할|
|---|---|
|**FastAPI**|데이터를 빠르게 받고 AI/RAG API를 제공하는 입구|
|**DRF**|데이터를 관리하고 백오피스를 만드는 운영 계층|
|**PostgreSQL**|센서·알람·AI 결과를 영속 저장하는 중심 DB|
|**Redis**|실시간 상태, 캐시, 큐를 담당하는 중간 저장소|
|**Celery**|알람·정리·주기 작업을 백그라운드에서 처리|
|**WebSocket**|위험 상태를 대시보드에 실시간 전달|
|**Airflow**|데이터 파이프라인을 정해진 시간에 자동 실행|
|**Kafka**|실시간 이벤트를 안정적으로 흘려보내는 스트리밍 통로|
|**Spark**|대량 이벤트를 window 단위로 집계·분석|
|**dbt**|데이터 마트와 품질 테스트를 관리|
|**Vector DB**|문서와 매뉴얼을 AI 검색 가능한 형태로 저장|
|**RAG**|안전 매뉴얼과 센서 문서를 검색해 답변 제공|
|**Prometheus/Grafana**|플랫폼이 정상 작동하는지 관찰|
|**Kubernetes**|여러 서비스를 운영형 구조로 배포|
|**GitHub Actions**|테스트와 배포를 자동화|
|**ChatGPT/Claude/Cursor**|개발·문서화·테스트 보조 도구|
FastAPI와 DRF로 AI 데이터 플랫폼의 백엔드 뼈대를 만들고,  
Airflow·Kafka·Spark로 데이터 흐름을 운영하며,  
dbt·Lineage·Governance로 품질을 관리하고,  
Vector DB·RAG·AI 이상탐지로 AI 서비스를 완성하는 과정입니다.


---
### AI 네이티브 데이터 플랫폼 엔지니어 과정 사전 기초 정리
이 수업을 이해하려면 최소한 아래 정도는 되어야 합니다.

|구분|알아야 할 내용|왜 필요한가|
|---|---|---|
|Python 기본|변수, 조건문, 반복문, 함수, 클래스 기초|모든 실습 코드의 기본 언어|
|Python 자료구조|`list`, `dict`, `tuple`, `set`|JSON, API 응답, 이벤트 데이터 처리에 필요|
|Python 파일 처리|파일 읽기/쓰기, 경로, `with open`, JSONL 저장|Raw 데이터 저장과 로그 처리에 필요|
|Python 모듈 구조|`import`, 패키지, `__init__.py`, 파일 분리|`collector/`, `pipeline/` 구조 이해에 필요|
|가상환경/패키지|`venv`, `pip`, `requirements.txt`|단계별 실습 환경 구성에 필요|
|데이터 형식|JSON, JSONL, CSV, Parquet 기초|Raw, Staging, Mart 데이터 이해에 필요|
|표 구조 이해|행, 열, 컬럼, 레코드, 2차원 데이터|Pandas, DB, Parquet 이해에 필요|
|Linux 명령어|`cd`, `ls`, `pwd`, `mkdir`, `touch`, `cat`, `tree`, `rm`, `cp`, `mv`|WSL2와 터미널 실습에 필요|
|Git 기본|`clone`, `status`, `add`, `commit`, `push`, `pull`, `branch`, `switch`|단계별 브랜치 실습과 GitHub 제출에 필요|
|GitHub 사용|repository, branch, pull request, commit history|수업 산출물 관리에 필요|
|API 기본|HTTP, URL, request, response, GET/POST, status code|FastAPI Collector와 데이터 수집 이해에 필요|
|FastAPI 또는 Django 기초|route, view, request body, response, schema|데이터를 API로 받고 저장하는 구조 이해에 필요|
|DB 기초|table, column, row, primary key, foreign key, SQL 기초|Django DB, DBeaver, Mart/모델 구조 이해에 필요|
|SQL 기초|`SELECT`, `WHERE`, `ORDER BY`, `GROUP BY`, `JOIN`|Staging/Mart 데이터 확인과 분석에 필요|
|문서 작성|Markdown, README, 표, 코드블록|수업 산출물과 포트폴리오 정리에 필요|

### 추가하면 좋은 핵심 기초
|추가 기초|이유|
|---|---|
|**경로 개념**|`data_lake/raw/`, `pipeline/config.py`, 상대경로/절대경로를 이해해야 함|
|**인코딩 개념**|한글 JSON, CSV 저장 시 UTF-8 문제를 자주 만남|
|**날짜와 시간 개념**|`event_time`, `created_at`, `processed_at`, UTC, KST, Airflow schedule 이해에 필요|
|**로그 개념**|파이프라인 실행 결과, 에러 추적, 운영 기록 이해에 필요|
|**예외 처리**|`try-except`, 검증 실패, Dead Letter 처리 이해에 필요|
|**데이터 검증 개념**|필수값, 타입, 중복, 누락, 범위 오류를 판단해야 함|
|**데이터 품질 개념**|Freshness, completeness, validity, duplicate 이해에 필요|
|**데이터 파티션 개념**|`date=2026-07-21/hour=09/` 구조 이해에 필요|
|**환경 변수 개념**|`.env`, DB 접속정보, API 키 관리 이해에 필요|
|**테스트 개념**|코드가 맞는지 확인하는 기본 사고 필요|
|**README 작성법**|포트폴리오에서 “무엇을 만들었는지” 설명해야 함|

### 도구별로 정리
|도구|사전 수준|수업에서의 역할|
|---|---|---|
|VSCode|기본 사용 가능|코드 작성, 터미널 실행|
|WSL2/Linux|기본 명령어 사용|Python, Git, 서버 실행|
|Git|add/commit/push 정도|단계별 실습 저장|
|GitHub|repo, branch, PR 이해|산출물 제출과 포트폴리오|
|DBeaver|DB 접속, 테이블 조회|DB 데이터 확인|
|Notion|문서 정리 수준|팀 문서, 회의록, 설계 정리|
|Jira|이슈, 스프린트, 칸반 정도|실무 협업 경험|
|Figma|화면 구조 확인 정도|대시보드/관리자 화면 이해|
|Jupyter Notebook|셀 실행, DataFrame 보기|데이터 탐색과 간단 분석|
|Postman 또는 Thunder Client|API 요청 테스트|FastAPI/Django API 확인|
|Docker Desktop|후반부 기초|컨테이너 배포 실습|
|Airflow UI|3단계 이후|DAG 실행 상태 확인|
|Grafana/Prometheus|후반부|운영 모니터링 이해|
DBeaver 사용법보다 먼저 DB, 테이블, SQL, 관계를 이해하는 것이 더 중요

학생들이 수업에 들어오기 전에 이 정도는 알고 있으면 좋은것
```
Python으로 리스트와 딕셔너리를 다룰 수 있다.
JSON 파일을 읽고 쓸 수 있다.
터미널에서 폴더를 이동하고 파일을 만들 수 있다.
Git으로 commit과 push를 할 수 있다.
API가 데이터를 주고받는 구조라는 것을 안다.
DB가 테이블 형태로 데이터를 저장한다는 것을 안다.
SQL SELECT문을 간단히 실행할 수 있다.
README.md에 실습 내용을 정리할 수 있다.
```

### 수업 중 실습을 하면서 익히면
|항목|수업 중 익히면 되는 이유|
|---|---|
|Pandas|Staging, Mart 만들 때 반복 사용하면서 익힘|
|Parquet|처음부터 깊게 몰라도 Raw와 Staging 차이를 배우며 이해 가능|
|Pydantic|FastAPI 데이터 검증 실습에서 자연스럽게 익힘|
|Django ORM|DB 모델과 관리자 화면 실습에서 익힘|
|FastAPI|Collector 실습에서 익힘|
|Airflow|3단계 파이프라인 자동화에서 익힘|
|Docker|후반 배포 단계에서 익힘|
|Redis/Celery|비동기 작업 단계에서 익힘|
|WebSocket|실시간 대시보드 단계에서 익힘|
|Prometheus/Grafana|운영 모니터링 단계에서 익힘|
|Kafka/Spark|후반 확장 개념으로 다루면 됨|
|dbt|DataOps/품질 관리 단계에서 다루면 됨|
|Vector DB/RAG|AI 서비스 연결 단계에서 다루면 됨|

---
특히 이 과정은 단순히 코드를 따라 치는 수업이 아니라, **데이터가 들어와서 검증되고, 정리되고, 목적별 데이터셋으로 바뀌고, 자동 실행되고, 품질 리포트까지 남는 흐름**을 이해하는 수업입니다. Pipeline은 Raw 읽기, 검증, Staging 저장, Mart 생성, Report 생성으로 이어지는 전체 처리 흐름을 배웁니다.

```
Python 기초는 배웠지만 실무 프로젝트 경험이 부족한 학생
백엔드와 데이터 엔지니어링 사이의 흐름을 배우고 싶은 학생
AI 모델 자체보다 AI가 사용할 데이터를 어떻게 만드는지 배우고 싶은 학생
포트폴리오로 데이터 플랫폼 프로젝트를 만들고 싶은 학생
주니어 데이터 엔지니어, 백엔드 개발자, AI 서비스 개발자를 목표로 하는 학생
```

이수업을 듣기전 준비가 필요한 상태
```
Python 변수, 함수, 파일 경로도 아직 어려운 학생
터미널 사용이 거의 처음인 학생
JSON과 테이블 구조를 전혀 모르는 학생
GitHub 사용 경험이 없는 학생
복잡한 폴더 구조를 보면 바로 포기하는 학생
```

```
초반에는 Python, JSON, Git, 터미널, 데이터 구조를 충분히 설명한다.
중반부터 Raw → Staging → Mart 흐름을 반복 실습한다.
후반에는 Airflow, Backfill, Quality Report, AI Training Dataset으로 확장한다.
모든 개념을 중기청 프로젝트 하나에만 묶지 말고 쇼핑몰, 병원, 금융, 교육, AI 서비스 로그 같은 범용 예시로 먼저 설명한다.
그 후 실습 프로젝트에 적용한다.
```

---
## 0. 개발 환경 준비
```
VSCode
WSL2
Python 가상환경
Git
GitHub
DBeaver
Postman 또는 Thunder Client
Jupyter Notebook
```

## 1. Python 기초 복습

```
변수
조건문
반복문
함수
클래스 기초
list
dict
파일 읽기/쓰기
모듈과 import
requirements.txt
```

## 2. 데이터 형식 이해

```
JSON
JSONL
CSV
Parquet 개념
행과 열
컬럼과 레코드
2차원 데이터
중첩 JSON
```

## 3. 터미널과 파일 구조

```
pwd
ls
cd
mkdir
touch
cat
tree
rm
cp
mv
상대경로
절대경로
```

## 4. Git과 GitHub

```
clone
status
add
commit
push
pull
branch
switch
merge 개념
pull request 개념
README 작성
```

## 5. API 기본

```
HTTP
GET
POST
Request
Response
Status Code
JSON Body
API Endpoint
FastAPI와 Django의 기본 차이
```

## 6. DB와 SQL 기본

```
Database
Table
Column
Row
Primary Key
Foreign Key
SELECT
WHERE
ORDER BY
GROUP BY
JOIN
DBeaver로 테이블 조회
```

## 7. 데이터 플랫폼 기초 사고

```
Raw 데이터란 무엇인가?
Staging 데이터란 무엇인가?
Mart 데이터란 무엇인가?
데이터 검증은 왜 필요한가?
데이터 품질은 왜 중요한가?
로그와 실행 이력은 왜 필요한가?
AI는 왜 Raw 데이터를 그대로 학습하지 않는가?
```

## 8. 협업 도구 기초

```
Notion
→ 문서 정리, 회의록, 일정 공유

Jira
→ 이슈 관리, 작업 상태 관리, 스프린트 경험

Figma
→ 화면 구조와 대시보드 기획 이해

GitHub
→ 코드 관리, 브랜치, PR, README 관리
```

---

# 최종 정리

AI 네이티브 데이터 플랫폼 엔지니어 과정을 위해 사전에 꼭 알아야 하는 것은 아래 7가지입니다.
```
1. Python 기본 문법과 자료구조
2. JSON, CSV, Parquet 같은 데이터 형식
3. 파일 읽기/쓰기와 폴더 구조
4. Linux 터미널 명령어
5. Git/GitHub 기본 사용
6. API로 데이터를 주고받는 구조
7. DB, SQL, 테이블 구조
```

그리고 수업 중 자연스럽게 익히면 좋은 것은 아래입니다.
```
FastAPI
Django
Pandas
Pydantic
Airflow
Docker
Redis/Celery
WebSocket
Prometheus/Grafana
Kafka/Spark
dbt(Data Build Tool)
RAG/Vector DB
Jira/Notion/Figma 협업 흐름
```