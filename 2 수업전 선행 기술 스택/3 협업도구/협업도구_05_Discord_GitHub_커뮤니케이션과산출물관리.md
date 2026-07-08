
> 역할: 수업 소통과 코드·산출물 관리  
> 사용 시점: 수업 전체 기간  
> 핵심 목적: 대화는 Discord에, 코드와 최종 결과물은 GitHub에 남긴다.

---

## 1. Discord의 역할
```text
Discord = 수업 커뮤니케이션 공간
```

Discord에서는 다음을 관리한다.
```text
수업 공지
질문과 답변
코드 오류 공유
팀별 대화
자료 링크 공유
실시간 피드백
```

---

## 2. Discord 채널 예시
```text
공지
질문
자료공유
오류해결
팀1
팀2
팀3
프로젝트발표
```

---

## 3. 좋은 질문 작성법

나쁜 질문:
```text
안 돼요.
오류 났어요.
왜 안 되죠?
```

좋은 질문:
```text
현재 단계: 2단계 FastAPI Collector 실행
실행 명령어: uvicorn main:app --reload
오류 메시지: ModuleNotFoundError: No module named 'schemas'
내가 시도한 것: 가상환경 재실행, pip install 확인
첨부: 터미널 캡처
```

질문은 다음 4가지를 포함하면 좋다.
```text
현재 단계
실행한 명령어
오류 메시지
내가 시도한 해결 방법
```

---

## 4. GitHub의 역할
```text
GitHub = 코드와 최종 산출물 관리 공간
```

GitHub에는 다음을 남긴다.
```text
실습 코드
README
docs 문서
sample_events
schemas
data_lake 구조
Pull Request 기록
커밋 기록
최종 제출물
```

---

## 5. Discord와 GitHub의 차이

| 구분 | Discord | GitHub |
|---|---|---|
| 목적 | 대화와 질문 | 코드와 산출물 저장 |
| 자료 성격 | 빠른 소통 | 공식 기록 |
| 예시 | 오류 질문, 공지 | README, 코드, PR |
| 나중에 찾기 | 어려울 수 있음 | 비교적 쉬움 |

---

## 6. 수업 운영 원칙
```text
질문은 Discord에 올린다.
해결된 내용은 Obsidian에 개인 기록으로 정리한다.
팀에서 공유해야 할 해결책은 Notion에 정리한다.
수정된 코드는 GitHub에 commit/push한다.
최종 산출물은 GitHub README와 docs에 남긴다.
```

---

## 7. GitHub에 남겨야 하는 것
```text
README.md
docs/
schemas/
sample_events/
src/
tests/
requirements.txt
.gitignore
실습 결과 코드
Pull Request 기록
```

---

## 8. Discord에만 남기면 안 되는 것

다음은 Discord에만 남기면 나중에 찾기 어렵다.
```text
최종 요구사항
팀 역할 분담
최종 제출 링크
중요한 오류 해결 방법
프로젝트 실행 방법
API 명세
데이터 계약 문서
```

이런 내용은 Notion 또는 GitHub 문서로 옮겨야 한다.

---

## 9. 한 문장 정리
```text
Discord는 빠른 대화와 질문을 위한 공간이고, GitHub는 코드와 최종 산출물을 공식적으로 남기는 공간이다.
```
