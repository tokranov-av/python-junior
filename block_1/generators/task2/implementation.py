import re
from typing import (
    Generator
)


def open_big_file(file_path: str) -> Generator[str, None, None]:
    """Открывает файл и возвращает строки содержащие слово 'error'."""

    with open(file_path, "r", encoding="utf-8") as file:
        for file_line in file:
            if re.search(r"\berror\b", file_line, re.I):
                yield file_line


if __name__ == "__main__":
    for line in open_big_file("log.txt"):
        print(line, end="")
