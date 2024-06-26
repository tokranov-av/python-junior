from typing import (
    Literal
)


class NumberOfLinesInFile:
    """Контекстный менеджер, который печатает количество строк в файле."""

    def __init__(self, file_path: str, mode: Literal["r", "w"]):
        self.file_path = file_path
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.file_path, self.mode)
        line_count = sum(1 for _ in self.file)
        print(f'\nКоличество строк в файле "{self.file_path}":', line_count)

        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


if __name__ == "__main__":
    with NumberOfLinesInFile("log.txt", "r") as file:
        pass
