![[Group 166.png]]

# Staging Parquet을 DuckDB로 조회하는 처리 순서

이 단계는 Staging Parquet을 다시 변환하거나 데이터베이스 테이블에 적재하는 과정이 아닙니다.

이미 생성된 다음 파일을 DuckDB SQL로 직접 읽어 조회하고 검증합니다.

```text
data_lake/staging/order_events/order_events.parquet
```

실행 명령:

```bash
python scripts/query_staging_duckdb.py
```

전체 흐름:

```text
조회 스크립트 실행
→ Staging 파일 경로 계산
→ query_staging() 호출
→ Staging Parquet 존재 확인
→ 메모리 기반 DuckDB 연결 생성
→ 첫 번째 SQL로 전체 주문 조회
→ 결과를 pandas DataFrame으로 반환
→ 터미널 출력
→ 두 번째 SQL로 주문 집계
→ 집계 결과를 DataFrame으로 반환
→ 터미널 출력
→ DuckDB 연결 종료
```

---

## ① 프로젝트 루트에서 DuckDB 조회 스크립트 실행

```bash
python scripts/query_staging_duckdb.py
```

Python은 다음 파일을 직접 실행합니다.

```text
scripts/query_staging_duckdb.py
```

이 명령은 Collector 서버를 호출하지 않습니다.

```text
FastAPI 서버 필요
X

Staging Parquet 파일 필요
O
```

따라서 다음 파일만 존재하면 서버를 끈 상태에서도 조회할 수 있습니다.

```text
data_lake/staging/order_events/order_events.parquet
```

---

## ② 필요한 모듈 불러오기

```python
from pathlib import Path

import duckdb
```

역할:

| 모듈 | 역할 |
|---|---|
| `Path` | Staging Parquet 파일 경로 관리 |
| `duckdb` | Parquet 파일에 SQL 실행 |

이 단계에서는 아직 Parquet 파일을 읽지 않습니다.

DuckDB 기능을 사용할 준비만 합니다.

---

## ③ 프로젝트 루트 경로 계산

```python
PROJECT_ROOT = Path(__file__).resolve().parents[1]
```

현재 파일:

```text
project-root/scripts/query_staging_duckdb.py
```

경로 계산:

```text
parents[0]
→ scripts/

parents[1]
→ project-root/
```

결과적으로 `PROJECT_ROOT`는 프로젝트 최상위 폴더를 가리킵니다.

---

## ④ 조회할 Staging 파일 경로 설정

```python
STAGING_FILE = (
    PROJECT_ROOT
    / "data_lake"
    / "staging"
    / "order_events"
    / "order_events.parquet"
)
```

실제 경로:

```text
data_lake/staging/order_events/order_events.parquet
```

이 단계에서는 경로만 준비합니다.

```text
Parquet 읽기
X

SQL 실행
X

조회 대상 경로 설정
O
```

---

## ⑤ 직접 실행 여부 확인

파일 맨 아래의 다음 코드가 실행됩니다.

```python
if __name__ == "__main__":
    query_staging()
```

다음 명령으로 직접 실행했기 때문에:

```bash
python scripts/query_staging_duckdb.py
```

조건이 참이 되고 `query_staging()` 함수가 호출됩니다.

---

## ⑥ `query_staging()` 함수 시작

```python
def query_staging() -> None:
```

이 함수는 다음 작업을 관리합니다.

```text
파일 확인
→ DuckDB 연결
→ 전체 데이터 조회
→ 집계 데이터 조회
→ 결과 출력
→ 연결 종료
```

---

## ⑦ Staging Parquet 파일 존재 여부 확인

```python
if not STAGING_FILE.exists():
    raise FileNotFoundError(
        f"Staging 파일을 찾을 수 없습니다: {STAGING_FILE}"
    )
```

Staging 파일이 없으면 SQL을 실행할 수 없습니다.

```text
Staging 파일 없음
↓
FileNotFoundError 발생
↓
프로그램 종료
```

이 경우 먼저 다음 명령으로 Staging을 만들어야 합니다.

```bash
python scripts/raw_to_staging_parquet.py
```

---

## ⑧ DuckDB 연결 생성

```python
connection = duckdb.connect()
```

파일 경로를 지정하지 않았으므로 메모리 기반 DuckDB 연결이 만들어집니다.

```text
duckdb.connect()
→ 현재 Python 프로세스에서 사용할 임시 연결
```

이 코드는 별도의 DuckDB 서버를 시작하지 않습니다.

```text
DuckDB 서버 설치·실행
X

Python 프로세스 안에서 분석 엔진 연결 생성
O
```

또한 Staging Parquet을 DuckDB 내부 테이블로 영구 저장하는 것도 아닙니다.

```text
Parquet 파일
→ read_parquet()로 직접 읽어 SQL 실행
```

---

## ⑨ `try` 블록 시작

```python
try:
```

조회 작업을 `try` 안에서 수행하는 이유는 조회 중 오류가 발생하더라도 마지막에 연결을 종료하기 위해서입니다.

```text
조회 성공
또는
조회 실패
↓
finally 실행
↓
connection.close()
```

---

## ⑩ 전체 주문 이벤트 조회 안내 출력

```python
print("\n[전체 주문 이벤트]")
```

터미널에 다음 제목이 출력됩니다.

```text
[전체 주문 이벤트]
```

---

## ⑪ 첫 번째 SQL 실행

```python
result = connection.execute(
    """
    SELECT
        event_id,
        order_id,
        customer_id,
        total_amount,
        currency,
        item_count,
        event_time
    FROM read_parquet(?)
    ORDER BY event_time
    """,
    [str(STAGING_FILE)]
).fetchdf()
```

처리 흐름:

```text
connection.execute()
↓
DuckDB가 SQL 해석
↓
read_parquet(?)로 Staging 파일 읽기
↓
필요한 컬럼 선택
↓
event_time 순으로 정렬
↓
fetchdf()로 pandas DataFrame 반환
```

---

## ⑫ `read_parquet(?)`가 Parquet을 테이블처럼 읽기

SQL의 다음 부분이 Staging 파일을 직접 읽습니다.

```sql
FROM read_parquet(?)
```

`?`에는 다음 값이 전달됩니다.

```python
[str(STAGING_FILE)]
```

즉:

```text
?
↓
data_lake/staging/order_events/order_events.parquet
```

경로를 문자열 결합으로 SQL 안에 직접 넣지 않고 매개변수로 전달합니다.

이 방식은 경로와 SQL 문장을 분리하여 더 안전하고 명확하게 관리할 수 있습니다.

---

## ⑬ 조회할 컬럼 선택

```sql
SELECT
    event_id,
    order_id,
    customer_id,
    total_amount,
    currency,
    item_count,
    event_time
```

Staging Parquet에서 필요한 컬럼만 선택합니다.

여기서 `order_id`, `customer_id`, `total_amount` 등을 바로 선택할 수 있는 이유는 Raw의 `payload`가 Staging 단계에서 이미 평탄화되었기 때문입니다.

```text
Raw
→ payload.order_id

Staging
→ order_id
```

---

## ⑭ 이벤트 발생 시간 순으로 정렬

```sql
ORDER BY event_time
```

의미:

```text
주문 이벤트 전체 조회
↓
event_time이 빠른 순서대로 정렬
```

---

## ⑮ `fetchdf()`로 SQL 결과를 DataFrame으로 받기

```python
.fetchdf()
```

DuckDB SQL 결과를 pandas DataFrame으로 변환하여 `result` 변수에 저장합니다.

```text
DuckDB SQL 결과
→ pandas DataFrame
→ result
```

이 코드는 조회 결과를 Parquet에 다시 저장하지 않습니다.

메모리에 DataFrame으로 가져오는 단계입니다.

---

## ⑯ 전체 주문 이벤트 결과 출력

```python
print(result)
```

예상 출력:

```text
        event_id      order_id customer_id  total_amount currency  item_count                event_time
0  evt-order-001    ORDER-1001    USER-001       89000.0      KRW           3 2026-07-21 04:00:00+00:00
```

표시되는 시간은 Staging 생성 과정에서 UTC로 변환된 값일 수 있습니다.

예:

```text
입력
2026-07-21T13:00:00+09:00

UTC 변환
2026-07-21 04:00:00+00:00
```

---

## ⑰ 주문 요약 안내 출력

```python
print("\n[주문 요약]")
```

터미널에 다음 제목을 출력합니다.

```text
[주문 요약]
```

---

## ⑱ 두 번째 집계 SQL 실행

```python
summary = connection.execute(
    """
    SELECT
        COUNT(*) AS order_count,
        SUM(total_amount) AS total_sales,
        AVG(total_amount) AS average_order_amount,
        SUM(item_count) AS total_item_count
    FROM read_parquet(?)
    """,
    [str(STAGING_FILE)]
).fetchdf()
```

처리 흐름:

```text
Staging Parquet 다시 읽기
↓
전체 주문 건수 계산
↓
총 주문 금액 계산
↓
평균 주문 금액 계산
↓
총 상품 개수 계산
↓
DataFrame으로 반환
```

---

## ⑲ 집계 함수별 의미

### 주문 건수

```sql
COUNT(*) AS order_count
```

```text
전체 행의 개수
→ 주문 이벤트 건수
```

### 총매출

```sql
SUM(total_amount) AS total_sales
```

```text
모든 total_amount 합계
→ 총 주문 금액
```

### 평균 주문 금액

```sql
AVG(total_amount) AS average_order_amount
```

```text
total_amount 평균
→ 주문 한 건당 평균 금액
```

### 총 상품 개수

```sql
SUM(item_count) AS total_item_count
```

```text
모든 item_count 합계
→ 주문된 전체 상품 수
```

---

## ⑳ 집계 결과를 DataFrame으로 받기

두 번째 SQL 끝에도 다음 코드가 있습니다.

```python
.fetchdf()
```

집계 결과가 pandas DataFrame으로 변환되어 `summary` 변수에 저장됩니다.

```text
집계 SQL 결과
→ pandas DataFrame
→ summary
```

---

## ㉑ 주문 요약 결과 출력

```python
print(summary)
```

예상 결과:

```text
   order_count  total_sales  average_order_amount  total_item_count
0            1      89000.0               89000.0               3.0
```

주문 데이터가 여러 건이면 모든 행을 기준으로 집계됩니다.

---

## ㉒ `finally` 블록 실행

```python
finally:
    connection.close()
```

조회 성공 여부와 관계없이 반드시 실행됩니다.

```text
전체 조회 성공
→ 집계 조회 성공
→ 연결 종료

또는

조회 중 오류 발생
→ 연결 종료
```

---

## ㉓ DuckDB 연결 종료

```python
connection.close()
```

현재 Python 프로세스에서 사용하던 DuckDB 연결을 닫습니다.

파일 기반 DB를 만든 것이 아니므로 별도의 데이터베이스 파일을 저장하는 과정은 없습니다.

```text
DuckDB 연결 종료
→ 프로그램 종료
```

---

# 파일별 최종 처리 순서

```text
① python scripts/query_staging_duckdb.py
↓
② scripts/query_staging_duckdb.py 시작
↓
③ PROJECT_ROOT 계산
↓
④ STAGING_FILE 경로 설정
↓
⑤ query_staging() 호출
↓
⑥ Staging Parquet 존재 여부 확인
↓
⑦ duckdb.connect()로 메모리 연결 생성
↓
⑧ try 블록 시작
↓
⑨ 첫 번째 SELECT 실행
↓
⑩ read_parquet(?)로 Staging 파일 직접 읽기
↓
⑪ 필요한 컬럼 선택
↓
⑫ event_time 순으로 정렬
↓
⑬ fetchdf()로 DataFrame 반환
↓
⑭ 전체 주문 데이터 출력
↓
⑮ 두 번째 집계 SELECT 실행
↓
⑯ COUNT·SUM·AVG 계산
↓
⑰ fetchdf()로 집계 DataFrame 반환
↓
⑱ 주문 요약 출력
↓
⑲ finally 실행
↓
⑳ connection.close()로 DuckDB 연결 종료
```

---

# DuckDB가 이 단계에서 하는 역할

```text
Staging Parquet
→ 분석할 대상 데이터

DuckDB
→ Parquet 파일에 SQL을 실행하는 분석 엔진

pandas DataFrame
→ SQL 조회 결과를 Python에서 표현하는 표 구조
```

DuckDB는 Staging Parquet 전용 도구는 아닙니다.

다음 데이터도 SQL로 조회할 수 있습니다.

```text
Parquet
CSV
JSON
DuckDB 내부 테이블
Pandas DataFrame
```

이 실습에서는 별도의 데이터베이스 서버나 적재 과정 없이 Parquet을 바로 SQL로 조회할 수 있어서 DuckDB를 사용합니다.

---

# 이 단계에서 데이터가 변경되는가?

```text
Staging Parquet 읽기
→ SQL 조회
→ 터미널 출력
```

따라서:

```text
Raw 변경
X

Staging 변경
X

Mart 생성
X

조회와 검증
O
```

이 스크립트는 Staging 결과가 분석 가능한 구조인지 확인하는 조회 프로그램입니다.

---

# 그림에서 번호를 붙일 때 권장 순서

```text
1. DuckDB 조회 스크립트 실행
2. Staging 파일 경로 설정
3. query_staging() 호출
4. Staging 파일 존재 확인
5. DuckDB 연결 생성
6. 전체 주문 SELECT 실행
7. read_parquet()로 Parquet 읽기
8. event_time 순 정렬
9. 결과를 DataFrame으로 변환
10. 전체 주문 출력
11. 집계 SELECT 실행
12. 주문 건수·총매출·평균·상품 수 계산
13. 집계 결과 출력
14. DuckDB 연결 종료
```
