# 브랜치 네이밍 규칙

> 프로젝트명: 중기청 관제플랫폼 기반 AI 데이터 플랫폼 구축 프로젝트  
> 기준 문서: `AI_네이티브_데이터_플랫폼_전체_개발_로드맵.md`

---

## 1. 목적

이 문서는 전체 수업 로드맵에 맞춰 GitHub 브랜치 이름을 통일하기 위한 기준 문서이다.

이전 방식은 `lesson/일차_순서_주제` 구조였다.

```text
lesson/01_01_project_overview
lesson/01_02_template_static_structure
lesson/01_03_django_run_readme
```
---

## 2. 전체 개발 흐름

전체 개발은 다음 흐름으로 진행된다.

```text
0단계: 프로젝트 기준선 정리
→ 1단계: AI 서비스와 데이터 플랫폼 아키텍처
→ 2단계: 데이터 수집과 레이크하우스 설계
→ 3단계: AI 워크로드를 위한 데이터 파이프라인 자동화
→ 중간 프로젝트: AI 서비스 로그 수집 및 학습 데이터셋 생성 파이프라인
→ 4단계: 대용량 로그와 실시간 이벤트 스트리밍
→ 5단계: AI 데이터 품질, 계보, 거버넌스
→ 6단계: RAG와 벡터 데이터 파이프라인
→ 최종 프로젝트: RAG 서비스용 문서 데이터 플랫폼 구축 프로젝트
→ 7단계: AI 서비스 피드백 데이터와 DataOps 운영
→ 기업 프로젝트: AI 서비스 데이터 품질 및 피드백 운영 플랫폼 프로젝트
```

브랜치 이름도 이 흐름과 같은 순서를 따른다.

---

## 3. 브랜치 네이밍 기본 규칙

### 3.1 기본 형식

```text
lesson/단계번호_단계핵심주제
project/프로젝트번호_프로젝트핵심주제
```

예시는 다음과 같다.

```text
lesson/01_ai_service_data_platform_architecture
project/01_ai_service_log_training_dataset_pipeline
```

---

### 3.2 작성 규칙

```text
1. 날짜를 넣지 않는다.
2. 수업 일차를 넣지 않는다.
3. 브랜치명은 전체 로드맵의 큰 단계명과 일치시킨다.
4. 영어 소문자와 숫자, 언더스코어만 사용한다.
5. 공백, 한글, 특수문자는 사용하지 않는다.
6. 공식 수업 브랜치는 단계별로 하나만 둔다.
7. 세부 실습 파일은 같은 단계 브랜치 안에서 커밋으로 관리한다.
```

---

## 4. 공식 브랜치 목록

### 4.1 전체 브랜치 목록

```text
main

lesson/00_project_baseline
lesson/01_ai_service_data_platform_architecture
lesson/02_data_collection_lakehouse_design
lesson/03_ai_workload_data_pipeline_automation

project/01_ai_service_log_training_dataset_pipeline

lesson/04_large_scale_log_realtime_event_streaming
lesson/05_ai_data_quality_lineage_governance
lesson/06_rag_vector_data_pipeline

project/02_rag_document_data_platform

lesson/07_ai_service_feedback_dataops

project/03_ai_service_data_quality_feedback_ops_platform
```

---

## 5. 단계별 브랜치 매핑

| 순서 | 전체 로드맵 단계 | 표준 브랜치명 | 브랜치 유형 |
|---:|---|---|---|
| 0 | 프로젝트 기준선 정리 | `lesson/00_project_baseline` | 기준선 |
| 1 | AI 서비스와 데이터 플랫폼 아키텍처 | `lesson/01_ai_service_data_platform_architecture` | 이론/실습 |
| 2 | 데이터 수집과 레이크하우스 설계 | `lesson/02_data_collection_lakehouse_design` | 이론/실습 |
| 3 | AI 워크로드를 위한 데이터 파이프라인 자동화 | `lesson/03_ai_workload_data_pipeline_automation` | 이론/실습 |
| P1 | AI 서비스 로그 수집 및 학습 데이터셋 생성 파이프라인 | `project/01_ai_service_log_training_dataset_pipeline` | 중간 프로젝트 |
| 4 | 대용량 로그와 실시간 이벤트 스트리밍 | `lesson/04_large_scale_log_realtime_event_streaming` | 이론/실습 |
| 5 | AI 데이터 품질, 계보, 거버넌스 | `lesson/05_ai_data_quality_lineage_governance` | 이론/실습 |
| 6 | RAG와 벡터 데이터 파이프라인 | `lesson/06_rag_vector_data_pipeline` | 이론/실습 |
| P2 | RAG 서비스용 문서 데이터 플랫폼 구축 프로젝트 | `project/02_rag_document_data_platform` | 최종 프로젝트 |
| 7 | AI 서비스 피드백 데이터와 DataOps 운영 | `lesson/07_ai_service_feedback_dataops` | 이론/실습 |
| P3 | AI 서비스 데이터 품질 및 피드백 운영 플랫폼 프로젝트 | `project/03_ai_service_data_quality_feedback_ops_platform` | 기업 프로젝트 |

---

## 6. 브랜치 생성 기준

브랜치는 항상 **직전 안정 브랜치**에서 새로 만든다.

```text
lesson/00_project_baseline
        ↓
lesson/01_ai_service_data_platform_architecture
        ↓
lesson/02_data_collection_lakehouse_design
        ↓
lesson/03_ai_workload_data_pipeline_automation
        ↓
project/01_ai_service_log_training_dataset_pipeline
        ↓
lesson/04_large_scale_log_realtime_event_streaming
        ↓
lesson/05_ai_data_quality_lineage_governance
        ↓
lesson/06_rag_vector_data_pipeline
        ↓
project/02_rag_document_data_platform
        ↓
lesson/07_ai_service_feedback_dataops
        ↓
project/03_ai_service_data_quality_feedback_ops_platform
```

이렇게 하면 학생이 어느 단계에서 실패하더라도 직전 브랜치로 돌아갈 수 있다.

---

## 7. 각 브랜치의 역할

### 7.1 `lesson/00_project_baseline`

0단계 기준선 브랜치이다.

이 브랜치에는 본격적인 기능 구현 코드를 넣지 않는다.

주요 목적은 다음과 같다.

```text
- 프로젝트 목적 정리
- 현재 상태 정리
- 수업 범위 정리
- 샘플 이벤트 정리
- seed 데이터 정리
- 브랜치 운영 기준 정리
```

주요 산출물은 다음과 같다.

```text
README.md
docs/current-state.md
docs/project-overview.md
docs/platform-scope.md
docs/branch-roadmap.md
sample_events/
seed/
```

---

### 7.2 `lesson/01_ai_service_data_platform_architecture`

1단계 브랜치이다.

전체 로드맵의 다음 단계에 해당한다.

```text
1단계: AI 서비스와 데이터 플랫폼 아키텍처
```

이 단계에서는 코드를 많이 작성하지 않는다.  
대신 이후 모든 코드가 따라갈 데이터 플랫폼 구조를 먼저 정의한다.

주요 산출물은 다음과 같다.

```text
README.md
docs/platform-scope.md
docs/ai-service-data-map.md
docs/domain-event-map.md
docs/c4-context.md
docs/c4-container.md
docs/data-flow-diagram.md
docs/tech-decision-table.md
docs/final-demo-scenario.md
```

핵심 질문은 다음이다.

```text
AI 서비스가 사용할 데이터는 어디서 생성되고, 어떤 흐름으로 이동하는가?
```

---

### 7.3 `lesson/02_data_collection_lakehouse_design`

2단계 브랜치이다.

전체 로드맵의 다음 단계에 해당한다.

```text
2단계: 데이터 수집과 레이크하우스 설계
```

이 단계에서는 데이터 계약과 저장 구조를 설계한다.

주요 산출물은 다음과 같다.

```text
schemas/
docs/data-contract.md
docs/schema-version-policy.md
docs/raw-staging-mart.md
docs/lakehouse-layout.md
docs/erd.md
collector/
sample_events/
seed/
data_lake/
```

핵심 질문은 다음이다.

```text
센서, 로그, 문서, 피드백 데이터는 어떤 계약으로 들어오고 어디에 저장되는가?
```

---

### 7.4 `lesson/03_ai_workload_data_pipeline_automation`

3단계 브랜치이다.

전체 로드맵의 다음 단계에 해당한다.

```text
3단계: AI 워크로드를 위한 데이터 파이프라인 자동화
```

이 단계에서는 반복되는 데이터 처리 작업을 Airflow 중심으로 자동화한다.

주요 산출물은 다음과 같다.

```text
airflow/dags/
docs/airflow-dag-flow.md
docs/backfill-policy.md
docs/idempotent-pipeline-policy.md
docs/training-dataset-definition.md
```

핵심 질문은 다음이다.

```text
Raw에서 Staging, Mart, Training Dataset까지 반복 작업을 어떻게 안정적으로 자동화할 것인가?
```

---

### 7.5 `project/01_ai_service_log_training_dataset_pipeline`

중간 프로젝트 브랜치이다.

전체 로드맵의 다음 프로젝트에 해당한다.

```text
중간 프로젝트: AI 서비스 로그 수집 및 학습 데이터셋 생성 파이프라인
```

이 프로젝트에서는 AI 서비스 로그와 오류 로그를 수집하고, 학습 데이터셋 후보로 정리한다.

주요 산출물은 다음과 같다.

```text
docs/mid-project-plan.md
docs/log-data-contract.md
docs/training-dataset-definition.md
docs/log-quality-report.md
collector/routes/logs.py
schemas/ai_service_log.schema.json
schemas/error_log.schema.json
airflow/dags/build_training_dataset_from_logs.py
data_lake/raw/ai_service_logs/
README_mid_project.md
```

핵심 질문은 다음이다.

```text
AI 서비스 운영 로그를 어떻게 학습 가능한 데이터셋으로 바꿀 것인가?
```

---

### 7.6 `lesson/04_large_scale_log_realtime_event_streaming`

4단계 브랜치이다.

전체 로드맵의 다음 단계에 해당한다.

```text
4단계: 대용량 로그와 실시간 이벤트 스트리밍
```

이 단계에서는 Kafka와 Spark를 통해 실시간 이벤트 처리 구조를 만든다.

주요 산출물은 다음과 같다.

```text
docs/kafka-topic-design.md
docs/streaming-flow.md
streaming/producers/
streaming/consumers/
streaming/spark/
templates/dashboard.html
static/js/dashboard_ws.js
```

핵심 질문은 다음이다.

```text
대량 이벤트를 실시간으로 안전하게 흘려보내고, 중복과 지연을 어떻게 처리할 것인가?
```

---

### 7.7 `lesson/05_ai_data_quality_lineage_governance`

5단계 브랜치이다.

전체 로드맵의 다음 단계에 해당한다.

```text
5단계: AI 데이터 품질, 계보, 거버넌스
```

이 단계에서는 데이터 품질과 계보, 권한 기준을 정리한다.

주요 산출물은 다음과 같다.

```text
dbt/
docs/data-quality-standard.md
docs/data-contract-review.md
docs/data-lineage.md
docs/drift-detection-policy.md
docs/pii-policy.md
docs/access-control-matrix.md
docs/data-quality-report.md
```

핵심 질문은 다음이다.

```text
AI와 RAG가 사용할 데이터가 믿을 수 있는 상태인지 어떻게 검증할 것인가?
```

---

### 7.8 `lesson/06_rag_vector_data_pipeline`

6단계 브랜치이다.

전체 로드맵의 다음 단계에 해당한다.

```text
6단계: RAG와 벡터 데이터 파이프라인
```

이 단계에서는 문서 데이터를 RAG 검색이 가능한 벡터 데이터로 변환한다.

주요 산출물은 다음과 같다.

```text
rag/
vector_db/
manifest/documents_manifest.json
schemas/rag_document_metadata.schema.json
docs/rag-data-pipeline.md
docs/document-metadata-policy.md
docs/chunking-strategy.md
docs/rag-search-quality-report.md
docs/document-freshness-policy.md
```

핵심 질문은 다음이다.

```text
문서를 어떻게 chunk, metadata, embedding으로 바꿔 RAG가 신뢰할 수 있게 검색하게 할 것인가?
```

---

### 7.9 `project/02_rag_document_data_platform`

최종 프로젝트 브랜치이다.

전체 로드맵의 다음 프로젝트에 해당한다.

```text
최종 프로젝트: RAG 서비스용 문서 데이터 플랫폼 구축 프로젝트
```

이 프로젝트에서는 RAG 문서 데이터 플랫폼을 하나의 결과물로 완성한다.

주요 산출물은 다음과 같다.

```text
docs/final-project-plan.md
docs/rag-document-platform-design.md
docs/rag-search-quality-report.md
rag/
vector_db/
manifest/documents_manifest.json
README_final_project.md
```

핵심 질문은 다음이다.

```text
알람 상황과 연결되는 신뢰 가능한 RAG 문서 검색 플랫폼을 어떻게 완성할 것인가?
```

---

### 7.10 `lesson/07_ai_service_feedback_dataops`

7단계 브랜치이다.

전체 로드맵의 다음 단계에 해당한다.

```text
7단계: AI 서비스 피드백 데이터와 DataOps 운영
```

이 단계에서는 피드백 데이터와 운영 모니터링을 연결한다.

주요 산출물은 다음과 같다.

```text
docs/feedback-data-contract.md
docs/dataops-monitoring-design.md
docs/retraining-candidate-policy.md
docs/service-observability.md
prometheus/
grafana/
.github/workflows/
```

핵심 질문은 다음이다.

```text
운영자 피드백과 서비스 로그를 어떻게 개선 사이클과 DataOps로 연결할 것인가?
```

---

### 7.11 `project/03_ai_service_data_quality_feedback_ops_platform`

기업 프로젝트 브랜치이다.

전체 로드맵의 다음 프로젝트에 해당한다.

```text
기업 프로젝트: AI 서비스 데이터 품질 및 피드백 운영 플랫폼 프로젝트
```

이 프로젝트에서는 앞 단계의 데이터 품질, 피드백, DataOps 구조를 통합한다.

주요 산출물은 다음과 같다.

```text
docs/enterprise-project-plan.md
docs/operation-scenario.md
docs/data-quality-feedback-platform-design.md
docs/final-operation-report.md
integrated_platform/
docker-compose.yml
k8s/
README_enterprise_project.md
```

핵심 질문은 다음이다.

```text
AI 서비스의 데이터 품질, 피드백, 운영 모니터링을 하나의 운영 플랫폼으로 어떻게 통합할 것인가?
```

---

## 8. 브랜치 생성 명령어

### 8.1 0단계 기준선 브랜치

```bash
git switch main
git pull origin main

git switch -c lesson/00_project_baseline
git push -u origin lesson/00_project_baseline
```

이미 브랜치가 존재한다면 다음처럼 이동한다.

```bash
git switch lesson/00_project_baseline
git pull origin lesson/00_project_baseline
```

---

### 8.2 1단계 브랜치 생성

```bash
git switch lesson/00_project_baseline
git pull origin lesson/00_project_baseline

git switch -c lesson/01_ai_service_data_platform_architecture
git push -u origin lesson/01_ai_service_data_platform_architecture
```

---

### 8.3 2단계 브랜치 생성

```bash
git switch lesson/01_ai_service_data_platform_architecture
git pull origin lesson/01_ai_service_data_platform_architecture

git switch -c lesson/02_data_collection_lakehouse_design
git push -u origin lesson/02_data_collection_lakehouse_design
```

---

### 8.4 3단계 브랜치 생성

```bash
git switch lesson/02_data_collection_lakehouse_design
git pull origin lesson/02_data_collection_lakehouse_design

git switch -c lesson/03_ai_workload_data_pipeline_automation
git push -u origin lesson/03_ai_workload_data_pipeline_automation
```

---

### 8.5 중간 프로젝트 브랜치 생성

```bash
git switch lesson/03_ai_workload_data_pipeline_automation
git pull origin lesson/03_ai_workload_data_pipeline_automation

git switch -c project/01_ai_service_log_training_dataset_pipeline
git push -u origin project/01_ai_service_log_training_dataset_pipeline
```

---

### 8.6 4단계 브랜치 생성

```bash
git switch project/01_ai_service_log_training_dataset_pipeline
git pull origin project/01_ai_service_log_training_dataset_pipeline

git switch -c lesson/04_large_scale_log_realtime_event_streaming
git push -u origin lesson/04_large_scale_log_realtime_event_streaming
```

---

### 8.7 5단계 브랜치 생성

```bash
git switch lesson/04_large_scale_log_realtime_event_streaming
git pull origin lesson/04_large_scale_log_realtime_event_streaming

git switch -c lesson/05_ai_data_quality_lineage_governance
git push -u origin lesson/05_ai_data_quality_lineage_governance
```

---

### 8.8 6단계 브랜치 생성

```bash
git switch lesson/05_ai_data_quality_lineage_governance
git pull origin lesson/05_ai_data_quality_lineage_governance

git switch -c lesson/06_rag_vector_data_pipeline
git push -u origin lesson/06_rag_vector_data_pipeline
```

---

### 8.9 최종 프로젝트 브랜치 생성

```bash
git switch lesson/06_rag_vector_data_pipeline
git pull origin lesson/06_rag_vector_data_pipeline

git switch -c project/02_rag_document_data_platform
git push -u origin project/02_rag_document_data_platform
```

---

### 8.10 7단계 브랜치 생성

```bash
git switch project/02_rag_document_data_platform
git pull origin project/02_rag_document_data_platform

git switch -c lesson/07_ai_service_feedback_dataops
git push -u origin lesson/07_ai_service_feedback_dataops
```

---

### 8.11 기업 프로젝트 브랜치 생성

```bash
git switch lesson/07_ai_service_feedback_dataops
git pull origin lesson/07_ai_service_feedback_dataops

git switch -c project/03_ai_service_data_quality_feedback_ops_platform
git push -u origin project/03_ai_service_data_quality_feedback_ops_platform
```

---

## 9. 기존 브랜치 정리 기준

기존의 일차/세부순서 기반 브랜치는 더 이상 공식 브랜치로 사용하지 않는다.

예시는 다음과 같다.

```text
lesson/01_01_project_overview
lesson/01_02_template_static_structure
lesson/01_03_django_run_readme
lesson/01_01_architecture_domain_events
```

이런 브랜치는 전체 로드맵 기준과 맞지 않으므로 삭제하거나 보관용으로만 둔다.

원격 브랜치를 삭제할 때는 다음 명령어를 사용한다.

```bash
git push origin --delete lesson/01_01_architecture_domain_events
```

로컬 브랜치가 있다면 다음 명령어로 삭제한다.

```bash
git branch -D lesson/01_01_architecture_domain_events
```

원격 브랜치 목록을 정리한다.

```bash
git fetch --prune
```

---

## 10. 학생 안내 원칙

학생에게는 공식 브랜치 목록만 안내한다.

세부 실습은 브랜치를 계속 쪼개지 않고 같은 단계 브랜치 안에서 커밋 단위로 관리한다.

예를 들어 1단계에서는 다음 브랜치 하나만 사용한다.

```text
lesson/01_ai_service_data_platform_architecture
```

커밋 예시는 다음과 같다.

```text
docs: define platform scope
docs: add AI service data map
docs: add domain event map
docs: add C4 context and container diagrams
docs: add data flow diagram
```

이 방식이 좋은 이유는 다음과 같다.

```text
1. 학생이 현재 어느 단계에 있는지 쉽게 알 수 있다.
2. GitHub 브랜치 목록이 복잡해지지 않는다.
3. 날짜가 바뀌어도 브랜치명을 수정할 필요가 없다.
4. 전체 로드맵과 브랜치 구조가 일치한다.
5. 강사가 단계별 기준 브랜치를 안정적으로 제공할 수 있다.
```

---

## 11. 최종 요약

공식 브랜치 구조는 다음과 같다.

```text
main

lesson/00_project_baseline
lesson/01_ai_service_data_platform_architecture
lesson/02_data_collection_lakehouse_design
lesson/03_ai_workload_data_pipeline_automation

project/01_ai_service_log_training_dataset_pipeline

lesson/04_large_scale_log_realtime_event_streaming
lesson/05_ai_data_quality_lineage_governance
lesson/06_rag_vector_data_pipeline

project/02_rag_document_data_platform

lesson/07_ai_service_feedback_dataops

project/03_ai_service_data_quality_feedback_ops_platform
```

한 줄로 정리하면 다음과 같다.

```text
브랜치 이름은 수업 날짜가 아니라 전체 로드맵의 단계 이름을 기준으로 만든다.
```
