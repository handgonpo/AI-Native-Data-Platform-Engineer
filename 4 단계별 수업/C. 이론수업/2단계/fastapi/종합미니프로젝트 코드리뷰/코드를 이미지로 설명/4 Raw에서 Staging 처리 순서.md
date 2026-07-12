![[Group 166.png]]

# Raw JSONL에서 Staging Parquet으로 변환되는 처리 순서

이 단계는 Collector 서버가 데이터를 받는 과정과 별개의 실행입니다.

이미 다음 Raw 파일이 존재하면 서버를 끈 상태에서도 실행할 수 있습니다.

```text
data_lake/raw/order_events/order_events.jsonl
```

실행 명령:

```bash
python scripts/raw_to_staging_parquet.py
```

전체 흐름은 다음과 같습니다.

```text
실행 명령 입력
→ raw_to_staging_parquet.py 시작
→ Raw·Staging 파일 경로 계산
→ build_staging_parquet() 호출
→ read_jsonl()로 Raw JSONL 읽기
→ JSON 한 줄씩 Python dict로 변환
→ flatten_order_event()로 payload 평탄화
→ pandas DataFrame 생성
→ 날짜·금액·상품 수 타입 정리
→ Staging 폴더 생성
→ Parquet 파일 저장
→ 생성 경로와 변환 건수 출력
```

---

## ① 프로젝트 루트에서 변환 스크립트 실행

```bash
python scripts/raw_to_staging_parquet.py
```

Python은 다음 파일을 직접 실행합니다.

```text
scripts/raw_to_staging_parquet.py
```

이 명령은 FastAPI 서버나 Collector API를 호출하지 않습니다.

```text
API 서버 호출
X

Raw JSONL 파일 직접 읽기
O
```

따라서 다음 조건만 충족하면 실행할 수 있습니다.

```text
가상환경 활성화
Raw JSONL 파일 존재
pandas와 pyarrow 설치
프로젝트 루트에서 명령 실행
```

---

## ② 모듈과 라이브러리 불러오기

스크립트 상단에서 다음 모듈을 불러옵니다.

```python
import json
from pathlib import Path
from typing import Any

import pandas as pd
```

각 역할은 다음과 같습니다.

| 모듈 | 역할 |
|---|---|
| `json` | JSON 문자열을 Python 딕셔너리로 변환 |
| `Path` | Raw와 Staging 파일 경로 관리 |
| `Any` | 다양한 값이 들어가는 딕셔너리 타입 표현 |
| `pandas` | 표 형태의 DataFrame 생성과 Parquet 저장 |

이 단계에서는 아직 Raw 데이터를 읽지 않습니다.

Python이 이후에 사용할 도구들을 준비하는 단계입니다.

---

## ③ 프로젝트 루트 경로 계산

다음 코드가 실행됩니다.

```python
PROJECT_ROOT = Path(__file__).resolve().parents[1]
```

현재 실행 중인 파일 위치:

```text
project-root/scripts/raw_to_staging_parquet.py
```

경로 계산:

```text
__file__
→ scripts/raw_to_staging_parquet.py

resolve()
→ 절대 경로로 변환

parents[0]
→ scripts/

parents[1]
→ project-root/
```

결과적으로 `PROJECT_ROOT`에는 프로젝트 최상위 폴더 경로가 저장됩니다.

---

## ④ Raw 입력 파일과 Staging 출력 파일 경로 설정

Raw 파일 경로:

```python
RAW_FILE = (
    PROJECT_ROOT
    / "data_lake"
    / "raw"
    / "order_events"
    / "order_events.jsonl"
)
```

실제 경로:

```text
data_lake/raw/order_events/order_events.jsonl
```

Staging 파일 경로:

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

이 단계는 경로를 변수에 저장할 뿐입니다.

```text
파일 읽기
X

파일 저장
X

입력·출력 위치 준비
O
```

---

## ⑤ 직접 실행 여부 확인

파일 맨 아래의 다음 코드가 실행됩니다.

```python
if __name__ == "__main__":
    build_staging_parquet()
```

현재 파일을 다음과 같이 직접 실행했기 때문에:

```bash
python scripts/raw_to_staging_parquet.py
```

조건이 참이 됩니다.

```text
__name__ == "__main__"
→ True
```

그래서 다음 함수가 호출됩니다.

```python
build_staging_parquet()
```

---

## ⑥ `build_staging_parquet()` 함수 시작

```python
def build_staging_parquet() -> None:
```

이 함수가 Raw에서 Staging으로 변환하는 전체 작업을 관리합니다.

가장 먼저 다음 코드를 실행합니다.

```python
raw_records = read_jsonl(RAW_FILE)
```

연결 흐름:

```text
build_staging_parquet()
↓
read_jsonl(RAW_FILE)
```

---

## ⑦ `read_jsonl()`이 Raw 파일 존재 여부 확인

```python
if not file_path.exists():
    raise FileNotFoundError(
        f"Raw 파일을 찾을 수 없습니다: {file_path}"
    )
```

Raw 파일이 없으면 변환 작업을 계속할 수 없습니다.

```text
Raw 파일 없음
↓
FileNotFoundError 발생
↓
프로그램 종료
```

Raw 파일이 있으면 다음 단계로 이동합니다.

---

## ⑧ Raw JSONL 파일을 읽기 모드로 열기

```python
with file_path.open(
    "r",
    encoding="utf-8"
) as file:
```

의미:

```text
"r"
→ 읽기 모드

encoding="utf-8"
→ 한글을 포함한 JSON을 올바르게 읽기
```

Raw 파일은 다음처럼 한 줄에 이벤트 하나가 저장되어 있습니다.

```json
{"event_id":"evt-order-001","event_type":"order_created","payload":{"order_id":"ORDER-1001","total_amount":89000}}
{"event_id":"evt-order-002","event_type":"order_created","payload":{"order_id":"ORDER-1002","total_amount":45000}}
```

---

## ⑨ JSONL을 한 줄씩 순회

```python
for line_number, line in enumerate(
    file,
    start=1
):
```

각 반복에서 다음 두 값을 가져옵니다.

| 값 | 의미 |
|---|---|
| `line_number` | 현재 줄 번호 |
| `line` | 해당 줄의 JSON 문자열 |

줄 번호는 오류가 발생한 위치를 알려주기 위해 사용합니다.

---

## ⑩ 공백과 빈 줄 처리

```python
stripped_line = line.strip()

if not stripped_line:
    continue
```

처리 흐름:

```text
줄 앞뒤 공백과 줄바꿈 제거
↓
빈 줄인지 확인
↓
빈 줄이면 건너뜀
```

빈 줄은 데이터 레코드가 아니므로 변환 대상에서 제외합니다.

---

## ⑪ JSON 문자열을 Python 딕셔너리로 변환

```python
records.append(
    json.loads(stripped_line)
)
```

변환 전:

```json
"{\"event_id\":\"evt-order-001\", ...}"
```

변환 후:

```python
{
    "event_id": "evt-order-001",
    "event_type": "order_created",
    "payload": {
        "order_id": "ORDER-1001",
        "total_amount": 89000
    }
}
```

즉:

```text
JSON 문자열 한 줄
→ Python dict 한 건
→ records 목록에 추가
```

---

## ⑫ 잘못된 JSON 형식 처리

JSON 문법이 잘못되어 있으면 다음 예외가 발생합니다.

```python
except json.JSONDecodeError as error:
    raise ValueError(
        f"{line_number}번째 줄의 JSON 형식이 잘못되었습니다."
    ) from error
```

예를 들어 쉼표나 중괄호가 잘못된 경우입니다.

```text
잘못된 JSON 발견
↓
JSONDecodeError 발생
↓
몇 번째 줄인지 포함한 ValueError로 변환
↓
프로그램 종료
```

이 검사는 API의 Pydantic 데이터 계약 검증과 다릅니다.

```text
Pydantic 검증
→ 필드, 타입, 범위 등 데이터 계약 검사

JSONDecodeError 검사
→ JSON 문법 자체가 올바른지 검사
```

---

## ⑬ `read_jsonl()`이 Raw 레코드 목록 반환

모든 줄을 정상적으로 읽으면 다음 값이 반환됩니다.

```python
return records
```

형태:

```python
[
    {
        "event_id": "evt-order-001",
        "payload": {
            "order_id": "ORDER-1001",
            "total_amount": 89000
        }
    },
    {
        "event_id": "evt-order-002",
        "payload": {
            "order_id": "ORDER-1002",
            "total_amount": 45000
        }
    }
]
```

반환 흐름:

```text
read_jsonl()
↓
build_staging_parquet()
↓
raw_records 변수에 저장
```

---

## ⑭ 변환할 Raw 데이터가 있는지 확인

```python
if not raw_records:
    print("변환할 Raw 데이터가 없습니다.")
    return
```

Raw 파일은 존재하지만 내용이 비어 있을 수 있습니다.

```text
Raw 레코드 0건
↓
안내 메시지 출력
↓
함수 종료
↓
Staging 파일 생성 안 함
```

레코드가 한 건 이상 있으면 평탄화 단계로 이동합니다.

---

## ⑮ `flatten_order_event()`로 각 이벤트 평탄화

다음 리스트 컴프리헨션이 실행됩니다.

```python
staging_records = [
    flatten_order_event(record)
    for record in raw_records
]
```

각 Raw 레코드가 한 번씩 다음 함수에 전달됩니다.

```python
flatten_order_event(record)
```

함수 안에서는 먼저 `payload`를 가져옵니다.

```python
payload = record.get("payload", {})
```

그다음 공통 필드와 `payload` 내부 필드를 하나의 딕셔너리로 만듭니다.

```python
return {
    "event_id": record.get("event_id"),
    "event_type": record.get("event_type"),
    "schema_version": record.get("schema_version"),
    "source_system": record.get("source_system"),
    "event_time": record.get("event_time"),
    "order_id": payload.get("order_id"),
    "customer_id": payload.get("customer_id"),
    "total_amount": payload.get("total_amount"),
    "currency": payload.get("currency"),
    "item_count": payload.get("item_count")
}
```

---

## ⑯ Raw의 중첩 구조를 평탄한 컬럼 구조로 변환

Raw 구조:

```json
{
  "event_id": "evt-order-001",
  "event_type": "order_created",
  "payload": {
    "order_id": "ORDER-1001",
    "customer_id": "USER-001",
    "total_amount": 89000,
    "currency": "KRW",
    "item_count": 3
  }
}
```

평탄화된 구조:

```python
{
    "event_id": "evt-order-001",
    "event_type": "order_created",
    "order_id": "ORDER-1001",
    "customer_id": "USER-001",
    "total_amount": 89000,
    "currency": "KRW",
    "item_count": 3
}
```

핵심 변화:

```text
payload.order_id
→ order_id 컬럼

payload.customer_id
→ customer_id 컬럼

payload.total_amount
→ total_amount 컬럼

payload.currency
→ currency 컬럼

payload.item_count
→ item_count 컬럼
```

`payload`라는 중첩 객체를 제거하고, 내부 값을 동일한 행의 컬럼으로 꺼냅니다.

---

## ⑰ pandas DataFrame 생성

평탄화된 레코드 목록으로 표 형태의 DataFrame을 만듭니다.

```python
dataframe = pd.DataFrame(staging_records)
```

구조:

```text
event_id | event_type | order_id | customer_id | total_amount | currency | item_count | event_time
```

예시:

| event_id | order_id | customer_id | total_amount | currency | item_count |
|---|---|---|---:|---|---:|
| evt-order-001 | ORDER-1001 | USER-001 | 89000 | KRW | 3 |

이때부터 각 필드를 컬럼 단위로 처리할 수 있습니다.

---

## ⑱ `event_time`을 날짜·시간 타입으로 표준화

```python
dataframe["event_time"] = pd.to_datetime(
    dataframe["event_time"],
    errors="coerce",
    utc=True
)
```

처리 내용:

```text
문자열 날짜
→ pandas datetime 타입

서로 다른 시간대
→ UTC 기준으로 통일
```

`errors="coerce"`의 의미:

```text
정상 날짜
→ datetime으로 변환

잘못된 날짜
→ 오류로 프로그램을 중단하지 않고 NaT로 변환
```

여기서 `NaT`는 날짜·시간 값이 유효하지 않다는 뜻입니다.

---

## ⑲ `total_amount`를 숫자 타입으로 표준화

```python
dataframe["total_amount"] = pd.to_numeric(
    dataframe["total_amount"],
    errors="coerce"
)
```

처리 내용:

```text
89000
→ 숫자

"89000"
→ 가능한 경우 숫자로 변환

"비쌈"
→ NaN
```

`NaN`은 유효한 숫자로 바꾸지 못했다는 뜻입니다.

---

## ⑳ `item_count`를 nullable 정수 타입으로 표준화

```python
dataframe["item_count"] = pd.to_numeric(
    dataframe["item_count"],
    errors="coerce"
).astype("Int64")
```

처리 순서:

```text
item_count 값을 숫자로 변환
↓
잘못된 값은 NaN 처리
↓
Int64 타입으로 변환
```

여기서 pandas의 `"Int64"`는 결측값을 허용하는 정수 타입입니다.

```text
일반 int
→ 결측값을 다루기 어려움

pandas Int64
→ 정수와 결측값을 함께 표현 가능
```

---

## ㉑ Staging 저장 폴더 생성

```python
STAGING_FILE.parent.mkdir(
    parents=True,
    exist_ok=True
)
```

예상 폴더:

```text
data_lake/staging/order_events/
```

옵션:

```text
parents=True
→ 필요한 상위 폴더까지 함께 생성

exist_ok=True
→ 폴더가 이미 있어도 오류를 발생시키지 않음
```

---

## ㉒ DataFrame을 Staging Parquet으로 저장

```python
dataframe.to_parquet(
    STAGING_FILE,
    index=False
)
```

저장 위치:

```text
data_lake/staging/order_events/order_events.parquet
```

`index=False`의 의미:

```text
pandas가 자동으로 만든 행 번호
→ Parquet 컬럼으로 저장하지 않음
```

중요한 점:

```text
같은 경로의 Parquet 파일이 이미 존재하면
→ 현재 DataFrame 결과로 다시 저장되어 교체됨
```

즉, 이 2단계 스크립트는 기존 Staging 파일 끝에 데이터를 추가하는 방식이 아니라, Raw 전체를 다시 읽어 Staging 파일을 재생성하는 방식입니다.

---

## ㉓ 생성 완료 결과 출력

```python
print(
    f"Staging Parquet 생성 완료: {STAGING_FILE}"
)

print(
    f"변환 건수: {len(dataframe)}"
)
```

예상 출력:

```text
Staging Parquet 생성 완료:
.../data_lake/staging/order_events/order_events.parquet

변환 건수: 1
```

---

# 파일별 최종 처리 순서

```text
① python scripts/raw_to_staging_parquet.py
↓
② scripts/raw_to_staging_parquet.py 시작
↓
③ PROJECT_ROOT 계산
↓
④ RAW_FILE·STAGING_FILE 경로 설정
↓
⑤ build_staging_parquet() 호출
↓
⑥ read_jsonl(RAW_FILE) 호출
↓
⑦ Raw JSONL 존재 여부 확인
↓
⑧ Raw JSONL 파일 열기
↓
⑨ 한 줄씩 읽기
↓
⑩ 빈 줄 제외
↓
⑪ json.loads()로 Python dict 변환
↓
⑫ Raw 레코드 목록 반환
↓
⑬ flatten_order_event() 반복 호출
↓
⑭ payload 내부 필드를 바깥 컬럼으로 평탄화
↓
⑮ pandas DataFrame 생성
↓
⑯ event_time을 UTC datetime으로 변환
↓
⑰ total_amount를 숫자로 변환
↓
⑱ item_count를 nullable Int64로 변환
↓
⑲ Staging 폴더 생성
↓
⑳ DataFrame을 Parquet으로 저장
↓
㉑ 생성 경로와 변환 건수 출력
```

---

# Raw와 Staging의 차이

```text
Raw JSONL
→ API로 들어온 이벤트를 원본에 가깝게 보존

Staging Parquet
→ payload 평탄화와 타입 표준화가 끝난 분석용 중간 데이터
```

이 스크립트가 수행하는 핵심은 다음과 같습니다.

```text
Raw 원본을 삭제하거나 수정하는 것이 아니라
Raw를 읽어서 별도의 Staging 결과를 새로 만든다.
```

---

# 그림에서 번호를 붙일 때 권장 순서

```text
1. 변환 스크립트 실행
2. Raw·Staging 경로 설정
3. build_staging_parquet() 호출
4. read_jsonl() 호출
5. Raw 파일 존재 확인
6. JSONL 한 줄씩 읽기
7. JSON 문자열을 dict로 변환
8. flatten_order_event() 호출
9. payload 평탄화
10. DataFrame 생성
11. 날짜·숫자·정수 타입 표준화
12. Staging 폴더 생성
13. Parquet 저장
14. 완료 경로와 변환 건수 출력
```
