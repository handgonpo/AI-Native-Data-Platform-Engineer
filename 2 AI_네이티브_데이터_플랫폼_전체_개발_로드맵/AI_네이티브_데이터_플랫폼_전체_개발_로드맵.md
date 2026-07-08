
> 실습 예제 도메인: 산업안전 관제플랫폼  
> 본 문서는 이미지 커리큘럼의 7개 이론 교과목과 3개 프로젝트 구성을 기준으로, 실제 수업에서 단계별로 개발을 진행할 수 있도록 재구성한 전체 개발 과정이다.  
> 산업안전 관제플랫폼 개발 흐름을 실습 기반으로 과정의 핵심이 단순 관제 시스템 개발이 아니라 AI 서비스가 신뢰할 수 있는 데이터를 수집·정제·검증·검색·운영하는 데이터 플랫폼 구축으로 로드맵을 기획하였다.

---
# 커리큐럼 전체 구성
---

![[AI 네이티브 데이터 플랫폼 엔지니어 과정/0 커리큐럼/images/커리큐럼.png]]

| 구분          | 구성                              |   시수 |
| ----------- | ------------------------------- | ---: |
| 사전 단계       | 0단계: 프로젝트 기준선 정리                |  16h |
| 이론/실습 교과목 1 | 1단계: AI 서비스와 데이터 플랫폼 아키텍처       |  24h |
| 이론/실습 교과목 2 | 2단계: AI 데이터 수집과 레이크하우스 설계       |  48h |
| 이론/실습 교과목 3 | 3단계: AI 워크로드를 위한 데이터 파이프라인 자동화  |  56h |
| 중간 프로젝트     | AI 서비스 로그 수집 및 학습 데이터셋 생성 파이프라인 |  92h |
| 이론/실습 교과목 4 | 4단계: 대용량 로그와 실시간 이벤트 스트리밍       |  56h |
| 이론/실습 교과목 5 | 5단계: AI 데이터 품질, 계보, 거버넌스        |  64h |
| 이론/실습 교과목 6 | 6단계: RAG와 벡터 데이터 파이프라인          |  56h |
| 최종 프로젝트     | RAG 서비스용 문서 데이터 플랫폼 구축 프로젝트     |  92h |
| 이론/실습 교과목 7 | 7단계: AI 서비스 피드백 데이터와 DataOps 운영 |  40h |
| 기업 프로젝트     | AI 서비스 데이터 품질 및 피드백 운영 플랫폼 프로젝트 | 184h |

> 이론 교과목은 360시간, 프로젝트는 368시간으로 구성 
> 0단계 프로젝트 기준선 정리 16시간은 본격적인 1~7단계 개발 전에 추가되는 사전 기준선 정리 단계이다.
> 전체 수업 시간표가 별도 기관 기준으로 조정될 경우, 각 교과목 내부 블록의 시수는 비율에 맞게 조정할 수 있다.

---

## 0. 목적

1. 위의 이미지 커리큘럼의 **교과목 순서, 시수, 프로젝트 구성**에 맞춰 전체 개발 과정
2. 수업 실습 예제는 산업안전 관제플랫폼 및 기타 예제
3. 산업안전 관제 플랫폼은 최소 껍데기 프로젝트에서 시작해, 단계별로 AI 네이티브 데이터 플랫폼을 완성할 수 있도록 한다.
4. 단순한 웹 대시보드 구현이 아니라, 데이터 계약, 레이크하우스, 파이프라인 자동화, 실시간 스트리밍, 품질 관리, RAG, 피드백 데이터, DataOps까지 연결된 실무형 로드맵으로 사용한다.

> 추가 기준: 본격적인 1단계 개발 전에 0단계 프로젝트 기준선 정리를 통해 프로젝트 목적, 데이터 소스, 이벤트 후보, 데이터 흐름, 시스템 경계, 산출물 기준을 먼저 맞춘다.

---

## 1. 전체 과정 개요

과정명
```text
AI 네이티브 데이터 플랫폼 엔지니어 과정
```

실습 프로젝트명
```text
산업안전 관제플랫폼 기반 AI 데이터 플랫폼 구축 프로젝트 및 기타 예제
```

과정의 핵심 질문
```text
AI 서비스가 신뢰할 수 있는 판단을 하려면, 
데이터는 어떻게 수집되고, 검증되고, 저장되고, 처리되고, 추적되고, 운영되어야 하는가?
```

이 과정의 답은 다음과 같다.
```text
이 과정은 단순히 AI 모델을 만드는 과정이 아니다.  
현업에서 AI 서비스를 운영할 때 가장 중요한 질문은 다음과 같다.

- 데이터가 제대로 들어오고 있는가?
- 중복 데이터와 오류 데이터는 어떻게 처리할 것인가?
- 늦게 도착한 데이터는 어떻게 감지할 것인가?
- 파이프라인을 다시 실행해도 결과가 안전한가?
- AI가 사용하는 데이터의 품질을 어떻게 검증할 것인가?
- 데이터가 어디서 생성되어 어디까지 흘러갔는지 추적할 수 있는가?
- 서비스 운영 중 데이터 흐름이 끊기거나 지연되면 어떻게 알 수 있는가?


이 과정의 답은 다음과 같다.

  AI 서비스는 모델만으로 운영되지 않는다.

  AI가 신뢰할 수 있는 판단을 하려면
  데이터 수집 구조, 검증 체계, 오류 처리 방식, 중복 방지, 재처리 가능성,
  데이터 품질 관리, 데이터 계보, 모니터링 체계가 함께 설계되어야 한다.

즉, AI 네이티브 데이터 플랫폼은
데이터가 들어오는 순간부터 AI가 판단하고 서비스가 운영되는 순간까지
전체 데이터 흐름을 안정적으로 관리하는 구조이다.


산업안전 관제플랫폼은 이 질문을 설명하기 위한 실습 도메인이다.  
센서 데이터, 전력 데이터, 작업자 위치 데이터, 알람 데이터, 문서 데이터, AI 추론 데이터, 
사용자 피드백 데이터를 모두 다루기 때문에 다음과 같은 현업형 데이터 엔지니어링 문제를 
자연스럽게 경험할 수 있다.


- Raw 데이터는 어떻게 저장할 것인가?
- Staging 데이터는 어떻게 검증할 것인가?
- Mart 데이터는 어떤 목적에 맞게 만들 것인가?
- AI 학습 데이터셋은 어떻게 구성할 것인가?
- RAG 문서 데이터는 어떻게 검색 가능하게 만들 것인가?
- 피드백 데이터는 어떻게 다시 서비스 개선에 활용할 것인가?
- 운영 중 데이터 품질과 흐름은 어떻게 관찰할 것인가?


따라서 이 과정의 핵심은 다음 한 문장으로 정리할 수 있다.

AI는 모델만으로 움직이지 않는다.
AI를 움직이게 하는 것은 신뢰 가능한 데이터 흐름과 운영 가능한 데이터 플랫폼이다.
```

---
## 2. 전체 과정에서 백엔드 AI 프레임 워크인 Django/DRF/FastAPI의 역할
| 단계                      | 핵심 목표                                       | Django/DRF<br>필요 정도 | FastAPI 필요 정도 | 실제 수업에서 다룰 범위                                                                                                                                                                                                       |
| ----------------------- | ------------------------------------------- | ------------------: | ------------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0단계                     | 프로젝트 기준선 정리                              |                  낮음 |            낮음 | Django/DRF/FastAPI를 구현하지 않는다. <br><br>프로젝트 목적, 데이터 소스, 도메인 이벤트, 데이터 흐름, 시스템 경계, 산출물 기준을 문서와 샘플 JSON으로 정리한다. <br><br>이 단계의 산출물이 1단계 아키텍처와 2단계 데이터 수집 설계의 기준이 된다. |
| 1단계                   . | AI 서비스와 <br>데이터 플랫폼 아키텍처 이해                 |                  낮음 |            낮음 | Django/FastAPI를 깊게 다루기보다 <br>전체 구조에서 각각 어디에 위치하는지만 설명한다. <br><br>Django는 화면과 백오피스, DRF는 서비스 API, FastAPI는 데이터 수집·AI 추론 API 역할로 소개한다.                                                                                |
| 2단계                     | 데이터 수집과 레이크하우스 설계                           |                  중간 |            높음 | 센서 데이터, 전력 데이터, 작업자 위치 <br>데이터를 받기 위한 FastAPI Collector가 필요하다. <br><br>Django는 아직 핵심은 아니지만, 나중에 화면과 연결될 데이터 구조를 이해하기 <br>위해 모델/API 개념을 간단히 연결한다.                                                                    |
| 3단계                     | Airflow 기반 <br>데이터 파이프라인 자동화                |                  낮음 | 낮음<br>~<br>중간 | 핵심은 Django/FastAPI가 아니라 <br>Raw → Staging → Mart → Report 자동화이다. <br><br>다만 Airflow가 처리할 데이터가 2단계 FastAPI Collector에서 만들어졌다는 흐름은 설명해야 한다.                                                                           |
| 4단계                     | Kafka/Spark <br>실시간 이벤트 스트리밍 및 AI 판단 연결   . |                  높음 |            높음 | 실제 관제플랫폼 구현에서 가장 연결이 많이 필요한 단계이다. <br><br>FastAPI는 실시간 데이터 수집 또는 AI 추론 API 역할을 하고, Django/DRF는 판단 결과를 저장하고 화면에 제공한다.<br><br>HTML/CSS/JavaScript로 만든 관제 화면과 연결하려면 Django View, DRF API, <br>필요 시 WebSocket 구조가 필요하다. |
| 5단계                     | 데이터 품질,<br>계보, 거버넌스                         |                  중간 | 낮음<br>~<br>중간 | 데이터 품질 결과, 검증 오류, 처리 이력, 데이터 계보를 관리 화면에서 확인하려면 Django Admin 또는 Django 화면이 유용하다. <br><br>FastAPI는 품질 점검 API나 외부 서비스 연동 정도로 제한된다.                                                                                     |
| 6단계                     | RAG와 벡터 <br>데이터 파이프라인                       |                  중간 |            높음 | RAG 검색, 임베딩, 벡터 검색, 문서 질의 API는 FastAPI로 구성하기 좋다. <br><br>Django는 사용자가 질문을 입력하고 결과를 확인하는 화면 또는 백오피스 역할을 한다. <br><br>프레임워크 자체보다 “문서 데이터가 서비스 API로 연결되는 흐름”을 중심으로 가르친다.                                                |
| 7단계                     | 피드백 데이터와 DataOps <br>운영                     |                  높음 |            중간 | 사용자 피드백, AI 응답 로그, 운영 지표, 품질 리포트를 화면에서 확인하려면 Django/DRF가 필요하다. <br><br>FastAPI는 AI 서비스 로그 수집, <br>피드백 수신, 추론 결과 저장 API로 <br>활용할 수 있다. <br><br>최종적으로 운영 가능한 데이터 플랫폼 구조를 완성하는 단계이다.                                   |

---
## 3. 관제플랫폼을 수업 예제로 사용

#### 도메인 개요

관제플랫폼은 산업현장의 다음 데이터를 수집하고 분석하는 예제 플랫폼으로 사용한다.
```text
주요 데이터
1. 유해가스 센서 데이터
2. 전력 사용량 데이터
3. 작업자 위치 데이터
4. 위험구역 및 지오펜스 데이터
5. 임계치 기준 데이터
6. 알람 발생 및 처리 데이터
7. AI 이상탐지 결과 데이터
8. RAG 대응 매뉴얼 문서 데이터
9. 사용자 확인, 조치, 피드백 데이터
10. 서비스 호출 로그와 오류 로그
11. 데이터 품질 점검 결과 데이터
12. 파이프라인 실행 이력과 처리 상태 데이터
13. AI 추론 요청, 응답, 실패 로그 데이터
14. 재학습 후보 데이터셋
```
이 데이터들은 단순히 화면에 보여주기 위한 데이터가 아니다.  
AI가 판단하고, 서비스가 운영되고, 운영 결과가 다시 데이터로 쌓이는 전체 흐름을 학습하기 위한 데이터이다.

#### 수업에서의 핵심 관점

관제 플랫폼을 “산업안전 대시보드”로만 보면 수업 범위가 좁아진다. 이 과정에서는 관제플랫폼을 다음과 같이 확장해서 본다.

| 일반적인 이해          | 본 과정에서의 이해                                             |
| ---------------- | ------------------------------------------------------ |
| 센서값을 보여주는 대시보드   | AI 서비스가 사용할 실시간 데이터 플랫폼                                |
| 알람을 화면에 표시하는 시스템 | 위험 판단 결과와 운영 피드백을 데이터로 축적하는 시스템                        |
| 단순 로그 저장         | AI 서비스 품질 개선을 위한 관찰 데이터 수집                             |
| 문서 검색 기능         | RAG를 위한 문서 수집, 정제, 임베딩, 검색 파이프라인                       |
| DB 테이블 설계        | Raw, Staging, Mart, Feature Dataset, Vector Dataset 설계 |
| API 개발           | 데이터 수집, AI 추론, 피드백 수집을 연결하는 서비스 입구                     |
| 배치 작업            | Airflow 기반 데이터 검증, 집계, 리포트 자동화                         |
| 실시간 처리           | Kafka/Spark 기반 이벤트 스트리밍과 실시간 위험 판단                     |
| 오류 처리            | Dead Letter, Validation Error, Retry, Checkpoint 설계    |
| 운영 모니터링          | 데이터 품질, 지연, 흐름 중단, SLA 위반 탐지                           |
| 서비스 개선           | 사용자 피드백과 운영 로그를 재학습 후보 데이터로 전환                         |

#### 최종적으로 완성할 플랫폼 흐름

```text
Sensor Simulator / Worker Location Generator / AI Service Log Generator / Document Loader
        ↓
FastAPI Collector / Log Collector / Document Ingestion API
        ↓
Data Contract / Schema Version / Validation Rule
        ↓
Raw Zone / Raw Tables / Raw Files
        ↓
Dead Letter / Validation Error Store / Retry Target
        ↓
Staging Validation / Schema Check / Dedup / Late Event Handling
        ↓
Checkpoint / Marker / Idempotent Processing
        ↓
Airflow Batch Pipeline / Kafka Streaming Pipeline
        ↓
Mart / Feature Dataset / Training Dataset / RAG Metadata Dataset
        ↓
Risk Engine / AI Inference API / RAG Search API / Feedback Collector
        ↓
Django / DRF / WebSocket / Dashboard / Admin / Report View
        ↓
Alarm Service / Data Quality Report / Lineage Report / DataOps Monitoring
        ↓
Prometheus / Grafana / CI/CD / 운영 리포트 / 재학습 후보 데이터셋
```

이 흐름에서 각 구성 요소의 의미는 다음과 같다.

| 구성 요소                | 수업에서 배우는 핵심                              |
| -------------------- | ---------------------------------------- |
| Sensor Simulator     | 실제 장비가 없어도 실시간 데이터를 생성하는 방법              |
| FastAPI Collector    | 외부 데이터를 API로 수집하는 방법                     |
| Data Contract        | 어떤 데이터가 들어와야 하는지 정의하는 방법                 |
| Raw Zone             | 원본 데이터를 손상하지 않고 저장하는 방법                  |
| Dead Letter          | 처리할 수 없는 데이터를 버리지 않고 추적하는 방법             |
| Staging Validation   | Raw 데이터를 분석 가능한 구조로 정제하는 방법              |
| Dedup                | 중복 데이터를 제거하는 방법                          |
| Late Event Handling  | 늦게 도착한 데이터를 감지하고 처리하는 방법                 |
| Checkpoint / Marker  | 파이프라인이 어디까지 처리했는지 기록하는 방법                |
| Airflow              | 배치 파이프라인을 자동 실행하고 관리하는 방법                |
| Kafka / Spark        | 실시간 이벤트 흐름을 처리하는 방법                      |
| Mart                 | 대시보드, AI, 리포트 목적에 맞는 데이터를 만드는 방법         |
| Feature Dataset      | AI 모델이 사용할 수 있는 입력 데이터를 만드는 방법           |
| RAG Metadata Dataset | 문서 검색과 출처 추적을 위한 메타데이터를 만드는 방법           |
| Risk Engine          | 센서값, 임계치, 위치, AI 판단 결과를 결합해 위험도를 계산하는 방법 |
| Django / DRF         | 처리 결과를 화면과 API로 제공하는 방법                  |
| WebSocket            | 실시간 알람과 상태 변화를 화면에 반영하는 방법               |
| Feedback Collector   | 사용자 확인, 조치, 평가 데이터를 다시 수집하는 방법           |
| Data Quality Report  | 데이터가 정상적으로 들어오고 처리되는지 점검하는 방법            |
| Lineage Report       | 데이터가 어디서 와서 어디로 이동했는지 추적하는 방법            |
| Prometheus / Grafana | 서비스와 데이터 파이프라인의 운영 상태를 관찰하는 방법           |
| 재학습 후보 데이터셋          | 운영 중 쌓인 데이터를 AI 개선에 다시 활용하는 방법           |

실습 예제를 통해 만들게 될 관제플랫폼을 만들면서 다음 질문에 답할 수 있어야 한다.
```
데이터는 어디에서 발생하는가?
데이터는 어떤 계약에 따라 수집되는가?
잘못된 데이터는 어떻게 분리하고 추적하는가?
중복 데이터는 어떻게 제거하는가?
늦게 도착한 데이터는 어떻게 감지하는가?
파이프라인을 다시 실행해도 같은 결과가 나오는가?
AI가 사용하는 데이터셋은 어떻게 만들어지는가?
RAG 검색에 사용할 문서는 어떻게 수집, 분할, 임베딩되는가?
AI의 판단 결과는 어떻게 저장되고 화면에 표시되는가?
사용자의 피드백은 어떻게 다시 데이터로 쌓이는가?
운영 중 데이터 흐름이 끊기면 어떻게 알 수 있는가?
데이터 품질과 계보는 어떻게 추적하는가?
```

따라서 이 과정에서 관제플랫폼은 다음을 모두 포함하는 종합 실습 프로젝트이다.
```
데이터 수집
→ 데이터 계약
→ Raw 저장
→ 오류 데이터 관리
→ Staging 검증
→ Mart 생성
→ 실시간 이벤트 처리
→ AI 추론
→ RAG 검색
→ 대시보드 연결
→ 사용자 피드백 수집
→ 데이터 품질 점검
→ 운영 모니터링
→ 재학습 후보 데이터 생성
```

---

## 4. 권장 기술 스택

이 과정은 웹 개발 과정이 아니라 **AI 네이티브 데이터 플랫폼 엔지니어 과정**이다.  
따라서 기술 스택의 중심은 화면 개발이 아니라 다음 흐름을 이해하고 구현하는 데 있다.

```
데이터 발생 
→ 데이터 수집 
→ Raw 저장 
→ Staging 검증 
→ Mart 생성 
→ AI/RAG 연결 
→ 대시보드 확인 
→ 피드백 수집 
→ 품질 점검 
→ 운영 모니터링
```

다만 수강생이 데이터가 실제 서비스에서 어떻게 사용되는지 이해하려면,  
산업안전 관제플랫폼의 HTML, CSS, JavaScript 화면과 데이터를 연결하는 경험이 필요하다.

따라서 이 과정의 기술 스택은 다음 기준으로 구성한다.

```
1. 데이터 흐름을 이해하기 위한 기술 
2. 데이터 처리를 자동화하기 위한 기술 
3. AI/RAG 서비스와 연결하기 위한 기술 
4. 처리 결과를 화면에서 확인하기 위한 최소 백엔드 기술 
5. 협업과 산출물 관리를 위한 도구 
6. 운영 환경을 이해하기 위한 배포/모니터링 기술
```

| 영역                | 권장 기술                                          | 수업 적용 방식                                                                                            |
| ----------------- | ---------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| 운영 환경             | Windows + WSL2 Ubuntu                          | 수업 기본 개발 환경. Linux 명령어, Python 실행, Git, Docker 실습 환경으로 사용                                           |
| 기본 명령어            | Linux Command, Bash                            | `cd`, `ls`, `mkdir`, `cat`, `touch`, `tree`, `grep`, `find`, `cp`, `mv`, `rm`, `chmod`, `curl` 등 실습 |
| 개발 도구             | VSCode, WSL Extension, Terminal                | WSL2 환경에서 코드 작성, 터미널 실행, Git 관리                                                                     |
| Python 기본         | Python, venv, pip, requirements.txt            | 데이터 처리 코드, API 서버, 파이프라인 코드 작성의 기본                                                                  |
| Python <br>데이터 처리 | pandas, pyarrow, json, csv, pathlib            | JSON, JSONL, CSV, Parquet 읽기/쓰기와 데이터 변환                                                             |
| 데이터 계약            | JSON Schema, Pydantic                          | 수집 데이터의 필수 필드, 타입, 스키마 버전 검증                                                                        |
| 백엔드 API           | FastAPI                                        | 센서 데이터 수집 API, AI 추론 API, RAG 검색 API, 피드백 수집 API                                                    |
| 서비스 백엔드           | Django, DRF                                    | 관제 화면, 관리자 화면, 알람 API, Mart 조회 API, 피드백 관리 API                                                      |
| 데이터베이스            | PostgreSQL                                     | 기준정보, 알람, 피드백, 사용자 조치, 메타데이터 저장                                                                     |
| DB 관리 도구          | DBeaver                                        | 테이블 조회, SQL 실행, 데이터 확인                                                                              |
| 파일 기반 <br>데이터 레이크 | Local File System → MinIO/S3 호환 구조             | Raw, Staging, Mart 데이터를 JSONL, CSV, Parquet 형태로 저장                                                  |
| 레이크하우스 실습         | Parquet, DuckDB, Spark SQL 선택                  | 경량 분석은 DuckDB, 대용량/분산 개념은 Spark SQL로 설명                                                             |
| 워크플로 <br>자동화      | Airflow                                        | Raw → Staging → Mart → Report 자동화, Backfill, 재처리                                                    |
| 실시간 <br>스트리밍      | Kafka, Spark Structured Streaming              | 실시간 센서 이벤트, 중복 제거, 지연 이벤트, Window 처리                                                                |
| 비동기 처리            | Celery, Redis                                  | AI 추론 후처리, 알람 생성, 문서 임베딩, 장시간 작업 처리                                                                 |
| 데이터 품질            | dbt Test, SQL Test, Great Expectations 선택      | Null 검사, 중복 검사, 범위 검사, Freshness 검사, 품질 리포트                                                         |
| 데이터 계보            | dbt Docs, OpenLineage 개념, Lineage Report       | 데이터가 Raw에서 Mart까지 어떻게 이동했는지 추적                                                                      |
| RAG               | LangChain 또는 LlamaIndex, Chroma/FAISS/pgvector | 문서 수집, chunking, embedding, vector search, 출처 표시                                                    |
| AI 추론             | scikit-learn, 간단한 이상탐지 모델                      | 유해가스, 전력 사용량, 작업자 위치 기반 위험 판단 실습                                                                    |
| 대시보드 화면           | HTML, CSS, JavaScript, Django Templates        | React 없이도 관제 화면 구성 및 데이터 연결                                                                         |
| 시각화               | Chart.js, Leaflet                              | 센서 그래프, 알람 현황, 작업자 위치, 위험구역 지도 표시                                                                   |
| 실시간 통신            | Django Channels, WebSocket                     | 실시간 알람, 센서 상태, 작업자 위치 변화 표시                                                                         |
| API 테스트           | curl, Postman 또는 Swagger UI                    | FastAPI/DRF API 요청, 응답 확인                                                                           |
| 테스트               | pytest, Django Test, 간단한 API 테스트               | 데이터 검증 함수, API 응답, 파이프라인 결과 검증                                                                      |
| 코드 품질             | ruff, black 선택                                 | Python 코드 포맷팅과 기본 품질 관리                                                                             |
| 환경 변수             | `.env`, python-dotenv                          | DB 접속정보, API Key, Secret 관리 기초                                                                      |
| 컨테이너              | Docker, Docker Compose                         | PostgreSQL, Redis, FastAPI, Django, Airflow, Kafka 실행                                               |
| Kubernetes <br>실습 | kind 또는 minikube                               | 후반부에서 운영 환경 개념 확인용                                                                                  |
| CI/CD             | GitHub Actions                                 | 테스트 자동 실행, 빌드 확인, 브랜치별 검증                                                                           |
| 모니터링              | Prometheus, Grafana                            | 수집 지연, 처리 실패, API 상태, 품질 실패, SLA 관찰                                                                 |
| 로그 관리             | Python logging, Django logging                 | 오류 로그, 서비스 호출 로그, AI 추론 로그 저장                                                                       |
| 협업 저장소            | Git, GitHub                                    | 브랜치, 커밋, PR, README, 코드 리뷰, 실습 산출물 관리                                                               |
| 이슈 관리             | Jira 또는 GitHub Issues                          | 기능 단위 작업 관리, 버그 관리, 스프린트 실습                                                                         |
| 문서 관리             | Notion, Obsidian                               | 수업 노트, 개념 정리, 실습 기록, 회고 작성                                                                          |
| 화면 설계             | Figma                                          | 관제 대시보드 화면 구조, 데이터 표시 위치, 사용자 흐름 설계                                                                 |
| 커뮤니케이션            | Discord                                        | 공지, 질문, 코드 공유, 팀별 소통                                                                                |

#### 반드시 필요한 핵심 기술
모든 기술을 깊게 배우는 것이 목적은 아니다.  
이 과정에서 반드시 필요한 핵심 기술은 다음과 같다.

| 구분                        | 반드시 필요한 이유                                |
| ------------------------- | ----------------------------------------- |
| WSL2 + Linux 명령어          | 실제 데이터 엔지니어링 환경은 터미널 기반 작업이 많기 때문         |
| Python                    | 데이터 처리, API, 파이프라인, AI/RAG 실습의 공통 언어      |
| JSON, CSV, JSONL, Parquet | 데이터 수집과 저장 형식을 이해하기 위해 필요                 |
| FastAPI                   | 외부 데이터 수집, AI 추론, RAG API를 만들기 위해 필요      |
| Django/DRF                | 관제 화면과 백오피스에서 데이터를 조회하고 관리하기 위해 필요        |
| PostgreSQL                | 서비스 데이터, 기준정보, 알람, 피드백 저장을 위해 필요          |
| Airflow                   | 데이터 파이프라인 자동화와 재처리를 이해하기 위해 필요            |
| Kafka/Spark               | 실시간 데이터 흐름, Window, 지연 데이터 처리를 이해하기 위해 필요 |
| dbt 또는 SQL Test           | 데이터 품질 검증을 체계적으로 하기 위해 필요                 |
| Docker Compose            | 여러 서비스를 함께 실행하는 환경을 이해하기 위해 필요            |
| Git/GitHub                | 단계별 실습 코드 관리와 협업을 위해 필요                   |
| Prometheus/Grafana        | 운영 중 데이터 흐름과 서비스 상태를 관찰하기 위해 필요           |

#### 백엔드 기술을 포함해야 하는 이유
이 과정은 데이터 과정이지만, 백엔드 기술이 전혀 없으면 수강생이 다음 흐름을 이해하기 어렵다.

```
센서 데이터가 어디로 들어오는가?
수집된 데이터가 어디에 저장되는가?
AI 판단 결과가 어떻게 화면에 표시되는가?
사용자 피드백은 어떻게 다시 데이터로 저장되는가?
RAG 검색 결과는 어떤 API를 통해 화면에 전달되는가?
```

따라서 Django, DRF, FastAPI는 웹 개발 자체를 깊게 가르치기 위한 목적이 아니라  
**데이터 플랫폼과 서비스 화면을 연결하기 위한 최소 백엔드 기술**로 사용한다.

| 기술               | 이 과정에서의 역할                                   | 깊이    |
| ---------------- | -------------------------------------------- | ----- |
| FastAPI          | 센서 수집 API, AI 추론 API, RAG 검색 API, 피드백 수집 API | 중간    |
| Django           | 관제 화면, 관리자 화면, 결과 확인 화면                      | 중간    |
| DRF              | 대시보드 데이터 API, 알람 API, 피드백 API                | 중간    |
| Django Templates | HTML/CSS/JavaScript 화면 연결                    | 낮음~중간 |
| WebSocket        | 실시간 알람과 센서 상태 표시                             | 중간    |
| Celery/Redis     | 비동기 작업 처리                                    | 낮음~중간 |

#### 협업 도구 적용 방식
이 과정에서는 협업 도구도 단순 소개가 아니라 실습 산출물 관리에 사용한다.

| 도구            | 수업 적용 방식                                    |
| ------------- | ------------------------------------------- |
| GitHub        | 브랜치별 실습 코드 관리, Pull Request, README 작성      |
| GitHub Issues | 간단한 기능 요청, 버그, 실습 체크리스트 관리                  |
| Jira          | 실제 프로젝트처럼 Epic, Story, Task, Bug를 나누어 작업 관리 |
| Figma         | 관제 대시보드 화면 설계, 데이터 표시 영역 정의                 |
| Notion        | 팀별 산출물 정리, 회의록, 요구사항 정리                     |
| Obsidian      | 개인 학습 노트, 개념 정리, 단계별 회고 작성                  |
| Discord       | 질문, 공지, 코드 공유, 팀별 커뮤니케이션                    |
| DBeaver       | DB 테이블 확인, SQL 실행, Mart 결과 확인               |
| VSCode        | WSL2 기반 코드 작성과 터미널 실행                       |

#### Jira를 수업에 적용하는 방식
Jira는 프로젝트의 진행 흐름을 이해할수 있을 정도로만 사용한다.

| Jira 개념 | 수업 적용 예시                                    |
| ------- | ------------------------------------------- |
| Epic    | 2단계 데이터 수집, 3단계 파이프라인, 4단계 실시간 처리 같은 큰 단위   |
| Story   | “센서 데이터를 FastAPI로 수집한다” 같은 사용자 관점 기능        |
| Task    | JSON Schema 작성, Raw 저장 함수 작성, Mart 생성 코드 작성 |
| Bug     | 중복 데이터 처리 오류, API 응답 오류, Airflow DAG 실패     |
| Sprint  | 1주 또는 단계별 실습 기간                             |
| Board   | To Do, In Progress, Review, Done 상태 관리      |
예를 들어 2단계에서는 다음과 같이 사용할 수 있다.
```
Epic: 데이터 수집과 레이크하우스 설계

Story:
- 유해가스 센서 데이터를 수집할 수 있다.
- 수집된 데이터를 Raw Zone에 JSONL로 저장할 수 있다.
- 잘못된 데이터는 Dead Letter로 분리할 수 있다.

Task:
- gas_event.schema.json 작성
- FastAPI collect/gas API 작성
- Raw JSONL 저장 함수 작성
- Validation Error 저장 경로 생성
```

#### Figma를 수업에 적용하는 방식
이 과정에서 시스템 구조, 데이터 흐름, API 연결, 파이프라인 구조처럼 정확한 기술 문서가 필요한 내용은 **Mermaid 다이어그램**을 우선 사용한다.

Mermaid는 Markdown 문서 안에 직접 작성할 수 있고, GitHub에서 바로 확인할 수 있으며, 코드처럼 변경 이력을 관리할 수 있다. 따라서 데이터 플랫폼 수업에서는 Mermaid가 기술 구조를 문서화하는 기본 도구가 된다.

Figma는 기술 다이어그램을 처음부터 손으로 그리는 도구로 사용하지 않는다.  
대신 Mermaid로 정리한 구조를 바탕으로, 팀 아이디어를 정리하거나 최종 발표용으로 시각화할 때 보조 도구로 사용한다.

| 구분                | 수업 적용 방식                                                        |
| ----------------- | --------------------------------------------------------------- |
| Mermaid           | 데이터 흐름, 시스템 아키텍처, API 연결, 파이프라인 구조, 오류 처리 흐름을 Markdown 문서 안에 작성 |
| Markdown + GitHub | Mermaid 다이어그램과 설명 문서를 함께 저장하고 변경 이력을 관리                         |
| Figma / FigJam    | 팀 아이디어 정리, 발표용 구조도 보정, 비전공자 설명용 시각화 보드로 활용                      |


Figma의 역할은 다음과 같이 정리할 수 있다.

| 사용 목적         | 수업 적용 방식                                                                     |
| ------------- | ---------------------------------------------------------------------------- |
| 팀 아이디어 보드     | 팀별 기능 아이디어, 데이터 활용 아이디어, 개선 방향을 자유롭게 정리                                      |
| 발표용 시각화       | Mermaid로 작성한 기술 구조를 최종 발표용으로 보기 좋게 재구성                                       |
| 비전공자 설명용 보드   | 복잡한 데이터 플랫폼 구조를 쉽게 이해할 수 있도록 단순화하여 표현                                        |
| 화면과 데이터 연결 설명 | 대시보드 화면의 각 영역이 어떤 API와 데이터셋에 연결되는지 시각적으로 표시                                  |
| 아키텍처 요약 보드    | FastAPI, Django, PostgreSQL, Airflow, Kafka, AI/RAG, Dashboard의 관계를 한 장으로 정리 |
| 회의 및 피드백 보드   | 팀 회의 중 의견, 문제점, 개선사항, 역할 분담을 정리                                              |
| 최종 프로젝트 발표 보조 | 시스템 구조, 데이터 흐름, AI/RAG 연결, DataOps 운영 흐름을 발표 자료로 정리                          |
#### Mermaid 다이어그램
| 문서화 대상                                       | 권장 도구          | 이유                                              |
| -------------------------------------------- | -------------- | ----------------------------------------------- |
| 전체 시스템 아키텍처                                  | Mermaid        | 구조 변경이 잦고 Git으로 관리하기 좋음                         |
| Sensor → Collector → Raw → Staging → Mart 흐름 | Mermaid        | 데이터 흐름을 정확하게 표현하기 좋음                            |
| Airflow DAG 흐름                               | Mermaid        | 작업 순서와 의존성을 코드처럼 관리하기 좋음                        |
| Kafka/Spark 스트리밍 흐름                          | Mermaid        | 이벤트 흐름을 단계별로 표현하기 좋음                            |
| RAG 문서 파이프라인                                 | Mermaid        | 문서 수집, Chunking, Embedding, Vector DB 흐름 표현에 적합 |
| Dead Letter, Retry, Checkpoint 흐름            | Mermaid        | 오류 처리와 재처리 흐름을 명확하게 정리하기 좋음                     |
| 최종 발표용 한 장 요약                                | Figma          | 시각적으로 보기 좋게 다듬기 좋음                              |
| 팀 브레인스토밍                                     | Figma / FigJam | 여러 사람이 동시에 아이디어를 붙이기 좋음                         |

권장 문서화 흐름
```text
1. 먼저 Markdown 문서에 Mermaid로 기술 구조를 작성한다.
2. GitHub docs 또는 README에 저장한다.
3. 필요하면 생성형 AI를 활용해 Mermaid 다이어그램을 개선한다.
4. 최종 발표나 팀 회의가 필요할 때 Figma에서 보기 좋게 재구성한다.
```

#### Notion과 Obsidian을 수업에 적용하는 방식
Notion과 Obsidian은 역할을 나누어 사용하는 것이 좋다.

| 도구       | 권장 역할                            |
| -------- | -------------------------------- |
| Notion   | 팀 산출물, 요구사항, 회의록, 제출물 관리         |
| Obsidian | 개인 학습 노트, 개념 연결, 수업 복습, 오류 해결 기록 |

#### WSL2와 Linux 명령어
데이터 엔지니어링 실무에서는 터미널 기반 작업이 많다.  
따라서 Windows만 사용하는 것보다 WSL2 Ubuntu 환경을 기준으로 수업하는 것이 좋다.

| 명령어      | 수업 적용 예시                   |
| -------- | -------------------------- |
| `pwd`    | 현재 경로 확인                   |
| `ls`     | 파일 목록 확인                   |
| `cd`     | 프로젝트 폴더 이동                 |
| `mkdir`  | Raw, Staging, Mart 폴더 생성   |
| `touch`  | 빈 파일 생성                    |
| `cat`    | 설정 파일, JSON 파일 내용 확인 또는 생성 |
| `echo`   | 간단한 텍스트 출력                 |
| `cp`     | 파일 복사                      |
| `mv`     | 파일 이동 또는 이름 변경             |
| `rm`     | 파일 삭제                      |
| `tree`   | 프로젝트 구조 확인                 |
| `grep`   | 로그에서 특정 문자열 검색             |
| `find`   | 특정 파일 검색                   |
| `chmod`  | 실행 권한 부여                   |
| `curl`   | API 요청 테스트                 |
| `python` | Python 코드 실행               |
| `pip`    | 패키지 설치                     |
| `docker` | 컨테이너 실행                    |
| `git`    | 버전 관리                      |

#### 단계별 기술 스택 적용
| 단계                    | 핵심 목표                                                           | 주요 기술                                                                                                                          | 적용 방식                                                                                                                                                                                          |
| --------------------- | --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0단계                   | 프로젝트 기준선 정리                                                    | WSL2, Linux Command, VSCode, Git, GitHub, Markdown, Mermaid, Obsidian, JSON                                                     | 본격적인 개발 전에 프로젝트 목적, 데이터 소스, 도메인 이벤트, 데이터 흐름, 시스템 경계, 컨벤션, 산출물 기준을 문서와 샘플 데이터로 정리한다.                                                                                 |
| 1단계                   | AI 서비스와 <br>데이터 플랫폼 아키텍처 이해                                     | WSL2, Linux Command, VSCode, Git, GitHub, Markdown, Mermaid, Obsidian, Notion, Figma/FigJam                                    | 개발 환경을 준비하고 전체 시스템 구조를 이해한다. <br><br>Mermaid로 데이터 흐름과 아키텍처를 문서화하고, GitHub에 수업 산출물을 관리한다. <br><br>Figma/FigJam은 기술 구조를 <br>처음부터 그리는 도구가 아니라 팀 아이디어 정리와 발표용 보조 시각화 도구로 사용한다.                     |
| 2단계                 . | 데이터 수집과 레이크하우스 설계                                               | Python, FastAPI, Pydantic, JSON Schema, PostgreSQL, DBeaver, JSON, JSONL, CSV, Parquet, Local File System                      | 센서 데이터, 전력 데이터, <br>작업자 위치 데이터를 FastAPI로 수집한다. <br><br>수집 데이터는 Data Contract와 Schema Version 기준으로 <br>검증하고, <br><br>정상 데이터는 Raw Zone에 저장하며, <br><br>오류 데이터는 Dead Letter로 <br>분리한다.             |
| 3단계                   | Airflow 기반 <br>데이터 파이프라인 자동화                                    | Airflow, Python, pandas, pyarrow, DuckDB, PostgreSQL, Parquet, Bash, Cron 개념                                                   | Raw 데이터를 읽어 Staging으로 검증·변환하고, Mart 데이터를 자동 생성한다. <br><br>Marker, Checkpoint, Backfill, Quality Report를 통해 파이프라인 재실행과 운영 기록을 학습한다.                                                             |
| 4단계                   | Kafka/Spark <br>기반 실시간 <br>이벤트 처리와 관제 화면 연결                     | Kafka, Spark Structured Streaming, FastAPI, Django, DRF, Django Templates, JavaScript, WebSocket, <br>Django Channels          | 실시간 센서 이벤트를 Kafka로 흘려보내고 Spark Streaming으로 Window 처리, 중복 제거, 지연 데이터 처리를 실습한다. <br><br>AI 위험 판단 결과를 Django/DRF API와 WebSocket을 통해 관제 화면에 연결한다.                                                  |
| 5단계                   | 데이터 품질, <br>계보, 거버넌스                                          . | dbt, SQL Test, Great Expectations 선택, PostgreSQL, DBeaver, Data Contract, Lineage Report, Markdown, Mermaid                    | 데이터 품질 규칙을 정의하고 Null, 중복, 범위, Freshness, Schema Compatibility를 검사한다. <br><br>Raw → Staging → Mart → AI Dataset으로 이어지는 데이터 계보를 문서화하고, <br>데이터 접근·보안·거버넌스 개념을 정리한다.                              |
| 6단계                   | RAG와 벡터 <br>데이터 파이프라인                                           | Python, FastAPI, LangChain <br>또는 <br>LlamaIndex, Chroma/FAISS/pgvector, PostgreSQL, Django, DRF, Embedding API                | 산업안전 대응 매뉴얼 문서를 수집하고 Chunking, Embedding, Vector DB 저장, 검색 API를 구현한다. <br><br>RAG 검색 결과는 출처와 함께 Django 화면 또는 API 응답으로 확인한다.                                                                    |
| 7단계                   | 피드백 데이터와 DataOps <br>운영                                         | Django, DRF, FastAPI, Celery, Redis, PostgreSQL, Airflow, Prometheus, Grafana, <br>Docker Compose, <br>GitHub Actions, Logging | 사용자 피드백, AI 추론 로그, <br>서비스 호출 로그, 오류 로그를 수집한다. <br><br>운영 지표, 품질 리포트, 실패 건수, 처리 지연, SLA 상태를 모니터링하고, <br>재학습 후보 데이터셋을 <br>생성한다. <br><br>Docker Compose와 GitHub Actions으로 통합 실행과 기본 CI/CD를 경험한다. |

---
## 5. 수업 운영 원칙

이 과정의 핵심은
AI 네이티브 데이터 플랫폼 엔지니어가 알아야 할 데이터 흐름, 데이터 처리 구조, 품질 관리, 운영 원칙을 충분히 이해한 뒤, 그 내용을 산업안전 관제플랫폼 예제에 단계별로 적용해보는 것이다.

따라서 수업은 다음 순서로 운영한다.
```text
범용 이론 설명
→ 간단한 미니 실습
→ 핵심 질문과 이해도 점검
→ 산업안전 관제플랫폼 응용 실습
→ 산출물 정리
```

산업안전 관제플랫폼은 수업의 전체 목적이 아니라,  
배운 내용을 실제 프로젝트에 적용해보기 위한 **응용 실습 도메인**이다.

---
#### 범용 이론을 먼저 충분히 이해한다

각 단계에서는 먼저 산업안전 도메인에 들어가기 전에,  
데이터 플랫폼에서 공통적으로 사용되는 개념을 범용 예제로 설명한다.

예를 들어 2단계 데이터 수집 수업에서는 바로 유해가스 센서 데이터를 다루기 전에 다음 개념을 먼저 설명한다.
```text
데이터 수집이란 무엇인가?
API로 데이터를 받는다는 것은 무엇인가?
JSON, CSV, JSONL, Parquet은 어떻게 다른가?
Raw 데이터는 왜 원본 그대로 저장해야 하는가?
Data Contract는 왜 필요한가?
Validation은 무엇을 검증하는가?
오류 데이터는 왜 Dead Letter로 분리해야 하는가?
```

즉, 먼저 **개념의 목적과 필요성**을 이해한 뒤 실습으로 넘어간다.

---
#### 미니 실습으로 개념을 먼저 익힌다

산업안전 관제플랫폼 실습에 들어가기 전에,  
작고 단순한 범용 데이터를 사용해 미니 실습을 진행한다.

예를 들어 다음과 같은 미니 실습을 사용할 수 있다.

|학습 주제|미니 실습 예시|
|---|---|
|데이터 수집|간단한 주문 데이터 또는 센서 데이터 JSON을 FastAPI로 받기|
|Raw 저장|입력 데이터를 JSONL 파일로 저장하기|
|Validation|필수 필드 누락, 타입 오류, 범위 오류 검증하기|
|Dead Letter|잘못된 데이터를 별도 폴더에 저장하기|
|Staging 변환|Raw JSONL을 정리해서 Parquet으로 변환하기|
|Mart 생성|대시보드용 요약 데이터 만들기|
|Airflow|간단한 Raw → Staging → Mart DAG 작성하기|
|Kafka|간단한 이벤트를 Topic으로 보내고 소비하기|
|RAG|짧은 문서를 Chunking하고 검색하기|
|Data Quality|Null, 중복, Freshness 검사하기|

미니 실습의 목적은 완성도 높은 프로젝트를 만드는 것이 아니라,  
각 개념을 작게 성공해보면서 구조를 이해하는 것이다.

---
#### 이해도 점검 후 산업안전 관제플랫폼에 적용한다
미니 실습 이후에는 핵심 개념을 이해했는지 질문으로 점검한다.

과정 중 반복해서 확인할 질문은 다음과 같다.
```text
이 데이터는 어디서 생성되는가?
이 데이터는 어떤 형식으로 들어오는가?
이 데이터의 필수 필드는 무엇인가?
Raw에는 왜 원본 그대로 저장해야 하는가?
Staging에서는 무엇을 검증하고 정리하는가?
Mart는 어떤 목적을 위해 만드는가?
오류 데이터는 어디에 저장하고 어떻게 추적하는가?
중복 데이터는 어떻게 처리하는가?
파이프라인을 다시 실행해도 안전한가?
AI 또는 RAG는 이 데이터를 어떻게 사용하는가?
운영 중 실패하면 어떻게 확인하고 재처리하는가?
```

이 질문에 대한 이해를 바탕으로,  
그날 배운 내용을 산업안전 관제플랫폼의 해당 부분에 적용한다.

예를 들어 2단계에서는 다음과 같이 연결한다.
```text
미니 실습:
간단한 JSON 데이터를 수집하고 Raw로 저장한다.

산업안전 관제플랫폼 응용:
유해가스 센서 데이터, 전력 데이터, 작업자 위치 데이터를 수집하고 Raw Zone에 저장한다.
```

---
#### 산업안전 관제플랫폼은 단계별 응용 실습으로 사용한다

산업안전 관제플랫폼은 처음부터 완성된 형태로 제공하지 않는다.  
각 단계에서 배운 개념을 적용할 수 있는 범위만 직접 구현한다.

| 단계     | 먼저 배우는 범용 개념                                | 산업안전 관제플랫폼 적용                             |
| ------ | ------------------------------------------- | ----------------------------------------- |
| 1단계  . | AI 데이터 플랫폼 구조, 데이터 흐름, 아키텍처                 | 관제플랫폼 전체 데이터 흐름과 <br>시스템 구조 설계            |
| 2단계    | 데이터 수집, Raw, Data Contract, Validation      | 센서/전력/작업자 위치 데이터 수집과 Raw 저장               |
| 3단계    | Batch Pipeline, Staging, Mart, Backfill     | Raw → Staging → Risk Mart 자동화             |
| 4단계    | 실시간 이벤트, Kafka, Window, <br>지연/중복 처리        | 실시간 위험 이벤트 처리와 대시보드 연결                    |
| 5단계    | Data Quality, Lineage, Governance           | 품질 리포트, 계보 문서, 데이터 검증 규칙 작성               |
| 6단계    | RAG, Chunking, Embedding, <br>Vector Search | 산업안전 대응 매뉴얼 검색 <br>파이프라인 구현               |
| 7단계    | Feedback, DataOps, Monitoring               | 사용자 피드백, AI 로그, 운영 지표, <br>재학습 후보 데이터셋 생성 |

즉, 산업안전 관제플랫폼은 그날 배운 내용을 확인하는 **최종 응용 실습 예제**이다.

---
#### 빈 껍데기에서 시작한다

수업은 최소한의 프로젝트 구조에서 시작한다.  
처음부터 완성된 모델, 완성된 대시보드, 완성된 DAG, 완성된 AI 기능을 제공하지 않는다.

초기 제공 범위는 다음 정도로 제한한다.
```text
- Django 프로젝트 기본 구조
- requirements.txt
- .env.example
- README.md 기본 안내
- docs/ 폴더
- sample_events/ 폴더
- templates/ 기본 화면 골격
- static/ 기본 CSS, JavaScript 골격
```

후반부에 필요한 Docker Compose, Airflow, Kafka, Redis, Prometheus, Grafana 등은  
처음부터 모두 제공하지 않고 단계별로 추가한다.

이렇게 하는 이유는 완성된 코드를 따라 치는 것이 아니라,  
데이터가 어떻게 생성되고, 저장되고, 처리되고, 화면과 AI에 연결되는지를 직접 경험하게 하기 
위해서이다.

---
#### 모든 구현은 데이터 흐름을 기준으로 설명한다
이 과정에서는 기능을 만들 때마다 항상 데이터 흐름을 기준으로 설명한다.

예를 들어 “알람 화면을 만든다”가 핵심이 아니다.  
중요한 것은 다음 흐름을 이해하는 것이다.
```text
센서 데이터 발생
→ 수집 API로 입력
→ Raw 저장
→ Staging 검증
→ Mart 생성
→ 위험도 판단
→ 알람 저장
→ Dashboard 표시
→ 사용자 확인/조치
→ Feedback 데이터 저장
→ 운영 리포트와 재학습 후보 데이터로 활용
```

따라서 수업 중 모든 구현은 다음 질문과 연결해서 설명한다.
```text
이 기능은 어떤 데이터를 사용하는가?
이 데이터는 어디에서 왔는가?
이 데이터는 어느 단계에서 검증되었는가?
이 데이터는 어떤 목적의 Mart로 바뀌었는가?
이 결과는 화면, AI, RAG, 운영 리포트 중 어디에 사용되는가?
이 과정에서 실패하면 어떻게 추적하고 재처리하는가?
```

---
#### 기능보다 산출물을 중요하게 본다

버튼과 화면만 완성했다고 해서 데이터 플랫폼을 이해한 것은 아니다.  
각 단계에서는 반드시 코드 산출물뿐 아니라 문서 산출물과 데이터 산출물을 함께 만든다.

반복적으로 작성할 산출물은 다음과 같다.
```text
- 데이터 계약서
- 이벤트 사전
- ERD
- API 명세서
- Raw/Staging/Mart 설계서
- 데이터 검증 규칙 문서
- Dead Letter 처리 문서
- Airflow DAG 설계서
- Kafka Topic 설계서
- Data Quality Report
- Data Lineage 문서
- RAG 문서 메타데이터 정의서
- 피드백 데이터 정의서
- 운영 모니터링 지표 정의서
- 최종 아키텍처 다이어그램
```

산출물은 Markdown, Mermaid, GitHub README, docs 폴더를 중심으로 관리한다.  
Figma/FigJam은 팀 아이디어 정리와 최종 발표용 시각화 보조 도구로 사용한다.

---
#### 수업 브랜치 운영 원칙

브랜치는 단계별로 안전하게 실습하고, 오류가 발생했을 때 특정 시점으로 돌아갈 수 있도록 운영한다.

이 저장소는 수업 내용을 단계별 브랜치로 나누어 관리한다.  
각 브랜치는 하나의 수업 단계 또는 실습 단위를 의미한다.

현재 저장소의 브랜치 구조는 다음과 같다.
```text
main 2026_7_21_source lesson/00_project_baseline lesson/01_ai_service_data_platform_architecture lesson/02_data_collection_lakehouse_design lesson/03_ai_workload_data_pipeline_automation lesson/04_large_scale_log_realtime_event_streaming lesson/05_ai_data_quality_lineage_governance 
lesson/06_rag_vector_data_pipeline 
lesson/07_ai_service_feedback_dataops
```

각 브랜치의 역할은 다음과 같다.

|브랜치|역할|
|---|---|
|`main`|저장소의 대표 브랜치. 전체 과정 소개, 최종 안내, 안정 버전 문서를 관리한다.|
|`2026_7_21_source`|수업 시작 전 초기 소스 기준 브랜치이다. 학생들에게 제공할 출발점 또는 원본 기준으로 사용한다.|
|`lesson/00_project_baseline`|프로젝트 기준선 브랜치이다. 기본 폴더 구조, README, docs, sample_events 등 최소 구조를 정리한다.|
|`lesson/01_ai_service_data_platform_architecture`|AI 서비스와 데이터 플랫폼 아키텍처를 이해하고 전체 데이터 흐름을 설계하는 브랜치이다.|
|`lesson/02_data_collection_lakehouse_design`|데이터 수집, Data Contract, Raw 저장, Lakehouse 구조를 설계하는 브랜치이다.|
|`lesson/03_ai_workload_data_pipeline_automation`|Raw → Staging → Mart 변환과 Airflow 기반 파이프라인 자동화를 실습하는 브랜치이다.|
|`lesson/04_large_scale_log_realtime_event_streaming`|Kafka/Spark 기반 실시간 이벤트 스트리밍, Window 처리, 지연/중복 이벤트 처리를 실습하는 브랜치이다.|
|`lesson/05_ai_data_quality_lineage_governance`|데이터 품질, 계보, 거버넌스, 품질 리포트와 운영 기준을 정리하는 브랜치이다.|
|`lesson/06_rag_vector_data_pipeline`|RAG 문서 수집, Chunking, Embedding, Vector DB, 검색 API를 실습하는 브랜치이다.|
|`lesson/07_ai_service_feedback_dataops`|AI 서비스 피드백, 로그 수집, DataOps 운영, 모니터링, 재학습 후보 데이터셋을 실습하는 브랜치이다.|

브랜치는 항상 직전 안정 브랜치에서 새로 만든다.
```text
2026_7_21_source
→ lesson/00_project_baseline
→ lesson/01_ai_service_data_platform_architecture
→ lesson/02_data_collection_lakehouse_design
→ lesson/03_ai_workload_data_pipeline_automation
→ lesson/04_large_scale_log_realtime_event_streaming
→ lesson/05_ai_data_quality_lineage_governance
→ lesson/06_rag_vector_data_pipeline
→ lesson/07_ai_service_feedback_dataops
```

이 구조를 사용하면 단계별로 다음 흐름을 따라갈 수 있다.
```text
기준 소스 확인
→ 프로젝트 기준선 이해
→ AI 데이터 플랫폼 아키텍처 이해
→ 데이터 수집과 레이크하우스 설계
→ 데이터 파이프라인 자동화
→ 실시간 이벤트 스트리밍
→ 데이터 품질과 계보 관리
→ RAG 벡터 데이터 파이프라인
→ 피드백 데이터와 DataOps 운영
```

브랜치 운영 기준은 다음과 같다.
```text
main
→ 전체 과정 소개와 최종 안정 문서 관리

2026_7_21_source
→ 수업 시작 전 초기 소스 기준

lesson/*
→ 수업 단계별 학습 코드와 문서 관리
```

향후 프로젝트 브랜치를 추가한다면 다음처럼 별도 규칙으로 운영한다.
```text
큰 lesson 브랜치
→ 해당 단계의 최종 안정본

세부 lesson 브랜치
→ 해당 단계 안에서 나누어 실습하는 중간 단위
```

예를 들면 다음과 같다
```
lesson/02_01_data_contract_schema
lesson/02_02_fastapi_collector
lesson/02_03_raw_jsonl_storage
lesson/02_04_validation_dead_letter
lesson/02_05_staging_parquet
lesson/02_06_lakehouse_structure
lesson/02_data_collection_lakehouse_design
```
즉, `02_01`부터 `02_06`까지 실습한 뒤,  
최종 정리본을 `lesson/02_data_collection_lakehouse_design`으로 두는 방식입니다.

1단계 AI 서비스와 데이터 플랫폼 아키텍처
```
lesson/01_01_ai_service_architecture
lesson/01_02_data_flow_mapping
lesson/01_03_domain_event_modeling
lesson/01_04_mermaid_architecture_docs
lesson/01_ai_service_data_platform_architecture
```

|브랜치|목적|
|---|---|
|`lesson/01_01_ai_service_architecture`|AI 서비스와 데이터 플랫폼 전체 구조 이해|
|`lesson/01_02_data_flow_mapping`|Sensor → Raw → Staging → Mart → AI → Dashboard 흐름 정리|
|`lesson/01_03_domain_event_modeling`|이벤트, 데이터 계약, 도메인 데이터 정의|
|`lesson/01_04_mermaid_architecture_docs`|Mermaid로 아키텍처와 데이터 흐름 문서화|
|`lesson/01_ai_service_data_platform_architecture`|1단계 최종 안정 브랜치|

2단계 데이터 수집과 레이크하우스 설계
```
lesson/02_01_data_contract_schema
lesson/02_02_fastapi_collector
lesson/02_03_raw_jsonl_storage
lesson/02_04_validation_dead_letter
lesson/02_05_staging_parquet
lesson/02_06_lakehouse_structure
lesson/02_data_collection_lakehouse_design
```

|브랜치|목적|
|---|---|
|`lesson/02_01_data_contract_schema`|JSON Schema, Pydantic, 데이터 계약 작성|
|`lesson/02_02_fastapi_collector`|FastAPI Collector로 데이터 수집|
|`lesson/02_03_raw_jsonl_storage`|Raw Zone에 JSONL 저장|
|`lesson/02_04_validation_dead_letter`|검증 실패 데이터 Dead Letter 저장|
|`lesson/02_05_staging_parquet`|Raw 데이터를 Staging Parquet으로 변환|
|`lesson/02_06_lakehouse_structure`|Raw/Staging/Mart 폴더 구조와 설계 문서 정리|
|`lesson/02_data_collection_lakehouse_design`|2단계 최종 안정 브랜치|

3단계 Airflow 기반 데이터 파이프라인 자동화
```
lesson/03_01_pipeline_package
lesson/03_02_raw_to_staging
lesson/03_03_staging_to_mart
lesson/03_04_quality_report
lesson/03_05_marker_checkpoint
lesson/03_06_backfill
lesson/03_07_airflow_dag
lesson/03_ai_workload_data_pipeline_automation
```

|브랜치|목적|
|---|---|
|`lesson/03_01_pipeline_package`|`pipeline/` 공통 패키지 구조 생성|
|`lesson/03_02_raw_to_staging`|Raw → Staging 변환 자동화|
|`lesson/03_03_staging_to_mart`|Staging → Mart 생성|
|`lesson/03_04_quality_report`|품질 리포트 생성|
|`lesson/03_05_marker_checkpoint`|Marker, Checkpoint로 처리 상태 기록|
|`lesson/03_06_backfill`|과거 데이터 재처리|
|`lesson/03_07_airflow_dag`|Airflow DAG로 자동 실행|
|`lesson/03_ai_workload_data_pipeline_automation`|3단계 최종 안정 브랜치|

4단계 Kafka/Spark 실시간 이벤트 스트리밍
```
lesson/04_01_kafka_topic_design
lesson/04_02_event_producer_consumer
lesson/04_03_spark_streaming_window
lesson/04_04_dedup_late_event_handling
lesson/04_05_realtime_risk_engine
lesson/04_06_django_websocket_dashboard
lesson/04_large_scale_log_realtime_event_streaming
```

|브랜치|목적|
|---|---|
|`lesson/04_01_kafka_topic_design`|Kafka Topic, Event 구조 설계|
|`lesson/04_02_event_producer_consumer`|Producer/Consumer 실습|
|`lesson/04_03_spark_streaming_window`|Spark Streaming Window 처리|
|`lesson/04_04_dedup_late_event_handling`|중복 데이터, 지연 이벤트 처리|
|`lesson/04_05_realtime_risk_engine`|실시간 위험 판단 로직 연결|
|`lesson/04_06_django_websocket_dashboard`|Django/DRF/WebSocket으로 화면 연결|
|`lesson/04_large_scale_log_realtime_event_streaming`|4단계 최종 안정 브랜치|

5단계 데이터 품질, 계보, 거버넌스
```
lesson/05_01_quality_rule_design
lesson/05_02_sql_dbt_tests
lesson/05_03_freshness_schema_check
lesson/05_04_lineage_report
lesson/05_05_governance_policy
lesson/05_06_quality_dashboard
lesson/05_ai_data_quality_lineage_governance
```

|브랜치|목적|
|---|---|
|`lesson/05_01_quality_rule_design`|데이터 품질 규칙 정의|
|`lesson/05_02_sql_dbt_tests`|SQL Test 또는 dbt Test 작성|
|`lesson/05_03_freshness_schema_check`|Freshness, Schema Compatibility 검사|
|`lesson/05_04_lineage_report`|Raw → Staging → Mart 계보 문서 작성|
|`lesson/05_05_governance_policy`|접근 제어, 보안, 거버넌스 기준 정리|
|`lesson/05_06_quality_dashboard`|품질 결과를 화면 또는 리포트로 확인|
|`lesson/05_ai_data_quality_lineage_governance`|5단계 최종 안정 브랜치|

6단계 RAG와 벡터 데이터 파이프라인
```
lesson/06_01_document_loader
lesson/06_02_chunking_metadata
lesson/06_03_embedding_vector_store
lesson/06_04_rag_search_api
lesson/06_05_source_citation_response
lesson/06_06_rag_service_logging
lesson/06_rag_vector_data_pipeline
```

|브랜치|목적|
|---|---|
|`lesson/06_01_document_loader`|산업안전 매뉴얼 문서 수집|
|`lesson/06_02_chunking_metadata`|문서 Chunking과 메타데이터 생성|
|`lesson/06_03_embedding_vector_store`|Embedding 생성 및 Vector DB 저장|
|`lesson/06_04_rag_search_api`|RAG 검색 API 구현|
|`lesson/06_05_source_citation_response`|출처 표시 응답 구조 작성|
|`lesson/06_06_rag_service_logging`|RAG 질의 로그와 응답 로그 저장|
|`lesson/06_rag_vector_data_pipeline`|6단계 최종 안정 브랜치|

7단계 피드백 데이터와 DataOps 운영
```
lesson/07_01_feedback_collection
lesson/07_02_ai_service_logs
lesson/07_03_dataops_metrics
lesson/07_04_prometheus_grafana
lesson/07_05_celery_redis_async_jobs
lesson/07_06_docker_compose_integration
lesson/07_07_github_actions_ci
lesson/07_08_retraining_candidate_dataset
lesson/07_ai_service_feedback_dataops
```

|브랜치|목적|
|---|---|
|`lesson/07_01_feedback_collection`|사용자 확인, 조치, 평가 피드백 수집|
|`lesson/07_02_ai_service_logs`|AI 추론 요청/응답/오류 로그 저장|
|`lesson/07_03_dataops_metrics`|운영 지표, 실패 건수, 처리 지연 지표 생성|
|`lesson/07_04_prometheus_grafana`|Prometheus/Grafana 모니터링 연결|
|`lesson/07_05_celery_redis_async_jobs`|비동기 작업 처리|
|`lesson/07_06_docker_compose_integration`|전체 서비스 Docker Compose 통합|
|`lesson/07_07_github_actions_ci`|GitHub Actions로 기본 CI 구성|
|`lesson/07_08_retraining_candidate_dataset`|재학습 후보 데이터셋 생성|
|`lesson/07_ai_service_feedback_dataops`|7단계 최종 안정 브랜치|

이 브랜치들은 실제 생성 후 문서에 반영한다.

브랜치 이동 방법은 다음과 같다.
```bash
git clone https://github.com/handgonpo/2026_7_21_diconai.git
cd 2026_7_21_diconai

git fetch --all

git switch lesson/00_project_baseline
git pull origin lesson/00_project_baseline
```

다른 단계로 이동할 때는 다음처럼 브랜치명만 바꾼다.
```bash
git switch lesson/02_data_collection_lakehouse_design
git pull origin lesson/02_data_collection_lakehouse_design
```

현재 브랜치를 확인하려면 다음 명령어를 사용한다.
```bash
git branch --show-current
```

원격 브랜치까지 모두 확인하려면 다음 명령어를 사용한다.
```bash
git branch -a
```

정리하면, 이 저장소의 브랜치 운영 원칙은 다음과 같다.
```text
lesson 브랜치: 수업 단계별 학습 코드와 문서
2026_7_21_source 브랜치: 수업 시작 전 기준 소스
main 브랜치: 전체 안내와 최종 안정 문서
project 브랜치: 현재는 사용하지 않으며, 실제 프로젝트 브랜치 생성 후 추가
```

---
# 교과목별 전체 과정

---
### 0단계. 프로젝트 기준선 정리 — 16h

본격적인 개발에 들어가기 전에 프로젝트 목적, 데이터 소스, 도메인 이벤트, 데이터 흐름, 시스템 경계, 컨벤션, 산출물 기준을 먼저 정리한다.  
0단계는 기능을 구현하는 단계가 아니라, 이후 1~7단계 개발이 흔들리지 않도록 프로젝트의 기준 언어와 기준 구조를 맞추는 단계이다.

산업안전 관제플랫폼에서는 유해가스 센서 데이터, 스마트 파워 전력 데이터, 작업자 위치 데이터, 위험구역 데이터, 알람 데이터, AI 판단 결과, RAG 대응 매뉴얼, 운영자 피드백이 어떤 흐름으로 연결될지 기준선을 작성한다.

핵심 산출물은 프로젝트 개요, 데이터 소스 맵, 도메인 이벤트 맵, 데이터 계약 후보 문서, 기준 데이터 흐름도, 시스템 경계 문서, 컨벤션 문서, 샘플 이벤트 JSON, 임계치 seed, 최종 시연 시나리오, 완료 체크리스트이다.

### 🔗 [[0단계_프로젝트_기준선_정리_로드맵_주니어용 — 16h]] 상세설명클릭
---
### 1단계. AI 서비스와 데이터 플랫폼 아키텍처 — 40h

AI 서비스가 모델만으로 운영되지 않는다는 점을 이해하고, 데이터가 어디서 발생해 AI, RAG, 대시보드, 피드백, 운영 지표로 연결되는지 전체 구조를 설계한다.  
산업안전 관제플랫폼에서 사용할 데이터 소스, 도메인 이벤트, 시스템 경계, Raw/Staging/Mart, Feature Dataset, Vector DB, 피드백 데이터의 역할을 정의한다.  
  
핵심 산출물은 전체 아키텍처, 데이터 흐름도, 도메인 이벤트 사전, C4 Context/Container, 최종 시연 시나리오이다.
### 🔗 [[1단계. AI 서비스와 데이터 플랫폼 아키텍처 — 24h]] 상세설명클릭
---
### 2단계. AI 데이터 수집과 레이크하우스 설계 — 48h

센서, 전력, 작업자 위치, AI 서비스 로그, RAG 문서 메타데이터, 피드백 데이터를 수집하고 Raw Zone에 원본으로 저장하는 구조를 만든다.  
Data Contract, schema_version, JSON Schema, Pydantic 검증을 통해 정상 데이터와 오류 데이터를 분리하고, 검증 실패 데이터는 Dead Letter에 저장한다.  
  
핵심 산출물은 FastAPI Collector, 데이터 계약서, Raw/Dead Letter 저장 구조, 기준정보 seed, Raw/Staging/Mart 설계서이다.

### 🔗 [[2단계. AI 데이터 수집과 레이크하우스 설계 — 48h]] 상세설명클릭
---
### 3단계. AI 워크로드를 위한 데이터 파이프라인 자동화 — 56h

2단계에서 수집한 Raw 데이터를 Staging, Mart, AI Training Dataset으로 자동 변환하는 Airflow 기반 배치 파이프라인을 만든다.  
데이터 검증, Mart 생성, 품질 리포트, Backfill, Marker, Checkpoint, 멱등성 개념을 적용하여 재실행 가능한 데이터 파이프라인 구조를 학습한다.  
  
핵심 산출물은 Airflow DAG, Raw→Staging 변환 코드, Risk Mart, Alarm Summary, AI Training Dataset, Backfill 정책 문서이다.

### 🔗 [[3단계. AI 워크로드를 위한 데이터 파이프라인 자동화 — 56h]] 상세설명클릭
---
### 4단계. 대용량 로그와 실시간 이벤트 스트리밍 — 56h

실시간으로 발생하는 센서 이벤트, 작업자 위치 이벤트, AI 추론 이벤트, 알람 이벤트를 Kafka Topic으로 흘려보내고 Spark Streaming 또는 Consumer로 처리한다.  
Window, Watermark, 중복 제거, 지연 이벤트 처리, 실시간 Risk Event 생성, WebSocket 대시보드 연결을 통해 끊기지 않는 관제 흐름을 만든다.  
  
핵심 산출물은 Kafka Topic 설계서, Producer/Consumer, Spark Streaming 코드, Risk Event, AlarmEvent, WebSocket 대시보드 MVP이다.

### 🔗 [[4단계. 대용량 로그와 실시간 이벤트 스트리밍 — 56h]] 상세설명클릭
---
### 5단계. AI 데이터 품질, 계보, 거버넌스 — 64h

AI와 RAG가 사용하는 데이터가 신뢰 가능한지 검증하기 위해 데이터 품질 기준, dbt/SQL Test, Freshness, Schema Compatibility, Drift, Lineage, PII, 접근 권한 기준을 만든다.  
Raw → Staging → Mart → AI/RAG → Feedback으로 이어지는 데이터 이동 경로를 추적하고, 품질 실패 데이터를 운영 리포트로 정리한다.  
  
핵심 산출물은 데이터 품질 기준표, dbt Test, Data Lineage 문서, Drift 정책, PII 정책, Access Control Matrix, Data Quality Report이다.

### 🔗 [[5단계. AI 데이터 품질, 계보, 거버넌스 — 64h]] 상세설명클릭
---
### 6단계. RAG와 벡터 데이터 파이프라인 — 56h

산업안전 매뉴얼, 가스 임계치 정의서, 장비 문서 같은 비정형 문서를 RAG 서비스가 검색할 수 있는 벡터 데이터로 변환한다.  
문서 원본 저장, Metadata 설계, Chunking, Embedding, Vector DB 저장, Hybrid Search, Metadata Filter, 출처 표시 응답 구조를 만든다.  
  
핵심 산출물은 RAG 문서 파이프라인, Document/Chunk Metadata, Embedding 코드, Vector DB, RAG Search API, Source Citation 정책, 검색 품질 리포트이다.

### 🔗 [[6단계. RAG와 벡터 데이터 파이프라인 — 56h]] 상세설명클릭

---
### 7단계. AI 서비스 피드백 데이터와 DataOps 운영 — 40h

운영 중 발생하는 오탐, 정탐, 미탐, RAG 답변 피드백, AI 추론 로그, 오류 로그, 운영 지표를 수집하여 서비스 개선 데이터로 전환한다.  
피드백 API, 재학습 후보 데이터셋, Prometheus/Grafana Metric, Celery/Redis 비동기 작업, Docker Compose, GitHub Actions를 통해 운영 가능한 DataOps 구조를 만든다.  
  
핵심 산출물은 피드백 데이터 정의서, 재학습 후보 데이터셋, DataOps Metric, Grafana 대시보드, SLA 정책, 운영 리포트, 통합 실행 구조이다.

### 🔗 [[7단계. AI 서비스 피드백 데이터와 DataOps 운영 — 40h]] 상세설명클릭

---
# PART B. 실제 개발 순서 요약
---

## B0. 이 파트의 목적

PART A는 각 교과목에서 무엇을 배우고 어떤 산출물을 만드는지 상세히 설명한다.  
PART B는 그 내용을 실제 개발 순서로 다시 정리한 요약 파트이다.

이 파트의 목적은 다음과 같다.
```text
1. 각 단계의 산출물이 다음 단계에서 어떻게 사용되는지 확인한다.
2. 중간 프로젝트, 최종 프로젝트, 기업 프로젝트가 어떤 단계 결과물을 기반으로 하는지 파악한다.
3. 취업 포트폴리오 관점에서 반드시 남겨야 할 산출물을 확인한다.
```

PART B는 수업 중 다음 질문에 빠르게 답하기 위한 기준 문서이다.
```text
지금 우리는 무엇을 만들고 있는가?
이 단계가 끝나면 무엇이 남아야 하는가?
이 결과물은 다음 단계에서 어디에 사용되는가?
최종적으로 학생 포트폴리오에는 어떤 흐름이 보여야 하는가?
```

---
## B1. 전체 개발 흐름 한눈에 보기

이 과정의 실제 개발 흐름은 다음과 같다.
```text
0단계. 프로젝트 기준선 정리
→ 프로젝트 목적, 데이터 소스, 이벤트, 데이터 흐름, 시스템 경계, 산출물 기준을 먼저 정리한다.

1단계. AI 서비스와 데이터 플랫폼 아키텍처
→ 전체 구조, 데이터 흐름, 도메인 이벤트, 시스템 경계를 정의한다.

2단계. AI 데이터 수집과 레이크하우스 설계
→ 데이터를 계약 기반으로 수집하고 Raw Zone과 Dead Letter 구조를 만든다.

3단계. AI 워크로드를 위한 데이터 파이프라인 자동화
→ Raw 데이터를 Staging, Mart, AI Training Dataset으로 자동 변환한다.

4단계. 대용량 로그와 실시간 이벤트 스트리밍
→ Kafka/Spark로 실시간 이벤트를 처리하고 대시보드에 연결한다.

5단계. AI 데이터 품질, 계보, 거버넌스
→ 데이터가 신뢰 가능한지 검증하고 계보와 권한 기준을 만든다.

6단계. RAG와 벡터 데이터 파이프라인
→ 산업안전 문서를 Chunking, Embedding, Vector DB로 검색 가능하게 만든다.

7단계. AI 서비스 피드백 데이터와 DataOps 운영
→ 운영 피드백과 로그를 수집하고 재학습 후보와 운영 지표로 연결한다.
```

이 흐름은 단순히 기능을 하나씩 추가하는 순서가 아니다.  
데이터가 생성되고, 수집되고, 검증되고, AI와 RAG에 사용되고, 다시 운영 피드백으로 돌아오는 전체 순환 구조이다.

```text
프로젝트 기준선 정리
데이터 발생
→ 데이터 수집
→ 원본 저장
→ 검증과 변환
→ 목적별 데이터셋 생성
→ 실시간 판단
→ 품질과 계보 확인
→ 문서 검색
→ 피드백 수집
→ 운영 지표 관찰
→ 개선 데이터 생성
```

---
## B2. 단계별 핵심 개발 순서

| 단계 | 실제 개발 핵심 | 다음 단계로 넘기는 결과물 |
|---|---|---|
| 0단계 | 프로젝트 목적, 데이터 소스, 이벤트 후보, 데이터 흐름, 시스템 경계, 산출물 기준 정리 | 1단계 아키텍처 설계 기준 |
| 1단계 | 프로젝트 목적, 데이터 소스, 도메인 이벤트, 전체 아키텍처 정의 | 데이터 계약과 수집 API 설계 기준 |
| 2단계 | FastAPI Collector, Schema, Raw Zone, Dead Letter, 기준정보 작성 | Raw JSONL, Data Contract, 기준정보 seed |
| 3단계 | Airflow DAG, Raw→Staging, Mart, AI Training Dataset, Backfill 구현 | Staging, Mart, Training Dataset, Quality Report |
| 4단계 | Kafka Topic, Producer/Consumer, Window, 중복/지연 처리, WebSocket 연결 | Risk Event, AlarmEvent, Dashboard Metric |
| 5단계 | dbt/SQL Test, Freshness, Lineage, Drift, PII, 권한 기준 작성 | Data Quality Report, Lineage, RAG 품질 Gate |
| 6단계 | 문서 Metadata, Chunking, Embedding, Vector DB, RAG API 구현 | Vector Index, RAG Query Log, 검색 품질 리포트 |
| 7단계 | 피드백 API, 실패 케이스, 재학습 후보, Metric, Grafana, CI 구성 | Retraining Candidate, DataOps Report, 운영 기준 |

---
## B3. 단계별 실제 개발 순서 요약

### 0단계 개발 순서

```text
프로젝트 목적 정의
→ 문제 정의
→ 도메인과 사용자 역할 정리
→ 데이터 소스와 데이터 유형 정리
→ 도메인 이벤트 후보 작성
→ 데이터 계약 후보 작성
→ Raw / Staging / Mart 기준 흐름 정의
→ 시스템 경계 설정
→ 컨벤션과 폴더 구조 정리
→ GitHub 기준선 산출물 작성
→ 완료 체크리스트 점검
```

0단계의 핵심은 코드를 작성하기 전에 프로젝트의 기준을 먼저 맞추는 것이다.  
프로젝트 목적, 데이터, 이벤트, 흐름, 범위, 산출물 기준이 정리되어야 1단계 아키텍처 설계와 2단계 데이터 수집 설계가 흔들리지 않는다.

### 1단계 개발 순서

```text
프로젝트 목표 정의
→ 도메인 범위 정의
→ 사용자 역할 정의
→ 데이터 소스 정의
→ 도메인 이벤트 정의
→ 전체 데이터 흐름 작성
→ C4 Context / Container 작성
→ 최종 시연 시나리오 작성
```

1단계의 핵심은 코드를 많이 작성하는 것이 아니다.  
앞으로 만들 모든 코드와 데이터 구조의 기준을 먼저 정하는 것이다.

### 2단계 개발 순서

```text
Data Contract 작성
→ JSON Schema / Pydantic Schema 작성
→ FastAPI Collector 구현
→ Raw Zone 폴더 구조 생성
→ JSONL 저장 구현
→ Validation Error / Dead Letter 저장
→ PostgreSQL 기준정보와 seed 작성
→ Raw/Staging/Mart 설계 문서 작성
```

2단계의 핵심은 데이터를 아무렇게나 받지 않는 것이다.  
AI가 사용할 수 있도록 계약에 맞게 수집하고, 원본을 보존하며, 오류 데이터를 추적 가능하게 분리한다.

### 3단계 개발 순서

```text
pipeline 패키지 생성
→ Raw 읽기 함수 작성
→ Staging 검증 함수 작성
→ Mart 생성 함수 작성
→ AI Training Dataset 생성
→ Marker / Checkpoint 기록
→ Backfill 구조 작성
→ Airflow DAG로 자동화
```

3단계의 핵심은 수동 데이터 처리를 자동 파이프라인으로 바꾸는 것이다.  
같은 파이프라인을 다시 실행해도 결과가 깨지지 않도록 멱등성과 재처리 기준을 함께 만든다.

### 4단계 개발 순서

```text
Kafka Topic 설계
→ Producer 작성
→ Consumer 작성
→ Spark Streaming 연결
→ Window Metric 생성
→ 중복/지연 이벤트 처리
→ Risk Event / AlarmEvent 생성
→ WebSocket Dashboard 연결
```

4단계의 핵심은 실시간 데이터를 안전하게 전달하고 처리하는 것이다.  
센서값, 작업자 위치, AI 판단 결과가 대시보드에 끊기지 않게 연결되어야 한다.

### 5단계 개발 순서

```text
데이터 품질 기준표 작성
→ SQL Test / dbt Test 작성
→ Staging 품질 검사
→ Mart 품질 검사
→ Freshness / Schema Compatibility 검사
→ Data Lineage 작성
→ PII / Access Control 기준 작성
→ Data Quality Report 작성
```

5단계의 핵심은 AI와 RAG가 사용하는 데이터를 그냥 믿지 않는 것이다.  
품질 기준, 계보, 권한 기준을 통해 데이터가 신뢰 가능한지 확인한다.

### 6단계 개발 순서

```text
문서 목록 정의
→ Document Metadata 작성
→ Text Extraction 구현
→ Chunking 구현
→ Chunk Metadata 생성
→ Embedding 생성
→ Vector DB 저장
→ Hybrid Search 구현
→ RAG API와 출처 표시 구현
→ 검색 품질 평가
```

6단계의 핵심은 문서를 단순 파일이 아니라 검색 가능한 데이터셋으로 바꾸는 것이다.  
RAG 답변은 반드시 출처, 문서 버전, 권한, 최신성 기준과 함께 관리되어야 한다.

### 7단계 개발 순서

```text
알람 피드백 구조 설계
→ RAG 피드백 구조 설계
→ AI/RAG 로그 저장
→ 실패 케이스 분류
→ 재학습 후보 데이터셋 생성
→ DataOps Metric 정의
→ Prometheus / Grafana 연결
→ Docker Compose 통합 실행
→ GitHub Actions CI 구성
→ 운영 리포트 작성
```

7단계의 핵심은 운영 중 발생하는 결과를 다시 데이터로 남기는 것이다.  
AI가 맞았는지, 틀렸는지, 왜 실패했는지, 어디서 지연되었는지를 관찰하고 개선 데이터로 전환한다.

---
## B4. 단계 간 입력과 출력 연결

각 단계는 독립적인 실습이 아니라 다음 단계의 입력을 만든다.

| 이전 단계 결과물 | 다음 단계에서 사용되는 방식 |
|---|---|
| 0단계 프로젝트 목적, 데이터 소스, 이벤트 후보, 시스템 경계 | 1단계 AI 서비스와 데이터 플랫폼 아키텍처 설계 기준 |
| 1단계 데이터 흐름, 이벤트 사전 | 2단계 Data Contract와 Collector API 설계 기준 |
| 2단계 Raw JSONL, Schema, 기준정보 | 3단계 Raw→Staging 자동 변환 입력 |
| 3단계 Staging, Mart, Training Dataset | 4단계 실시간 판단 기준과 Dashboard 기준 데이터 |
| 4단계 Risk Event, AlarmEvent, Dashboard Metric | 5단계 품질 검사와 Lineage 추적 대상 |
| 5단계 Data Quality Report, RAG 품질 Gate | 6단계 RAG 문서 데이터 입력 기준 |
| 6단계 Vector Index, RAG Query Log | 7단계 RAG 피드백과 DataOps 분석 입력 |
| 7단계 Feedback, Retraining Candidate, Operation Report | 후속 프로젝트와 포트폴리오 개선 근거 |

이 연결을 이해하지 못하면 각 단계가 따로 떨어진 실습처럼 보인다.  
학생은 각 단계의 산출물이 다음 단계에서 어디에 쓰이는지 계속 확인해야 한다.

---
## B5. 프로젝트와의 연결

이 과정에는 이론/실습 교과목 외에 중간 프로젝트, 최종 프로젝트, 기업 프로젝트가 포함된다.  
프로젝트는 별도의 새로운 기술을 갑자기 추가하는 시간이 아니라, 앞에서 만든 단계별 산출물을 묶어 실제 포트폴리오 형태로 정리하는 시간이다.

| 프로젝트 | 활용하는 단계 | 핵심 목표 |
|---|---|---|
| 중간 프로젝트 | 2단계 + 3단계 | AI 서비스 로그를 수집하고 학습 데이터셋으로 변환한다. |
| 최종 프로젝트 | 5단계 + 6단계 | RAG 서비스용 문서 데이터 플랫폼을 구축한다. |
| 기업 프로젝트 | 1단계~7단계 전체 | 수집, 품질, RAG, 피드백, 운영을 통합한 AI 데이터 플랫폼을 완성한다. |

0단계 기준선 산출물은 중간 프로젝트, 최종 프로젝트, 기업 프로젝트에 들어가기 전에도 공통 기준 자료로 활용한다.  

프로젝트 상세 요구사항, 평가 기준, 기업 요구사항은 별도 문서에서 확정한다.  
PART B에서는 프로젝트가 어떤 단계 결과물을 기반으로 하는지만 정리한다.

---
## B6. 학생 포트폴리오 관점의 핵심 산출물

학생이 취업을 목적으로 이 과정을 수강한다면, 단순히 “코드를 작성했다”보다 다음 산출물이 남아야 한다.

| 구분 | 포트폴리오에 남겨야 할 핵심 산출물 |
|---|---|
| 기준선 | 프로젝트 개요, 데이터 소스 맵, 도메인 이벤트 맵, 데이터 계약 후보, 시스템 경계, 완료 체크리스트 |
| 아키텍처 | C4 Context, C4 Container, 전체 데이터 흐름도 |
| 데이터 수집 | Data Contract, FastAPI Collector, Raw Zone, Dead Letter |
| 파이프라인 | Airflow DAG, Raw→Staging, Mart, Backfill, Quality Report |
| 실시간 처리 | Kafka Topic, Producer/Consumer, Window 처리, WebSocket Dashboard |
| 품질 관리 | dbt/SQL Test, Data Quality Report, Data Lineage |
| RAG | Document Metadata, Chunking, Embedding, Vector DB, Source Citation |
| DataOps | Feedback API, Retraining Candidate, Prometheus/Grafana, Operation Report |

학생 포트폴리오에서 중요한 것은 완성된 화면 하나가 아니다.  
데이터가 들어와서 AI 서비스와 운영 개선으로 이어지는 전체 흐름을 설명할 수 있어야 한다.

---
## B7. 시간이 부족해도 생략하면 안 되는 것

수업 시간이 부족하거나 학생 수준 차이가 커도 다음 항목은 생략하지 않는다.

```text
Data Contract
Raw / Staging / Mart 구분
Dead Letter
event_id / trace_id / schema_version
Airflow DAG 기본 구조
Backfill과 멱등성 개념
Kafka Topic 설계 또는 실시간 이벤트 흐름도
데이터 품질 테스트
Data Lineage
RAG Metadata와 Source Citation
Feedback Data
DataOps Metric
```

이 항목들은 AI 네이티브 데이터 플랫폼을 설명하는 최소 기준이다.  
기술 구현을 일부 단순화하더라도 이 개념과 산출물은 반드시 남겨야 한다.

---
## B8. 시간이 부족할 때 단순화 가능한 것

다음 항목은 수업 시간이나 학생 수준에 따라 단순화할 수 있다.

```text
Kafka와 Spark 전체 구현을 Python Consumer 예제로 축소
Kubernetes 배포 생략
고급 ML 모델 학습 생략
복잡한 LLM 프롬프트 엔지니어링 생략
Grafana 대시보드를 JSON 초안 수준으로 축소
GitHub Actions를 기본 테스트 실행 수준으로 축소
RAG UI를 완성형 챗봇이 아니라 API 응답 확인으로 축소
```

단순화하더라도 데이터 흐름의 의미는 유지해야 한다.

예를 들어 Kafka를 완전하게 구현하지 못하더라도 다음 흐름은 설명되어야 한다.
```text
이벤트 발생
→ 메시지 흐름
→ 실시간 처리
→ 위험 판단
→ 대시보드 반영
→ 운영 지표 기록
```

---
## B9. 강사용 운영 기준

강사는 각 단계 수업을 진행할 때 다음 기준을 확인한다.

```text
1. 오늘 수업이 전체 데이터 흐름 중 어디에 해당하는가?
2. 오늘 만든 산출물이 다음 단계에서 어디에 쓰이는가?
3. 학생이 단순히 코드를 따라 친 것이 아니라, 왜 이 구조가 필요한지 설명할 수 있는가?
4. 산출물이 GitHub에 남아 있는가?
5. 문서, 코드, 샘플 데이터, 실행 결과가 함께 정리되어 있는가?
```

강사는 매 단계가 끝날 때 학생에게 다음 질문을 반복해서 확인한다.
```text
이 데이터는 어디서 왔는가?
이 데이터는 어디에 저장되는가?
이 데이터는 어떻게 검증되는가?
이 데이터는 어떤 AI/RAG/대시보드 기능에 사용되는가?
이 데이터는 운영 중 어떻게 추적되는가?
```

---
## B10. 학생이 반드시 기억해야 할 개발 흐름

```text
수집한다
→ 원본을 보존한다
→ 검증한다
→ 목적별 데이터셋으로 만든다
→ 실시간으로 판단한다
→ 품질과 계보를 확인한다
→ 문서를 검색 가능하게 만든다
→ 피드백을 다시 데이터로 남긴다
→ 운영 지표로 관찰한다
→ 개선 데이터로 전환한다
```

이 흐름을 이해하면 산업안전 관제플랫폼뿐 아니라 다른 AI 서비스에도 같은 데이터 플랫폼 구조를 적용할 수 있다.

이 과정의 핵심은 다음 한 문장으로 정리할 수 있다.
```text
AI는 모델만으로 움직이지 않는다.
AI를 움직이게 하는 것은 신뢰 가능한 데이터 흐름과 운영 가능한 데이터 플랫폼이다.
```
