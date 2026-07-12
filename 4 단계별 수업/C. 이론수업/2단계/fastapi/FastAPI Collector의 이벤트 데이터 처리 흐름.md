![[Pasted image 20260710122654.png]]

```text
1. 클라이언트가 URL로 HTTP 요청을 보낸다.
2. FastAPI가 요청의 URL과 GET·POST 방식을 확인한다.
3. 해당 URL에 연결된 Python 함수를 찾는다.
4. Pydantic이 입력 데이터의 필수값, 타입, 범위를 검사한다.
5. 정상 데이터이면 Python 함수를 실행한다.
6. 함수가 반환한 값을 JSON으로 바꾸어 클라이언트에게 응답한다.
7. 검증에 실패하면 함수는 실행되지 않고 422 오류를 반환한다.
```

#### FastAPI Collector의 이벤트 데이터 처리 흐름 이미지 설명

이 흐름은 센서나 외부 시스템에서 발생한 이벤트 JSON이 FastAPI Collector로 전달되고, 데이터 계약 검증을 거쳐 정상 데이터와 오류 데이터로 구분되는 과정을 나타낸다.
```
센서·외부 시스템
→ 이벤트 JSON 전송
→ POST /api/collect/gas
→ FastAPI Endpoint 찾기
→ Pydantic 데이터 계약 검증
→ 정상: Collector 함수 실행
→ 검증 성공 결과 반환
→ JSON 응답

검증 실패
→ 422 오류 응답

2단계 본 실습
→ 검증된 이벤트를 Raw JSONL에 저장
```

### 1. 센서·외부 시스템에서 이벤트 JSON 전송

센서, 외부 애플리케이션 또는 다른 시스템에서 발생한 데이터를 JSON 형식으로 Collector API에 전송한다.

예를 들어 가스 센서에서 다음과 같은 이벤트가 발생할 수 있다.
```json
{
  "event_id": "evt-gas-001",
  "event_type": "gas_sensor_measured",
  "event_time": "2026-07-21T09:00:00+09:00",
  "payload": {
    "sensor_id": "GAS-001",
    "co": 23.5,
    "h2s": 3.1,
    "unit": "ppm"
  }
}
```

이 JSON은 가스 센서에서 측정된 데이터를 표현한 이벤트 한 건이다.

---
### 2. `POST /api/collect/gas`로 데이터 전송

외부 시스템은 이벤트 JSON을 다음 Collector API 주소로 전송한다.
```
POST /api/collect/gas
```

각 부분의 의미는 다음과 같다.

|구성|의미|
|---|---|
|`POST`|JSON 데이터를 서버에 전송하는 HTTP 메서드|
|`/api`|API 기능을 나타내는 공통 경로|
|`/collect`|데이터를 수집하는 기능|
|`/gas`|가스 이벤트를 수집하는 대상|

즉, 다음과 같은 의미다.
```
가스 이벤트 JSON을
Collector API로 전송한다.
```

---
### 3. FastAPI가 연결된 Endpoint 찾기

==`용어설명`==
- Endpoint란 클라이언트가 특정 API 기능을 사용하기 위해 요청을 보내는 주소와 요청 방식(GET·POST 등)을 함께 의미한다.

FastAPI는 요청의 HTTP 메서드와 URL을 확인한다.
```
HTTP 메서드 + API 주소(Path)
= Endpoint

POST + /api/collect/gas
= 가스 이벤트 수집 Endpoint
```

그다음 해당 요청과 연결된 Python 함수를 찾는다.
```python
@app.post("/api/collect/gas")
def collect_gas_event(event: GasSensorEvent):
    ...
```

여기에서 데코레이터는 API 주소와 Python 함수를 연결한다.
```
POST /api/collect/gas 요청
              ↓
collect_gas_event() 함수
```

---
### 4. Pydantic 데이터 계약 검증
FastAPI는 Collector 함수를 바로 실행하지 않는다.

==`용어설명`==
Pydantic이란 API로 들어온 데이터의 필드, 타입, 필수값, 범위가 약속한 기준에 맞는지 자동으로 검사하는 Python 도구다.

먼저 Pydantic을 사용하여 전달받은 JSON이 데이터 계약을 지키는지 검사한다.
```
필수 필드가 모두 있는가?
데이터 타입이 올바른가?
날짜 형식이 올바른가?
숫자 범위를 지키는가?
payload 구조가 올바른가?
```

예를 들어 다음과 같은 데이터 계약이 있다고 가정한다.
```python
class GasPayload(BaseModel):
    sensor_id: str
    co: float
    h2s: float
    unit: str
```
###### Pydantic은 다음 기준을 검사한다.
| 필드          | 데이터 계약 |
| ----------- | ------ |
| `sensor_id` | 문자열    |
| `co`        | 숫자     |
| `h2s`       | 숫자     |
| `unit`      | 문자열    |
검증 결과에 따라 처리 흐름이 정상과 실패로 나뉜다.

---
### 5. 검증 성공 → Collector 함수 실행

이벤트 JSON이 데이터 계약을 모두 지키면 검증에 성공한다.
```python
Pydantic 데이터 계약 검증
             ↓
           정상
             ↓
Collector 함수 실행
```

검증된 데이터가 다음 함수로 전달된다.
```python
def collect_gas_event(event: GasSensorEvent):
    return {
        "message": "가스 이벤트 검증 성공",
        "event_id": event.event_id
    }
```

이 단계부터 실제 데이터 수집 처리 로직이 실행된다.

---
### 6. 검증 성공 결과 반환

Collector 함수는 처리 결과를 Python 딕셔너리 형태로 반환한다.
```python
return {
    "message": "가스 이벤트 검증 성공",
    "event_id": event.event_id
}
```

FastAPI는 Python 딕셔너리를 자동으로 JSON 형식으로 변환한다.
```json
{
  "message": "가스 이벤트 검증 성공",
  "event_id": "evt-gas-001"
}
```

---
### 7. JSON 응답

FastAPI는 처리 결과를 JSON 형식으로 외부 시스템에 반환한다.
```
Collector 함수
→ Python 딕셔너리 반환
→ FastAPI가 JSON으로 변환
→ 외부 시스템에 HTTP 응답
```

외부 시스템은 응답을 확인하여 이벤트가 정상적으로 처리되었는지 알 수 있다.

---
### 8. 검증 실패 → `422` 오류 응답

필수 필드가 없거나 데이터 타입이 잘못되면 Pydantic 검증에 실패한다.

예를 들어 `co`는 숫자여야 하지만 다음과 같이 문자가 들어왔다고 가정한다.
```json
{
  "payload": {
    "sensor_id": "GAS-001",
    "co": "높음",
    "h2s": 3.1,
    "unit": "ppm"
  }
}
```

Pydantic은 데이터 계약 위반을 발견한다.
```
이벤트 JSON 요청
        ↓
Pydantic 데이터 계약 검증
        ↓
      검증 실패
        ↓
Collector 함수 실행 안 됨
        ↓
FastAPI가 자동으로 오류 처리
        ↓
422 상태 코드 + 오류 내용 JSON 반환
```

이 경우 Collector 함수는 실행되지 않는다.
FastAPI는 어떤 필드에서 문제가 발생했는지 오류 정보를 JSON으로 반환한다.

별도의 예외 처리 코드를 작성하지 않아도, Pydantic 검증에 실패하면 FastAPI가 자동으로 오류를 처리하여 `422` 상태 코드와 오류 내용을 JSON으로 반환한다.

예를 들어 `value`는 숫자여야 하는데 문자열 `"높음"`이 들어오면 다음과 같은 오류 정보가 자동으로 반환된다.
```json
{
  "detail": [
    {
      "loc": ["body", "value"],
      "msg": "Input should be a valid number"
    }
  ]
}
```
여기서 `422`는 서버가 요청 자체는 받았지만, 요청 데이터가 정의된 Pydantic 데이터 계약을 지키지 않아 처리할 수 없다는 의미다.


### 🔗 [[2단계_미니프로젝트_Raw 원본 저장까지#3. FastAPI란?]]