import json
from pathlib import Path
from typing import Any


def append_jsonl(
    file_path: Path,
    record: dict[str, Any]
) -> None:
    """딕셔너리 한 건을 JSONL 파일 끝에 추가한다."""

    file_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with file_path.open(
        "a",
        encoding="utf-8"
    ) as file:
        file.write(
            json.dumps(
                record,
                ensure_ascii=False
            )
            + "\n"
        )




        